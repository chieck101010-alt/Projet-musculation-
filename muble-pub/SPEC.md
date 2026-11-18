# SPEC — Muble « 2 minutes chrono »

GOAL:    le spectateur comprend en 5 étapes comment réserver un VTC sur Muble, et a envie de réserver son premier trajet.
OUTPUT:  HyperFrames, 1080 × 1920, 30 i/s. Version principale 72 s (2160 images), version courte 25 s (750 images).
TIME:    la voix off est l'horloge : chaque texte arrive sur le mot qui le dit. Musique électro légère ~104 BPM.

LOOK
- Fond : deux mondes seulement.
  1. **Le monde réel** : vidéos Adobe Stock (déjà recadrées 9:16 et étalonnées dans `assets/footage/`, vignette 18 %).
  2. **Le monde Muble** : un plateau violet Muble, exactement comme la section CTA du site — dégradé linéaire 160° de #6A2BC2 à #4C14A6, avec une seule tache de lumière lilas (#C4A6FF à 18 %) en haut à droite. Pas de « vide noir ».
- Encre : blanc #FFFFFF sur violet et sur vidéo ; #111018 sur les cartes blanches.
- Accent : lilas #C4A6FF, sur **un seul mot par plan** (le mot-clé du sous-titre ou du titre).
- Typo : Plus Jakarta Sans (police du site, fichier dans `assets/fonts/`).
  - Titres : 800, 104–132 px, interlettrage −3 %, 1 à 2 lignes.
  - Étiquettes d'étape : 800, 44 px.
  - Sous-titres : 700, 60 px, ombre portée 0 4 18 rgba(0,0,0,.45), max 5 mots par groupe.
  - Interface du site dans le téléphone : tailles du site × 2,2 (mobile 390 px → écran 860 px).
- Matière du téléphone : châssis graphite (dégradé #3A3842 → #121117), arête claire 2 px rgba(255,255,255,.28), rayon 118 px, Dynamic Island 210 × 62 px, ombre 0 60 120 rgba(20,0,50,.55). Écran 860 × 1864 px avant mise à l'échelle.
- Grain : 3 % sur tout le film (texture fixe, pas d'animation de bruit).

OBJECTS
- Le téléphone (voir matière ci-dessus) qui affiche l'interface Muble reconstruite d'après les captures : en-tête avec logo + menu, formulaire « Réservez votre trajet », cartes véhicules Éco / Berline, bouton « Réserver mon trajet ».
- Le chrono : anneau de 5 segments (épaisseur 14 px, Ø 168 px), segments gris clair à 25 % qui se remplissent en blanc ; au centre, temps en 800 44 px « 0:00 » → « 1:48 ». S'arrête avant 2:00 : coche ✓.
- Le doigt : disque blanc 64 px à 55 % d'opacité, qui s'enfonce (échelle 0,8) au contact, sans anneau d'onde.
- La frise « après l'envoi » : 4 jalons reliés par une ligne qui se trace (📞 rappel → 🔒 prix figé → 💳 paiement → 🚘 chauffeur), icônes dessinées en SVG au trait 4 px, pas d'emoji.
- Le logo : SVG vectorisé d'après le logo officiel (`assets/logo/`), jamais déformé.

MOTION
- Entrées : expo.out 0,5–0,7 s ; sorties : power3.in 0,3 s (40 % plus court).
- Caméra (zoom sur un champ) : power2.inOut 0,8 s.
- Ressort du téléphone : back.out(1.2) pour l'arrivée, puis immobile.
- Saisie : 1 lettre toutes les 2 images (0,067 s).
- Titres par mot : flou 6 px → 0 et opacité 0 → 1 en 0,13 s, 0,07 s d'écart.
- Transitions entre plans réels : whip (0,2 s, flou horizontal 18 px) ou coupe sèche sur le temps fort. Entrée dans le monde Muble : « l'objet devient le monde » (le bouton / la carte grandit jusqu'à remplir le cadre).

SHOTS (v72, à recaler sur la voix)
- S1 0–7 s : 3 plans réels de 1,6–2 s, chaque question en titre, puis inondation violette et logo.
- S2 7–17 s : chauffeur + tour Eiffel, puis le téléphone monte en 3D et se pose.
- S3 17–45 s : démo, 5 étapes, chrono en haut, étiquettes ①–⑤, zooms sur les champs ; frise après l'envoi.
- S4 45–55 s : 3 arguments en plein écran sur vidéo réelle.
- S5 55–64 s : 4 coupes au tempo : Aéroports / Gares / Rendez-vous / Sorties.
- S6 64–72 s : Paris de nuit → téléphone → logo + signature + bouton.

BANNED
- Vide noir avec éléments flottants ; lueurs, néons, orbes, particules décoratives ; cartes en verre.
- Trois cartes en rang ; titres qui bougent pendant la lecture ; tout qui glisse vers le haut en fondu.
- Anneaux d'onde au clic ; emoji à la place d'icônes ; logo collé dans un coin.
- Fausse interface : aucun écran non vu sur les captures (pas d'écran de paiement, pas de prix chiffré).
- Texte dans les 168 px du haut et sous 1330 px (zone des boutons TikTok/Snap), sauf texture.

QA
- 0,0 s : une image forte avec un texte déjà lisible (pas de noir, pas de logo).
- Chaque étape : le champ qui est nommé par la voix est visible et zoomé quand le mot est dit.
- Fin : logo net, signature lisible ≥ 2 s.
