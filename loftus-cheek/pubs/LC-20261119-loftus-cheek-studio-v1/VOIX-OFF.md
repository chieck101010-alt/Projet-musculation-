# VOIX OFF — PROJET 001 (v2, synchronisée sur 28 s)
Voix : homme FR, jeune adulte, légèrement grave, élégante, naturelle, charismatique, pointe d'énergie urbaine.
Musique : 120 BPM → 1 temps = 0,5 s · drops à 6,0 s et 22,0 s.
Prononciation : LOFTUS-CHEEK = « LOF-tusse TCHIK » · « DM » = « dé-èm » · « IA » = « i-a ».

| Début | Fin | Réplique | Jeu | Image au même moment |
|---|---|---|---|---|
| 0,3 | 1,4 | « Votre produit est fort… » | calme, proche du micro | photo vendeur, secousse |
| 1,7 | 2,8 | « …mais personne ne s'arrête. » | léger sourire, chute de voix | fissure → éclats de verre (2,0) |
| 3,4 | 5,6 | « Il lui manque… une dimension. » | lent, pause avant « une dimension » | particules chrome, travelling avant |
| 6,0 | — | *(silence : impact du drop)* | | flash + LC 3D |
| 6,5 | 7,6 | « LOFTUS-CHEEK. » | posé, assuré, articulé | nom qui claque, reflet |
| 9,1 | 9,8 | « Streetwear. » | énergique, sec | survêtement |
| 11,1 | 11,8 | « Sneakers. » | énergique | sneaker |
| 13,2 | 14,2 | « Parfums… » | ralenti, voix plus douce | flacon en verre |
| 15,2 | 16,3 | « Accessoires. » | élégant | montre chrome |
| 17,0 | 17,9 | « Publicité IA. » | rythmé, sur le temps | mot 1 |
| 18,0 | 19,2 | « Motion design 3D. » | rythmé | mot 2 |
| 19,5 | 20,2 | « Voix off. » | rythmé | mot 3 |
| 20,4 | 21,9 | « Des vidéos qui arrêtent le scroll. » | montée d'intensité | mosaïque qui recule |
| 22,0 | — | *(silence : 2e drop)* | | zoom à travers le C |
| 23,2 | 26,0 | « Donnez une nouvelle dimension à votre marque. » | grave, charismatique | logo complet |
| 26,3 | 27,3 | « Contact en DM. » | complice, sûr de lui | bouton CONTACT EN DM |
| 27,3 | 28,0 | *(silence)* | | image finale fixe |

Total ≈ 45 mots ≈ 15 s de parole sur 28 s : la musique respire.

## Méthode (gratuite) de synchronisation
1. La voix est générée **en une seule prise** (ton naturel et continu).
2. Découpage automatique aux silences (ffmpeg) → un fichier par réplique dans `audio/voix/`.
3. Chaque réplique est placée à sa seconde exacte dans HyperFrames. Pour corriger une phrase, on ne régénère qu'elle.
