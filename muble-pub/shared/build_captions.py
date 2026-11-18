#!/usr/bin/env python3
"""Construit compositions/captions.html à partir des mots minutés de la voix off.

Entrée : JSON [{"text": "Muble,", "start": 7.12, "end": 7.48}, ...] (temps globaux du film).
Usage : python3 shared/build_captions.py <mots.json> <durée_film> <sortie.html> [--skip-before T]
Les groupes font 2 à 5 mots, coupés aux fins de phrase, aux pauses ≥ 0,15 s ou à 5 mots.
"""
import html
import json
import re
import sys

KEYWORDS = {
    "muble", "premium", "départ", "destination", "date", "passagers", "bagages", "véhicule",
    "coordonnées", "exact", "validation", "sécurité", "professionnel", "avance", "île-de-france",
    "simplicité", "maintenant", "déplacer", "étapes", "budget", "professionnels", "sorties", "voyages",
}

def clean(w):
    return re.sub(r"[^\wÀ-ÿ'-]", "", w).lower()

def groups(words, skip_before):
    out, cur = [], []
    for i, w in enumerate(words):
        if w["start"] < skip_before:
            continue
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        end_sentence = re.search(r"[.?!:,]$", w["text"]) is not None
        pause = nxt is not None and nxt["start"] - w["end"] >= 0.15
        if len(cur) >= 5 or (len(cur) >= 2 and (end_sentence or pause)) or nxt is None or (end_sentence and re.search(r"[.?!]$", w["text"])):
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out

def main():
    src, total, dst = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    skip_before = 0.0
    if "--skip-before" in sys.argv:
        skip_before = float(sys.argv[sys.argv.index("--skip-before") + 1])
    words = json.load(open(src))
    gs = groups(words, skip_before)
    items, js = [], []
    for gi, g in enumerate(gs):
        start = max(0.0, g[0]["start"] - 0.08)
        nxt_start = gs[gi + 1][0]["start"] - 0.08 if gi + 1 < len(gs) else total
        end = min(g[-1]["end"] + 0.35, nxt_start - 0.02, total)
        spans = []
        lit = False
        for w in g:
            t = html.escape(w["text"])
            k = clean(w["text"])
            if not lit and k in KEYWORDS:
                spans.append(f'<span class="cw acc">{t}</span>')
                lit = True
            else:
                spans.append(f'<span class="cw">{t}</span>')
        gid = f"cap-g{gi}"
        items.append(
            f'      <div id="{gid}" class="cap-g clip" data-start="{start:.3f}" data-duration="{end - start:.3f}" data-track-index="{gi % 2}"><div class="cap-pill">{" ".join(spans)}</div></div>'
        )
        js.append(
            f'      tl.fromTo("#{gid} .cap-pill", {{ opacity: 0, y: 14, scale: 0.97 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.18, ease: "power3.out" }}, {start:.3f});\n'
            f'      tl.to("#{gid} .cap-pill", {{ opacity: 0, duration: 0.1, ease: "power2.in" }}, {end - 0.1:.3f});'
        )
    doc = f"""<template>
  <style>
    @font-face {{ font-family: "Plus Jakarta Sans"; src: url("assets/fonts/PlusJakartaSans-Variable-latin.woff2") format("woff2"); font-weight: 200 800; }}
    #root {{ position: absolute; inset: 0; pointer-events: none; font-family: "Plus Jakarta Sans", sans-serif; }}
    .cap-g {{ position: absolute; left: 0; top: 1218px; width: 1080px; display: flex; justify-content: center; }}
    .cap-pill {{ max-width: 900px; padding: 14px 30px 16px; border-radius: 26px; background: rgba(30, 6, 70, 0.84); color: #fff; font-size: 50px; font-weight: 700; line-height: 1.15; letter-spacing: -0.01em; text-align: center; box-shadow: 0 10px 30px rgba(10, 0, 30, 0.35); }}
    .cap-pill .acc {{ color: #c4a6ff; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920">
{chr(10).join(items)}
    <div id="cap-driver" class="clip" data-start="0" data-duration="{total}" data-track-index="2" style="position:absolute;width:1px;height:1px;opacity:0"></div>
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      tl.to("#cap-driver", {{ opacity: 0, duration: {total} }}, 0);
{chr(10).join(js)}
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
    open(dst, "w").write(doc)
    print(f"{len(gs)} groupes écrits dans {dst}")

if __name__ == "__main__":
    main()
