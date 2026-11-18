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

MAXC = 30

def _len(ws):
    return len(" ".join(x["text"] for x in ws))

def _balanced(ws):
    """Coupe une suite de mots en parts de longueur proche, chacune ≤ MAXC si possible."""
    if _len(ws) <= MAXC or len(ws) == 1:
        return [ws]
    k = -(-_len(ws) // MAXC)
    if k == 2:
        best = min(range(1, len(ws)), key=lambda i: max(_len(ws[:i]), _len(ws[i:])))
        return [ws[:best], ws[best:]]
    target = _len(ws) / k
    parts, cur = [], []
    for w in ws:
        if cur and _len(cur + [w]) > target * 1.12 and len(parts) < k - 1:
            parts.append(cur); cur = []
        cur.append(w)
    parts.append(cur)
    return parts

def groups(words, skip_before):
    """Phrases → propositions (virgules) → groupes ≤ 30 caractères, équilibrés, jamais à cheval sur deux phrases."""
    out, sent = [], []
    def flush_sentence():
        if not sent:
            return
        clauses, cur = [], []
        for w in sent:
            cur.append(w)
            if w["text"].endswith(","):
                clauses.append(cur); cur = []
        if cur:
            clauses.append(cur)
        merged, acc = [], []
        for c in clauses:
            if acc and _len(acc + c) > MAXC and _len(acc) >= 12:
                merged.append(acc); acc = []
            acc = acc + c
        if acc:
            merged.append(acc)
        for m in merged:
            out.extend(_balanced(m))
        sent.clear()
    prev = None
    for w in words:
        if w["start"] < skip_before:
            continue
        if prev is not None and (w.get("line") != prev.get("line") or w["start"] - prev["end"] > 0.6):
            flush_sentence()
        sent.append(w); prev = w
        if re.search(r"[.?!:]$", w["text"]):
            flush_sentence()
    flush_sentence()
    return out

def main():
    src, total, dst = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    skip = []  # plages [début, fin] sans sous-titres, ex. --skip 0:5 66.4:72
    if "--skip" in sys.argv:
        for r in sys.argv[sys.argv.index("--skip") + 1:]:
            if ":" not in r:
                break
            a, b = r.split(":"); skip.append((float(a), float(b)))
    words = [w for w in json.load(open(src)) if not any(a <= w["start"] < b for a, b in skip)]
    gs = groups(words, 0.0)
    items, js = [], []
    for gi, g in enumerate(gs):
        start = max(0.0, g[0]["start"] - 0.08)
        nxt_start = gs[gi + 1][0]["start"] - 0.08 if gi + 1 < len(gs) else total
        end = min(g[-1]["end"] + 0.35, nxt_start - 0.02, total)
        for a, b in skip:
            if start < a < end:
                end = a
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
    .cap-g {{ position: absolute; left: 0; top: 1170px; width: 1000px; display: flex; justify-content: center; }}
    .cap-pill {{ max-width: 820px; padding: 14px 28px 16px; border-radius: 26px; background: rgba(30, 6, 70, 0.84); color: #fff; font-size: 47px; font-weight: 700; line-height: 1.15; letter-spacing: -0.01em; text-align: center; box-shadow: 0 10px 30px rgba(10, 0, 30, 0.35); }}
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
