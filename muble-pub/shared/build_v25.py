#!/usr/bin/env python3
"""Construit la version courte 25 s (projet HyperFrames muble-pub/v25) à partir :
- du rendu « propre » (sans sous-titres) de la version 72 s : v25/assets/footage/clean72.mp4
- d'extraits de la même voix off, de la même musique et des mêmes bruitages.
Usage : python3 shared/build_v25.py   (depuis muble-pub/)
"""
import json, os, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "v25")
NAME, TITLE = "muble-pub-25s", "Muble — pub VTC premium (25 s)"
A = os.path.join(ROOT, "assets")
TOTAL = 25.0

# (début dans la version courte, début dans le film 72 s, durée)
SEG = [
    ("A", 0.00, 0.00, 1.40),   # « Un rendez-vous ? »
    ("B", 1.40, 1.40, 1.20),   # « Un avion à prendre ? »
    ("C", 2.60, 5.00, 2.40),   # inondation violette + logo
    ("D", 5.00, 12.45, 3.40),  # le téléphone monte, chrono
    ("E", 8.40, 18.95, 2.00),  # étape 1 : adresse de départ
    ("F", 10.40, 23.75, 1.65), # étape 2 : date, heure, passagers
    ("G", 12.05, 29.60, 2.00), # étape 3 : Éco / Berline
    ("H", 14.05, 36.85, 1.40), # étape 4 : e-mail
    ("I", 15.45, 38.55, 1.40), # étape 5 : envoi, chrono 1:48
    ("J", 16.85, 40.00, 4.30), # rappel avec le prix exact, prix figé
    ("K", 21.15, 50.20, 1.20), # chauffeurs professionnels
    ("L", 22.35, 67.00, 2.65), # logo, signature, bouton
]
# extraits de voix : (nom, fichier, début dans le fichier, fin dans le fichier, placement)
VO = [
    ("k01", "vo01", 0.0, 2.50, 0.00),
    ("k02", "vo02", 0.0, None, 2.70),
    ("k03", "vo04", 0.0, None, 5.45),
    ("k04", "vo09", 0.0, 4.85, 16.02),
    ("k05", "vo13", 0.0, None, 22.85),
]
# décalage des mots minutés (temps du film 72 s → temps de la version courte), pour les sous-titres
WORDS = [("vo02", -2.40, None), ("vo04", -7.45, None), ("vo09", -23.18, 39.20 + 4.85)]
MUSIC_OFFSET = 52.7  # la chute naturelle de la musique tombe à ~24,3 s
SFX = [  # (fichier, début, volume, media-start, durée)
    ("impact-bass-1", 0.02, 0.35, 0, None), ("whoosh-short", 1.36, 0.5, 0, None), ("whoosh", 2.58, 0.55, 0, None),
    ("impact-bass-2", 3.55, 0.5, 0, None), ("sparkle", 4.48, 0.4, 0, None), ("whoosh", 4.98, 0.5, 0, None),
    ("pop", 6.25, 0.45, 0, None), ("whoosh-short", 8.38, 0.4, 0, None), ("click-soft", 8.80, 0.55, 0, None),
    ("typing", 8.88, 0.28, 0, 1.4), ("whoosh", 10.38, 0.4, 0, None), ("click-soft", 10.65, 0.55, 0, None),
    ("click-soft", 11.20, 0.55, 0, None), ("click-soft", 11.85, 0.55, 0, None), ("whoosh-short", 12.03, 0.4, 0, None),
    ("click-soft", 13.85, 0.55, 0, None), ("whoosh", 14.03, 0.4, 0, None), ("click-soft", 14.10, 0.5, 0, None),
    ("typing", 14.18, 0.28, 0, 1.0), ("whoosh-short", 15.43, 0.4, 0, None), ("click", 15.75, 0.7, 0, None),
    ("pop", 15.87, 0.5, 0, None), ("pop", 17.05, 0.28, 0, None), ("pop", 19.05, 0.28, 0, None),
    ("riser", 19.85, 0.25, 1.8, 2.5), ("whoosh", 21.13, 0.45, 0, None), ("impact-bass-1", 22.35, 0.55, 0, None),
    ("sparkle", 22.40, 0.4, 0, None),
]

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-1500:])
    return r

def dur(f):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).stdout)

def main():
    for d in ("assets/audio/vo", "assets/audio/sfx", "assets/fonts", "assets/footage", "compositions", "renders"):
        os.makedirs(os.path.join(V, d), exist_ok=True)
    for f in ("hyperframes.json",):
        shutil.copy(os.path.join(ROOT, f), os.path.join(V, f))
    json.dump({"name": NAME, "private": True, "type": "module"}, open(os.path.join(V, "package.json"), "w"), indent=2)
    json.dump({"id": NAME, "name": TITLE, "createdAt": "2026-11-18T20:30:00.000Z"}, open(os.path.join(V, "meta.json"), "w"), indent=2)
    shutil.copy(os.path.join(A, "fonts/PlusJakartaSans-Variable-latin.woff2"), os.path.join(V, "assets/fonts/"))
    clean = os.path.join(V, "assets/footage/clean72.mp4")
    src_clean = os.path.join(ROOT, "v25/assets/footage/clean72.mp4")
    if not os.path.exists(clean) and os.path.exists(src_clean):
        os.link(src_clean, clean)
    if not os.path.exists(clean):
        raise SystemExit("manque v25/assets/footage/clean72.mp4 (rendu 72 s sans sous-titres)")
    # voix
    vo_rows = []
    for name, src, a, b, t in VO:
        out = os.path.join(V, f"assets/audio/vo/{name}.wav")
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", str(a), "-i", os.path.join(A, f"audio/vo/{src}-n.wav")]
        if b is not None:
            cmd += ["-t", str(b - a), "-af", f"afade=t=out:st={b - a - 0.06:.3f}:d=0.06"]
        sh(cmd + [out])
        vo_rows.append(f'      <audio id="{name}" class="clip" src="assets/audio/vo/{name}.wav" data-start="{t:.2f}" data-duration="{dur(out):.3f}" data-track-index="2" data-volume="1"></audio>')
    # piste voix complète → clé de ducking
    ins, fl = [], []
    for i, (name, _, _, _, t) in enumerate(VO):
        ins += ["-i", os.path.join(V, f"assets/audio/vo/{name}.wav")]
        fl.append(f"[{i}:a]adelay={int(t * 1000)}:all=1[a{i}]")
    fl.append("".join(f"[a{i}]" for i in range(len(VO))) + f"amix=inputs={len(VO)}:normalize=0,apad=whole_dur={TOTAL}[v]")
    key = os.path.join(V, "assets/audio/vo-track.wav")
    sh(["ffmpeg", "-y", "-v", "error", *ins, "-filter_complex", ";".join(fl), "-map", "[v]", "-t", str(TOTAL), "-ar", "48000", key])
    sh(["ffmpeg", "-y", "-v", "error", "-ss", str(MUSIC_OFFSET), "-t", str(TOTAL), "-i", os.path.join(A, "audio/music-raw.mp3"), "-i", key, "-filter_complex",
        f"[0:a]aresample=48000,volume=-7dB,afade=t=in:d=0.15,afade=t=out:st={TOTAL - 0.7}:d=0.7[m];[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0[k];"
        "[m][k]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=420:makeup=1[d]", "-map", "[d]", "-t", str(TOTAL), os.path.join(V, "assets/audio/music-bed.wav")])
    # bruitages
    sfx_rows, lanes = [], [0.0, 0.0, 0.0]
    for i, (f, t, v, ms, d) in enumerate(sorted(SFX, key=lambda x: x[1])):
        dst = os.path.join(V, f"assets/audio/sfx/{f}.mp3")
        if not os.path.exists(dst):
            shutil.copy(os.path.join(A, f"audio/sfx/{f}.mp3"), dst)
        length = d if d else dur(dst) - ms
        length = min(length, TOTAL - t)
        lane = next((j for j, e in enumerate(lanes) if e <= t + 1e-6), None)
        if lane is None:
            lanes.append(0.0); lane = len(lanes) - 1
        lanes[lane] = t + length
        msa = f' data-media-start="{ms}"' if ms else ""
        sfx_rows.append(f'      <audio id="sfx{i:02d}" class="clip" src="assets/audio/sfx/{f}.mp3" data-start="{t:.2f}" data-duration="{length:.3f}"{msa} data-track-index="{4 + lane}" data-volume="{v}"></audio>')
    # sous-titres
    words = json.load(open(os.path.join(A, "audio/vo-words.json")))
    short = []
    for line, shift, until in WORDS:
        for w in words:
            if w["line"] == line and (until is None or w["end"] <= until + 0.05):
                short.append({**w, "start": round(w["start"] + shift, 3), "end": round(w["end"] + shift, 3)})
    json.dump(short, open(os.path.join(V, "assets/audio/vo-words.json"), "w"), ensure_ascii=False)
    sh(["python3", os.path.join(ROOT, "shared/build_captions.py"), os.path.join(V, "assets/audio/vo-words.json"), str(TOTAL), os.path.join(V, "compositions/captions.html")])
    # composition racine
    vids = "\n".join(
        f'      <video id="seg{k}" class="clip" src="assets/footage/clean72.mp4" data-start="{t:.2f}" data-duration="{d:.2f}" data-media-start="{s:.2f}" data-track-index="0" muted playsinline></video>'
        for k, t, s, d in SEG)
    html = f'''<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #4c14a6; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; }}
      #root > video {{ position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; object-fit: cover; z-index: 1; }}
      #captions {{ z-index: 5; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
      <!-- MUBLE — {TITLE} : montage d'extraits du film 72 s (rendu sans sous-titres) -->
{vids}
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{TOTAL}" data-track-index="1" data-track-kind="captions" data-width="1080" data-height="1920"></div>
      <!-- Voix off : extraits de la voix Gemini « Achird » -->
{chr(10).join(vo_rows)}
      <audio id="music" class="clip" src="assets/audio/music-bed.wav" data-start="0" data-duration="{TOTAL}" data-track-index="3" data-volume="1"></audio>
{chr(10).join(sfx_rows)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
'''
    open(os.path.join(V, "index.html"), "w").write(html)
    print(NAME, "prêt :", len(SEG), "plans,", len(VO), "extraits de voix,", len(SFX), "bruitages,", len(short), "mots")

if __name__ == "__main__":
    main()
