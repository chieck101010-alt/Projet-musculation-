# REVIEW — Évolution 3 mois (1 min 44, 1920×1080, 30 i/s)

## Choix
- Storyline A « La salle » (choix de l'utilisateur), durée demandée ~1 min 30 → 103.6 s
  (22 exercices × 2.8 s + 4 cartes jour + repos + intro/outro). Autres pistes : `STORYLINES.md`.
- Tout est modélisé en code (Three.js dans HyperFrames) : salle, mannequin anatomique à 14 groupes
  musculaires, 16 mouvements distincts animés par cinématique inverse, machines et barres.
- Programme repris à l'identique (ordre, noms, 3 × 10 à 12) ; jour 3 = repos.
- Avant = photo chambre, après = photo parc (indiqué par l'utilisateur).
- Comparaison : seulement 3 différences visibles entre les 2 photos (pectoraux, épaules, bras),
  avec la mention « lumière, tenue et pose différentes ». Rien d'inventé (pas de poids, pas de chiffres).
- Son : voix off masculine FR (Gemini TTS « Orus », 9 répliques via Flora), musique ElevenLabs Music
  (via Flora) montée en 3 morceaux calés sur les temps (passage calme sur le repos, drop sur le jour 4,
  pause puis drop sur la révélation de l'après), bruitages HyperFrames.

## Mesuré / regardé
- `check` : 0 erreur. Gardés : fichiers longs (gym 3D = un seul plan), canvas plein cadre.
- Les explications ont été raccourcies à 4–6 mots pour tenir dans 2.8 s ; à 1 min 30 c'est la limite
  de lecture. Une version ~2 min 30 donnerait plus de confort.
- Son mesuré, pas écouté.

## Plus faible / à faire avec plus de temps
- Le mannequin est stylisé (pas un écorché médical) ; les poses assises/couchées gardent un léger
  aspect « poupée articulée ».
- 4K : possible avec `render --resolution 4k`, environ 4× plus long (rendu logiciel WebGL).
