# QUIET / LOUD — film de mode 9:16

Film créatif original (TikTok, Snapchat, Instagram Reels). Aucun produit, logo ou nom de marque existant, aucune boutique ni appel à l'achat.

## Concept

Deux mondes qui se répondent :
- **QUIET** : les codes du luxe contemporain (retenue, silence, espace vide, matières). Inspiration : campagnes Prada récentes, studio blanc et calme (SS26), « Simple Stories » (FW26), sans les copier.
- **LOUD** : l'énergie du streetwear (rue de nuit, mouvement, coupes sur le beat).
- La personne qui regarde est **entre les deux**. Message final : « Ton style parle en premier. »

## Identité visuelle

| Élément | Choix |
|---|---|
| Couleurs | Blanc galerie `#F2F0EB`, noir encre `#0D0E11`, gris béton `#8A8C91`, un seul accent bleu électrique `#1462FF` |
| Typos | Serif italique (le calme) + grotesque condensée extra-grasse (le bruit) + sans-serif sobre pour les sous-titres |
| Mouvement | QUIET : lent, beaucoup d'espace, zooms très doux. LOUD : coupes au beat, saccades, flou de mouvement, zooms rapides |
| Texture | Grain film léger et vignette sur tout le film |

## Storyboard (32,3 s, 1080×1920, 30 i/s — minutages du montage final)

| Temps | Image | Texte à l'écran | Voix off FR | Voix off NL | Son |
|---|---|---|---|---|---|
| 0,0–3,6 s | Studio blanc, silhouette immobile en doudoune noire, zoom avant très lent | **QUIET.** (serif italique géant) | « Le luxe, c'est le silence. » | « Luxe is stilte. » | Pulsation grave, presque le silence |
| 3,6–10,7 s | 3 gros plans : couture de survêtement, zip de doudoune, sneaker blanche ; volets et travellings lents | COUPE. / MATIÈRE. / DÉTAIL. | « Une coupe nette. Une matière qui tombe juste. Un détail que personne ne voit… sauf toi. » | « Een strakke snit. Stof die precies valt. Een detail dat niemand ziet… behalve jij. » | Nappes, déclencheur photo à chaque plan |
| 10,7 s (drop) | Flash blanc puis noir | **LOUD.** qui claque | — | — | Whoosh inversé + impact grave, la musique démarre |
| 10,7–15,5 s | Rue de nuit (survêtement marine), passage souterrain (doudoune, casquette) ; coupes sur le beat, zooms rapides | **LOUD.** condensé géant, saccadé | « La rue, c'est le bruit. Le mouvement. L'énergie. » | « De straat is lawaai. Beweging. Energie. » | Kick, claps |
| 15,5–20,3 s | Diptyque vertical studio / rue, un trait bleu les sépare | ENTRE LES DEUX — **TOI.** | « Et entre les deux… il y a toi. Ta silhouette. Ton rythme. » | « En daartussen… sta jij. Jouw silhouet. Jouw ritme. » | |
| 20,3–25,1 s | 4 silhouettes plein cadre sur le beat (survêtement, doudoune, hoodie, accessoires), puis en bandes verticales qui glissent | 01 — 04 + nom de la pièce | « Ta façon d'entrer dans une pièce. Pas besoin de crier pour être vu. » | « Hoe jij een ruimte binnenloopt. Je hoeft niet te schreeuwen om gezien te worden. » | Déclencheurs photo |
| 25,1–32,3 s | Carton final, le « / » en bleu | **QUIET / LOUD** — « Ton style parle en premier. » | « Quiet. Loud. Ton style parle en premier. » | « Quiet. Loud. Jouw stijl spreekt eerst. » | Impact sur LOUD, la musique s'éteint en fondu |

Sous-titres de la voix off en bas de l'écran (dans les zones sûres), pour le visionnage sans le son.

## Production

| Élément | Outil | Coût (devis FLORA du 18/11/2026) |
|---|---|---|
| 3 photos principales (studio, rue, souterrain) | FLORA — Nano Banana 2.1, 2K | 3 × 0,077 $ |
| 6 photos (3 gros plans, 3 silhouettes studio) | FLORA — Seedream 5.5, 2K | 6 × 0,024 $ |
| Voix off FR + NL | FLORA — ElevenLabs v3 | 2 × 0,121 $ |
| Musique 60 s instrumentale | FLORA — ElevenLabs Music v2.5 | 0,204 $ |
| 2 bruitages (whoosh/impact, déclencheurs photo) | FLORA — ElevenLabs Sound Effects | 2 × 0,144 $ |
| Montage, typo animée, transitions, sous-titres, rendu MP4 | HyperFrames (+ hyperframes-registry) | gratuit |
| **Total** | | **≈ 1,11 $** (solde disponible : 1,72 $) |

Plans vidéo IA (Kling, MiniMax…) non retenus : 0,48 à 1,30 $ par plan de 5 s, hors budget. Les mouvements de caméra sont faits dans HyperFrames.

## Livrables

- `renders/quiet-loud-FR.mp4` et `renders/quiet-loud-NL.mp4` — 1080×1920, 30 i/s, 32,3 s, voix off, musique, bruitages, sous-titres.

## Refaire une version

`python3 tools/build.py fr` (ou `nl`) réécrit `index.html` pour la langue voulue, puis rendu HyperFrames. Les scènes de `compositions/` sont communes aux deux langues ; seuls la voix, les sous-titres et les mots à l'écran changent.
