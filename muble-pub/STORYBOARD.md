# MUBLE — Pub VTC premium : concept et storyboard (à valider)

## 1. Brief

| | |
|---|---|
| Marque | Muble, VTC premium à Paris et en Île-de-France |
| Objectif | Faire comprendre comment on réserve sur le site, puis faire réserver un premier trajet |
| Cibles | Voyageurs (aéroports, gares), jeunes adultes qui sortent, professionnels, touristes, familles et groupes |
| Plateformes | TikTok, Snapchat, Instagram Reels : vertical 9:16, 1080×1920, 30 images/s |
| Durée | Version principale : 72 s. Version courte proposée en plus : 25 s |
| Voix off | Homme de 25 à 35 ans, français naturel, dynamique et rassurant |
| Fin | Logo Muble + « Votre trajet, en toute simplicité. » + « Réservez votre chauffeur dès maintenant. » + adresse du site (à confirmer) |

## 2. Ce que je sais vraiment du site (vérifié sur tes captures)

| Élément | Texte exact sur le site |
|---|---|
| Promesse | « Votre chauffeur VTC, réservé en 2 minutes. » |
| Sous-titre | « Un prix clair figé avant validation, un chauffeur professionnel et une voiture impeccable. Aéroports, gares, rendez-vous, soirées — vous roulez, on s'occupe du reste. » |
| 3 garanties | « Prix figé, zéro surprise » · « Suivi de course en direct » · « Paiement sécurisé Stripe » |
| Formulaire | « Réservez votre trajet » — « Renseignez votre trajet, on vous rappelle avec le prix exact. » Champs : adresse de départ, adresse d'arrivée, date (+ un 2e champ coupé, sans doute l'heure), passagers (« 1 passager »), bagages (« Aucun bagage »), nom, téléphone, e-mail… la suite n'est pas visible |
| Véhicules | « Une catégorie pour chaque trajet. » « Du trajet malin au transfert VIP, le prix s'affiche avant la validation dans chaque catégorie. » **Éco** (jusqu'à 3 passagers, « L'essentiel, au meilleur prix pour vos trajets du quotidien. ») · **Berline** (jusqu'à 3 passagers, description coupée) · autres catégories non visibles |
| Pourquoi Muble | « Le confort d'un chauffeur privé, la simplicité d'une appli. » · badge « 100 % chauffeurs professionnels » |
| FAQ : prix | « Non. Le prix est calculé et figé avant votre validation. Les majorations (nuit, week-end, jours fériés, forte demande) sont intégrées au tarif affiché. » |
| FAQ : à l'avance | Réservation possible jusqu'à plusieurs semaines à l'avance. Confirmation, puis informations du chauffeur avant la prise en charge |
| FAQ : paiement | En ligne par carte bancaire, Apple Pay ou Google Pay, de façon sécurisée. Facture envoyée automatiquement après la course |
| FAQ non ouvertes | « Puis-je annuler ma course ? » · « Gérez-vous les bagages, sièges enfant et animaux ? » |
| Boutons | « Réserver mon trajet → » · « Nous contacter » |

### Ce qui manque ou reste flou

1. **L'adresse du site.** Il est en mode « preview » (bandeau « This is a preview »). Je n'ai trouvé aucun site Muble en ligne. Sans lien, je ne peux pas naviguer dessus.
2. **Le logo en haute définition** (PNG transparent ou SVG). Sur les captures, il est flou.
3. **Le bas du formulaire** : le bouton d'envoi, et s'il y a un choix de catégorie dans le formulaire.
4. **Ce qui se passe après l'envoi** : un écran de confirmation ? un e-mail ?
5. **Une contradiction à trancher** : le formulaire dit « on vous rappelle avec le prix exact », mais la section véhicules dit « le prix s'affiche avant la validation ». Ma lecture : demande → rappel avec le prix exact → validation → paiement en ligne. À confirmer.
6. **La liste complète des catégories** (Éco, Berline… et « VIP » ? Van ?) et les modèles de voitures, s'ils sont connus.
7. **La vidéo de référence** que tu avais envoyée à ChatGPT (le fichier .mp4) : je ne l'ai pas reçue.
8. Le suivi de course en direct et le paiement Stripe : je ne peux pas les tester. Je les montre seulement si tu confirmes qu'ils marchent.

## 3. Inventaire des outils et des skills

| Outil / skill | Ce qu'il apporte à cette pub | Utilisé ? |
|---|---|---|
| **Adobe Stock** (connecteur Adobe) | Vraies vidéos de chauffeurs, de Paris et de voyageurs, en HD, **gratuites** (catégorie « free »). Testé : une vidéo licenciée et téléchargée (chauffeur en costume devant la tour Eiffel, 1080p, 20 s, 0 €) | **Oui**, pour toutes les scènes « vraie vie » |
| **Adobe** (détourage, retouche, polices) | Détourer le logo si besoin, vectoriser le logo si tu n'as pas de fichier HD, étalonner des images | Oui, si besoin |
| **FLORA → ElevenLabs v3** | La voix off la plus naturelle et expressive (0,12 $ par prise) | Oui si tu recharges FLORA (voir budget) |
| **FLORA → Gemini 3.1 Flash TTS** | Voix française native, correcte, très bon marché (0,013 $ par prise) | Alternative si on reste dans le solde actuel |
| **FLORA → ElevenLabs Music v2.5** | Musique électro légère et premium sur mesure, sans voix (0,10 $) | **Oui** |
| **FLORA → ElevenLabs Sound Effects** | Clics, tapotements, frappe au clavier, whoosh, signature sonore du logo (0,14 $ chacun) | Oui |
| FLORA → vidéo IA (Kling v4, MiniMax…) | Plans générés par IA (0,48 à 1,30 $ par plan) | **Non** : les vraies vidéos Adobe Stock sont plus crédibles et gratuites. Les voitures générées par IA ont souvent des défauts |
| FLORA → 3D | Modèles 3D générés | Non : la skill HyperFrames a déjà un vrai iPhone 3D |
| **HyperFrames** + **hyperframes-registry** | Montage, motion design, 3D, sous-titres, rendu MP4. Blocs trouvés : `vfx-iphone-device` (vrai iPhone 3D dont l'écran affiche du HTML), `parallax-device-dive` (la caméra plonge dans l'écran), `ui-focus-zoom`, `gesture-tap` (doigt qui tape), `cursor-zoom-follow`, `whip-pan`, `logo-outro`, styles de sous-titres | **Oui**, outil principal |
| **Canva** | Visuels fixes (affiche, story). La génération vidéo Canva est bloquée sur ton offre actuelle | Plus tard, pour une story ou une affiche si tu veux |
| **Google Drive** | Aucun fichier « Muble » trouvé dans ton Drive | Pour déposer les vidéos finies |
| **Recherche web** | Tendances et références (voir plus bas) | Oui |
| Runway | Connexion en échec (le proxy refuse) | Non disponible pour l'instant |
| Descript | Montage par le texte | Non nécessaire |
| Skills `studio-pub`, `hyperframes`, `hyperframes-registry`, `media-use` | Méthode de l'agence, montage, effets prêts à l'emploi, mixage audio | Oui |
| Skills `reverse-any-video`, `style-sampling` | Copier une vidéo de référence ou un style | Seulement si tu m'envoies ta vidéo de référence |
| Skill `apify-ultimate-scraper` | Analyser des pubs concurrentes sur TikTok | Non : la recherche web suffit pour ce projet |

## 4. Ce que dit la recherche

- **Les 3 premières secondes décident de tout.** Les guides TikTok de 2026 conseillent de montrer tout de suite le bénéfice ou le problème, puis le contexte (3–7 s), puis la démo. Les pubs qui montrent le résultat dès les 2 premières secondes font mieux que celles qui commencent par une mise en place.
- **Le texte à l'écran porte le message**, car beaucoup de vidéos courtes sont regardées sans le son. D'où des sous-titres précis et des mots-clés animés (typographie cinétique, la tendance motion la plus citée en 2026).
- **3D d'interface + typo animée + transitions fluides** : c'est le mélange qui revient dans les démos d'applications.
- **La réservation à l'avance est le segment qui grandit le plus** chez les géants du VTC : Uber rachète Blacklane (chauffeurs premium) en 2026, et ses campagnes « Uber Reserve » misent sur les trajets vers l'aéroport réservés à l'avance. Muble est exactement sur ce créneau : il faut l'assumer.
- **En France, Heetch (avec BETC) a pris l'angle du prix**. Muble ne doit pas copier cet angle « le moins cher » : son atout, c'est **le prix figé + le chauffeur pro + la réservation à l'avance**.

Sources : [Heetch × BETC, « le VTC le moins cher » (CB News)](https://www.cbnews.fr/marques/heetch-betc-presentent-vtc-moins-cher) · [La Réclame : Heetch comparateur de prix](https://lareclame.fr/betc-heetch-vtc-comparateur-prix-314180) · [Skift : Uber rachète Blacklane (mars 2026)](https://skift.com/2026/03/30/uber-to-buy-blacklane-in-push-to-accelerate-premium-services/) · [Executive Traveller : Uber Elite / Blacklane](https://www.executivetraveller.com/news/uber-elite-blacklane-chauffeur) · [Uber Reserve × Mother (Creative Salon)](https://creative.salon/articles/work/uber-reserve-mother) · [Stackmatix : règle des 3 premières secondes sur TikTok](https://stackmatix.com/blog/tiktok-creative-best-practices-2026) · [Segwise : 25 accroches vidéo 2026](https://segwise.ai/blog/video-ad-hooks-drive-conversions) · [Adwave : vidéo promo d'application](https://adwave.com/resources/mobile-app-promo-video) · [Videobolt : tendances motion 2026](https://blog.videobolt.net/post/top-motion-graphics-trends-2026) · [Renderforest : tendances design 2026](https://www.renderforest.com/blog/design-trends-in-2026)

## 5. Le concept : « 2 MINUTES CHRONO »

La promesse du site, « réservé en 2 minutes », devient le fil rouge de la pub. Un **chronomètre violet** (un anneau lumineux) apparaît pendant la démo. Chaque étape de réservation remplit un morceau de l'anneau. À la fin, le chrono s'arrête **avant 2:00** avec une coche : « Demande envoyée ». Le spectateur *voit* que c'est simple et rapide, au lieu de seulement l'entendre.

Autour de ce fil rouge : de vraies images de Paris et de chauffeurs (Adobe Stock), un iPhone en 3D qui affiche l'interface Muble, et des textes animés.

### Identité visuelle

- **Couleurs** (relevées sur tes captures) : violet Muble #6A2BC2, violet profond #3B0F7A, noir nuit #0B0714 pour le côté premium, graphite #1C1A22, blanc #FFFFFF, gris clair des cartes #F3F3F6, lueur lilas #C4A6FF. Vert du badge « chauffeurs pro » #2E9E6B, en petite touche.
- **Typographie** : Plus Jakarta Sans, la police du site (très probable d'après les captures). ExtraBold pour les titres, Medium pour les textes.
- **Images réelles** : étalonnage commun « nuit parisienne » (noirs profonds, reflets violets) pour que tous les plans aient l'air d'un même film.
- **Interface** : je **reconstruis l'interface Muble à l'identique** en HTML, d'après tes captures (mêmes textes, même ordre des champs, mêmes couleurs, même police). Elle sera nette, sans le bandeau « This is a preview », et je pourrai animer la saisie lettre par lettre. Je n'invente aucun écran que je n'ai pas vu.
- **Mouvements** : la caméra plonge dans l'écran du téléphone, zooms doux sur chaque champ, doigt qui tape avec une onde, transitions « whip » (balayage rapide) entre les plans réels, léger grain de film, reflets de lumière violets.
- **Sous-titres** : blancs, gras, mot important surligné en violet, placés au-dessus de la zone des boutons TikTok/Snap.

## 6. Storyboard — version principale (72 s)

| Temps | Image | Texte à l'écran | Voix off | Son |
|---|---|---|---|---|
| **SCÈNE 1 — ACCROCHE** | | | | |
| 0,0–1,6 s | Plan réel : homme d'affaires qui sort d'une voiture, pressé | **Un rendez-vous ?** | « Un rendez-vous ? » | Musique qui démarre fort + impact grave |
| 1,6–3,0 s | Coupe : voyageuse avec sa valise sur un quai de gare | **Un avion à prendre ?** | « Un avion à prendre ? » | Whoosh |
| 3,0–5,0 s | Coupe : Champs-Élysées de nuit, lumières qui défilent | **Besoin d'un chauffeur à Paris ?** | « Ou simplement besoin de vous déplacer ? » | Whoosh |
| 5,0–7,0 s | Balayage violet, le logo Muble arrive en 3D avec un reflet de lumière | Logo Muble | « Découvrez Muble. » | Signature sonore du logo (scintillement + basse douce) |
| **SCÈNE 2 — PRÉSENTATION** | | | | |
| 7,0–11,5 s | Plan réel : chauffeur en costume qui marche vers la berline noire, tour Eiffel au fond | Petit titre : « VTC premium · Paris & Île-de-France » | « Muble, votre service de VTC premium à Paris et en Île-de-France. » | Musique, rythme qui s'installe |
| 11,5–17,0 s | Un iPhone 3D monte dans le cadre et tourne doucement. À l'écran : la page d'accueil Muble (« Votre chauffeur VTC, réservé en 2 minutes. » + les 3 garanties). Le chrono violet apparaît : 0:00 | « Réservé en 2 minutes » | « Réservez votre chauffeur simplement, en quelques étapes. » | Petit « pop » à l'apparition du chrono |
| **SCÈNE 3 — DÉMO DU SITE** | | | | |
| 17,0–22,5 s | La caméra plonge dans l'écran : formulaire « Réservez votre trajet ». Doigt qui tape « Adresse de départ » → saisie « Gare de Lyon, Paris 12e ». Puis « Adresse d'arrivée » → « Aéroport Paris-CDG ». À côté du téléphone, une petite ligne de trajet animée relie les deux points | Étiquette **① Votre trajet** · chrono 1/5 | « Première étape : indiquez votre adresse de départ et votre destination. » | Tap + frappe au clavier |
| 22,5–28,0 s | Zoom sur la date et l'heure, puis passagers et bagages (valeurs d'exemple : 2 passagers, bagages selon les choix réels du site) | **② Date, passagers, bagages** · chrono 2/5 | « Choisissez ensuite la date, le nombre de passagers et vos besoins en bagages. » | Taps |
| 28,0–33,5 s | Les cartes véhicules sortent de l'écran et flottent en 3D autour du téléphone : **Éco**, **Berline** (+ autres catégories si tu me les confirmes). Le doigt choisit Berline, la carte s'illumine | **③ Votre véhicule** · chrono 3/5 | « Sélectionnez le véhicule adapté à votre trajet, selon vos envies et votre budget. » | Whoosh doux + tap |
| 33,5–38,5 s | Retour au formulaire : nom, téléphone, e-mail se remplissent (numéro masqué) | **④ Vos coordonnées** · chrono 4/5 | « Renseignez vos coordonnées pour recevoir les informations concernant votre réservation. » | Frappe au clavier |
| 38,5–45,0 s | Tap sur le bouton d'envoi. Le chrono s'arrête avant 2:00 avec une coche ✓. Puis une frise animée (hors de l'écran du téléphone, pas une fausse interface) : 📞 Rappel avec le prix exact → 🔒 Prix figé, vous validez → 💳 Paiement en ligne sécurisé (CB, Apple Pay, Google Pay) → 🚘 Infos chauffeur avant la prise en charge | **⑤ Prix exact, puis vous validez** | « Muble vous rappelle avec le prix exact, figé avant votre validation. Puis vous payez en ligne, en toute sécurité. » | Petite sonnerie de téléphone + carillon de validation |
| **SCÈNE 4 — AVANTAGES** | | | | |
| 45,0–48,5 s | Plan réel : chauffeur qui ouvre la portière à une passagère | **CHAUFFEURS PROFESSIONNELS** + badge « 100 % chauffeurs professionnels » | « Avec Muble, profitez d'un chauffeur professionnel, » | Impact sur le mot |
| 48,5–52,0 s | Carte « Prix figé » qui se verrouille (cadenas), sans montant inventé. En fond : passager dans la voiture la nuit | **PRIX FIXÉ À L'AVANCE** + « majorations incluses » | « d'un prix connu à l'avance » | Clic de cadenas |
| 52,0–55,0 s | Plan réel : homme d'affaires à l'arrière, smartphone en main | **RÉSERVATION SIMPLE** (+ « Suivi de course en direct » et « Paiement sécurisé Stripe » si tu confirmes) | « et d'un trajet organisé selon vos besoins. » | Impact |
| **SCÈNE 5 — POUR QUI** | | | | |
| 55,0–57,2 s | Voyageur avec valise devant un aéroport | **Aéroports.** | « Pour vos déplacements professionnels, | Coupe sur le temps fort |
| 57,2–59,4 s | Vue aérienne de la gare de Lyon | **Gares.** | vos voyages | Coupe |
| 59,4–61,6 s | Professionnel en costume qui sort de la voiture | **Rendez-vous.** | ou vos sorties, | Coupe |
| 61,6–64,0 s | Amis / couple qui marchent dans Paris de nuit | **Sorties.** | Muble vous accompagne en Île-de-France. » | Coupe |
| **SCÈNE 6 — APPEL À L'ACTION** | | | | |
| 64,0–67,0 s | Vue aérienne de nuit (pont Alexandre III, lumières). Transition : les lumières deviennent l'écran du téléphone, qui affiche le bouton « Réserver mon trajet → » | — | « Muble. Votre chauffeur privé, en toute simplicité. » | Montée de la musique |
| 67,0–72,0 s | Fond violet profond, le logo Muble au centre avec un reflet de lumière. Le doigt tape « Réserver mon trajet » | **VOTRE TRAJET, EN TOUTE SIMPLICITÉ.** puis **Réservez votre chauffeur dès maintenant.** + adresse du site | « Réservez dès maintenant. » | Signature sonore du logo, fin de la musique |

Durée totale de la voix off : environ 150 mots, soit 55 à 58 secondes de parole. Il reste de l'air pour la musique et les transitions.

### Plans réels proposés (Adobe Stock, catégorie gratuite)

| Scène | Plan | N° Adobe Stock |
|---|---|---|
| S1 « Un rendez-vous ? » | Homme d'affaires qui sort d'une voiture | 482289372 |
| S1 « Un avion à prendre ? » | Bagages à l'aéroport (déjà vertical) | 746098855 |
| S1 « Besoin d'un chauffeur à Paris ? » | Champs-Élysées de nuit | 557621523 |
| S2 + S4 | Chauffeur en costume, berline noire, tour Eiffel (**déjà téléchargé**, 1080p, 20 s) | 264564019 |
| S4 « Prix fixé à l'avance » | Passager à l'arrière, la nuit | 596558039 |
| S4 « Réservation simple » | Smartphone en main à l'arrière d'une voiture | 440314317 |
| S5 « Aéroports. » | Voyageur à l'aéroport (déjà vertical) | 1270012406 |
| S5 « Gares. » | Gare de Lyon vue du ciel | 526417762 |
| S5 « Sorties. » | Amies dans la rue, la nuit | 226798580 |
| S6 | Paris de nuit, pont Alexandre III | 178022166 |

Les plans horizontaux seront recadrés en vertical sur le sujet. Les vraies voitures Muble ne sont pas connues : ces plans montrent « un chauffeur, une berline », jamais un modèle présenté comme celui de Muble.

## 7. Version courte (25 s) pour Snap et TikTok

0–3 s : accroche (3 questions très rapides) → 3–5 s : logo → 5–17 s : démo accélérée en 4 étapes avec le chrono → 17–21 s : les 3 avantages → 21–25 s : logo + « Réservez votre chauffeur dès maintenant ».

## 8. Son

- **Voix off** : je te propose d'abord 2 ou 3 essais courts (la même phrase) pour que tu choisisses la voix.
- **Musique** : électro légère et élégante, environ 100–110 BPM, générée sur mesure (ElevenLabs Music), baissée automatiquement sous la voix.
- **Bruitages** : taps, frappe au clavier, whoosh, cadenas, carillon de validation, signature du logo, tous synchronisés à l'image.
- **Mixage** : volume normalisé pour les réseaux (−14 LUFS), la musique ne couvre jamais la voix.

## 9. Budget

| Poste | Outil | Coût estimé |
|---|---|---|
| Vidéos réelles (8 à 10 plans) | Adobe Stock, catégorie gratuite | **0 €** |
| Interface, 3D, montage, sous-titres, rendu | HyperFrames | **0 €** |
| Musique | ElevenLabs Music v2.5 (via FLORA) | ≈ 0,10 $ (≈ 0,40 $ avec 2 ou 3 essais) |
| Bruitages | ElevenLabs Sound Effects (via FLORA) | ≈ 0,15 $ chacun, 5 ou 6 sons ≈ 0,85 $ |
| Voix off, option A (la meilleure) | ElevenLabs v3 (via FLORA) | ≈ 0,12 $ par prise, ≈ 1,50 à 2 $ avec les reprises |
| Voix off, option B (économique) | Gemini 3.1 Flash TTS, français natif (via FLORA) | ≈ 0,013 $ par prise, ≈ 0,15 $ au total |

**Total option A : environ 3 $. Total option B : environ 1,20 $.**
**Attention : ton solde FLORA actuel est de 0,61 $.** Il ne suffit pas pour l'option A. Il faut recharger FLORA (https://app.flora.ai/home?display=plans), ou partir sur l'option B en limitant les essais.

## 10. Production (après ta validation)

1. Télécharger les plans Adobe Stock choisis (gratuits) et les étalonner.
2. Reconstruire l'interface Muble à l'identique, puis l'animer dans l'iPhone 3D.
3. Générer la voix, la musique et les bruitages (après accord sur le prix).
4. Monter dans HyperFrames, sous-titres compris.
5. Contrôle qualité : orthographe, zones sûres TikTok/Snap/Reels, son, durée, résolution 1080×1920.
6. Livraison dans `muble-pub/renders/` + Google Drive si tu veux.
