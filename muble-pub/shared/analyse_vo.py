#!/usr/bin/env python3
"""Analyse chaque prise de voix : durée, début/fin de parole, sonie, transcription Whisper (fr)."""
import json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(os.path.dirname(ROOT), ".claude/skills/hyperframes/scripts/plugin-cli.mjs")
SCR = os.environ.get("SCRATCH", "/tmp")
def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)
out = {}
files = sorted(f for f in os.listdir(os.path.join(ROOT, "assets/audio/vo")) if f.endswith(".wav"))
only = sys.argv[1:]
cache_p = os.path.join(ROOT, "assets/audio/vo/analyse.json")
cache = json.load(open(cache_p)) if os.path.exists(cache_p) else {}
for f in files:
    name = f[:-4]
    if only and name not in only and name in cache:
        out[name] = cache[name]; continue
    if not only and name in cache:
        out[name] = cache[name]; continue
    p = os.path.join(ROOT, "assets/audio/vo", f)
    dur = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).stdout)
    sd = run(["ffmpeg", "-hide_banner", "-i", p, "-af", "silencedetect=noise=-40dB:d=0.12", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", sd)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", sd)]
    onset = ends[0] if starts and starts[0] < 0.05 and ends else 0.0
    offset = starts[-1] if starts and (not ends or starts[-1] > ends[-1]) else dur
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", run(["ffmpeg", "-hide_banner", "-i", p, "-af", "ebur128", "-f", "null", "-"]).stderr)
    tmp = os.path.join(SCR, f"tr_{name}.wav")
    run(["ffmpeg", "-y", "-v", "error", "-i", p, "-ar", "16000", "-ac", "1", tmp])
    tr = run(["node", SK, "transcribe", tmp, "--engine", "whisper", "--model", "small", "--language", "fr", "--json", "--dir", SCR])
    words = []
    for line in tr.stderr.splitlines():
        try:
            j = json.loads(line)
        except Exception:
            continue
        if j.get("type") == "words":
            words += j["words"]
    out[name] = {"duration": round(dur, 3), "onset": round(onset, 3), "offset": round(offset, 3), "lufs": float(lufs[-1]) if lufs else None,
                 "text": " ".join(w["text"] for w in words), "words": words}
    print(name, out[name]["duration"], out[name]["onset"], out[name]["offset"], out[name]["lufs"], "|", out[name]["text"])
json.dump(out, open(cache_p, "w"), ensure_ascii=False, indent=1)
