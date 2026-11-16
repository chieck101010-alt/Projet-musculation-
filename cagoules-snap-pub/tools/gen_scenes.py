#!/usr/bin/env python3
"""Generates the static HTML scenes of the cagoules ad (authoring-time only)."""
import random, os, sys

OUT = sys.argv[1]
BAR = 1.6667  # 144 bpm, 4 beats

OUTER = "M34 540 C 52 500 86 474 100 446 C 60 398 46 318 50 222 C 56 92 126 26 200 26 C 274 26 344 92 350 222 C 354 318 340 398 300 446 C 314 474 348 500 366 540 Z"
HOLE = "M200 150 C 252 150 282 198 282 262 C 282 334 248 372 200 372 C 152 372 118 334 118 262 C 118 198 148 150 200 150 Z"


def bala(p, color, width, extra_attr=""):
    """Inline SVG balaclava (stylised placeholder for a product photo). p = unique id prefix."""
    return f"""<svg class="bala" viewBox="0 0 400 540" width="{width}" height="{round(width*1.35)}" {extra_attr}>
  <defs>
    <pattern id="{p}-knit" width="10" height="12" patternUnits="userSpaceOnUse">
      <path d="M0 0 L5 6 L10 0 M0 6 L5 12 L10 6" stroke="rgba(0,0,0,.32)" stroke-width="1.5" fill="none"/>
      <path d="M0 2 L5 8 L10 2" stroke="rgba(255,255,255,.12)" stroke-width="1" fill="none"/>
    </pattern>
    <pattern id="{p}-rib" width="9" height="40" patternUnits="userSpaceOnUse"><rect width="4.5" height="40" fill="rgba(0,0,0,.26)"/></pattern>
    <radialGradient id="{p}-light" cx="34%" cy="22%" r="85%">
      <stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity=".6"/>
    </radialGradient>
    <radialGradient id="{p}-hole" cx="50%" cy="38%" r="62%">
      <stop offset="0" stop-color="#000"/><stop offset=".8" stop-color="#060606"/><stop offset="1" stop-color="#202020"/>
    </radialGradient>
    <clipPath id="{p}-clip"><path d="{OUTER}"/></clipPath>
  </defs>
  <path d="{OUTER}" fill="{color}"/>
  <g clip-path="url(#{p}-clip)">
    <rect width="400" height="540" fill="url(#{p}-knit)"/>
    <rect y="448" width="400" height="92" fill="url(#{p}-rib)"/>
    <path d="M86 446 Q200 474 314 446" stroke="rgba(0,0,0,.45)" stroke-width="4" fill="none"/>
    <path d="M200 22 L200 148" stroke="rgba(0,0,0,.4)" stroke-width="3" fill="none"/>
    <path d="M64 230 C 72 330 100 410 150 448" stroke="rgba(0,0,0,.18)" stroke-width="3" fill="none"/>
    <path d="M340 230 C 330 330 300 410 250 448" stroke="rgba(0,0,0,.18)" stroke-width="3" fill="none"/>
    <rect width="400" height="540" fill="url(#{p}-light)"/>
  </g>
  <path d="{HOLE}" fill="none" stroke="{color}" stroke-width="22"/>
  <path d="{HOLE}" fill="none" stroke="rgba(0,0,0,.35)" stroke-width="22" stroke-dasharray="3 4"/>
  <path d="{HOLE}" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2.5" transform="translate(200 261) scale(1.075) translate(-200 -261)"/>
  <path d="{HOLE}" fill="url(#{p}-hole)"/>
</svg>"""


HEAD = """<template>
  <style>
    #root { position:absolute; inset:0; overflow:hidden; font-family:"Archivo Black", sans-serif; color:#f2f2f2; }
    #root .abs { position:absolute; }
    #root .lg { font-family:"League Gothic", sans-serif; text-transform:uppercase; line-height:.86; letter-spacing:.005em; }
    #root .mono { font-family:"Space Mono", monospace; text-transform:uppercase; letter-spacing:.08em; }
    #root .center-x { left:0; width:1080px; text-align:center; }
%CSS%
  </style>
"""

def write(name, css, body, script, dur, comp_id):
    html = HEAD.replace("%CSS%", css) + f"""  <div id="root" data-composition-id="{comp_id}" data-width="1080" data-height="1920">
{body}
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
{script}
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{comp_id}"] = tl;
    }})();
  </script>
</template>
"""
    with open(os.path.join(OUT, "compositions", name), "w") as f:
        f.write(html)

# ---------------------------------------------------------------- S1 HOOK
D1 = round(2 * BAR, 3)
row = "CAGOULES ✕ CAGOULES ✕ CAGOULES ✕ CAGOULES ✕ "
css1 = """
    #h-bg { inset:0; background:radial-gradient(120% 70% at 50% 62%, #222226 0%, #0a0a0a 62%); }
    .h-row { left:0; white-space:nowrap; font-size:300px; color:transparent; -webkit-text-stroke:2px #34343a; }
    #h-row1 { top:560px; } #h-row2 { top:860px; } #h-row3 { top:1160px; }
    #h-prod { left:300px; top:610px; width:480px; height:648px; }
    #h-shadow { left:290px; top:1235px; width:500px; height:60px; border-radius:50%; background:radial-gradient(closest-side, rgba(0,0,0,.85), rgba(0,0,0,0)); }
    .h-line { font-size:178px; }
    #h-l1 { top:250px; } #h-l2 { top:400px; } #h-l3 { top:550px; color:#FFFC00; }
    #h-tag { top:330px; left:110px; width:860px; height:190px; background:#FFFC00; color:#0a0a0a; display:flex; align-items:center; justify-content:center; white-space:nowrap; font-size:96px; letter-spacing:-.02em; transform-origin:50% 50%; }
    #h-sub { top:550px; font-size:34px; color:#d6d6d6; }
    #h-flash { inset:0; background:#fff; opacity:0; }
"""
body1 = f"""    <div id="h-bg" class="abs"></div>
    <div id="h-row1" class="abs lg h-row">{row}</div>
    <div id="h-row2" class="abs lg h-row">{row}</div>
    <div id="h-row3" class="abs lg h-row">{row}</div>
    <div id="h-shadow" class="abs"></div>
    <div id="h-prod" class="abs">{bala("h1", "#1f1f22", 480)}</div>
    <div id="h-l1" class="abs lg center-x h-line">T'as pas</div>
    <div id="h-l2" class="abs lg center-x h-line">encore</div>
    <div id="h-l3" class="abs lg center-x h-line">la tienne ?</div>
    <div id="h-tag" class="abs">CAGOULES NIKE</div>
    <div id="h-sub" class="abs mono center-x">Sélection streetwear</div>
    <div id="h-flash" class="abs"></div>"""
B = 0.4167
js1 = f"""
      tl.fromTo("#h-row1", {{ x: 0 }}, {{ x: -700, duration: {D1}, ease: "none" }}, 0);
      tl.fromTo("#h-row2", {{ x: -700 }}, {{ x: 0, duration: {D1}, ease: "none" }}, 0);
      tl.fromTo("#h-row3", {{ x: -200 }}, {{ x: -900, duration: {D1}, ease: "none" }}, 0);
      // product is on screen at frame 0, punches on every beat
      tl.fromTo("#h-prod", {{ scale: 0.94, rotation: -3 }}, {{ scale: 1, rotation: 0, duration: 0.3, ease: "expo.out" }}, 0);
      [{B}, {2*B}, {3*B}].forEach((t, i) => {{
        tl.to("#h-prod", {{ scale: 1.07, rotation: i % 2 ? 2 : -2, duration: 0.03, ease: "none" }}, t - 0.03);
        tl.to("#h-prod", {{ scale: 1, rotation: 0, duration: 0.3, ease: "power3.out" }}, t);
      }});
      gsap.set("#h-l2, #h-l3, #h-tag, #h-sub", {{ opacity: 0 }});
      tl.fromTo("#h-l2", {{ opacity: 0, scale: 1.7 }}, {{ opacity: 1, scale: 1, duration: 0.14, ease: "power4.out" }}, {B});
      tl.fromTo("#h-l3", {{ opacity: 0, scale: 1.7 }}, {{ opacity: 1, scale: 1, duration: 0.14, ease: "power4.out" }}, {2*B});
      // bar 2: the question flips into the product name
      tl.to("#h-l1, #h-l2, #h-l3", {{ yPercent: -60, opacity: 0, duration: 0.14, ease: "power3.in", stagger: 0.03 }}, {BAR - 0.16});
      tl.fromTo("#h-tag", {{ opacity: 0, scaleX: 0, skewX: -14 }}, {{ opacity: 1, scaleX: 1, skewX: -6, duration: 0.22, ease: "expo.out" }}, {BAR});
      tl.fromTo("#h-tag", {{ x: -14 }}, {{ x: 0, duration: 0.24, ease: "rough({{ strength: 2, points: 8, randomize: false }})" }}, {BAR + 0.02});
      tl.fromTo("#h-sub", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }}, {BAR + 0.08});
      tl.to("#h-prod", {{ scale: 1.12, duration: 0.03, ease: "none" }}, {BAR - 0.03});
      tl.to("#h-prod", {{ scale: 1.02, duration: 0.47, ease: "expo.out" }}, {BAR});
      tl.to("#h-prod", {{ scale: 1.1, duration: {BAR - 0.6}, ease: "power1.in" }}, {BAR + 0.5});
      tl.to("#h-flash", {{ opacity: 1, duration: 0.12, ease: "power2.in" }}, {D1 - 0.13});
"""
write("hook.html", css1, body1, js1, D1, "hook")

# ---------------------------------------------------------------- S2 MODELS
models = [
    ("noir", "Noir ébène", "#1f1f22", "#0b0b0c", "#2a2a2e", "#f2f2f2"),
    ("gris", "Gris chiné", "#8e8e93", "#2b2b2f", "#3c3c42", "#f2f2f2"),
    ("blanc", "Blanc glacier", "#ececec", "#cfcfd2", "#bdbdc2", "#0a0a0a"),
    ("kaki", "Kaki army", "#5b6146", "#1d2017", "#2e3325", "#f2f2f2"),
]
D2 = round(4 * BAR, 3)
css2 = """
    .m-block { inset:0; }
    .m-bg { inset:0; }
    .m-giant { top:760px; left:0; white-space:nowrap; font-size:560px; color:transparent; }
    .m-count { top:240px; font-size:30px; }
    .m-name { top:318px; font-size:168px; }
    .m-prod { left:280px; top:470px; width:520px; height:702px; }
    .m-shadow { left:260px; top:1150px; width:580px; height:64px; border-radius:50%; background:radial-gradient(closest-side, rgba(0,0,0,.6), rgba(0,0,0,0)); }
    .m-pill { top:1196px; left:200px; width:680px; height:76px; border:3px solid currentColor; border-radius:38px; display:flex; align-items:center; justify-content:center; gap:22px; font-size:28px; }
    .m-dot { width:28px; height:28px; border-radius:50%; border:3px solid currentColor; }
    .m-ticks { top:214px; left:340px; width:400px; height:8px; display:flex; gap:12px; }
    .m-tick { flex:1; height:8px; border-radius:4px; }
"""
body2 = []
js2 = ""
for i, (k, name, col, bg, giant, ink) in enumerate(models):
    s = round(i * BAR, 3)
    ticks = "".join(
        f'<div class="m-tick" style="background:{("#FFFC00" if j == i else (ink + "33" if ink.startswith("#0") else "rgba(255,255,255,.22)"))}"></div>'
        for j in range(4))
    body2.append(f"""    <div id="m-{k}" class="abs m-block clip" data-start="{s}" data-duration="{round(BAR,3) if i < 3 else round(D2 - s, 3)}" style="color:{ink}">
      <div class="abs m-bg" style="background:radial-gradient(100% 60% at 50% 60%, {giant} 0%, {bg} 70%)"></div>
      <div id="m-{k}-giant" class="abs lg m-giant" style="-webkit-text-stroke:3px {giant if k != 'blanc' else '#b0b0b5'}">{k} {k} {k}</div>
      <div class="abs m-ticks">{ticks}</div>
      <div id="m-{k}-count" class="abs mono center-x m-count">Modèle 0{i+1} / 04</div>
      <div id="m-{k}-name" class="abs lg center-x m-name">{name}</div>
      <div id="m-{k}-shadow" class="abs m-shadow"></div>
      <div id="m-{k}-prod" class="abs m-prod">{bala("m" + k, col, 520)}</div>
      <div id="m-{k}-pill" class="abs mono m-pill"><span class="m-dot" style="background:{col}"></span>Cagoule Nike · coloris {k}</div>
    </div>""")
    js2 += f"""
      tl.fromTo("#m-{k}-giant", {{ x: -80 }}, {{ x: -560, duration: {BAR}, ease: "none" }}, {s});
      tl.fromTo("#m-{k}-prod", {{ x: 760, skewX: -18, rotation: 8 }}, {{ x: 0, skewX: 0, rotation: 0, duration: 0.32, ease: "expo.out" }}, {s});
      tl.fromTo("#m-{k}-prod", {{ scale: 1 }}, {{ scale: 1.06, duration: {round(BAR - 0.52, 3)}, ease: "none" }}, {s + 0.3});
      tl.fromTo("#m-{k}-name", {{ y: 70, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.26, ease: "power4.out" }}, {s + 0.04});
      tl.fromTo("#m-{k}-count", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.12 }}, {s});
      tl.fromTo("#m-{k}-pill", {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.24, ease: "power3.out" }}, {s + 0.16});
      tl.fromTo("#m-{k}-shadow", {{ opacity: 0, scaleX: .4 }}, {{ opacity: 1, scaleX: 1, duration: 0.3, ease: "expo.out" }}, {s});"""
    if i < 3:
        js2 += f"""
      tl.to("#m-{k}-prod", {{ x: -760, skewX: 18, duration: 0.18, ease: "power3.in" }}, {s + BAR - 0.19});
      tl.to("#m-{k}-name, #m-{k}-pill", {{ opacity: 0, duration: 0.12 }}, {s + BAR - 0.13});"""
    else:
        js2 += f"""
      tl.to("#m-{k}-prod", {{ scale: 1.6, y: -80, opacity: 0, duration: 0.2, ease: "power3.in" }}, {D2 - 0.21});"""
write("models.html", css2, "\n".join(body2), js2, D2, "models")

# ---------------------------------------------------------------- S3 DETAILS
D3 = round(2 * BAR, 3)
W3 = 760
S3 = W3 / 400
def cam(px, py, sc):
    return round((200 - px) * S3 * sc), round((270 - py) * S3 * sc)
shots = [
    ("01", "Maille épaisse", 300, 330, 3.6),
    ("02", "Coupe ajustée", 132, 200, 2.5),
    ("03", "Finitions nettes", 200, 492, 2.4),
]
css3 = f"""
    #d-bg {{ inset:0; background:radial-gradient(90% 55% at 50% 52%, #26262b 0%, #0b0b0c 70%); }}
    #d-view {{ left:70px; top:500px; width:940px; height:800px; overflow:hidden; border-radius:28px; background:radial-gradient(80% 70% at 50% 45%, #3a3a40, #121214); }}
    #d-cam {{ left:{470 - W3//2}px; top:{400 - round(W3*1.35)//2}px; width:{W3}px; height:{round(W3*1.35)}px; }}
    .d-corner {{ width:70px; height:70px; border-color:#FFFC00; border-style:solid; border-width:0; }}
    #d-c1 {{ left:96px; top:526px; border-top-width:6px; border-left-width:6px; }}
    #d-c2 {{ left:914px; top:526px; border-top-width:6px; border-right-width:6px; }}
    #d-c3 {{ left:96px; top:1204px; border-bottom-width:6px; border-left-width:6px; }}
    #d-c4 {{ left:914px; top:1204px; border-bottom-width:6px; border-right-width:6px; }}
    #d-kicker {{ top:250px; font-size:30px; color:#FFFC00; }}
    .d-title {{ top:300px; font-size:176px; }}
    #d-zoom {{ left:120px; top:552px; font-size:28px; color:#FFFC00; background:rgba(0,0,0,.55); padding:6px 14px; border-radius:6px; }}
    #d-final {{ top:300px; font-size:176px; color:#FFFC00; }}
"""
titles = "\n".join(f'    <div id="d-t{n}" class="abs lg center-x d-title">{t}</div>' for n, t, *_ in shots)
body3 = f"""    <div id="d-bg" class="abs"></div>
    <div id="d-kicker" class="abs mono center-x">Dans le détail</div>
{titles}
    <div id="d-final" class="abs lg center-x">Qualité visible.</div>
    <div id="d-view" class="abs"><div id="d-cam" class="abs">{bala("d", "#8e8e93", W3)}</div></div>
    <div id="d-c1" class="abs d-corner"></div><div id="d-c2" class="abs d-corner"></div>
    <div id="d-c3" class="abs d-corner"></div><div id="d-c4" class="abs d-corner"></div>
    <div id="d-zoom" class="abs mono">Zoom ×3.6</div>"""
js3 = """
      gsap.set("#d-t02, #d-t03, #d-final", { opacity: 0 });
      tl.fromTo("#d-c1, #d-c2, #d-c3, #d-c4", { scale: 1.5, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.25, ease: "expo.out" }, 0);"""
seg = [0, 0.8, 1.6, 2.2]
for i, (n, t, px, py, sc) in enumerate(shots):
    x, y = cam(px, py, sc)
    x2, y2 = cam(px + (14 if i != 2 else 0), py - 8, sc * 1.12)
    st, en = seg[i], seg[i + 1]
    js3 += f"""
      tl.set("#d-cam", {{ x: {x}, y: {y}, scale: {sc} }}, {st});
      tl.to("#d-cam", {{ x: {x2}, y: {y2}, scale: {round(sc*1.12,3)}, duration: {round(en-st,3)}, ease: "none" }}, {st});
      tl.set("#d-zoom", {{ textContent: "Zoom ×{sc}".replace(".", ",") }}, {st});
      tl.fromTo("#d-t{n}", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.22, ease: "power4.out" }}, {st + 0.02});
      tl.to("#d-t{n}", {{ opacity: 0, y: -40, duration: 0.12, ease: "power2.in" }}, {round(en - 0.12,3)});
      tl.to("#d-view", {{ scale: {0.97 if st > 0 else 1}, duration: 0.02, ease: "none" }}, {max(st - 0.04, 0)});
      tl.to("#d-view", {{ scale: 1, duration: 0.25, ease: "expo.out" }}, {st + (0 if st > 0 else 0.02)});"""
js3 += f"""
      tl.to("#d-cam", {{ x: 0, y: 0, scale: 0.92, duration: 0.3, ease: "expo.inOut" }}, 2.2);
      tl.to("#d-zoom", {{ opacity: 0, duration: 0.1 }}, 2.2);
      tl.fromTo("#d-final", {{ opacity: 0, scale: 1.5 }}, {{ opacity: 1, scale: 1, duration: 0.18, ease: "power4.out" }}, 2.22);
      tl.to("#d-cam", {{ scale: 0.96, duration: {round(D3 - 2.5, 3)}, ease: "none" }}, 2.5);
"""
write("details.html", css3, body3, js3, D3, "details")

# ---------------------------------------------------------------- S4 URBAN
D4 = round(2 * BAR, 3)
rnd = random.Random(7)
blds, x = [], -20
while x < 1100:
    w = rnd.randint(110, 230)
    h = rnd.randint(520, 1050)
    wins = []
    for wy in range(40, h - 40, 52):
        for wx in range(22, w - 30, 40):
            if rnd.random() < 0.18:
                c = rnd.choice(["#ffd66b", "#ffe9a8", "#9fc3ff"])
                wins.append(f'<i style="left:{wx}px;top:{wy}px;background:{c}"></i>')
    shade = rnd.choice(["#0d0e13", "#111219", "#15161e"])
    blds.append(f'<div class="u-b" style="left:{x}px;width:{w}px;height:{h}px;background:{shade}">{"".join(wins)}</div>')
    x += w + rnd.randint(-10, 12)
rain = "".join(
    f'<i style="left:{rnd.randint(0,1080)}px;top:{rnd.randint(0,3840)}px;height:{rnd.randint(40,110)}px;opacity:{rnd.uniform(.15,.5):.2f}"></i>'
    for _ in range(140))
css4 = """
    #u-sky { inset:0; background:linear-gradient(#050608 0%, #11131b 55%, #1d1a20 100%); }
    #u-city { left:0; bottom:0; width:1080px; height:1100px; }
    .u-b { position:absolute; bottom:0; }
    .u-b i { position:absolute; width:16px; height:24px; opacity:.85; }
    #u-glow { left:540px; top:640px; width:900px; height:1300px; margin-left:-450px; background:radial-gradient(closest-side, rgba(255,252,0,.20), rgba(255,252,0,0)); }
    #u-lamp { left:536px; top:560px; width:8px; height:60px; background:#2b2b30; }
    #u-lampbulb { left:500px; top:612px; width:80px; height:18px; border-radius:9px; background:#fff7b0; box-shadow:0 0 60px 20px rgba(255,247,176,.55); }
    #u-cone { left:240px; top:628px; width:600px; height:1300px; background:linear-gradient(rgba(255,247,176,.22), rgba(255,247,176,0) 80%); clip-path:polygon(42% 0, 58% 0, 100% 100%, 0 100%); }
    #u-rain { left:0; top:0; width:1080px; height:3840px; }
    #u-rain i { position:absolute; width:2px; background:linear-gradient(rgba(220,230,255,0), rgba(220,230,255,.9)); transform:rotate(8deg); }
    #u-fig { left:190px; top:780px; width:700px; height:1140px; }
    .u-t { font-size:200px; }
    #u-l1 { top:250px; } #u-l2 { top:420px; color:#FFFC00; font-size:250px; }
    #u-l3 { top:250px; } #u-l4 { top:420px; color:#FFFC00; font-size:176px; }
    #u-flash { inset:0; background:#dfe6ff; opacity:0; }
    #u-world { inset:0; }
"""
fig = f"""<svg viewBox="0 0 700 1140" width="700" height="1140">
  <defs><linearGradient id="u-hood" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fffc00" stop-opacity=".35"/><stop offset=".12" stop-color="#0c0c0f"/><stop offset=".88" stop-color="#0c0c0f"/><stop offset="1" stop-color="#9fc3ff" stop-opacity=".35"/>
  </linearGradient></defs>
  <path d="M30 1140 C 40 760 120 610 260 560 L440 560 C 580 610 660 760 670 1140 Z" fill="url(#u-hood)"/>
  <path d="M200 600 C 260 650 440 650 500 600 L470 700 C 410 730 290 730 230 700 Z" fill="#050507"/>
</svg>"""
body4 = f"""    <div id="u-world" class="abs">
      <div id="u-sky" class="abs"></div>
      <div id="u-city" class="abs">{"".join(blds)}</div>
      <div id="u-glow" class="abs"></div>
      <div id="u-cone" class="abs"></div>
      <div id="u-lamp" class="abs"></div>
      <div id="u-lampbulb" class="abs"></div>
      <div id="u-fig" class="abs">{fig}<div id="u-head" class="abs" style="left:170px;top:90px">{bala("u", "#1a1a1d", 360)}</div></div>
      <div id="u-rain" class="abs">{rain}</div>
    </div>
    <div id="u-l1" class="abs lg center-x u-t">Faite pour</div>
    <div id="u-l2" class="abs lg center-x u-t">la rue.</div>
    <div id="u-l3" class="abs lg center-x u-t">Style street.</div>
    <div id="u-l4" class="abs lg center-x u-t">Zéro compromis.</div>
    <div id="u-flash" class="abs"></div>"""
js4 = f"""
      gsap.set("#u-l2, #u-l3, #u-l4", {{ opacity: 0 }});
      tl.fromTo("#u-world", {{ scale: 1.0 }}, {{ scale: 1.1, duration: {D4}, ease: "none", transformOrigin: "50% 70%" }}, 0);
      tl.fromTo("#u-rain", {{ y: -1920 }}, {{ y: -200, duration: {D4}, ease: "none" }}, 0);
      tl.fromTo("#u-fig", {{ y: 260 }}, {{ y: 0, duration: 0.6, ease: "expo.out" }}, 0);
      tl.fromTo("#u-l1", {{ opacity: 0, x: -120 }}, {{ opacity: 1, x: 0, duration: 0.2, ease: "power4.out" }}, 0.05);
      tl.fromTo("#u-l2", {{ opacity: 0, scale: 1.6 }}, {{ opacity: 1, scale: 1, duration: 0.16, ease: "power4.out" }}, {B});
      tl.to("#u-l1, #u-l2", {{ opacity: 0, duration: 0.08 }}, {BAR - 0.08});
      tl.to("#u-flash", {{ opacity: 0.85, duration: 0.02, ease: "none" }}, {BAR - 0.02});
      tl.to("#u-flash", {{ opacity: 0, duration: 0.35, ease: "power2.out" }}, {BAR});
      tl.fromTo("#u-world", {{ x: -18 }}, {{ x: 0, duration: 0.35, ease: "rough({{ strength: 3, points: 10, randomize: false }})" }}, {BAR});
      tl.fromTo("#u-l3", {{ opacity: 0, x: 120 }}, {{ opacity: 1, x: 0, duration: 0.2, ease: "power4.out" }}, {BAR});
      tl.fromTo("#u-l4", {{ opacity: 0, scale: 1.6 }}, {{ opacity: 1, scale: 1, duration: 0.16, ease: "power4.out" }}, {BAR + B});
      tl.to("#u-l3, #u-l4", {{ opacity: 0, duration: 0.1 }}, {D4 - 0.12});
"""
write("urban.html", css4, body4, js4, D4, "urban")

# ---------------------------------------------------------------- S5 CTA
D5 = 5.833
css5 = """
    #c-bg { inset:0; background:#0a0a0a; }
    #c-yellow { inset:0; background:#FFFC00; clip-path:polygon(100% 0, 100% 0, 100% 0, 100% 0); }
    .c-t { color:#0a0a0a; }
    #c-l1 { top:250px; font-size:230px; }
    #c-l2 { top:440px; font-size:300px; }
    #c-card { left:110px; top:740px; width:860px; height:330px; background:#0a0a0a; border-radius:44px; }
    #c-label { top:62px; left:0; width:860px; text-align:center; font-size:30px; color:#FFFC00; }
    #c-handle-wrap { top:120px; left:0; width:860px; height:150px; overflow:hidden; text-align:center; }
    #c-handle { display:inline-block; font-size:112px; color:#fff; letter-spacing:-.02em; line-height:150px; }
    #c-btn { left:250px; top:1100px; width:580px; height:120px; border-radius:60px; background:#0a0a0a; color:#FFFC00; display:flex; align-items:center; justify-content:center; font-size:52px; letter-spacing:.02em; }
    #c-ripple { left:470px; top:1090px; width:140px; height:140px; border-radius:50%; border:6px solid #0a0a0a; opacity:0; }
    #c-note { top:1240px; font-size:28px; color:#0a0a0a; }
    #c-row { left:0; top:1430px; width:1080px; height:300px; display:flex; justify-content:center; gap:30px; }
    #c-row .c-mini { width:200px; height:270px; }
"""
minis = "".join(f'<div id="c-mini-{k}" class="c-mini">{bala("c" + k, col, 200)}</div>' for k, _, col, *_ in models)
body5 = f"""    <div id="c-bg" class="abs"></div>
    <div id="c-yellow" class="abs"></div>
    <div id="c-l1" class="abs lg center-x c-t">Rejoins</div>
    <div id="c-l2" class="abs lg center-x c-t">le snap</div>
    <div id="c-card" class="abs">
      <div id="c-label" class="abs mono">Ajoute-nous sur Snapchat</div>
      <div id="c-handle-wrap" class="abs"><span id="c-handle" data-var-text="handle">@TON.SNAP</span></div>
    </div>
    <div id="c-btn" class="abs">+ AJOUTER</div>
    <div id="c-ripple" class="abs"></div>
    <div id="c-note" class="abs mono center-x">Commande direct en message</div>
    <div id="c-row" class="abs">{minis}</div>"""
js5 = """
      tl.to("#c-yellow", { clipPath: "polygon(-60% 0, 100% 0, 100% 100%, 0% 100%)", duration: 0.3, ease: "expo.out" }, 0);
      tl.fromTo("#c-l1", { opacity: 0, y: -90 }, { opacity: 1, y: 0, duration: 0.2, ease: "power4.out" }, 0.12);
      tl.fromTo("#c-l2", { opacity: 0, scale: 1.7 }, { opacity: 1, scale: 1, duration: 0.18, ease: "power4.out" }, 0.42);
      tl.fromTo("#c-card", { opacity: 0, y: 120, rotation: -4 }, { opacity: 1, y: 0, rotation: 0, duration: 0.4, ease: "expo.out" }, 0.83);
      tl.fromTo("#c-label", { opacity: 0 }, { opacity: 1, duration: 0.2 }, 1.0);
      tl.fromTo("#c-handle", { yPercent: 110 }, { yPercent: 0, duration: 0.36, ease: "expo.out" }, 1.08);
      tl.fromTo("#c-btn", { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)" }, 1.66);
      tl.fromTo("#c-note", { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, 1.9);
      tl.fromTo("#c-row .c-mini", { y: 300, opacity: 0 }, { y: 0, opacity: 1, duration: 0.45, ease: "expo.out", stagger: 0.08 }, 2.0);
      // tap on the button
      tl.to("#c-btn", { scale: 0.92, duration: 0.08, ease: "power2.in" }, 2.92);
      tl.to("#c-btn", { scale: 1, duration: 0.3, ease: "back.out(3)" }, 3.0);
      tl.set("#c-ripple", { scale: 0.4 }, 2.9);
      tl.to("#c-ripple", { opacity: 0.9, duration: 0.02, ease: "none" }, 2.98);
      tl.to("#c-ripple", { opacity: 0, scale: 4.5, duration: 0.6, ease: "power2.out" }, 3.0);
      tl.set("#c-btn", { textContent: "✓ AJOUTÉ" }, 3.0);
      tl.fromTo("#c-card", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 1, ease: "power2.out" }, 3.0);
      tl.to("#c-row", { x: -20, duration: 2.5, ease: "none" }, 3.3);
"""
write("cta.html", css5, body5, js5, D5, "cta")

print("durations", D1, D2, D3, D4, D5, "total", round(D1 + D2 + D3 + D4 + D5, 3))

p = os.path.join(OUT, "compositions", "cta.html")
t = open(p).read().replace(
    '<div id="root" data-composition-id="cta"',
    """<div id="root" data-composition-variables='[{"id":"handle","type":"string","label":"Pseudo Snapchat","default":"@TON.SNAP","maxLength":16}]' data-composition-id="cta\"""", 1)
open(p, "w").write(t)
