# STORYBOARD — PROJET 001 · « NOUVELLE DIMENSION » (v2 validée en direction)
LC-20261119-loftus-cheek-studio-v1 · 28 s · 9:16 · 1080×1920 · 30 i/s · musique 120 BPM (1 mesure = 2 s)

## Concept
**Le chrome qui transforme.** On commence par ce que tous les vendeurs connaissent : une photo produit plate, prise au téléphone, sur un lit.
Elle **se brise comme du verre**. Les éclats deviennent du chrome liquide qui forme le **monogramme LC**.
Ensuite, chaque produit traverse ce chrome et en ressort en version pub : street, puis luxe.
Message : *votre produit est déjà bon, nous lui donnons une nouvelle dimension.* L'appel à l'action final reprend le même mot.

Pourquoi ça marche : le vendeur se reconnaît dès la 1re seconde (sa propre photo), la casse crée la surprise (l'accroche), et l'avant/après prouve le savoir-faire sans un mot de trop.

## Identité visuelle
- Couleurs : noir `#050505`, anthracite `#1A1A1D`, chrome (dégradé `#F2F2F4 → #8A8A90 → #2B2B2F`), blanc `#F5F5F5`, champagne `#D8C3A0` (touches luxe uniquement).
- Typos (libres de droits, vérifiées en production) : titres larges et futuristes (type *Unbounded* / *Syncopate*), texte courant *Manrope*, accent luxe *Cormorant Garamond* (scène parfum).
- Logo : **L = coin de viseur caméra**, **C = bague d'objectif / diaphragme**. Le L s'emboîte dans l'ouverture du C. 3 variantes SVG à choisir avant l'animation 3D.
- Grain argentique léger sur toute la vidéo, vignettage, lumière principale froide et reflets champagne.

## Storyboard
| # | Temps | Image / caméra | Texte à l'écran | Voix off | Son |
|---|---|---|---|---|---|
| 1 · ACCROCHE | 0,0–3,0 | Photo produit « style vendeur » : sneaker sur un lit, lumière jaune, cadre de travers, légère secousse de téléphone. À 1,5 s, fissure ; à 2,0 s, l'image **explose en éclats de verre** vers la caméra (temps fort). | « VOTRE PUB RESSEMBLE À ÇA ? » (police simple, façon Snap) | « Votre produit est fort… mais personne ne s'arrête. » | Ambiance pièce plate → craquement → **impact basse + verre** sur le 1er temps fort |
| 2 · LA BASCULE | 3,0–6,0 | Vide noir. Les éclats deviennent des **particules chrome** qui tourbillonnent et convergent. Travelling avant lent. Balayage de lumière. | « IL LUI MANQUE UNE DIMENSION. » (lettres qui apparaissent avec un reflet) | « Il lui manque… une dimension. » | Montée (riser), cordes graves |
| 3 · LOGO | 6,0–9,0 | **Monogramme LC chrome en 3D** qui pivote de ¾ vers la face. Flash blanc sur le temps fort. « LOFTUS-CHEEK » claque en dessous, reflet qui court sur les lettres. | LOFTUS-CHEEK | « LOFTUS-CHEEK. » | **DROP** : braam ciné + 808, impact |
| 4a · STREET | 9,0–11,0 | Survêtement en studio, lumière urbaine contrastée (néon froid), caméra qui tourne vite autour. Sortie en whip pan. | STREETWEAR (glitch RGB bref) | « Streetwear… » | Hi-hats trap, whoosh court |
| 4b · STREET | 11,0–13,0 | Sneaker en 2,5D (effet de profondeur), traits de vitesse, secousse sur le temps. | SNEAKERS | « …sneakers… » | Whoosh + impact sec |
| 4c · LUXE | 13,0–15,0 | **Bascule luxe** : tout ralentit. Flacon de parfum 3D en verre, reflets dorés, fumée légère, mouvement de caméra lent en arc. Transition par fuite de lumière. | PARFUMS (serif élégante) | « …parfums… » | La batterie s'efface, nappe + scintillement |
| 4d · LUXE | 15,0–17,0 | Montre / chaîne chrome, orbite lente, reflet d'objectif (lens flare) qui traverse le métal. | ACCESSOIRES | « …accessoires. » | Petit « tiiing » métal |
| 5 · SERVICES | 17,0–22,0 | Les 4 produits se rangent en **mosaïque 2×2** qui recule. Puis 3 mots claquent un par un, plein écran, en alternant les sens d'entrée, chaque mot calé sur un temps. | PUBLICITÉ IA · MOTION DESIGN 3D · VOIX OFF — puis « QUI ARRÊTENT LE SCROLL » | « Publicité IA. Motion design 3D. Voix off. Des vidéos qui arrêtent le scroll. » | 808 qui revient, montée filtrée vers le drop |
| 6 · FINAL | 22,0–28,0 | Zoom ciné à travers l'objectif du C → **logo complet** : LC chrome qui s'assemble, halo, LOFTUS-CHEEK, puis AI CREATIVE STUDIO. Bouton pilule « CONTACT EN DM » qui pulse. Les 1,5 dernières secondes restent fixes (boucle propre sur Reels). | Donnez une nouvelle dimension à votre marque. · AI CREATIVE STUDIO · **CONTACT EN DM** | « Donnez une nouvelle dimension à votre marque. Contact en DM. » | 2e drop sur 22,0, puis résonance qui s'éteint |

Zones de sécurité : textes entre 250 px du haut et 340 px du bas (interfaces Reels et Snap).
Sous-titres : oui, mots clés en chrome (la vidéo reste compréhensible sans le son).

## Voix off — texte intégral (≈ 45 mots, débit posé)
> Votre produit est fort… mais personne ne s'arrête.
> Il lui manque… une dimension.
> LOFTUS-CHEEK.
> Streetwear. Sneakers. Parfums. Accessoires.
> Publicité IA. Motion design 3D. Voix off.
> Des vidéos qui arrêtent le scroll.
> Donnez une nouvelle dimension à votre marque. Contact en DM.

Choix du « vous » partout, pour rester cohérent avec ta phrase finale imposée. (Variante « tu », plus street, possible si tu préfères.)
Prononciation à verrouiller : « Loftus-Cheek » = *LOF-tusse TCHIK*.

## Effets prévus (bibliothèque hyperframes-registry, vérifiés)
| Moment | Bloc / composant | Rôle |
|---|---|---|
| Accroche | `camera-shake`, éclats de verre faits sur mesure (Three.js), inspirés de `glass-shard-title` | Casse de la photo |
| Bascule | `particle-text-dissolve`, `light-sweep-pass` | Particules chrome, balayage lumineux |
| Logo | `extruded-logo`, `logo-sting`, `shimmer-sweep` | LC 3D chrome, nom qui claque, reflet |
| Street | `rgb-glitch-text`, `whip-pan-cut` | Énergie, coupes sèches |
| Luxe | `light-leak`, `lens-flare`, flacon 3D Three.js | Lumière ciné, reflets |
| Services | `parallax-zoom`, `caption-kinetic-slam` | Mosaïque, mots plein écran |
| Final | `cinematic-zoom`, `logo-outro` | Zoom à travers l'objectif, logo final |
| Partout | `grain-overlay` | Texture cinéma |

L'animation du logo sera fabriquée **à part** (`identite/logo/`), en intro de 2 s et en final de 5 s, pour être réutilisée dans toutes tes pubs.

## Musique et sound design
- **Musique** (générée, instrumentale, 28 s, 120 BPM) : « hybride trap cinématique ». 808 profonde, hi-hats fins, cordes et cuivres graves, un *braam* sur le logo. Deux drops (6,0 s et 22,0 s), la batterie s'efface pendant le passage luxe (13–17 s), fin qui résonne.
- **Bruitages gratuits** (bibliothèque Pixabay incluse, usage commercial autorisé) : `whoosh-cinematic`, `whoosh-short`, `impact-bass-1/2`, `riser`, `glitch-1/2`, `sparkle`.
- **En option** (payant) : bruit de verre brisé sur mesure via ElevenLabs Sound Effects.
- Mixage : voix au premier plan (≈ −14 LUFS au global), musique abaissée sous la voix, bruitages calés à l'image près.

## Visuels produits
Aucune photo fournie : je propose de **générer 4 visuels studio sans marque** (survêtement, sneaker, montre, + la photo « ratée » de l'accroche).
Le parfum est modélisé en 3D, gratuitement, dans HyperFrames. Aucun logo de vraie marque.
Version « ratée » de l'accroche : créée gratuitement en dégradant le visuel sneaker (ffmpeg : couleurs ternes, flou, recadrage de travers).

## Estimation des coûts (prix FLORA vérifiés le 19/11/2026)
| Élément | Outil | Prix unitaire | Qté | Total |
|---|---|---|---|---|
| Test de 3 voix (1 phrase chacune) | Gemini 3.1 Flash TTS (FR) | 0,013 $ | 3 | 0,04 $ |
| Voix complète (+1 reprise) | Gemini 3.1 Flash TTS | 0,013 $ | 2 | 0,03 $ |
| Musique (2 essais) | Lyria 3.5 | 0,105 $ | 2 | 0,21 $ |
| Visuels produits (3 + 2 reprises) | Seedream 5.5 | 0,024 $ | 5 | 0,12 $ |
| Bruitages | Bibliothèque gratuite | 0 $ | — | 0 $ |
| Flacon 3D, logo 3D, animations, montage, rendu | HyperFrames (local) | 0 $ | — | 0 $ |
| **Total formule recommandée** | | | | **≈ 0,40 $** |

Autres formules :
- **Éco (tient dans 0,13 $)** : voix Gemini (0,07 $) + 1 essai musique Stable Audio 3 (0,044 $). Produits dessinés en 3D/chrome stylisé, sans photos. Rendu plus « graphique », moins réaliste.
- **Premium (≈ 1,90 $)** : voix ElevenLabs v3 (3 prises, 0,36 $) + musique ElevenLabs Music (2 essais, 0,72 $) + visuels Nano Banana Pro (4, 0,72 $) + verre brisé sur mesure (0,14 $).

---
## v2 — Améliorations validées (19/11/2026)
1. **Accroche** : l'image « ratée » et l'image « pub » sont **le même produit** (la ratée est dérivée de la belle). La casse révèle la version pro derrière : vraie transformation avant/après. Éclats en Three.js avec verre réaliste (réfraction, arêtes brillantes, flou de mouvement), puis passage au chrome.
2. **Logo LC** : composition autonome `identite/logo/` en Three.js. Métal physique (chrome brossé + biseaux polis), studio de lumière virtuel (3 sources + environnement réfléchissant), pivot lent puis arrêt net sur le temps. Variantes : intro 2 s, final 5 s, fond transparent.
3. **Streetwear** : visuels photoréalistes générés (survêtement, sneaker), animés en **2,5D** (carte de profondeur → vraie parallaxe), lumière néon animée, flou de mouvement, whip pans sur les temps. Option : 2 plans en image→vidéo pour un vrai mouvement de tissu.
4. **Luxe** : rythme ralenti (plans de 2 s sans coupe), flacon 3D en verre physique avec liquide ambré visible, caustiques dorées, fumée volumétrique légère. Montre : visuel photoréaliste + reflet spéculaire animé.
5. **Services** : typo haut de gamme large (Unbounded / Syncopate), remplissage chrome, chaque mot calé sur un temps.
6. **Final** : CONTACT EN DM en blanc pur sur pilule sombre, ≥ 64 px, contraste maximal, tenu 3 s.
7. **Audio** : voir VOIX-OFF.md. Musique : trap cinématique premium, transitions sur les temps forts.

---
## v3 — Décision client (19/11/2026)
- **On garde** : logo LC 3D (identite/logo/anim) et éclats de verre 3D de l'accroche.
- **On retire** : le flacon de parfum 3D (compositions/parfum.html conservé pour archive, non utilisé).
- **Produits = vidéos IA réalistes** : 4 visuels photoréalistes sans marque (survêtement, sneaker, parfum, montre) → chacun animé en clip vidéo IA (image → vidéo), puis monté dans HyperFrames (coupes sur les temps, transitions, textes, étalonnage commun).
- La sneaker sert aussi à l'accroche (version « ratée » fabriquée gratuitement depuis la même image).

### Clips vidéo prévus (5 s générés, ~2 s utilisés chacun)
| Produit | Mouvement demandé à l'IA | Univers |
|---|---|---|
| Survêtement | Tissu qui bouge sous un souffle d'air, travelling rapide, néon froid | STREET |
| Sneaker | Rotation lente sur socle, lumière qui balaie, particules | STREET |
| Parfum | Caméra en arc lent, fumée dorée, reflets sur le verre, liquide qui ondule | LUXE |
| Montre | Gros plan macro, reflet qui glisse sur le métal, trotteuse | LUXE |
