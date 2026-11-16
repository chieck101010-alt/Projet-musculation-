#!/usr/bin/env python3
"""Authoring-time generator for the Venez Shop balaclava ad scenes.
Usage: python3 tools/gen_scenes.py .   (writes compositions/*.html)
All timings are local to each scene; scene starts live in index.html."""
import os, sys, json

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
B = 0.4286          # one beat at 140 bpm
Y = "#FFFC00"       # Snapchat yellow

NIKE = open(os.path.join(OUT, "assets/logos/nike.svg")).read().split('d="')[1].split('"')[0]
SNAP = open(os.path.join(OUT, "assets/logos/snapchat.svg")).read().split('d="')[1].split('"')[0]
TIKTOK = open(os.path.join(OUT, "assets/logos/tiktok.svg")).read().split('d="')[1].split('"')[0]

def swoosh(w, color="#fff", cls="", ident=""):
    h = round(w * 0.5)
    i = f' id="{ident}"' if ident else ""
    return f'<svg{i} class="{cls}" viewBox="0 6.5 24 10" width="{w}" height="{round(w*10/24)}"><path d="{NIKE}" fill="{color}"/></svg>'

ICONS = {
    "shield": '<path d="M12 2 L20 5 V11 C20 16 16.5 20 12 22 C7.5 20 4 16 4 11 V5 Z"/><path d="M8 12 L11 15 L16.5 9"/>',
    "grid": '<path d="M9 3 L8 21 M16 3 L15 21 M3 8.5 H21 M3 15.5 H21"/>',
    "snow": '<path d="M12 2 V22 M3.3 7 L20.7 17 M3.3 17 L20.7 7 M9 3.5 L12 6 L15 3.5 M9 20.5 L12 18 L15 20.5"/>',
    "diamond": '<path d="M6 3 H18 L22 9 L12 21 L2 9 Z"/><path d="M2 9 H22 M9 3 L7.5 9 L12 21 L16.5 9 L15 3"/>',
    "truck": '<path d="M2 6 H14 V16 H2 Z M14 9 H18.5 L22 12.5 V16 H14"/><circle cx="6.5" cy="17.5" r="2"/><circle cx="17.5" cy="17.5" r="2"/>',
    "box": '<path d="M3 7.5 L12 3 L21 7.5 V16.5 L12 21 L3 16.5 Z M3 7.5 L12 12 L21 7.5 M12 12 V21 M7.5 5.2 L16.5 9.7"/>',
    "pin": '<path d="M12 22 C12 22 5 14.5 5 9.5 A7 7 0 0 1 19 9.5 C19 14.5 12 22 12 22 Z"/><circle cx="12" cy="9.5" r="2.6"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="10.5" rx="2"/><path d="M8 10.5 V7.5 A4 4 0 0 1 16 7.5 V10.5"/>',
}
def icon(name, size, color="#fff", sw=1.8):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')

def brush(ident, w, h, color="#fff", seed=3, extra=""):
    """Rough-edged brush block (turbulence-displaced rectangle)."""
    return f'''<svg id="{ident}" class="abs" viewBox="0 0 {w} {h}" width="{w}" height="{h}" {extra}>
  <defs><filter id="{ident}-f" x="-10%" y="-30%" width="120%" height="160%">
    <feTurbulence type="fractalNoise" baseFrequency="0.02 0.09" numOctaves="2" seed="{seed}"/>
    <feDisplacementMap in="SourceGraphic" scale="{round(h*0.13)}"/></filter></defs>
  <rect x="{round(w*0.05)}" y="{round(h*0.18)}" width="{round(w*0.9)}" height="{round(h*0.64)}" fill="{color}" filter="url(#{ident}-f)"/>
</svg>'''

HEAD = """<template>
  <style>
    @font-face { font-family: "Marker"; src: url("assets/fonts/permanent-marker.woff2") format("woff2"); font-display: block; }
    #root { position:absolute; inset:0; overflow:hidden; font-family:"Archivo Black", sans-serif; color:#f4f4f4; background:#050505; }
    #root .abs { position:absolute; }
    #root .mk { font-family:"Marker", "Archivo Black", sans-serif; text-transform:uppercase; line-height:1; }
    #root .lg { font-family:"League Gothic", sans-serif; text-transform:uppercase; line-height:.86; }
    #root .mono { font-family:"Space Mono", monospace; text-transform:uppercase; letter-spacing:.06em; }
    #root .cx { left:0; width:1080px; text-align:center; }
    #root .glow { filter: drop-shadow(0 0 18px rgba(255,255,255,.55)); }
%CSS%
  </style>
"""

def write(name, comp_id, css, body, js, root_extra=""):
    html = HEAD.replace("%CSS%", css) + f"""  <div id="root" {root_extra} data-composition-id="{comp_id}" data-width="1080" data-height="1920">
{body}
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
{js}
      window.__timelines = window.__timelines || {{}};
      window.__timelines["{comp_id}"] = tl;
    }})();
  </script>
</template>
"""
    with open(os.path.join(OUT, "compositions", name), "w") as f:
        f.write(html)

def punch(sel, t, big, small=1, dur=0.3, extra_from="", extra_to=""):
    """Instant jump to `big` just before t, settle to `small` from t (seek-safe, no fromTo baseline)."""
    return (f'      tl.to("{sel}", {{ scale: {big}{extra_from}, duration: 0.02, ease: "none" }}, {round(t-0.02,3)});\n'
            f'      tl.to("{sel}", {{ scale: {small}{extra_to}, duration: {dur}, ease: "expo.out" }}, {round(t,3)});\n')

SCENES = {}

# ================================================================ 1 HOOK  (photo: wearer)
D = round(5 * B, 3)
SCENES["hook"] = D
css = """
    #h-photo { left:-420px; top:0; width:1920px; height:1920px; background:url("assets/img/porte-hd.png") center/cover; transform-origin:46% 41%; }
    #h-shade { inset:0; background:linear-gradient(rgba(0,0,0,.78) 0%, rgba(0,0,0,.15) 38%, rgba(0,0,0,0) 60%, rgba(0,0,0,.6) 100%); }
    .h-slice { left:0; width:1080px; height:1920px; background:url("assets/img/porte-hd.png") center/cover; opacity:0; mix-blend-mode:screen; }
    #h-r { clip-path: inset(30% 0 52% 0); filter: sepia(1) saturate(6) hue-rotate(-50deg); }
    #h-c { clip-path: inset(58% 0 26% 0); filter: sepia(1) saturate(6) hue-rotate(140deg); }
    #h-wesh { top:240px; left:120px; font-size:150px; transform:rotate(-7deg); color:#fff; }
    #h-tvu { top:420px; font-size:236px; }
    #h-flash { inset:0; background:#fff; opacity:0; }
"""
body = """    <div id="h-photo" class="abs"></div>
    <div id="h-r" class="abs h-slice"></div>
    <div id="h-c" class="abs h-slice"></div>
    <div id="h-shade" class="abs"></div>
    <div id="h-wesh" class="abs mk glow">Wesh,</div>
    <div id="h-tvu" class="abs lg cx">T'as vu ça ?</div>
    <div id="h-flash" class="abs"></div>"""
js = f"""
      gsap.set("#h-tvu", {{ opacity: 0 }});
      // frame 0: tight on the eyes, then the whip-out lands on the beat
      tl.fromTo("#h-photo", {{ scale: 2.3 }}, {{ scale: 2.05, duration: {B}, ease: "none" }}, 0);
      tl.to("#h-photo", {{ scale: 1.0, duration: 0.32, ease: "expo.out" }}, {B});
      tl.to("#h-photo", {{ scale: 1.08, duration: {round(D - B - 0.32, 3)}, ease: "none" }}, {round(B + 0.32, 3)});
      tl.fromTo("#h-wesh", {{ scale: 1.25 }}, {{ scale: 1, duration: 0.3, ease: "power4.out" }}, 0);
      tl.to("#h-tvu", {{ opacity: 1, duration: 0.02 }}, 0.86);
      tl.fromTo("#h-tvu", {{ scale: 1.8 }}, {{ scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, 0.86);
      // RGB glitch slices on the beats
"""
for t in (B, 2 * B + 0.3, 4 * B):
    js += f"""      tl.to("#h-r, #h-c", {{ opacity: 0.9, duration: 0.01 }}, {round(t,3)});
      tl.to("#h-r", {{ x: 34, duration: 0.01 }}, {round(t,3)});
      tl.to("#h-c", {{ x: -30, duration: 0.01 }}, {round(t,3)});
      tl.to("#h-r, #h-c", {{ opacity: 0, x: 0, duration: 0.1, ease: "steps(3)" }}, {round(t+0.08,3)});
      tl.to("#h-photo", {{ x: 14, duration: 0.03 }}, {round(t,3)});
      tl.to("#h-photo", {{ x: 0, duration: 0.12, ease: "rough({{ strength: 2, points: 6, randomize: false }})" }}, {round(t+0.03,3)});
"""
js += f"""      tl.to("#h-flash", {{ opacity: 1, duration: 0.1, ease: "power2.in" }}, {round(D - 0.11, 3)});
"""
write("hook.html", "hook", css, body, js)

# ================================================================ 2 PRICE (cutout + Nike logo + 20€)
D = round(10 * B, 3)
SCENES["price"] = D
T_NAME, T_PRICE, T_OUAIS = 0.2, 1.48, 2.58  # "Cagoule Nike" / "vingt balles" / "ouais"
css = """
    #p-bg { inset:0; background:radial-gradient(90% 55% at 50% 58%, #2b2b2e 0%, #0b0b0c 60%, #030303 100%); }
    #p-flash { inset:0; background:#fff; opacity:1; }
    #p-rays { left:-460px; top:-200px; width:2000px; height:2000px; opacity:.16;
      background:repeating-conic-gradient(from 0deg at 50% 50%, rgba(255,255,255,.9) 0deg 4deg, rgba(255,255,255,0) 4deg 18deg);
      -webkit-mask-image: radial-gradient(circle at 50% 50%, #000 0%, transparent 60%); mask-image: radial-gradient(circle at 50% 50%, #000 0%, transparent 60%); }
    #p-swoosh { left:260px; top:200px; }
    #p-name { top:450px; font-size:96px; transform:rotate(-4deg); }
    #p-splash { left:40px; top:640px; }
    #p-splash { left:40px; top:560px; width:1000px; height:800px; background:radial-gradient(closest-side, rgba(255,255,255,.55), rgba(255,255,255,.12) 55%, rgba(255,255,255,0)); }
    #p-prod { left:140px; top:560px; width:800px; height:800px; }
    #p-prod img { width:800px; height:800px; filter: drop-shadow(0 0 2px rgba(255,255,255,.9)) drop-shadow(0 0 26px rgba(255,255,255,.35)); }
    #p-price { left:520px; top:960px; width:470px; height:300px; transform:rotate(-9deg); }
    #p-price-txt { left:0; top:52px; width:470px; text-align:center; font-size:200px; color:#0a0a0a; }
    #p-ouais { top:1250px; left:190px; width:700px; font-size:34px; color:#0a0a0a; background:#fff; padding:10px 0; text-align:center; }
"""
body = f"""    <div id="p-stage" class="abs" style="inset:0">
    <div id="p-bg" class="abs"></div>
    <div id="p-rays" class="abs"></div>
    <div id="p-swoosh-wrap" class="abs" style="left:0;top:0;width:1080px;height:420px">{swoosh(560, "#fff", "abs glow", "p-swoosh")}</div>
    <div id="p-name" class="abs mk cx glow">Cagoule Nike</div>
    <div id="p-splash" class="abs"></div>
    <div id="p-prod" class="abs"><img src="assets/img/produit-cutout.png" alt=""/></div>
    <div id="p-price" class="abs">{brush("p-price-bg", 470, 300, "#fff", 9)}<div id="p-price-txt" class="abs mk">20€</div></div>
    <div id="p-ouais" class="abs mono">Ouais, t'as bien entendu.</div>
    </div>
    <div id="p-flash" class="abs"></div>"""
js = f"""
      gsap.set("#p-name, #p-price, #p-ouais", {{ opacity: 0 }});
      tl.to("#p-flash", {{ opacity: 0, duration: 0.25, ease: "power2.out" }}, 0);
      tl.fromTo("#p-rays", {{ rotation: 0 }}, {{ rotation: 40, duration: {D}, ease: "none" }}, 0);
      // product drops in and lands on the first beat
      tl.fromTo("#p-prod", {{ y: -1300, rotation: -25 }}, {{ y: 0, rotation: 0, duration: 0.38, ease: "power4.in" }}, 0);
      tl.fromTo("#p-splash", {{ scale: 0.2, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "expo.out" }}, 0.38);
      tl.to("#p-prod", {{ y: -14, duration: 0.05 }}, 0.38);
      tl.to("#p-prod", {{ y: 0, duration: 0.25, ease: "bounce.out" }}, 0.43);
      tl.to("#p-prod", {{ rotation: 3, scale: 1.04, duration: {round(D-0.9,3)}, ease: "sine.inOut" }}, 0.68);
      // the swoosh draws in left to right, then the name
      tl.fromTo("#p-swoosh", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 0.32, ease: "power3.out" }}, {T_NAME});
      tl.fromTo("#p-swoosh", {{ x: -60 }}, {{ x: 0, duration: 0.5, ease: "expo.out" }}, {T_NAME});
      tl.to("#p-name", {{ opacity: 1, duration: 0.02 }}, {T_NAME + 0.3});
      tl.fromTo("#p-name", {{ scale: 1.6 }}, {{ scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, {T_NAME + 0.3});
      // 20€ stamp on "vingt balles"
      tl.to("#p-price", {{ opacity: 1, duration: 0.02 }}, {T_PRICE});
      tl.fromTo("#p-price", {{ scale: 2.6 }}, {{ scale: 1, duration: 0.16, ease: "power4.in", immediateRender: false }}, {T_PRICE});
      tl.to("#p-stage", {{ x: 16, y: -10, duration: 0.03 }}, {T_PRICE + 0.16});
      tl.to("#p-stage", {{ x: 0, y: 0, duration: 0.3, ease: "rough({{ strength: 3, points: 8, randomize: false }})" }}, {T_PRICE + 0.19});
"""
js += punch("#p-price", T_PRICE + 1.29, 1.12, 1)
js += f"""      tl.fromTo("#p-ouais", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.25 }}, {T_OUAIS});
      tl.to("#p-prod", {{ x: -900, rotation: -20, duration: 0.2, ease: "power3.in" }}, {round(D - 0.2, 3)});
"""
write("price.html", "price", css, body, js)

# ================================================================ 3 DETAILS (photo zooms)
D = round(12 * B, 3)
SCENES["details"] = D
VW, VH = 940, 860
IMG = 1200
shots = [  # label, icon, focus (fraction of image), zoom, start, end
    ("Tissu respirant", "grid", (0.44, 0.13), 3.0, 0.0, 1.2),
    ("Confort optimal", "shield", (0.57, 0.33), 3.6, 1.2, 2.45),
    ("Idéal toutes saisons", "snow", (0.40, 0.70), 2.6, 2.45, 3.9),
]
css = f"""
    #d-bg {{ inset:0; background:radial-gradient(90% 55% at 50% 55%, #222226 0%, #070708 70%); }}
    #d-view {{ left:{(1080-VW)//2}px; top:470px; width:{VW}px; height:{VH}px; overflow:hidden; border-radius:30px; background:#cfcfcf; }}
    #d-img {{ left:{(VW-IMG)//2}px; top:{(VH-IMG)//2}px; width:{IMG}px; height:{IMG}px; background:url("assets/img/produit.png") center/cover; }}
    .d-c {{ width:76px; height:76px; border-color:{Y}; border-style:solid; border-width:0; }}
    #d-c1 {{ left:{(1080-VW)//2+26}px; top:496px; border-top-width:7px; border-left-width:7px; }}
    #d-c2 {{ left:{(1080+VW)//2-102}px; top:496px; border-top-width:7px; border-right-width:7px; }}
    #d-c3 {{ left:{(1080-VW)//2+26}px; top:{470+VH-102}px; border-bottom-width:7px; border-left-width:7px; }}
    #d-c4 {{ left:{(1080+VW)//2-102}px; top:{470+VH-102}px; border-bottom-width:7px; border-right-width:7px; }}
    #d-zoom {{ left:{(1080-VW)//2+40}px; top:{470+VH-88}px; font-size:30px; color:{Y}; background:rgba(0,0,0,.72); padding:6px 16px; border-radius:8px; }}
    #d-kick {{ top:236px; font-size:32px; color:{Y}; }}
    .d-lab {{ top:290px; left:0; width:1080px; display:flex; align-items:center; justify-content:center; gap:22px; font-size:80px; white-space:nowrap; }}
    #d-final {{ top:216px; left:40px; width:1000px; font-size:84px; line-height:1.12; }}
    #d-badges {{ left:0; top:1350px; width:1080px; display:flex; justify-content:center; gap:22px; }}
"""
labs = "\n".join(
    f'    <div id="d-l{i}" class="abs mk d-lab glow">{icon(ic, 96)}<span>{t}</span></div>'
    for i, (t, ic, *_r) in enumerate(shots))
body = f"""    <div id="d-bg" class="abs"></div>
    <div id="d-kick" class="abs mono cx">Zoom sur les détails</div>
{labs}
    <div id="d-final" class="abs mk glow" style="text-align:center">Qualité · Confort<br/>Protection</div>
    <div id="d-view" class="abs"><div id="d-img" class="abs"></div></div>
    <div id="d-c1" class="abs d-c"></div><div id="d-c2" class="abs d-c"></div>
    <div id="d-c3" class="abs d-c"></div><div id="d-c4" class="abs d-c"></div>
    <div id="d-zoom" class="abs mono">Zoom ×3,0</div>"""
js = """
      gsap.set("#d-l1, #d-l2, #d-final", { opacity: 0 });
      tl.fromTo(".d-c", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.3, ease: "expo.out" }, 0);
"""
def camxy(fx, fy, z):
    return round((0.5 - fx) * IMG * z), round((0.5 - fy) * IMG * z)
for i, (t, ic, (fx, fy), z, st, en) in enumerate(shots):
    x, y = camxy(fx, fy, z)
    x2, y2 = camxy(fx + 0.012, fy - 0.01, z * 1.1)
    zt = f"Zoom ×{z:.1f}".replace(".", ",")
    js += f"""      tl.set("#d-img", {{ x: {x}, y: {y}, scale: {z} }}, {st});
      tl.to("#d-img", {{ x: {x2}, y: {y2}, scale: {round(z*1.1,3)}, duration: {round(en-st,3)}, ease: "none" }}, {st});
      tl.set("#d-zoom", {{ textContent: "{zt}" }}, {st});
      tl.to("#d-l{i}", {{ opacity: 1, duration: 0.02 }}, {st});
      tl.fromTo("#d-l{i}", {{ y: 70 }}, {{ y: 0, duration: 0.24, ease: "power4.out", immediateRender: false }}, {st});
      tl.to("#d-l{i}", {{ opacity: 0, duration: 0.1 }}, {round(en - 0.1, 3)});
"""
    if st > 0:
        js += punch("#d-view", st, 0.95, 1, 0.28)
PB = shots[-1][5]
js += f"""      tl.to("#d-img", {{ x: 0, y: 0, scale: 0.92, duration: 0.35, ease: "expo.inOut" }}, {PB});
      tl.to("#d-zoom, #d-kick", {{ opacity: 0, duration: 0.1 }}, {PB});
      tl.to("#d-final", {{ opacity: 1, duration: 0.02 }}, {PB + 0.05});
      tl.fromTo("#d-final", {{ scale: 1.5 }}, {{ scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, {PB + 0.05});
      tl.to("#d-img", {{ scale: 0.96, duration: {round(D - PB - 0.35, 3)}, ease: "none" }}, {PB + 0.35});
"""
write("details.html", "details", css, body, js)

# ================================================================ 4 STYLE (wearer photo, split slide)
D = round(7 * B, 3)
SCENES["style"] = D
css = """
    .s-half { left:-420px; width:1920px; height:960px; overflow:hidden; }
    .s-half div { position:absolute; left:0; width:1920px; height:1920px; background:url("assets/img/porte-hd.png") center/cover; }
    #s-top { top:0; } #s-top div { top:0; }
    #s-bot { top:960px; } #s-bot div { top:-960px; }
    #s-world { inset:0; transform-origin:50% 45%; }
    #s-shade { inset:0; background:linear-gradient(rgba(0,0,0,.82) 0%, rgba(0,0,0,.25) 34%, rgba(0,0,0,0) 55%, rgba(0,0,0,.5) 100%); }
    #s-leak1 { left:-300px; top:300px; width:900px; height:900px; border-radius:50%; background:radial-gradient(closest-side, rgba(255,240,190,.45), rgba(255,240,190,0)); mix-blend-mode:screen; }
    #s-leak2 { left:600px; top:900px; width:800px; height:800px; border-radius:50%; background:radial-gradient(closest-side, rgba(255,252,0,.25), rgba(255,252,0,0)); mix-blend-mode:screen; }
    #s-l1 { top:240px; font-size:150px; }
    #s-l2 { top:400px; font-size:130px; }
    #s-under { left:170px; top:560px; }
    #s-carre { top:640px; font-size:44px; color:#FFFC00; }
"""
body = """    <div id="s-world" class="abs">
      <div id="s-top" class="abs s-half"><div></div></div>
      <div id="s-bot" class="abs s-half"><div></div></div>
      <div id="s-leak1" class="abs"></div>
      <div id="s-leak2" class="abs"></div>
      <div id="s-shade" class="abs"></div>
    </div>
    <div id="s-l1" class="abs mk cx glow">Le style</div>
    <div id="s-l2" class="abs mk cx glow">au quotidien</div>
    <svg id="s-under" class="abs" viewBox="0 0 740 60" width="740" height="60"><path id="s-under-p" d="M10 40 C 200 10 450 12 730 30" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round" stroke-dasharray="760" stroke-dashoffset="760"/></svg>
    <div id="s-carre" class="abs mono cx">C'est carré.</div>"""
js = f"""
      gsap.set("#s-l2, #s-carre", {{ opacity: 0 }});
      tl.fromTo("#s-top", {{ x: 1100 }}, {{ x: 0, duration: 0.34, ease: "expo.out" }}, 0);
      tl.fromTo("#s-bot", {{ x: -1100 }}, {{ x: 0, duration: 0.34, ease: "expo.out" }}, 0);
      tl.fromTo("#s-world", {{ scale: 1.0 }}, {{ scale: 1.12, duration: {D}, ease: "none" }}, 0);
      tl.fromTo("#s-leak1", {{ x: -200, opacity: 0.3 }}, {{ x: 700, opacity: 1, duration: {D}, ease: "none" }}, 0);
      tl.fromTo("#s-leak2", {{ x: 200 }}, {{ x: -500, duration: {D}, ease: "none" }}, 0);
      tl.fromTo("#s-l1", {{ opacity: 0, x: -140 }}, {{ opacity: 1, x: 0, duration: 0.22, ease: "power4.out" }}, 0.3);
      tl.to("#s-l2", {{ opacity: 1, duration: 0.02 }}, 0.62);
      tl.fromTo("#s-l2", {{ x: 140 }}, {{ x: 0, duration: 0.22, ease: "power4.out", immediateRender: false }}, 0.62);
      tl.to("#s-under-p", {{ strokeDashoffset: 0, duration: 0.4, ease: "power2.out" }}, 0.9);
      tl.to("#s-carre", {{ opacity: 1, duration: 0.15 }}, 2.3);
      tl.to("#s-top", {{ x: -1100, duration: 0.2, ease: "power3.in" }}, {round(D-0.2,3)});
      tl.to("#s-bot", {{ x: 1100, duration: 0.2, ease: "power3.in" }}, {round(D-0.2,3)});
"""
write("style.html", "style", css, body, js)

# ================================================================ 5 DELIVERY (IDF map + cards)
D = round(18 * B, 3)
SCENES["delivery"] = D
DEPTS = [  # num, polygon, label pos
    ("95", "60,40 300,10 560,60 540,170 380,190 300,170 200,190 80,170", (310, 100)),
    ("93", "380,190 540,170 560,300 430,320 400,250", (478, 252)),
    ("92", "200,190 300,170 310,240 270,300 300,330 300,380 230,400 180,300", (240, 292)),
    ("75", "310,240 400,250 430,320 380,340 300,330 270,300", (352, 292)),
    ("94", "380,340 430,320 560,300 570,420 420,440", (492, 382)),
    ("91", "230,400 300,380 300,330 380,340 420,440 450,550 200,560 160,470", (318, 470)),
]
C1, C2, C3 = 0.12, 2.82, 5.18   # card times (voice phrases)
css = f"""
    #v-bg {{ inset:0; background:radial-gradient(80% 50% at 50% 40%, #1c1c20 0%, #050505 70%); }}
    #v-title {{ top:228px; font-size:112px; transform:rotate(-4deg); }}
    #v-sub {{ top:360px; font-size:32px; color:{Y}; }}
    #v-map {{ left:240px; top:440px; width:600px; height:570px; }}
    #v-map polygon {{ fill:rgba(255,255,255,.04); stroke:rgba(255,255,255,.55); stroke-width:3; stroke-linejoin:round; }}
    #v-map text {{ font-family:"League Gothic", sans-serif; font-size:52px; fill:#fff; text-anchor:middle; }}
    #v-truck {{ left:-200px; top:690px; }}
    .v-card {{ left:70px; width:940px; height:96px; border:3px solid rgba(255,255,255,.85); border-radius:22px; background:rgba(0,0,0,.6);
      display:flex; align-items:center; gap:24px; padding:0 30px; font-size:34px; }}
    .v-card .v-price {{ margin-left:auto; font-family:"Marker", sans-serif; font-size:52px; color:{Y}; }}
    #v-c1 {{ top:1030px; }} #v-c2 {{ top:1140px; }} #v-c3 {{ top:1250px; }}
"""
polys = "\n".join(
    f'      <g id="v-d{n}"><polygon points="{p}"/><text x="{x}" y="{y + 18}">{n}</text></g>' for n, p, (x, y) in DEPTS)
body = f"""    <div id="v-bg" class="abs"></div>
    <div id="v-title" class="abs mk cx glow" data-layout-allow-occlusion>Livraison</div>
    <div id="v-sub" class="abs mono cx">Rapide &amp; sécurisée · Île-de-France</div>
    <svg id="v-map" class="abs glow" viewBox="0 0 600 570">
{polys}
    </svg>
    <div id="v-truck" class="abs">{icon("truck", 170, "#fff", 1.6)}</div>
    <div id="v-c1" class="abs v-card">{icon("truck", 56)}<span>Livraison Paris &amp; IDF</span><span class="v-price">+5€</span></div>
    <div id="v-c2" class="abs v-card">{icon("box", 56)}<span>Envoi La Poste 24/48h</span><span class="v-price">+5€</span></div>
    <div id="v-c3" class="abs v-card">{icon("pin", 56)}<span>Dispo sur place · 93</span><span class="v-price">Saint-Denis</span></div>"""
js = """
      gsap.set(".v-card", { opacity: 0 });
      tl.fromTo("#v-title", { scale: 1.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.2, ease: "power4.out" }, 0);
      tl.fromTo("#v-sub", { opacity: 0 }, { opacity: 1, duration: 0.2 }, 0.2);
      tl.fromTo("#v-map", { scale: 0.85, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.35, ease: "expo.out" }, 0.1);
      tl.fromTo("#v-truck", { x: 0 }, { x: 1500, duration: 0.9, ease: "power2.in" }, 0.15);
"""
order = ["93", "75", "92", "94", "95", "91"]
for i, n in enumerate(order):
    t = round(0.43 + i * B, 3)
    col = "rgba(255,252,0,.35)" if n == "93" else "rgba(255,255,255,.14)"
    js += f"""      tl.to("#v-d{n} polygon", {{ fill: "{col}", stroke: "#fff", duration: 0.12 }}, {t});
      tl.fromTo("#v-d{n}", {{ scale: 1.08, transformOrigin: "50% 50%" }}, {{ scale: 1, duration: 0.3, ease: "expo.out", immediateRender: false }}, {t});
"""
for cid, t in (("v-c1", C1 + 0.3), ("v-c2", C2), ("v-c3", C3)):
    js += f"""      tl.to("#{cid}", {{ opacity: 1, duration: 0.02 }}, {t});
      tl.fromTo("#{cid}", {{ x: 600 }}, {{ x: 0, duration: 0.3, ease: "expo.out", immediateRender: false }}, {t});
"""
js += f"""      tl.to("#v-d93 polygon", {{ fill: "rgba(255,252,0,.95)", duration: 0.1 }}, {C3});
      tl.to("#v-d93 text", {{ fill: "#0a0a0a", duration: 0.1 }}, {C3});
      tl.to("#v-map", {{ scale: 1.04, duration: {round(D - C3, 3)}, ease: "none" }}, {C3});
      tl.to(".v-card, #v-map, #v-title, #v-sub", {{ x: -1100, duration: 0.2, ease: "power3.in", stagger: 0.02 }}, {round(D - 0.3, 3)});
"""
write("delivery.html", "delivery", css, body, js)

# ================================================================ 6 TRUST
D = round(6 * B, 3)
SCENES["trust"] = D
badges = [("diamond", "Produits testés", 0.12), ("lock", "Paiement sécurisé", 1.1), ("truck", "Envoi rapide", 1.6)]
css = f"""
    #t-bg {{ inset:0; background:radial-gradient(80% 50% at 50% 50%, #1b1b1f 0%, #050505 70%); }}
    #t-swoosh {{ left:340px; top:250px; }}
    #t-head {{ top:430px; font-size:100px; }}
    .t-b {{ left:90px; width:900px; height:200px; display:flex; align-items:center; gap:40px; padding:0 50px; border-radius:30px;
      border:4px solid #fff; background:rgba(255,255,255,.05); font-size:56px; }}
    #t-b0 {{ top:600px; }} #t-b1 {{ top:840px; }} #t-b2 {{ top:1080px; }}
    #t-wipe {{ inset:0; background:{Y}; clip-path:polygon(0 100%, 100% 100%, 100% 100%, 0 100%); }}
"""
bb = "\n".join(f'    <div id="t-b{i}" class="abs t-b glow">{icon(ic, 120, "#fff", 1.6)}<span>{t}</span></div>' for i, (ic, t, _) in enumerate(badges))
body = f"""    <div id="t-bg" class="abs"></div>
    {swoosh(400, "#fff", "abs glow", "t-swoosh")}
    <div id="t-head" class="abs mk cx glow">Zéro stress</div>
{bb}
    <div id="t-wipe" class="abs"></div>"""
js = """
      gsap.set(".t-b", { opacity: 0 });
      tl.fromTo("#t-swoosh", { clipPath: "inset(0 100% 0 0)" }, { clipPath: "inset(0 0% 0 0)", duration: 0.3, ease: "power3.out" }, 0);
      tl.fromTo("#t-head", { scale: 1.5, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.2, ease: "power4.out" }, 0.1);
"""
for i, (_, _, t) in enumerate(badges):
    js += f"""      tl.to("#t-b{i}", {{ opacity: 1, duration: 0.02 }}, {t});
      tl.fromTo("#t-b{i}", {{ scale: 0.6, rotation: {(-6, 5, -4)[i]} }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.4)", immediateRender: false }}, {t});
"""
js += f"""      tl.to("#t-wipe", {{ clipPath: "polygon(0 0%, 100% -30%, 100% 100%, 0 100%)", duration: 0.26, ease: "power3.in" }}, {round(D - 0.27, 3)});
"""
write("trust.html", "trust", css, body, js)

# ================================================================ 7 CTA
D = 8.7
SCENES["cta"] = D
T_HANDLE, T_TIKTOK, T_MERCI = 1.6, 3.65, 6.1
css = f"""
    #c-bg {{ inset:0; background:{Y}; }}
    #c-rays {{ left:-460px; top:-300px; width:2000px; height:2000px; opacity:.18;
      background:repeating-conic-gradient(from 0deg at 50% 50%, #fff 0deg 5deg, rgba(255,255,255,0) 5deg 16deg); }}
    #c-l1 {{ top:226px; font-size:200px; color:#0a0a0a; }}
    #c-l2 {{ top:388px; font-size:200px; color:#0a0a0a; }}
    #c-prod {{ left:290px; top:1390px; width:500px; height:500px; transform:rotate(14deg); }}
    #c-prod img {{ width:500px; height:500px; }}
    #c-snap {{ left:70px; top:590px; width:940px; height:250px; background:#0a0a0a; border-radius:46px; }}
    #c-ghost {{ left:34px; top:34px; width:182px; height:182px; background:{Y}; border-radius:40px; display:flex; align-items:center; justify-content:center; }}
    #c-snap-lab {{ left:250px; top:44px; font-size:30px; color:{Y}; }}
    #c-handle-wrap {{ left:246px; top:84px; width:680px; height:130px; overflow:hidden; }}
    #c-handle {{ display:inline-block; font-size:92px; color:#fff; line-height:130px; letter-spacing:-.01em; }}
    #c-add {{ left:440px; top:860px; font-size:66px; color:#0a0a0a; transform:rotate(-5deg); }}
    #c-arrow {{ left:330px; top:850px; }}
    #c-only {{ top:990px; font-size:30px; color:#0a0a0a; }}
    #c-tt {{ left:150px; top:1060px; width:780px; height:150px; background:#0a0a0a; border-radius:75px; display:flex; align-items:center; gap:28px; padding:0 40px; }}
    #c-tt-txt {{ font-size:54px; color:#fff; }}
    #c-tt-lab {{ font-family:"Space Mono", monospace; font-size:28px; color:{Y}; letter-spacing:.04em; }}
    #c-merci {{ top:1236px; font-size:64px; color:#0a0a0a; transform:rotate(-3deg); }}
    #c-foot {{ top:1330px; font-size:30px; color:#0a0a0a; }}
    #c-ripple {{ left:60px; top:620px; width:200px; height:200px; border-radius:50%; border:8px solid {Y}; opacity:0; }}
"""
body = f"""    <div id="c-bg" class="abs"></div>
    <div id="c-rays" class="abs"></div>
    <div id="c-l1" class="abs lg cx">Commande</div>
    <div id="c-l2" class="abs lg cx">sur snap</div>
    <div id="c-prod" class="abs"><img src="assets/img/produit-cutout.png" alt=""/></div>
    <div id="c-snap" class="abs">
      <div id="c-ghost" class="abs"><svg viewBox="0 0 24 24" width="128" height="128"><path d="{SNAP}" fill="#fff" stroke="#0a0a0a" stroke-width=".9"/></svg></div>
      <div id="c-snap-lab" class="abs mono">Snapchat</div>
      <div id="c-handle-wrap" class="abs"><span id="c-handle" data-var-text="snap">naskoo_1ter</span></div>
    </div>
    <div id="c-ripple" class="abs"></div>
    <svg id="c-arrow" class="abs" viewBox="0 0 100 100" width="100" height="100"><path d="M90 85 C 60 80 30 60 22 18 M8 34 L22 14 L40 30" stroke="#0a0a0a" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div id="c-add" class="abs mk">Ajoute-moi !!</div>
    <div id="c-only" class="abs mono cx">Commandes uniquement par Snapchat</div>
    <div id="c-tt" class="abs"><svg viewBox="0 0 24 24" width="84" height="84"><path d="{TIKTOK}" fill="#fff"/></svg><div><div id="c-tt-lab">Suis-nous sur TikTok</div><div id="c-tt-txt" data-var-text="tiktok">@venez_shop75</div></div></div>
    <div id="c-merci" class="abs mk cx">Merci pour la force !</div>
    <div id="c-foot" class="abs mono cx">Good vibes only · 93/75</div>"""
js = f"""
      gsap.set("#c-snap, #c-add, #c-arrow, #c-only, #c-tt, #c-merci, #c-foot", {{ opacity: 0 }});
      tl.fromTo("#c-rays", {{ rotation: 0 }}, {{ rotation: 50, duration: {D}, ease: "none" }}, 0);
      tl.fromTo("#c-l1", {{ y: -120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.2, ease: "power4.out" }}, 0.05);
      tl.fromTo("#c-l2", {{ scale: 1.7, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.2, ease: "power4.out" }}, 0.45);
      tl.fromTo("#c-prod", {{ y: 600, rotation: 60 }}, {{ y: 0, rotation: 14, duration: 0.45, ease: "expo.out" }}, 0.3);
      tl.to("#c-prod", {{ rotation: -8, y: 20, duration: {round(D-0.8,3)}, ease: "sine.inOut" }}, 0.75);
      tl.to("#c-snap", {{ opacity: 1, duration: 0.02 }}, 0.85);
      tl.fromTo("#c-snap", {{ y: 160, rotation: -5 }}, {{ y: 0, rotation: 0, duration: 0.4, ease: "expo.out", immediateRender: false }}, 0.85);
      tl.fromTo("#c-handle", {{ clipPath: "inset(0 100% 0 0)" }}, {{ clipPath: "inset(0 0% 0 0)", duration: 1.6, ease: "steps(11)" }}, {T_HANDLE});
      tl.to("#c-add, #c-arrow", {{ opacity: 1, duration: 0.02 }}, {T_HANDLE + 1.3});
      tl.fromTo("#c-add", {{ scale: 1.8 }}, {{ scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, {T_HANDLE + 1.3});
      tl.fromTo("#c-arrow path", {{ strokeDasharray: 200, strokeDashoffset: 200 }}, {{ strokeDashoffset: 0, duration: 0.3, ease: "power2.out", immediateRender: false }}, {T_HANDLE + 1.3});
      tl.fromTo("#c-only", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.2, immediateRender: false }}, {T_HANDLE + 1.5});
      tl.to("#c-tt", {{ opacity: 1, duration: 0.02 }}, {T_TIKTOK});
      tl.fromTo("#c-tt", {{ x: -900 }}, {{ x: 0, duration: 0.35, ease: "expo.out", immediateRender: false }}, {T_TIKTOK});
      // the add button gets pressed
      tl.set("#c-ripple", {{ scale: 0.3 }}, {T_HANDLE + 2.0});
      tl.to("#c-ripple", {{ opacity: 1, duration: 0.02 }}, {T_HANDLE + 2.1});
      tl.to("#c-ripple", {{ opacity: 0, scale: 3.2, duration: 0.6, ease: "power2.out" }}, {T_HANDLE + 2.12});
"""
js += punch("#c-snap", T_HANDLE + 2.12, 0.94, 1, 0.35)
js += f"""      tl.to("#c-merci", {{ opacity: 1, duration: 0.02 }}, {T_MERCI});
      tl.fromTo("#c-merci", {{ scale: 1.6 }}, {{ scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }}, {T_MERCI});
      tl.to("#c-foot", {{ opacity: 1, duration: 0.3 }}, {T_HANDLE + 2.6});
"""
write("cta.html", "cta", css, body, js,
      root_extra="""data-composition-variables='[{"id":"snap","type":"string","label":"Pseudo Snapchat","default":"naskoo_1ter"},{"id":"tiktok","type":"string","label":"Compte TikTok","default":"@venez_shop75"}]'""")

json.dump(SCENES, open(os.path.join(OUT, "tools", "scene_durations.json"), "w"), indent=1)
print(SCENES, "total", round(sum(SCENES.values()), 3))
