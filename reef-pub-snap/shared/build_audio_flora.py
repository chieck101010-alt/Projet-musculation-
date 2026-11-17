"""REEF 33 — assemble le son FLORA (ElevenLabs) dans les 3 vidéos.

- voix : mp3 FLORA -> assets/audio/voN.wav (silences coupés, volume normalisé)
- musique : mp3 FLORA -> assets/audio/music.wav (30 s, fondu de fin) puis music-ducked.wav (baissée sous la voix)
- bruitages : sons FLORA placés aux instants des actions -> assets/audio/sfx.wav
- met à jour data-start / data-duration des voix dans index.html et les sous-titres (compositions/captions.html)

Usage : python3 build_audio_flora.py <dossier reef-pub-snap> <dossier des mp3 FLORA>
"""
import re, subprocess, sys, os

ROOT, SRC = sys.argv[1], sys.argv[2]
DUR = 30.0

# départs des voix (s) ; une voix ne doit pas chevaucher la suivante
STARTS = {
    "v1-street": [0.2, 2.5, 6.25, 14.8, 22.45, 27.3],
    "v2-cinema": [0.5, 2.4, 8.5, 11.8, 15.1, 19.2, 27.5],
    "v3-tiktok": [0.15, 2.2, 8.3, 17.0, 24.4],
}
# bruitages : (nom du son FLORA, instant, gain)
SFX = {
    "v1-street": [("impact", 0.38, 1.0), ("whoosh", 1.25, 0.6), ("whoosh", 5.75, 0.6), ("whoosh", 6.15, 0.5),
                  ("whoosh", 7.95, 0.5), ("whoosh", 9.75, 0.5), ("whoosh", 13.75, 0.6), ("whoosh", 21.8, 0.7),
                  ("glitch", 22.4, 0.8), ("glitch", 23.9, 0.45), ("glitch", 25.3, 0.45), ("impact", 24.6, 0.45),
                  ("shimmer", 27.3, 0.7)],
    "v2-cinema": [("wind", 0.0, 0.8), ("sandrise", 2.4, 0.7), ("shimmer", 8.2, 0.5), ("shimmer", 11.5, 0.5),
                  ("shimmer", 14.8, 0.5), ("splash", 21.35, 1.0), ("shimmer", 26.0, 0.6)],
    "v3-tiktok": [("impact", 0.0, 0.45), ("whoosh", 1.8, 0.5), ("whoosh", 7.8, 0.5), ("whoosh", 15.8, 0.5),
                  ("whoosh", 23.8, 0.5), ("pop", 2.05, 0.7), ("pop", 8.15, 0.7), ("pop", 9.4, 0.7), ("pop", 10.6, 0.7),
                  ("pop", 12.2, 0.7), ("pop", 16.2, 0.7), ("pop", 18.2, 0.7), ("pop", 25.2, 0.7), ("shimmer", 24.6, 0.6)],
}


def run(*a):
    subprocess.run(a, check=True, stdin=subprocess.DEVNULL)


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)


for v, starts in STARTS.items():
    a = f"{ROOT}/{v}/assets/audio"
    # voix
    durs = []
    for k in range(1, len(starts) + 1):
        out = f"{a}/vo{k}.wav"
        run("ffmpeg", "-v", "error", "-y", "-i", f"{SRC}/{v}-vo{k}.mp3", "-af",
            "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
            "highpass=f=70,loudnorm=I=-16:TP=-1.5", "-ar", "44100", "-ac", "1", out)
        durs.append(round(dur(out), 3))
    for k in range(len(starts) - 1):
        assert starts[k] + durs[k] <= starts[k + 1] - 0.05, (v, k + 1, starts[k], durs[k], starts[k + 1])
    assert starts[-1] + durs[-1] <= DUR, (v, "dernière voix trop longue", durs[-1])

    # musique : 30 s, fondu de fin
    run("ffmpeg", "-v", "error", "-y", "-i", f"{SRC}/{v}-music.mp3", "-af",
        f"apad=whole_dur={DUR},atrim=0:{DUR},afade=t=out:st={DUR-1.5}:d=1.5,loudnorm=I=-15:TP=-1.5",
        "-ar", "44100", "-ac", "2", f"{a}/music.wav")

    # bruitages
    ins, flt = [], []
    for i, (name, t0, g) in enumerate(SFX[v]):
        ins += ["-i", f"{SRC}/sfx-{name}.mp3"]
        ms = int(t0 * 1000)
        flt.append(f"[{i}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume={g},adelay={ms}|{ms}[s{i}]")
    n = len(SFX[v])
    flt.append("".join(f"[s{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0,apad=whole_dur={DUR},atrim=0:{DUR}[out]")
    run("ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(flt), "-map", "[out]", "-ar", "44100", f"{a}/sfx.wav")

    # musique baissée sous la voix
    ins, flt = ["-i", f"{a}/music.wav"], []
    for k, t0 in enumerate(starts):
        ins += ["-i", f"{a}/vo{k+1}.wav"]
        ms = int(t0 * 1000)
        flt.append(f"[{k+1}:a]aformat=channel_layouts=stereo,adelay={ms}|{ms}[d{k}]")
    flt.append("".join(f"[d{k}]" for k in range(len(starts))) + f"amix=inputs={len(starts)}:normalize=0,apad=whole_dur={DUR}[vo]")
    flt.append("[0:a][vo]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350:makeup=1[out]")
    run("ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(flt), "-map", "[out]", "-t", str(DUR), "-ar", "44100", f"{a}/music-ducked.wav")

    # index.html : départs et durées des voix
    p = f"{ROOT}/{v}/index.html"; s = open(p).read()
    for k, t0 in enumerate(starts, 1):
        s, c = re.subn(rf'(<audio id="vo{k}" class="clip" src="assets/audio/vo{k}.wav") data-start="[\d.]+" data-duration="[\d.]+"',
                       rf'\1 data-start="{t0}" data-duration="{durs[k-1]}"', s)
        assert c == 1, (v, k)
    s = s.replace("<!-- voix off (Piper, voix IA locale) -->", "<!-- voix off (ElevenLabs v3 via FLORA) -->")
    s = s.replace("<!-- son : musique et bruitages composés par synthèse (shared/synth_audio.py) -->",
                  "<!-- son : musique ElevenLabs Music et bruitages ElevenLabs SFX via FLORA (shared/build_audio_flora.py) -->")
    open(p, "w").write(s)

    # sous-titres
    p = f"{ROOT}/{v}/compositions/captions.html"; s = open(p).read()
    for k, t0 in enumerate(starts, 1):
        s, c = re.subn(rf'show\("c{k}", [\d.]+, [\d.]+\);', f'show("c{k}", {t0}, {round(t0 + durs[k-1] + 0.15, 3)});', s)
        assert c == 1, (v, "cap", k)
    open(p, "w").write(s)
    print(v, "voix", durs)
