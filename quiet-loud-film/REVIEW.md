# REVIEW — QUIET / LOUD

## Choix créatifs

- Film de mode original, sans produit, logo ni nom de marque existants, et sans boutique ni appel à l'achat (demande du client).
- Concept « QUIET / LOUD » : le silence du luxe (studio blanc, gros plans matières, serif italique) contre le bruit de la rue (nuit, néons, condensée Anton, coupes sur le beat). La personne qui regarde est « entre les deux ».
- Une seule couleur d'accent : bleu électrique `#1462FF` (trait du diptyque, mot « Toi. / Jij. », barre du carton final).
- Le drop de la musique (beat 9,635 s du morceau) est calé sur 10,70 s du film, au flash qui fait passer de QUIET à LOUD.
- La voix off est découpée en 13 phrases posées sur une grille commune : les deux langues coupent aux mêmes images. « toi / jij » tombe sur 17,3 s et « Loud » sur 26,3 s dans les deux versions.
- « LOUD. » passe derrière la passante (détourage Adobe) dans la rue ; dans le souterrain, le mot plein passe devant et les deux contours derrière, pour rester lisible.

## Choix techniques (rendu sans carte graphique)

- La machine de rendu n'a pas de GPU : le grain WebGL de HyperFrames et le flou de mouvement passaient par une capture d'écran image par image (≈ 3 s par image, plus d'une heure par version). Ils ont été retirés du rendu.
- Vignette : gravée directement dans les photos (`assets/graded/`, ffmpeg `vignette`), photos ramenées à 1340×2400.
- Grain : ajouté après le rendu sur le MP4 entier (ffmpeg `noise`, grain animé léger), voir `tools/finish.sh`.

## Mesuré

- `hyperframes check` : 0 erreur.
- Fichiers livrés : `renders/quiet-loud-FR.mp4` et `renders/quiet-loud-NL.mp4`, 1080×1920, 30 i/s, 32,3 s, H.264 + AAC 48 kHz, ≈ 15 Mo chacun.
- Son (ffmpeg ebur128) : FR −14,5 LUFS, pic −1,0 dB ; NL −14,6 LUFS, pic −1,2 dB (cible réseaux −16 à −14 LUFS).
- Images extraites des MP4 finaux et regardées : textes, sous-titres et mots à l'écran dans la bonne langue.
- Planches d'images vérifiées à 0 ; 2 ; 4,4 ; 6,4 ; 7,6 ; 9 ; 10,6–10,9 (flash) ; 11,6 ; 12,95 ; 13,4 ; 14 ; 14,6 ; 16,2 ; 16,6 ; 17,8 ; 20,45 ; 21,2 ; 22 ; 23,5 ; 25,4 ; 26,7 ; 27 ; 29,5 ; 29,6 ; 32,05 s.

## Avertissements gardés volontairement

- `outside_safe_zone` sur « LOUD. » (rue et souterrain) : le bas des lettres frôle la colonne d'icônes de TikTok ; le mot reste lisible.
- `outside_safe_zone` sur « Quiet. » (bord haut de YouTube Shorts, quelques pixels).
- `contrast_aa_failure` sur « LOUD. » dans le souterrain : mesuré sur la lumière bleue derrière ; à l'image, le mot blanc sur le blouson noir se lit.
- `duplicate_media_discovery_risk` : la photo studio sert deux fois dans la scène des silhouettes (plein cadre puis bande), c'est voulu.

## Ce que personne n'a vérifié

- Le son a été mesuré (niveaux, présence, calage), pas écouté.
- Les mannequins et vêtements sont générés par IA (FLORA) : ce ne sont pas de vraies pièces.

## Plan le plus faible

- Le passage souterrain : le mot plein devant le mannequin est efficace, mais l'image est statique entre deux punch-ins. Avec plus de budget, un plan vidéo IA (≈ 0,50 à 1,30 $ par plan de 5 s) donnerait du vrai mouvement aux scènes de rue.
