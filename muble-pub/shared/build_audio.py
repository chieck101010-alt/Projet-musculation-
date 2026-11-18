#!/usr/bin/env python3
"""Prépare l'audio de la pub 72 s.

- normalise chaque phrase de voix à -16 LUFS (assets/audio/vo/voNN-n.wav)
- fabrique la musique de fond calée, avec fondus et baisse automatique sous la voix (assets/audio/music-bed.wav)
- écrit les mots minutés (temps du film) pour les sous-titres (assets/audio/vo-words.json)
"""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, "assets/audio")
TOTAL = 72.0
MUSIC_OFFSET = 5.775  # la chute naturelle de la musique (77 s) tombe sur le logo final (~71,2 s)

# début de chaque fichier de voix dans le film (secondes)
PLACE = {
    "vo01": 0.00, "vo02": 5.10, "vo03": 7.60, "vo04": 12.90, "vo05": 17.25, "vo06": 22.30, "vo07": 27.95,
    "vo08": 33.75, "vo09": 39.20, "vo10": 48.30, "vo11": 56.30, "vo12": 63.30, "vo13": 68.40,
}
TEXT = {
    "vo01": "Un rendez-vous ? Un avion à prendre ? Ou simplement besoin de vous déplacer ?",
    "vo02": "Découvrez Muble.",
    "vo03": "Muble, votre service de VTC premium à Paris et en Île-de-France.",
    "vo04": "Réservez votre chauffeur simplement, en quelques étapes.",
    "vo05": "Première étape : indiquez votre adresse de départ et votre destination.",
    "vo06": "Choisissez ensuite la date, le nombre de passagers et vos besoins en bagages.",
    "vo07": "Sélectionnez le véhicule adapté à votre trajet, selon vos envies et votre budget.",
    "vo08": "Renseignez vos coordonnées pour recevoir les informations concernant votre réservation.",
    "vo09": "Muble vous rappelle avec le prix exact, figé avant votre validation. Puis vous payez en ligne, en toute sécurité.",
    "vo10": "Avec Muble, profitez d'un chauffeur professionnel, d'un prix connu à l'avance et d'un trajet organisé selon vos besoins.",
    "vo11": "Pour vos déplacements professionnels, vos voyages ou vos sorties, Muble vous accompagne en Île-de-France.",
    "vo12": "Muble. Votre chauffeur privé, en toute simplicité.",
    "vo13": "Réservez dès maintenant.",
}

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stderr[-2000:])
    return r

def tokens(text):
    out = []
    for t in text.split():
        if re.fullmatch(r"[?!:;»]", t) and out:
            out[-1] += " " + t
        else:
            out.append(t)
    return out

def main():
    ana = json.load(open(os.path.join(A, "vo/analyse.json")))
    # 1) voix normalisées
    for k in PLACE:
        sh(["ffmpeg", "-y", "-v", "error", "-i", f"{A}/vo/{k}.wav", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-ac", "1", f"{A}/vo/{k}-n.wav"])
    # 2) piste voix complète (clé du ducking)
    inputs, filt = [], []
    for i, (k, t) in enumerate(PLACE.items()):
        inputs += ["-i", f"{A}/vo/{k}-n.wav"]
        filt.append(f"[{i}:a]adelay={int(t * 1000)}:all=1[a{i}]")
    filt.append("".join(f"[a{i}]" for i in range(len(PLACE))) + f"amix=inputs={len(PLACE)}:normalize=0,apad=whole_dur={TOTAL}[v]")
    sh(["ffmpeg", "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filt), "-map", "[v]", "-t", str(TOTAL), "-ar", "48000", f"{A}/vo-track.wav"])
    # 3) musique calée + baisse sous la voix
    sh(["ffmpeg", "-y", "-v", "error", "-ss", str(MUSIC_OFFSET), "-t", str(TOTAL), "-i", f"{A}/music-raw.mp3", "-i", f"{A}/vo-track.wav", "-filter_complex",
        "[0:a]aresample=48000,volume=-7dB,afade=t=in:d=0.25,afade=t=out:st=71.1:d=0.9[m];"
        "[1:a]aresample=48000,pan=stereo|c0=c0|c1=c0[k];"
        "[m][k]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=420:makeup=1[d]",
        "-map", "[d]", "-t", str(TOTAL), f"{A}/music-bed.wav"])
    # 4) mots minutés (texte exact du script, temps de Whisper ou répartis)
    words = []
    for k, t0 in PLACE.items():
        info = ana[k]
        toks = tokens(TEXT[k])
        ws = info["words"]
        onset = info["onset"]
        span_end = info["offset"]
        if len(ws) == len(toks):
            for tok, w in zip(toks, ws):
                words.append({"text": tok, "start": round(t0 + onset + w["start"], 3), "end": round(t0 + onset + w["end"], 3), "line": k})
        else:
            total_chars = sum(len(x) for x in toks)
            cur = onset
            dur = span_end - onset
            for tok in toks:
                d = dur * len(tok) / total_chars
                words.append({"text": tok, "start": round(t0 + cur, 3), "end": round(t0 + cur + d, 3), "line": k})
                cur += d
            print("répartition proportionnelle pour", k, len(ws), "≠", len(toks))
    json.dump(words, open(f"{A}/vo-words.json", "w"), ensure_ascii=False, indent=0)
    print("ok", len(words), "mots")

if __name__ == "__main__":
    main()
