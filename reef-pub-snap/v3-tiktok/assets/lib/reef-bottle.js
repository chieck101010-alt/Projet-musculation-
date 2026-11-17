// REEF 33 — flacon 3D partagé par les 3 pubs.
// Proportions mesurées sur le packshot officiel ; la plaque gravée est la découpe du packshot.
// Unité : largeur du corps = 1. Le pied du flacon est en y = 0.

export const DIM = {
  BW: 1.0, BD: 0.62, BH: 2.08, CH: 0.11, BAND: 0.055,
  NECK_R: 0.235, NECK_H: 0.34, CAP_R: 0.40, CAP_H: 0.255,
  PL_W: 0.30, PL_H: 1.52, PL_Y: -0.047,
};
DIM.TOTAL_H = DIM.BH + DIM.NECK_H + DIM.CAP_H;

function bodyShape(THREE, w, d, ch) {
  const s = new THREE.Shape(), hw = w / 2, hd = d / 2;
  s.moveTo(-hw + ch, -hd); s.lineTo(hw - ch, -hd); s.lineTo(hw, -hd + ch); s.lineTo(hw, hd - ch);
  s.lineTo(hw - ch, hd); s.lineTo(-hw + ch, hd); s.lineTo(-hw, hd - ch); s.lineTo(-hw, -hd + ch); s.closePath();
  return s;
}
function prism(THREE, w, d, ch, h, bevel) {
  const geo = new THREE.ExtrudeGeometry(bodyShape(THREE, w, d, ch), {
    depth: h, bevelEnabled: bevel > 0, bevelThickness: bevel, bevelSize: bevel, bevelSegments: 3, curveSegments: 1,
  });
  geo.rotateX(-Math.PI / 2);
  return geo;
}

// Environnement studio : bandes lumineuses douces pour les reflets dorés.
export function studioEnv(THREE, renderer, warm = 1) {
  const env = new THREE.Scene();
  env.background = new THREE.Color(0x050403);
  const strip = (w, h, x, y, z, ry, c, k) => {
    const m = new THREE.Mesh(new THREE.PlaneGeometry(w, h),
      new THREE.MeshBasicMaterial({ color: new THREE.Color(c).multiplyScalar(k), side: THREE.DoubleSide }));
    m.position.set(x, y, z); m.rotation.y = ry; env.add(m);
  };
  strip(2.2, 9, -4.5, 1, 1.5, Math.PI / 2.4, 0xffe2b0, 3.2 * warm);
  strip(1.2, 9, 4.6, 1, -0.5, -Math.PI / 2.2, 0xfff4e4, 2.0);
  strip(8, 1.2, 0, 5, 0, 0, 0xffffff, 0.9);
  strip(1.0, 7, 1.5, 1, -5, 0, 0xc98a3a, 1.4 * warm);
  const pm = new THREE.PMREMGenerator(renderer);
  const tex = pm.fromScene(env, 0.04).texture;
  pm.dispose();
  return tex;
}

export async function buildBottle(THREE, plateUrl) {
  const D = DIM;
  const gold = new THREE.MeshStandardMaterial({ color: 0xd8b46a, metalness: 1, roughness: 0.32 });
  const goldSatin = new THREE.MeshStandardMaterial({ color: 0xcfa85e, metalness: 1, roughness: 0.42 });
  const black = new THREE.MeshPhysicalMaterial({ color: 0x050505, roughness: 0.58, metalness: 0, clearcoat: 0.2, clearcoatRoughness: 0.45, envMapIntensity: 0.35 });

  const g = new THREE.Group();
  const body = new THREE.Mesh(prism(THREE, D.BW, D.BD, D.CH, D.BH, 0.012), black);
  body.castShadow = true; g.add(body);
  const band = new THREE.Mesh(prism(THREE, D.BW + 0.03, D.BD + 0.03, D.CH + 0.01, D.BAND, 0.006), gold);
  band.position.y = D.BH - 0.004; g.add(band);
  const neck = new THREE.Mesh(new THREE.CylinderGeometry(D.NECK_R, D.NECK_R, D.NECK_H, 64), gold);
  neck.position.y = D.BH + D.NECK_H / 2; g.add(neck);
  const cap = new THREE.Mesh(new THREE.CylinderGeometry(D.CAP_R, D.CAP_R, D.CAP_H, 6), goldSatin);
  cap.rotation.y = Math.PI / 6;
  cap.position.y = D.BH + D.NECK_H + D.CAP_H / 2 - 0.01; cap.castShadow = true; g.add(cap);

  const tex = await new THREE.TextureLoader().loadAsync(plateUrl);
  tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8;
  const plateMat = new THREE.MeshStandardMaterial({ map: tex, metalness: 0.35, roughness: 0.38, envMapIntensity: 0.6 });
  const plate = new THREE.Mesh(new THREE.BoxGeometry(D.PL_W, D.PL_H, 0.012),
    [goldSatin, goldSatin, goldSatin, goldSatin, plateMat, goldSatin]);
  plate.position.set(0, D.BH / 2 + D.PL_Y, D.BD / 2 + 0.012); g.add(plate);

  return { group: g, mats: { gold, goldSatin, black, plateMat }, parts: { body, band, neck, cap, plate } };
}

// Petits utilitaires d'animation déterministes.
export const clamp01 = (x) => (x < 0 ? 0 : x > 1 ? 1 : x);
export const lerp = (a, b, x) => a + (b - a) * x;
export const seg = (t, a, b) => clamp01((t - a) / (b - a));
export const E = {
  out2: (x) => 1 - (1 - x) * (1 - x),
  out3: (x) => 1 - Math.pow(1 - x, 3),
  out4: (x) => 1 - Math.pow(1 - x, 4),
  in2: (x) => x * x,
  in3: (x) => x * x * x,
  inOut2: (x) => (x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2),
  inOut3: (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  back: (x, s = 1.7) => { const c = s + 1; return 1 + c * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2); },
};
export function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
