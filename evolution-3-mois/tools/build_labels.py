# Generates compositions/labels.html (exercise cards, day cards, rest card, reveal title).
# Timings mirror compositions/gym.html: SLOT 2.8 s, CARD 1.4 s.
import html, pathlib

SLOT, CARD = 2.8, 1.4
EX = {
 "bench":     ("Développé couché", "Barre à la poitrine, puis pousse.", "Pectoraux · Triceps · Deltoïdes avant"),
 "incline":   ("Développé incliné", "Cible le haut des pectoraux.", "Haut des pectoraux · Deltoïdes avant · Triceps"),
 "pecdeck":   ("Écarté à la machine (ou aux câbles)", "Bras semi-tendus, referme devant toi.", "Pectoraux"),
 "rope":      ("Extension triceps à la corde", "Coudes fixes, écarte la corde.", "Triceps"),
 "overhead":  ("Extension triceps au-dessus de la tête", "Coudes vers le plafond, tends.", "Triceps (longue portion)"),
 "skull":     ("Barre front", "Coudes fixes, barre vers le front.", "Triceps"),
 "bbrow":     ("Rowing barre buste penché", "Dos droit, tire au nombril.", "Dorsaux · Trapèzes · Rhomboïdes · Biceps"),
 "cablerow":  ("Rowing poulie basse (prise large)", "Tire au buste, serre les omoplates.", "Haut du dos · Dorsaux · Deltoïdes arrière"),
 "pulldown":  ("Tirage vertical (prise large)", "Tire la barre sous le menton.", "Grand dorsal · Biceps"),
 "preacher":  ("Curl pupitre", "Bras calés, monte sans élan.", "Biceps"),
 "hammer":    ("Curl marteau", "Prise neutre, pouces vers le haut.", "Brachial · Biceps · Avant-bras"),
 "bbcurl":    ("Curl barre", "Coudes collés, monte la barre.", "Biceps"),
 "revfly":    ("Oiseau inversé à la machine", "Poitrine calée, ouvre vers l'arrière.", "Deltoïdes arrière · Trapèzes"),
 "frontraise":("Élévation frontale", "Monte devant, jusqu'aux épaules.", "Deltoïdes avant"),
 "latraise":  ("Élévation latérale", "Écarte sur les côtés, coudes souples.", "Deltoïdes moyens"),
 "dbpress":   ("Développé épaules haltères", "Pousse les haltères vers le haut.", "Deltoïdes · Triceps"),
 "pulley":    ("Extension triceps à la poulie", "Coudes collés, pousse vers le bas.", "Triceps"),
}
DAYS = [
 (1, 12.2, "Pectoraux & triceps", ["bench","incline","pecdeck","rope","overhead","skull"]),
 (2, 30.4, "Dos & biceps", ["bbrow","cablerow","pulldown","preacher","hammer","bbcurl"]),
 (4, 54.6, "Épaules isolées", ["revfly","frontraise","latraise","dbpress"]),
 (5, 67.2, "Biceps & triceps", ["pulley","overhead","skull","bbcurl","hammer","preacher"]),
]
REST = (48.6, 54.6)
START = 7.0  # this composition is mounted at film 7.0; all times below are local
L = lambda t: round(t - START, 3)

els, tw = [], []
# reveal title
els.append(f'''<div id="lb-reveal" class="clip lb-reveal" data-start="{L(8.0)}" data-duration="{round(12.1-8.0,2)}">
  <div class="lb-kicker">Le programme</div>
  <div class="lb-reveal-t"><span>5 jours</span> <span class="acc">·</span> <span>4 séances</span> <span class="acc">·</span> <span>1 repos</span></div>
</div>''')
tw.append(f'''tl.fromTo("#lb-reveal .lb-kicker", {{opacity:0, filter:"blur(8px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.2, ease:"power4.out"}}, {L(8.05)});
tl.fromTo("#lb-reveal .lb-reveal-t span", {{opacity:0, y:0, filter:"blur(10px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.16, ease:"power4.out", stagger:0.12}}, {L(9.3)});
tl.to("#lb-reveal > *", {{opacity:0, filter:"blur(10px)", duration:0.18, ease:"power3.in"}}, {L(11.85)});''')

for d, card, group, exs in DAYS:
    did = f"lb-d{d}"
    els.append(f'''<div id="{did}-card" class="clip lb-card" data-start="{L(card)}" data-duration="{CARD}">
  <div class="lb-card-day">Jour {d}</div>
  <div class="lb-card-grp">{html.escape(group)}</div>
  <div class="lb-card-n">{len(exs)} exercices</div>
</div>''')
    tw.append(f'''tl.fromTo("#{did}-card .lb-card-day", {{clipPath:"inset(100% 0% 0% 0%)", y:40}}, {{clipPath:"inset(0% 0% 0% 0%)", y:0, duration:0.32, ease:"expo.out"}}, {L(card+0.02)});
tl.fromTo("#{did}-card .lb-card-grp", {{opacity:0, filter:"blur(10px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.18, ease:"power4.out"}}, {L(card+0.2)});
tl.fromTo("#{did}-card .lb-card-n", {{opacity:0}}, {{opacity:1, duration:0.15, ease:"power2.out"}}, {L(card+0.12)});
tl.to("#{did}-card > *", {{opacity:0, filter:"blur(12px)", x:-40, duration:0.16, ease:"power3.in", stagger:0.03}}, {L(card+CARD-0.22)});''')
    t_day0 = card + CARD
    els.append(f'''<div id="{did}-head" class="clip lb-head" data-start="{L(t_day0)}" data-duration="{round(len(exs)*SLOT,2)}"><b>Jour {d}</b> · {html.escape(group)}</div>''')
    tw.append(f'''tl.fromTo("#{did}-head", {{opacity:0}}, {{opacity:1, duration:0.2, ease:"power2.out"}}, {L(t_day0)});''')
    for k, e in enumerate(exs):
        name, expl, mus = EX[e]
        t0 = t_day0 + k*SLOT
        eid = f"{did}-e{k+1}"
        els.append(f'''<div id="{eid}" class="clip lb-ex" data-start="{L(t0+0.12)}" data-duration="{round(SLOT-0.12,2)}">
  <div class="lb-idx">{k+1:02d} <span>/ {len(exs):02d}</span></div>
  <div class="lb-name">{html.escape(name)}</div>
  <div class="lb-sets">3 × 10 à 12</div>
  <div class="lb-expl">{html.escape(expl)}</div>
  <div class="lb-mus">{html.escape(mus)}</div>
</div>''')
        tw.append(f'''tl.fromTo("#{eid} .lb-idx", {{opacity:0}}, {{opacity:1, duration:0.12}}, {L(t0+0.14)});
tl.fromTo("#{eid} .lb-name", {{clipPath:"inset(0% 100% 0% 0%)"}}, {{clipPath:"inset(0% 0% 0% 0%)", duration:0.3, ease:"power3.out"}}, {L(t0+0.16)});
tl.fromTo("#{eid} .lb-sets", {{opacity:0, filter:"blur(8px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.14, ease:"power4.out"}}, {L(t0+0.26)});
tl.fromTo("#{eid} .lb-expl", {{opacity:0, filter:"blur(6px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.16, ease:"power4.out"}}, {L(t0+0.3)});
tl.fromTo("#{eid} .lb-mus", {{opacity:0}}, {{opacity:1, duration:0.16, ease:"power2.out"}}, {L(t0+0.38)});
tl.to("#{eid} > *", {{opacity:0, filter:"blur(8px)", duration:0.12, ease:"power3.in", stagger:0.015}}, {L(t0+SLOT-0.17)});''')
    if d == 2:
        r0, r1 = REST
        els.append(f'''<div id="lb-rest" class="clip lb-card lb-rest" data-start="{L(r0)}" data-duration="{round(r1-r0,2)}">
  <div class="lb-card-day">Jour 3</div>
  <div class="lb-card-grp">Repos</div>
  <div class="lb-card-n">Récupération · sommeil · nutrition</div>
</div>''')
        tw.append(f'''tl.fromTo("#lb-rest .lb-card-day", {{clipPath:"inset(100% 0% 0% 0%)", y:40}}, {{clipPath:"inset(0% 0% 0% 0%)", y:0, duration:0.4, ease:"expo.out"}}, {L(r0+0.1)});
tl.fromTo("#lb-rest .lb-card-grp", {{opacity:0, filter:"blur(10px)"}}, {{opacity:1, filter:"blur(0px)", duration:0.3, ease:"power4.out"}}, {L(r0+0.5)});
tl.fromTo("#lb-rest .lb-card-n", {{opacity:0}}, {{opacity:1, duration:0.3}}, {L(r0+1.2)});
tl.to("#lb-rest > *", {{opacity:0, filter:"blur(12px)", duration:0.2, ease:"power3.in", stagger:0.04}}, {L(r1-0.35)});''')

DUR = round(85.4 - START, 2)
out = f'''<template>
  <style>
    #root {{ position:absolute; inset:0; font-family:"Montserrat", sans-serif; color:#f3f4f6; pointer-events:none; }}
    #lb-scrim {{ position:absolute; left:0; top:0; width:1100px; height:1080px;
      background: linear-gradient(90deg, rgba(12,13,16,0.82) 0%, rgba(12,13,16,0.62) 45%, rgba(12,13,16,0) 100%); }}
    .lb-head {{ position:absolute; left:200px; top:132px; font-family:"Oswald", sans-serif; font-weight:500; font-size:34px;
      letter-spacing:0.06em; text-transform:uppercase; color:#c9ced6; }}
    .lb-head b {{ color:var(--accent,#ff4d2e); font-weight:700; }}
    .lb-ex {{ position:absolute; left:200px; top:300px; width:780px; }}
    .lb-idx {{ font-family:"Oswald", sans-serif; font-weight:700; font-size:46px; color:var(--accent,#ff4d2e); letter-spacing:0.02em; }}
    .lb-idx span {{ color:#7d8592; font-weight:500; }}
    .lb-name {{ margin-top:6px; font-family:"Oswald", sans-serif; font-weight:700; font-size:80px; line-height:0.98;
      text-transform:uppercase; letter-spacing:-0.005em; color:#ffffff; }}
    .lb-sets {{ margin-top:22px; font-family:"Oswald", sans-serif; font-weight:600; font-size:58px; color:var(--accent,#ff4d2e); }}
    .lb-expl {{ margin-top:14px; font-size:34px; font-weight:600; line-height:1.25; color:#e3e6eb; max-width:740px; }}
    .lb-mus {{ margin-top:18px; font-size:30px; font-weight:700; color:#ff9a84; max-width:760px; }}
    .lb-card {{ position:absolute; left:200px; top:330px; }}
    .lb-card-day {{ font-family:"Oswald", sans-serif; font-weight:700; font-size:250px; line-height:0.9; text-transform:uppercase;
      color:#ffffff; letter-spacing:-0.01em; }}
    .lb-card-grp {{ margin-top:18px; font-family:"Oswald", sans-serif; font-weight:600; font-size:76px; text-transform:uppercase;
      color:var(--accent,#ff4d2e); }}
    .lb-card-n {{ margin-top:14px; font-size:34px; font-weight:600; color:#d4d8de; }}
    .lb-rest .lb-card-grp {{ color:#8fb4ff; }}
    .lb-reveal {{ position:absolute; left:200px; top:400px; }}
    .lb-kicker {{ font-family:"Oswald", sans-serif; font-weight:700; font-size:128px; text-transform:uppercase; line-height:1; }}
    .lb-reveal-t {{ margin-top:22px; font-family:"Oswald", sans-serif; font-weight:500; font-size:56px; text-transform:uppercase; color:#e3e6eb; }}
    .lb-reveal-t span {{ display:inline-block; }}
    .acc {{ color:var(--accent,#ff4d2e); }}
  </style>
  <div id="root" data-composition-id="labels" data-width="1920" data-height="1080">
    <div id="lb-scrim" class="clip" data-start="{L(7.6)}" data-duration="{round(85.4-7.6,2)}"></div>
{chr(10).join(els)}
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      tl.fromTo("#lb-scrim", {{opacity:0}}, {{opacity:1, duration:0.6, ease:"power2.out"}}, {L(7.6)});
{chr(10).join(tw)}
      window.__timelines = window.__timelines || {{}};
      window.__timelines["labels"] = tl;
    }})();
  </script>
</template>
'''
pathlib.Path(__file__).resolve().parent.parent.joinpath("compositions/labels.html").write_text(out, encoding="utf-8")
print("labels.html written, duration", DUR)
