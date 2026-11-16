# REVIEW — « Un seul cadeau » · Père Noël & Cie (48.4 s, 1920×1080, 30 i/s)

## Choix créatifs
- Storyline A retenue : on suit UN cadeau rouge de l'usine du Pôle Nord jusque sous le sapin, en un seul plan-séquence
  isométrique (caméra orthographique Three.js, élévation 35.26°). Non construites : B « maison de poupée » (zooms sans fin),
  C « rapport annuel » (parodie corporate). Voir `STORYLINES.md`.
- Tout est modélisé en code (Three.js + GSAP dans HyperFrames) : aucune image ni vidéo générée.
- Récit visuel : chaque livraison allume les fenêtres d'une maison ; au dézoom, toute la carte s'allume en vague
  et les routes or partent du Pôle Nord.
- Le compteur « 2 000 000 000 » est posé sur une étiquette d'expédition tamponnée (lisible malgré le décor chargé).
- Carte de fin : le cadeau géant tombe, le couvercle saute, un mini-traîneau en sort et « tire » le logotype.
- Son : voix off FR (Gemini 3.1 Flash TTS, voix Algieba, via Flora, 7 répliques placées une par une),
  musique Lyria 3.5 (via Flora) coupée sur un temps à 38.12 s vers sa fin, bruitages Pixabay fournis par HyperFrames.

## Mesuré / regardé
- `hyperframes check` : 0 erreur. Avertissements gardés exprès : `composition_file_too_large` (le monde 3D est un
  seul plan continu, un seul fichier) et `canvas_content_at_edge` (le monde est plein cadre, voulu).
- Regardé : planches de revue, plage du décollage (13.4–15.2), premier largage (16.2–17.4), toute la séquence maison
  (24–31), dézoom (31.8–37.8), carte de fin (38.3–48.15), feuille téléphone 360 px.
- Le son a été mesuré (placement, silences, structure de la musique), pas écouté.
- Les chiffres (2 milliards, 24 fuseaux) sont de la fiction publicitaire, pas des données réelles.

## Le plan le plus faible
- Le survol de la ville (15–23 s) : les cadeaux largués restent petits à l'image. Avec plus de temps :
  un ou deux punch-ins sur une cheminée au moment de l'impact.
- La voix off a été générée avec des indications de ton entre crochets ; à réécouter pour confirmer qu'elles
  n'ont pas été lues à voix haute (les durées mesurées suggèrent que non).
