# Check-list contrôle qualité (avant chaque livraison)

## Textes
- [ ] Orthographe et accents vérifiés (texte à l'écran, sous-titres, nom de marque, prix).
- [ ] Chaque texte reste à l'écran assez longtemps pour être lu (≈ 2 s minimum pour la ligne finale).
- [ ] Aucun texte ne se chevauche (`hyperframes check` → `content_overlap`).

## Visuels officiels
- [ ] Le produit, le logo et la gravure viennent des fichiers officiels, sans déformation.
- [ ] Aucune face du produit inventée de façon trompeuse (ce qui est deviné est dit à l'utilisateur).
- [ ] Pas de halo ni de bord coupé visible sur les détourages.

## Plateforme
- [ ] Format : 1080×1920 (9:16) pour Snap/TikTok/Reels, 30 i/s, durée exacte demandée.
- [ ] Safe zones : rien d'important dans les 168 px du haut ; textes et produit entre 168 et 1330 px ; rien sous la barre d'actions à droite.
- [ ] L'image 0 n'est jamais noire et porte déjà l'accroche (c'est la miniature).
- [ ] Sous-titres présents (beaucoup regardent sans le son).

## Son
- [ ] Voix off présente, compréhensible, au bon moment.
- [ ] Musique baissée sous la voix (ducking).
- [ ] Bruitages calés sur les actions visibles.
- [ ] Volume final autour de −16 LUFS, sans saturation.

## Fichier final
- [ ] `ffprobe` : bonne résolution, durée, piste audio présente.
- [ ] Quelques images extraites du MP4 regardées (le rendu correspond aux captures).
- [ ] Fichiers commités et poussés ; vidéos envoyées à l'utilisateur.
