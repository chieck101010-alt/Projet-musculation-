#!/usr/bin/env python3
"""Build the two language roots of QUIET / LOUD from one schedule.

  python3 tools/build.py          -> index.html (FR) + nl.html (NL)
                                     compositions/captions-fr.html, captions-nl.html

Scenes in compositions/ are shared; only the voice clips, the captions and the
on-screen words (host variable values) change between languages.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHRASES = json.loads((ROOT / "tools" / "phrases.json").read_text())


def _media_len(path):
    import subprocess
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return float(out.strip())


for _lang, _ph in PHRASES.items():
    for _p in _ph:
        _p["dur"] = round(_media_len(ROOT / "assets" / "audio" / _lang / f"{_p['id']}.wav") - 0.005, 3)

DURATION = 32.3
MUSIC_START = 1.065  # music beat 9.635 s (the drop) lands on film 10.70 s
DROP = 10.7

# Film time at which each phrase's speech starts. p08 and p12 are placed by an
# anchor word ("toi"/"jij" on 17.3, "loud" on 26.3) so both languages hit the cut.
ONSET = {
    "p01": 0.30, "p02": 3.75, "p03": 5.40, "p04": 7.42,
    "p05": 11.30, "p06": 12.50, "p07": 13.70,
    "p08": ("anchor", 17.30), "p09": 18.20,
    "p10": 20.60, "p11": 22.75,
    "p12": ("anchor", 26.30), "p13": 27.50,
}
# NL phrases that run longer get a nudge so nothing overlaps
ONSET_LANG = {"nl": {"p06": 12.62, "p07": 13.80}}
NO_CAPTION = {"p12", "p13"}  # the end card already shows these words

WORDS = {
    "fr": {
        "details": {"w1": "Coupe.", "w2": "Matière.", "w3": "Détail."},
        "between": {"label": "Entre les deux", "word": "Toi."},
        "lineup": {"n1": "Survêtement", "n2": "Doudoune", "n3": "Hoodie", "n4": "Accessoires"},
        "endcard": {"tagline": "Ton style parle en premier."},
    },
    "nl": {
        "details": {"w1": "Snit.", "w2": "Stof.", "w3": "Detail."},
        "between": {"label": "Daartussen", "word": "Jij."},
        "lineup": {"n1": "Trainingspak", "n2": "Puffer", "n3": "Hoodie", "n4": "Accessoires"},
        "endcard": {"tagline": "Jouw stijl spreekt eerst."},
    },
}

# Long single-breath lines are split for reading, at a word boundary.
MANUAL_SPLIT = {
    ("fr", "p11"): ["Pas besoin de crier", "pour être vu."],
    ("nl", "p11"): ["Je hoeft niet te schreeuwen", "om gezien te worden."],
}

SCENES = [
    # id, start, duration, lane, z
    ("quiet", 0.0, 4.3, 1, 1),
    ("details", 3.6, 7.3, 2, 2),
    ("loud", 10.7, 5.5, 1, 3),
    ("between", 15.5, 4.8, 2, 4),
    ("lineup", 20.3, 5.4, 1, 6),
    ("endcard", 25.1, DURATION - 25.1, 2, 5),
]

SFX = [
    # id, file, film time of the hit, offset of the hit inside the file, volume
    ("sfx-shut-1", "shutter-a", 3.60, 0.0, 0.55),
    ("sfx-shut-2", "shutter-b", 5.30, 0.0, 0.5),
    ("sfx-shut-3", "shutter-c", 7.25, 0.0, 0.55),
    ("sfx-riser", "impact", DROP, 0.47, 0.75),
    ("sfx-whoosh", "whoosh", 13.10, 0.40, 0.55),
    ("sfx-shut-4", "shutter-a", 20.30, 0.0, 0.5),
    ("sfx-shut-5", "shutter-b", 20.90, 0.0, 0.45),
    ("sfx-shut-6", "shutter-c", 21.50, 0.0, 0.5),
    ("sfx-shut-7", "shutter-a", 22.10, 0.0, 0.45),
    ("sfx-burst", "shutter-burst", 22.70, 0.0, 0.45),
    ("sfx-hit", "hit", 26.30, 0.06, 0.7),
]
SFX_LEN = {"shutter-a": 0.14, "shutter-b": 0.14, "shutter-c": 0.16, "shutter-burst": 0.42,
           "impact": 3.03, "whoosh": 0.5, "hit": 1.6}

# Music level (film time -> gain). The voice sits on top; the bed opens up in the gaps.
MUSIC_ENV = [
    (MUSIC_START, 0.55), (10.45, 0.55), (10.70, 0.9), (11.15, 0.32),
    (14.30, 0.32), (14.55, 0.55), (15.60, 0.55), (15.85, 0.3),
    (24.60, 0.3), (24.85, 0.5), (25.25, 0.3),
    (29.30, 0.3), (29.80, 0.62), (31.10, 0.62), (DURATION, 0.0),
]


def r(x):
    return round(x + 1e-9, 3)


def schedule(lang):
    out = []
    for p in PHRASES[lang]:
        o = ONSET_LANG.get(lang, {}).get(p["id"], ONSET[p["id"]])
        if isinstance(o, tuple):
            o = o[1] - p["anchor"]
        start = o - p["lead"]
        out.append({**p, "onset": r(o), "start": r(start), "end": r(start + p["dur"])})
    for a, b in zip(out, out[1:]):
        assert a["end"] <= b["start"] + 0.02, (lang, a["id"], a["end"], b["id"], b["start"])
    return out


def caption_groups(lang, sched):
    groups = []
    for p in sched:
        if p["id"] in NO_CAPTION:
            continue
        s0, s1 = p["src"]
        to_film = lambda t: p["onset"] + (t - s0)  # noqa: E731
        if "split" in p:
            if "… " in p["text"]:
                parts = [x.strip() for x in p["text"].split("… ", 1)]
                parts[0] += "…"
            else:
                parts = [x.strip() for x in p["text"].split(". ", 1)]
                parts[0] += "."
            a, b = p["split"]
            groups.append((parts[0], to_film(s0), to_film(a)))
            groups.append((parts[1], to_film(b), to_film(s1)))
        elif (lang, p["id"]) in MANUAL_SPLIT:
            parts = MANUAL_SPLIT[(lang, p["id"])]
            frac = len(parts[0]) / (len(parts[0]) + len(parts[1]))
            mid = s0 + (s1 - s0) * frac
            groups.append((parts[0], to_film(s0), to_film(mid)))
            groups.append((parts[1], to_film(mid), to_film(s1)))
        else:
            groups.append((p["text"], to_film(s0), to_film(s1)))
    # open just before the first word, hold a little after the last, never overlap
    final = []
    for i, (text, a, b) in enumerate(groups):
        start = max(0.15, a - 0.06)
        end = b + 0.3
        if i + 1 < len(groups):
            end = min(end, groups[i + 1][1] - 0.08)
        end = max(end, start + 0.5 + 0.12 * len(text.split()))
        if i + 1 < len(groups):
            end = min(end, groups[i + 1][1] - 0.08)
        final.append((text, r(start), r(end)))
    return final


def captions_html(lang, groups):
    items, tweens = [], []
    for i, (text, a, b) in enumerate(groups):
        gid = f"cap-{i + 1:02d}"
        items.append(f'    <div id="{gid}" class="cap"><span>{text}</span></div>')
        tweens.append(
            f'    tl.set("#{gid}", {{ visibility: "visible" }}, {a});\n'
            f'    tl.fromTo("#{gid} span", {{ opacity: 0, filter: "blur(6px)" }}, '
            f'{{ opacity: 1, filter: "blur(0px)", duration: 0.12, ease: "power4.out" }}, {a});\n'
            f'    tl.to("#{gid} span", {{ opacity: 0, duration: 0.1, ease: "power2.in" }}, {r(b - 0.1)});\n'
            f'    tl.set("#{gid}", {{ visibility: "hidden" }}, {b});'
        )
    return f"""<template>
  <style>
    #root {{
      position: absolute;
      inset: 0;
      pointer-events: none;
    }}
    .cap {{
      position: absolute;
      left: 120px;
      width: 660px;
      bottom: 682px;
      text-align: center;
      visibility: hidden;
    }}
    .cap span {{
      display: inline-block;
      max-width: 660px;
      padding: 12px 24px 14px;
      border-radius: 8px;
      background: rgba(13, 14, 17, 0.58);
      color: #f2f0eb;
      font-family: Inter, sans-serif;
      font-weight: 700;
      font-size: 40px;
      text-wrap: balance;
      line-height: 1.2;
      letter-spacing: -0.005em;
      opacity: 0;
    }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(items)}
  </div>
  <script>
    // generated by tools/build.py ({lang}) — edit phrases.json / build.py, then rebuild
    const tl = gsap.timeline({{ paused: true }});
{chr(10).join(tweens)}
    window.__timelines["captions"] = tl;
  </script>
</template>
"""


def music_automation():
    pts = [{"t": r(t - MUSIC_START), "v": v} for t, v in MUSIC_ENV]
    return json.dumps({"version": 1, "lanes": [{"target": "volume", "points": pts}]}, separators=(",", ":"))


def root_html(lang, sched):
    w = WORDS[lang]
    hosts = []
    for sid, start, dur, lane, z in SCENES:
        vals = w.get(sid)
        vv = f" data-variable-values='{json.dumps(vals, ensure_ascii=False)}'" if vals else ""
        hosts.append(
            f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" '
            f'data-start="{start}" data-duration="{r(dur)}" data-track-index="{lane}" data-track-kind="graphics" '
            f'data-width="1080" data-height="1920" style="z-index: {z}"{vv}></div>'
        )
    hosts.append(
        '      <div id="editorial-flash-overlay" data-composition-id="editorial-flash-overlay" '
        'data-composition-src="compositions/editorial-flash-overlay.html" '
        f'data-start="{r(DROP - 0.62)}" data-duration="1" data-track-index="3" data-track-kind="graphics" '
        'data-width="1080" data-height="1920" style="z-index: 8"></div>'
    )
    hosts.append(
        f'      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions-{lang}.html" '
        f'data-start="0" data-duration="{DURATION}" data-track-index="4" data-track-kind="captions" '
        'data-width="1080" data-height="1920" style="z-index: 9"></div>'
    )
    audio = []
    for p in sched:
        audio.append(
            f'      <audio id="vo-{p["id"]}" class="clip" data-start="{p["start"]}" data-duration="{p["dur"]}" '
            f'data-track-index="20" data-volume="1" src="assets/audio/{lang}/{p["id"]}.wav"></audio>'
        )
    audio.append(
        f'      <audio id="music" class="clip" data-start="{MUSIC_START}" data-duration="{r(DURATION - MUSIC_START)}" '
        f"data-track-index=\"21\" data-volume=\"1\" data-automation='{music_automation()}' "
        'src="assets/audio/music-bed.mp3"></audio>'
    )
    for sid, f, hit, off, vol in SFX:
        start = r(hit - off + 0.033)  # the peak lands one frame after the picture
        audio.append(
            f'      <audio id="{sid}" class="clip" data-start="{start}" data-duration="{SFX_LEN[f]}" '
            f'data-track-index="{23 if sid == "sfx-whoosh" else 22}" data-volume="{vol}" src="assets/audio/sfx/{f}.wav"></audio>'
        )
    title = "QUIET / LOUD — " + ("FR" if lang == "fr" else "NL")
    return f"""<!doctype html>
<!-- generated by tools/build.py — edit the schedule there, then: python3 tools/build.py -->
<html lang="{lang}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>{title}</title>
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}
      html,
      body {{
        margin: 0;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
        background: #0d0e11;
      }}
      #root {{
        position: relative;
        width: 1080px;
        height: 1920px;
        overflow: hidden;
      }}
    </style>
  </head>
  <body>
    <div
      id="root"
      data-composition-id="main"
      data-start="0"
      data-duration="{DURATION}"
      data-width="1080"
      data-height="1920"
      data-motion-blur="on"
    >
{chr(10).join(hosts)}
{chr(10).join(audio)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""


def main():
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "fr"
    for lang in ("fr", "nl"):
        sched = schedule(lang)
        groups = caption_groups(lang, sched)
        (ROOT / "compositions" / f"captions-{lang}.html").write_text(captions_html(lang, groups))
        if lang == target:
            (ROOT / "index.html").write_text(root_html(lang, sched))
            print("index.html ->", lang)
        print(lang, "phrases:", [(p["id"], p["start"], p["end"]) for p in sched])
        print(lang, "captions:", groups)


if __name__ == "__main__":
    main()
