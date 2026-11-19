# LOFTUS-CHEEK · PROJET 001 · REFONTE V2

## 1. Défauts du montage V1 (diagnostic honnête)
| Défaut | Cause | Conséquence |
|---|---|---|
| « Diaporama » | 4 photos fixes + zooms (Ken Burns) | Aucune sensation de volume ni de tournage |
| Pas de vraie caméra | Les mouvements sont des recadrages 2D | La perspective ne change jamais |
| Univers incohérents | Images de sources différentes (FLORA, Canva), lumières différentes | On sent le collage |
| Transitions plates | Coupes, fondus, whip pan 2D | Rien ne relie les scènes entre elles |
| Éclats de verre | Bon principe, mais tranches grises et sans réfraction | Effet « carton » |
| Services | Texte sur mosaïque sombre et figée | Moment mort à 17–22 s |
| Pas de son | Budget voix/musique non débloqué | Impossible de juger le rythme |

## 2. Test technique 3D (19/11, gratuit) — `renders/apercus/test-3d-modeles-libres.jpg`
Vrais modèles 3D PBR libres (CC-BY 4.0) chargés dans HyperFrames/Three.js avec HDRI et ombres douces.
- **Sneaker (Shopify)** : vrai volume, maille, coutures, semelle texturée → nettement plus crédible qu'une photo. MAIS modèle de running générique bleu avec marquage « FOAM » et bandes : pas assez tendance streetwear.
- **Montre (DGG)** : métal crédible MAIS logo « 3D Commerce » sur le cadran et style montre tactique → inutilisable.
- **Limite technique** : la session n'a pas de carte graphique (rendu logiciel). Le rendu raster reste « CG / jeu vidéo » ; le path tracing (lumière photoréaliste) coûterait plusieurs minutes PAR image en 1080×1920 → irréaliste pour 28 s.

## 3. Conclusion : la meilleure solution pour le photoréalisme
**Hybride « tournage IA + réalisation HyperFrames »**
- Plans produits = **vidéos IA image→vidéo** (Kling / MiniMax / Seedance) : vraies orbites caméra, profondeur de champ, reflets et matières physiques.
- HyperFrames = **réalisation** : transitions construites sur le mouvement (raccords dans l'axe, traversées, passage de lumière), logo LC 3D, étalonnage commun, grain, typographie, sous-titres, synchronisation musique/voix/bruitages.
- 3D Three.js gardée là où elle excelle : logo LC chrome, éclats de verre (refaits avec réfraction), particules.

## 4. Nouvelle direction artistique — « UN SEUL STUDIO, UNE SEULE CAMÉRA »
Toute la pub semble tournée dans **un même studio noir** par **une caméra qui ne s'arrête jamais** : chaque produit est relié au suivant par un mouvement (la caméra traverse, plonge, glisse).
- Lumière : clé blanche douce + contre-jour bleu (street) qui **vire au doré** (luxe) pendant la transition.
- Optique : 50–85 mm, profondeur de champ courte, fumée légère, sol miroir sombre.
- Étalonnage unique : noirs profonds, chrome froid, touches champagne. Grain fin sur tout.
- Typo : un seul système (titres larges espacés, Montserrat ; accents luxe en serif).

## 5. Storyboard V2 (28 s · musique 120 BPM, coupes sur les temps)
| Temps | Plan | Caméra / mouvement | Transition vers la suite | Voix off | Son |
|---|---|---|---|---|---|
| 0,0–2,0 | Vidéo « téléphone » : sneaker posée sur un lit, lumière jaune | Tremblé main | Flash → **verre qui éclate** (3D, réfraction réelle) | « Votre produit est fort… mais personne ne s'arrête. » | Ambiance chambre → craquement + impact |
| 2,0–4,5 | La même sneaker dans le studio noir | **Orbite basse** lente, la lumière s'allume progressivement | La sneaker tourne et sa face sombre remplit l'écran (wipe par l'objet) | « Il lui manque… une dimension. » | Riser |
| 4,5–6,0 | Gros plans matières : cuir, coutures, semelle | Macro, mise au point qui glisse | Reflet chrome qui balaie | — | Whoosh |
| 6,0–8,5 | LOGO LC 3D | Pivot ¾ → face, arrêt net | Flash sur le drop | « LOFTUS-CHEEK. » | DROP 1 |
| 8,5–12,5 | Ensemble survêtement porté (mannequin) qui avance vers la caméra + sneaker en rotation rapide | Travelling arrière, tissu qui bouge | Match-cut sur le mouvement | « Streetwear. Sneakers. » | Hi-hats, impacts |
| 12,5–13,0 | **Transition lumière** : le néon bleu se transforme en lumière dorée | Traversée d'un faisceau | — | — | Souffle + scintillement |
| 13,0–15,5 | Parfum : flacon en verre, liquide qui ondule, fumée | Dolly lent, arc 20° | La caméra plonge dans le reflet du verre | « Parfums… » | Batterie coupée, nappe |
| 15,5–17,0 | Montre : macro cadran, aiguille qui avance | Rotation subtile, reflet qui glisse | Le reflet du verre de montre devient la scène suivante | « Accessoires. » | Tic + tiiing métal |
| 17,0–22,0 | Services : 3 mots sur un **travelling continu** en ralenti à travers les produits (pas d'écran figé) | Glissement latéral continu | Zoom à travers l'objectif du C | « Publicité IA. Motion design 3D. Voix off. Des vidéos qui arrêtent le scroll. » | Montée filtrée |
| 22,0–28,0 | Final logo + « Donnez une nouvelle dimension à votre marque. » + CONTACT EN DM | Logo 3D | Image finale fixe (boucle) | « Donnez une nouvelle dimension à votre marque. Contact en DM. » | DROP 2 → résonance |

## 6. Éléments nécessaires
| Élément | Méthode | État |
|---|---|---|
| Logo LC 3D | Three.js (existant) | ✅ réutilisé |
| Éclats de verre | Three.js, à refaire avec réfraction + éclats plus fins | 🔧 gratuit |
| Particules, lumière, fumée d'appoint, grain | HyperFrames | 🔧 gratuit |
| Sneaker « tendance » | Photo IA (référence client) → 3 vidéos IA (orbite, macro, rotation) | 💲 |
| Vidéo « téléphone » de l'accroche | Vidéo IA à partir de la même sneaker | 💲 |
| Ensemble survêtement porté | Photo IA (réf. client bleu marine, autre mannequin) → vidéo IA | 💲 |
| Parfum | Photo IA (réf. client) → vidéo IA | 💲 |
| Montre | Photo IA → vidéo IA macro | 💲 |
| Voix off, musique, bruitages | FLORA (ElevenLabs / Gemini) + bibliothèque gratuite | 💲 |

## 7. Coûts estimés (FLORA, prix catalogue 19/11)
⚠️ **La génération VIDÉO n'est pas incluse dans le forfait gratuit FLORA** (refus « paid_plan_required » le 19/11). Il faut un forfait payant (Starter ≈ 18 $/mois d'après les guides publics, à vérifier sur flora.ai).
| Poste | Calcul | Coût |
|---|---|---|
| 5 photos produits 2K (+2 reprises) | 7 × 0,077 $ | ≈ 0,54 $ |
| 8 clips vidéo 5 s (+2 reprises) | 10 × 0,21 à 0,29 $ (MiniMax Turbo / Kling 2.5) | ≈ 2,10 à 2,90 $ |
| Voix off (tests + prise finale) | Gemini ≈ 0,07 $ ou ElevenLabs ≈ 0,36 $ | 0,07 à 0,36 $ |
| Musique (2 essais) | 2 × 0,10 $ | 0,20 $ |
| 2 bruitages sur mesure (verre, métal) | 2 × 0,14 $ | 0,29 $ |
| **Total** | | **≈ 3,20 à 4,30 $** (sur le budget mensuel Starter) |
Alternative sans FLORA : vidéos Canva (moteur Seedance, 720p) sur la limite IA Canva, épuisée jusqu'au renouvellement.

## 8. Ce qu'il faut recevoir du client
1. Les vidéos de référence (en pièces jointes ou dans Google Drive › LOFTUS-CHEEK).
2. Photo de la sneaker « tendance » souhaitée, du parfum, de l'ensemble (en fichiers).
3. Accord budget + forfait FLORA payant actif.

## 9. Mise à jour 19/11 soir — Scenario connecté (remplace FLORA)
Références client reçues (assets/references-client/) : sneakers On Cloudtilt noire + blanche, ensemble On vert (mannequin à remplacer par une autre personne), parfum Nishane Hacivat. ⚠️ Marques réelles (On, Nishane) : même avertissement droits que Nike, choix du client.

Coûts chiffrés par Scenario (dry run, en Creative Units) :
| Poste | Modèle | CU unitaire | Qté | CU |
|---|---|---|---|---|
| Photos studio d'après références | GPT Image 2.5 Sunburst (2K, 9:16) | 13 | 5 (+4 reprises) | ≈ 117 |
| Clips vidéo 5 s | MiniMax H3 (2K) | 130 | 8 (+2 reprises) | ≈ 1 300 |
| (option qualité max) | Seedance 2.5 1080p | 570 | — | trop cher pour ce budget |
| Voix, musique, bruitages | ElevenLabs via Scenario | à chiffrer | — | ≈ 50–150 (estimation) |
| **Total** | | | | **≈ 1 450–1 600 CU** |

Forfait Scenario actuel : **gratuit = 50 CU/jour** (d'après le centre d'aide Scenario) → suffit pour ~3 photos/jour, PAS pour la vidéo (130 CU minimum par clip).
Forfaits payants (d'après les sources publiques, à vérifier sur scenario.com/pricing) : ≈ 15 $/mois pour ~1 500 CU (juste), ≈ 45 $/mois pour ~5 000 CU (confortable).

## 10. Analyse de la référence « Muble 25 s » (pub VTC réalisée par le studio, branche pub-muble-vtc)
Ce qui marche et qu'on reprend :
1. **Deux mondes seulement** : le monde réel (vraies vidéos Adobe Stock, licence gratuite, recadrées 9:16 et étalonnées en commun) + le monde de la marque (plateau violet). → LC : vraies vidéos + plateau noir/chrome LC.
2. **Accroche en vraie vidéo dès 0,0 s**, avec une question en titre (« Un rendez-vous ? »). Jamais de noir ni de logo au départ.
3. **La voix off est l'horloge** : chaque texte arrive sur le mot dit ; sous-titres par groupes de 5 mots max, un seul mot en couleur d'accent.
4. **Un objet réel au centre de la démonstration** (le téléphone avec la vraie interface) → LC : un téléphone qui montre la story Snap/Insta d'un vendeur, AVANT (photo plate) puis APRÈS (pub LC). C'est la preuve du savoir-faire pour la cible.
5. **Transition « l'objet devient le monde »** (le bouton grandit jusqu'à remplir le cadre), whips de 0,2 s sur les temps forts.
6. **Règles strictes (BANNED)** : pas de vide noir avec éléments flottants, pas de néons/orbes/particules décoratives, pas de texte qui glisse en fondu.
7. Son : voix Gemini « Achird », musique Stable Audio, bruitages de la bibliothèque.

Recherche Adobe Stock gratuite (vidéos 4K) : montre homme sur fond noir lumière commerciale (487598737), mécanisme de montre (238946280), trotteuse (991749818), parfum vaporisé sur fond noir (472882133), sneakers blanches néon bleu (674248639), homme en streetwear qui marche de nuit en ville, ralenti (313222787), jeune homme confiant qui marche, travelling (425453036). Téléchargement bloqué tant que les hôtes Adobe (t3/t4.ftcdn.net + hôte de téléchargement sous licence) ne sont pas autorisés.
