"""REEF 33 — musique et bruitages composés par synthèse (numpy seul), libres de droits.

Usage : python3 synth_audio.py <dossier reef-pub-snap>
Écrit, pour chaque vidéo : assets/audio/music.wav et assets/audio/sfx.wav (44,1 kHz, stéréo, 30 s).
Tout est déterministe (graine fixe) : relancer donne exactement les mêmes fichiers.
"""
import sys, wave, os
import numpy as np

SR = 44100
DUR = 30.0
N = int(SR * DUR)
rng = np.random.default_rng(33)


def tt(d):
    return np.arange(int(SR * d)) / SR


def place(buf, sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= len(buf):
        return
    s = sig[: len(buf) - i] * gain
    l, r = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    buf[i:i + len(s), 0] += s * l * 1.414
    buf[i:i + len(s), 1] += s * r * 1.414


def lp(x, a):  # passe-bas 1 pôle
    y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc += a * (v - acc); y[i] = acc
    return y


def lp_fast(x, cutoff):
    # passe-bas par FFT (rapide pour de longs signaux)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (f / cutoff) ** 4)
    return np.fft.irfft(X, len(x))


def hp_fast(x, cutoff):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 - 1 / (1 + (f / max(cutoff, 1)) ** 4)
    return np.fft.irfft(X, len(x))


def env(n, a, d, s=0.0, r=0.0, sus=0.0):
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-4), np.exp(-(t - a) / max(d, 1e-4)) * (1 - s) + s)
    return e


def note(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def reverb(x, wet=0.25, size=1.0):
    # réverbe simple : peignes + passe-tout (Schroeder)
    out = np.zeros_like(x)
    for dl, g in [(1557, 0.84), (1617, 0.83), (1491, 0.82), (1422, 0.81)]:
        d = int(dl * size); y = np.zeros(len(x) + d)
        y[: len(x)] += x
        for i in range(d, len(y)):
            y[i] += g * y[i - d] * 0.5
        out += y[: len(x)]
    out /= 4
    return x * (1 - wet) + out * wet


def conv_reverb(x, seconds=2.2, wet=0.3):
    n = int(SR * seconds)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / (SR * seconds / 6))
    ir = lp_fast(ir, 6000); ir /= np.sqrt((ir ** 2).sum())
    y = np.fft.irfft(np.fft.rfft(x, len(x) + n) * np.fft.rfft(ir, len(x) + n))[: len(x)]
    return x * (1 - wet) + y * wet * 0.6


# ---------------- instruments ----------------
def kick808(f0=50, d=0.9):
    t = tt(d); f = f0 + 90 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.tanh(1.6 * np.sin(ph) * np.exp(-t / (d / 3)))


def snare(d=0.25, tone=190):
    t = tt(d)
    n = hp_fast(rng.standard_normal(len(t)), 1200) * np.exp(-t * 18)
    b = np.sin(2 * np.pi * tone * t) * np.exp(-t * 30)
    return 0.6 * n + 0.5 * b


def clap(d=0.3):
    t = tt(d); n = hp_fast(rng.standard_normal(len(t)), 900)
    e = sum(np.exp(-np.clip(t - k * 0.011, 0, None) * 60) * (t >= k * 0.011) for k in range(3)) + np.exp(-t * 14) * 0.6
    return n * e * 0.5


def hat(d=0.06, open_=False):
    t = tt(0.3 if open_ else d)
    n = hp_fast(rng.standard_normal(len(t)), 7000)
    return n * np.exp(-t * (9 if open_ else 70)) * 0.35


def pluck_oud(freq, d=1.4, bright=0.5):
    # Karplus-Strong : corde pincée
    n = int(SR * d); p = max(2, int(SR / freq))
    buf = rng.uniform(-1, 1, p) * 0.8
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        nxt = buf[(i + 1) % p]
        buf[i % p] = 0.996 * (bright * buf[i % p] + (1 - bright) * nxt) if True else 0
    return out * np.exp(-np.arange(n) / (SR * d * 0.5))


def pad(freqs, d, bright=1200):
    t = tt(d); x = np.zeros(len(t))
    for f in freqs:
        for det in (-0.004, 0.0, 0.0037):
            x += np.sign(np.sin(2 * np.pi * f * (1 + det) * t)) * 0.3 + np.sin(2 * np.pi * f * (1 + det) * t) * 0.7
    x = lp_fast(x, bright)
    a = np.minimum(1, t / 1.2) * np.minimum(1, (d - t) / 1.2)
    return x * a / (len(freqs) * 3)


def keys(freqs, d):
    t = tt(d); x = np.zeros(len(t))
    for f in freqs:
        x += (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) * np.exp(-t * 3) + 0.15 * np.sin(6 * np.pi * f * t) * np.exp(-t * 5))
    trem = 1 + 0.12 * np.sin(2 * np.pi * 4.5 * t)
    return x * np.exp(-t / (d * 0.6)) * trem / len(freqs)


# ---------------- bruitages ----------------
def sfx_impact(d=1.6):
    t = tt(d)
    boom = np.sin(2 * np.pi * np.cumsum(38 + 120 * np.exp(-t * 20)) / SR) * np.exp(-t * 2.4)
    crack = hp_fast(rng.standard_normal(len(t)), 2000) * np.exp(-t * 45)
    return np.tanh(1.8 * boom) * 0.9 + crack * 0.5


def sfx_whoosh(d=0.6, up=True):
    t = tt(d); n = rng.standard_normal(len(t))
    out = np.zeros(len(t)); seg = 512
    for i in range(0, len(t), seg):
        k = i / len(t); c = 400 + (5000 if up else 3000) * (k if up else 1 - k)
        out[i:i + seg] = lp_fast(n[i:i + seg] if len(n[i:i + seg]) == seg else np.pad(n[i:i + seg], (0, seg - len(n[i:i + seg]))), c)[: len(n[i:i + seg])]
    e = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
    return out * e * 0.6


def sfx_tick(f=3200):
    t = tt(0.25)
    return (np.sin(2 * np.pi * f * t) + 0.5 * np.sin(2 * np.pi * f * 1.48 * t)) * np.exp(-t * 28) * 0.35


def sfx_pop():
    t = tt(0.12); f = 900 * np.exp(-t * 25) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 40) * 0.6


def sfx_glitch(d=0.35):
    t = tt(d); x = np.sign(np.sin(2 * np.pi * 110 * t)) * (rng.random(len(t)) > 0.5)
    step = (np.floor(t * 40) % 3 == 0)
    return (x * step + hp_fast(rng.standard_normal(len(t)), 3000) * 0.3) * 0.35 * np.exp(-t * 4)


def sfx_wind(d=8.0):
    t = tt(d); n = rng.standard_normal(len(t))
    w = lp_fast(n, 700) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.18 * t + 1))
    a = np.minimum(1, t / 1.5) * np.minimum(1, (d - t) / 1.5)
    return w * a * 1.2


def sfx_splash(d=1.6):
    t = tt(d); x = hp_fast(rng.standard_normal(len(t)), 1500) * np.exp(-t * 6) * 0.6
    for k in range(26):
        t0 = rng.uniform(0.02, 1.1); f = rng.uniform(900, 2600); i = int(t0 * SR)
        dd = tt(0.08); drop = np.sin(2 * np.pi * np.cumsum(f * (1 + dd * 6)) / SR) * np.exp(-dd * 50) * rng.uniform(0.1, 0.3)
        x[i:i + len(drop)] += drop[: len(x) - i]
    return x


def sfx_shimmer(d=2.5):
    t = tt(d); x = np.zeros(len(t))
    for k, f in enumerate([2093, 2637, 3136, 3951, 4186]):
        x += np.sin(2 * np.pi * f * t) * np.exp(-np.clip(t - k * 0.09, 0, None) * 2.5) * (t > k * 0.09)
    return x * 0.12


def sfx_riser(d=1.2):
    t = tt(d); f = 200 + 1800 * (t / d) ** 2
    return (np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.3 + hp_fast(rng.standard_normal(len(t)), 2500) * 0.25) * (t / d) ** 2


def sfx_thud():
    t = tt(0.6); return np.sin(2 * np.pi * np.cumsum(60 + 80 * np.exp(-t * 30)) / SR) * np.exp(-t * 7) * 0.8


# ---------------- musiques ----------------
def music_street():
    m = np.zeros((N, 2)); bpm = 140; b = 60 / bpm; t0 = 0.38  # premier temps = impact du flacon
    roots = [45, 45, 41, 43]  # La, La, Fa, Sol (mesures)
    bars = int((DUR - t0) / (4 * b)) + 1
    def silent(t):  # coupure avant le prix + arrêt pendant la fin
        return 21.9 <= t < 22.4
    for bar in range(bars):
        for beat in range(4):
            for sub in range(4):
                t = t0 + (bar * 4 + beat + sub / 4) * b
                if t >= DUR - 0.05 or silent(t):
                    continue
                if t > 27.0 and not (beat == 0 and sub == 0):
                    continue
                if sub == 0 and (beat in (0,) or (beat == 2 and bar % 2 == 1)):
                    place(m, kick808(note(roots[bar % 4] - 12) if t < 27 else 45), t, 0.9)
                if sub == 2 and beat == 3 and bar % 2 == 0:
                    place(m, kick808(note(roots[bar % 4] - 12), 0.4), t, 0.6)
                if beat in (1, 3) and sub == 0 and t < 27:
                    place(m, clap(), t, 0.55); place(m, snare(), t, 0.3)
                if t < 27 and t >= 1.5:
                    roll = (bar % 4 == 3 and beat == 3)
                    if roll:
                        for r in range(3):
                            place(m, hat(0.03), t + r * b / 12, 0.4, 0.3)
                    elif sub % 2 == 0 or (bar % 2 == 1 and sub == 3):
                        place(m, hat(), t, 0.45 if sub == 0 else 0.3, 0.25)
        # nappe sombre
        tb = t0 + bar * 4 * b
        if tb < 27.0:
            r = roots[bar % 4]
            place(m, pad([note(r + 12), note(r + 15), note(r + 19)], 4 * b, 900), tb, 0.35)
            # cloche aiguë (mélodie trap)
            mel = [76, 74, 72, 74][bar % 4]
            if bar >= 1:
                for k, off in enumerate([0, 0.75, 1.5, 2.5]):
                    if not silent(tb + off * b):
                        place(m, keys([note(mel - (k % 2) * 3)], 0.6) * 0.5, tb + off * b, 0.25, -0.2)
    place(m, pad([note(45), note(52), note(57)], 3.0, 700), 27.0, 0.5)
    m[:, 0] = conv_reverb(m[:, 0], 1.4, 0.18); m[:, 1] = conv_reverb(m[:, 1], 1.5, 0.18)
    return m


def music_cinema():
    m = np.zeros((N, 2))
    hijaz = [57, 58, 61, 62, 64, 65, 67, 69]  # La Hijaz : La Sib Do# Ré Mi Fa Sol La
    place(m, pad([note(33), note(40), note(45)], 26.5, 500), 0.0, 0.9)            # bourdon
    place(m, pad([note(57), note(64)], 9.0, 1400), 8.0, 0.35)
    place(m, pad([note(58), note(65)], 3.0, 1400), 17.0, 0.3)
    # phrase d'oud
    phrase = [(0.6, 4), (1.2, 3), (1.6, 2), (2.0, 1), (2.6, 0), (4.2, 2), (4.6, 3), (5.0, 4), (5.4, 5), (6.2, 4)]
    for rep, base in [(0, 0.0), (1, 8.2), (2, 14.6)]:
        for (dt, idx) in phrase:
            t = base + dt
            if t < 25:
                place(m, pluck_oud(note(hijaz[idx] + (12 if rep == 2 else 0)), 1.6, 0.55), t, 0.45, -0.3 + 0.1 * idx)
    # chapitres : une note longue par chapitre
    for t, idx in [(8.2, 0), (11.5, 3), (14.8, 4)]:
        place(m, pluck_oud(note(hijaz[idx] - 12), 2.4, 0.6), t, 0.6, 0.0)
    # percussions (tambour sur cadre) qui montent jusqu'à l'éclaboussure
    bpm = 90; b = 60 / bpm
    t = 17.5; k = 0
    while t < 21.4:
        place(m, sfx_thud(), t, 0.35 + 0.4 * (t - 17.5) / 4, 0.0)
        if k % 2 == 1:
            place(m, hat(0.05), t + b / 2, 0.15)
        t += b if t < 20 else b / 2; k += 1
    place(m, sfx_riser(1.3), 20.1, 0.5)
    place(m, kick808(45, 2.5), 21.4, 0.9)
    place(m, pad([note(45), note(52), note(57), note(61)], 6.0, 1800), 21.4, 0.45)
    place(m, pluck_oud(note(69), 3.0, 0.6), 27.0, 0.5)
    m[:, 0] = conv_reverb(m[:, 0], 3.0, 0.4); m[:, 1] = conv_reverb(m[:, 1], 3.2, 0.4)
    fade = np.ones(N); i = int(28.0 * SR); fade[i:] = np.linspace(1, 0, N - i)
    return m * fade[:, None]


def music_tiktok():
    m = np.zeros((N, 2)); bpm = 96; b = 60 / bpm
    chords = [[60, 64, 67, 71], [57, 60, 64, 67], [62, 65, 69, 72], [55, 59, 62, 65]]  # Do maj7, La m7, Ré m7, Sol 7
    bars = int(DUR / (4 * b)) + 1
    for bar in range(bars):
        tb = bar * 4 * b
        if tb >= DUR:
            break
        place(m, keys([note(x) for x in chords[bar % 4]], 4 * b), tb, 0.35)
        place(m, keys([note(chords[bar % 4][0] - 24)], 4 * b), tb, 0.35)
        for beat in range(4):
            t = tb + beat * b
            if t >= DUR - 0.1:
                continue
            if beat in (0, 2):
                place(m, kick808(55, 0.35) * 0.7, t, 0.55)
            if beat in (1, 3):
                place(m, snare(0.18, 220), t, 0.3)
            place(m, hat(0.04), t + b / 2, 0.25, 0.3)
            place(m, hat(0.03), t, 0.15, 0.3)
    crackle = np.zeros(N); idx = rng.integers(0, N, 900); crackle[idx] = rng.uniform(-0.25, 0.25, 900)
    m[:, 0] += lp_fast(crackle, 5000); m[:, 1] += lp_fast(crackle, 5000)
    m[:, 0] = lp_fast(m[:, 0], 7000); m[:, 1] = lp_fast(m[:, 1], 7000)
    return m


# ---------------- bruitages par vidéo (calés sur les images) ----------------
def sfx_street():
    s = np.zeros((N, 2))
    place(s, sfx_impact(), 0.38, 0.9)
    for t in (1.5, 6.0, 14.0):
        place(s, sfx_whoosh(0.5), t - 0.3, 0.5)
    for k in range(4):
        place(s, sfx_tick(3000 + k * 220), 2.0 + k * 0.43, 0.5, -0.3 + k * 0.2)
    for t, pan in ((6.15, 0.5), (7.95, -0.5), (9.75, 0.4)):
        place(s, sfx_whoosh(0.45), t, 0.45, pan)
    place(s, sfx_whoosh(0.6), 22.0, 0.6)
    place(s, sfx_glitch(), 22.4, 0.6); place(s, sfx_glitch(0.2), 23.9, 0.35); place(s, sfx_glitch(0.2), 25.3, 0.35)
    place(s, sfx_impact(1.0), 24.6, 0.45)
    place(s, sfx_shimmer(), 27.3, 0.6)
    return s


def sfx_cinema():
    s = np.zeros((N, 2))
    place(s, sfx_wind(8.4), 0.0, 0.55)
    place(s, sfx_riser(2.5) * 0.6, 2.4, 0.5)
    for t in (8.2, 11.5, 14.8):
        place(s, sfx_shimmer(1.8), t, 0.5)
    place(s, sfx_splash(), 21.4, 0.85)
    place(s, sfx_shimmer(3.0), 26.2, 0.6)
    return s


def sfx_tiktok():
    s = np.zeros((N, 2))
    place(s, sfx_impact(0.8) * 0.6, 0.0, 0.5)
    for t in (2.0, 8.0, 16.0, 24.0):
        place(s, sfx_whoosh(0.35), t - 0.2, 0.4)
    for t in (2.05, 8.15, 9.4, 10.6, 12.2, 16.2, 19.6, 25.2):
        place(s, sfx_pop(), t, 0.55)
    place(s, sfx_shimmer(), 24.6, 0.5)
    return s


def write(path, x, peak=0.89):
    x = x / max(1e-9, np.abs(x).max()) * peak
    d = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes())


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    for v, mus, sfx in (("v1-street", music_street, sfx_street), ("v2-cinema", music_cinema, sfx_cinema), ("v3-tiktok", music_tiktok, sfx_tiktok)):
        write(f"{root}/{v}/assets/audio/music.wav", mus())
        write(f"{root}/{v}/assets/audio/sfx.wav", sfx())
        print("ok", v)
