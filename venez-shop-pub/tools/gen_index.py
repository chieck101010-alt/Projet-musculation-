#!/usr/bin/env python3
"""Writes index.html: scene hosts, voice, music and sound effects."""
import json, sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
D = json.load(open(os.path.join(OUT, "tools/scene_durations.json")))
order = ["hook", "price", "details", "style", "delivery", "trust", "cta"]
starts, t = {}, 0.0
for k in order:
    starts[k] = round(t, 3); t += D[k]
TOTAL = round(t, 3)
VO = {"vo1": (0.0, 1.88), "vo2": (1.95, 4.32), "vo3": (6.3, 5.0), "vo4": (11.4, 2.85),
      "vo5": (14.3, 7.56), "vo6": (22.1, 2.45), "vo7": (24.6, 7.6)}
S = starts
SFX = [  # id, file, start, dur, volume, extra
    ("sfx-open", "impact-bass-1", 0.0, 1.6, 0.5, ""),
    ("sfx-g1", "glitch-1", 0.43, 0.3, 0.35, ' data-fade-out="0.1"'),
    ("sfx-g2", "glitch-2", 1.16, 0.3, 0.35, ' data-fade-out="0.1"'),
    ("sfx-g3", "glitch-1", 1.71, 0.3, 0.35, ' data-fade-out="0.1"'),
    ("sfx-drop", "whoosh-short", S["price"], 0.57, 0.5, ""),
    ("sfx-land", "impact-bass-2", S["price"] + 0.38, 1.0, 0.45, ' data-fade-out="0.4"'),
    ("sfx-price", "impact-bass-1", S["price"] + 1.48, 1.8, 0.6, ' data-fade-out="0.5"'),
    ("sfx-d1", "click-soft", S["details"] + 0.02, 0.36, 0.6, ""),
    ("sfx-d2", "click-soft", S["details"] + 1.2, 0.36, 0.6, ""),
    ("sfx-d3", "click", S["details"] + 2.45, 0.36, 0.5, ""),
    ("sfx-d4", "whoosh-short", S["details"] + 3.9, 0.57, 0.45, ""),
    ("sfx-split", "whoosh", S["style"], 0.57, 0.55, ""),
    ("sfx-truck", "whoosh-cinematic", S["delivery"] + 0.15, 1.2, 0.4, ' data-fade-out="0.4"'),
    ("sfx-c1", "pop", S["delivery"] + 0.42, 0.72, 0.4, ""),
    ("sfx-c2", "pop", S["delivery"] + 2.82, 0.72, 0.4, ""),
    ("sfx-c3", "pop", S["delivery"] + 5.18, 0.72, 0.4, ""),
    ("sfx-out", "whoosh-short", S["delivery"] + D["delivery"] - 0.3, 0.57, 0.45, ""),
    ("sfx-b1", "pop", S["trust"] + 0.12, 0.72, 0.4, ""),
    ("sfx-b2", "pop", S["trust"] + 1.1, 0.72, 0.4, ""),
    ("sfx-b3", "pop", S["trust"] + 1.6, 0.72, 0.4, ""),
    ("sfx-wipe", "whoosh", S["cta"] - 0.27, 0.57, 0.5, ""),
    ("sfx-cta", "impact-bass-2", S["cta"] + 0.02, 1.4, 0.5, ' data-fade-out="0.4"'),
    ("sfx-k1", "key-press", S["cta"] + 1.6, 0.43, 0.45, ""),
    ("sfx-k2", "key-press", S["cta"] + 2.04, 0.43, 0.45, ""),
    ("sfx-k3", "key-press", S["cta"] + 2.6, 0.43, 0.45, ""),
    ("sfx-tt", "whoosh-short", S["cta"] + 3.65, 0.57, 0.45, ""),
    ("sfx-tap", "click", S["cta"] + 3.72, 0.36, 0.7, ""),
    ("sfx-merci", "pop", S["cta"] + 6.1, 0.72, 0.45, ""),
]
# pack effects into Studio lanes without overlap
lanes, rows = [], []
for sid, f, st, du, vol, ex in sorted(SFX, key=lambda x: x[2]):
    for i, end in enumerate(lanes):
        if end <= st: lanes[i] = st + du; lane = i; break
    else:
        lanes.append(st + du); lane = len(lanes) - 1
    rows.append(f'      <audio id="{sid}" class="clip" src="assets/audio/sfx/{f}.mp3" data-start="{round(st,3)}" data-duration="{du}" data-track-index="{5+lane}" data-volume="{vol}"{ex}></audio>')
hosts = "\n".join(
    f'      <div id="{k}" data-composition-id="{k}" data-composition-src="compositions/{k}.html" data-start="{starts[k]}" data-duration="{D[k]}" data-track-index="0" data-track-kind="graphics" data-width="1080" data-height="1920"'
    + (""" data-variable-values='{"snap":"naskoo_1ter","tiktok":"@venez_shop75"}'""" if k == "cta" else "") + "></div>"
    for k in order)
vos = "\n".join(
    f'      <audio id="{k}" class="clip" src="assets/audio/{k}.wav" data-start="{st}" data-duration="{du}" data-track-index="3" data-volume="1"></audio>'
    for k, (st, du) in VO.items())
html = f"""<!doctype html>
<html lang="fr" data-composition-variables='[{{"id":"snap","type":"string","label":"Pseudo Snapchat","default":"naskoo_1ter"}},{{"id":"tiktok","type":"string","label":"Compte TikTok","default":"@venez_shop75"}}]'>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #050505; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #050505; }}
      #grain {{ position: absolute; inset: -60px; z-index: 10; pointer-events: none; opacity: 0.1; mix-blend-mode: overlay;
        background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='240' height='240' filter='url(%23n)'/></svg>"); }}
      #vignette {{ position: absolute; inset: 0; z-index: 9; pointer-events: none;
        background: radial-gradient(120% 80% at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,.5) 100%); }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <!-- scenes, cut on the beats of the 140 bpm track -->
{hosts}
      <div id="vignette" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="1"></div>
      <div id="grain" class="clip" data-start="0" data-duration="{TOTAL}" data-track-index="2"></div>

      <!-- voice-over: Gemini 3.1 Flash TTS (voice Puck, fr-FR) via FLORA -->
{vos}
      <!-- music: Lyria 3.5 via FLORA, entered on its first full-energy beat -->
      <audio id="music" class="clip" src="assets/audio/music.mp3" data-start="0" data-duration="{TOTAL}" data-track-index="4" data-volume="0.32" data-fade-out="1.6"></audio>
      <!-- sound on visible actions -->
{chr(10).join(rows)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      tl.fromTo("#grain", {{ x: 0, y: 0 }}, {{ x: 60, y: -40, duration: {TOTAL}, ease: "steps({round(TOTAL*12)})" }}, 0);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
open(os.path.join(OUT, "index.html"), "w").write(html)
print(starts, TOTAL)
