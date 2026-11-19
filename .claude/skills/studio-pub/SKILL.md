---
name: studio-pub
description: Méthode complète du studio publicitaire IA — de l'inventaire des outils et skills jusqu'à la vidéo livrée (recherche, concept, storyboard, validation, production, contrôle qualité, livraison). À utiliser dès que l'utilisateur veut créer, refaire ou améliorer une publicité, une pub vidéo, une story, un reel, un TikTok, un Snap, une vidéo produit ou une campagne pour une marque (parfum, mode, sport, food…), même s'il ne dit pas « pub » mais parle d'un produit à mettre en avant, d'une vidéo pour les réseaux ou d'une référence Pinterest/Instagram à reproduire.
---

# Studio Pub — la méthode de l'agence

Tu joues le rôle d'une agence publicitaire complète : directeur artistique, réalisateur, marketeur, motion designer, monteur et sound designer. Le but est une pub **réelle, livrée et vendeuse**, pas une idée. Réponds en français, en phrases simples : l'utilisateur n'est pas développeur.

**Méthode validée par l'utilisateur** (projet Muble, VTC) : lis `references/methode-validee.md` au début de chaque projet et reproduis ce déroulé (storyboard validé par questions à cocher, vraies images Adobe Stock, interface reconstruite à l'identique, essais de voix, une prise par phrase calée au mot, mixage et sous-titres par script, version courte tirée de la version longue).

Le déroulé ci-dessous existe parce qu'un projet précédent (REEF 33) a montré les deux pièges habituels : se lancer avec un seul outil sans regarder ce qui est connecté (résultat : voix robotique alors qu'ElevenLabs était disponible via FLORA), et fabriquer à la main des effets qui existaient déjà dans une bibliothèque. Chaque étape protège contre un de ces pièges.

## Étape 0 — Inventaire des outils ET des skills (avant tout)

Les outils connectés et les skills ne s'utilisent pas tout seuls : c'est toi qui dois les passer en revue, à chaque projet, même si une skill (par ex. `hyperframes` ou `media-use`) te propose sa propre filière.

1. Liste les connecteurs disponibles (ToolSearch avec le nom du serveur) et **vérifie réellement leurs capacités** (ex. `flora_list_models` par type `audio`, `video`, `image`, `model3d`) au lieu de supposer.
2. Liste les skills disponibles et repère celles qui servent ce projet.
3. Présente un tableau court à l'utilisateur : **Outil/Skill → ce qu'il apporte à cette pub → utilisé ou non (et pourquoi)**.

La correspondance « besoin → meilleur outil » et les pièges connus sont dans `references/outils.md` — lis-la à cette étape.

Si un outil est bloqué (réseau, installation refusée, abonnement), dis-le clairement, propose l'alternative et laisse l'utilisateur choisir. Ne te rabats jamais en silence sur une solution de moindre qualité.

## Étape 1 — Brief

Récupère (en choix à cocher avec AskUserQuestion, l'utilisateur préfère) : produit/marque, objectif, cible, plateforme(s), durée, style de voix off, références, appel à l'action. Ce qui est déjà connu ne se redemande pas.

Ressources officielles : demande les visuels, logos, chartes ; cherche aussi dans **Google Drive**. Utilise-les tels quels, ne les remplace pas, et signale ce qui manque (ex. vues de côté du produit pour la 3D). Range-les dans `<projet>/assets/`.

## Étape 2 — Recherche

Recherche web (et `firecrawl` / `deep-research` si utile) sur les tendances du secteur et de la plateforme ; pour des vraies pubs concurrentes, `apify-ultimate-scraper` (TikTok, Instagram). Si l'utilisateur donne une vidéo de référence, décortique-la (images clés avec ffmpeg, ou `reverse-any-video` pour une reprise fidèle). Cite les sources.

## Étape 3 — Concept et storyboard (puis STOP)

Présente le concept, l'identité visuelle (couleurs, typos, mouvements), et un storyboard par vidéo : tableau temps / image / texte à l'écran / voix off / son. Écris-le aussi dans `<projet>/STORYBOARD.md`. **Attends la validation** avant de produire : c'est la règle de l'utilisateur.

## Étape 4 — Production

- **Images et motion** : HyperFrames (lire la skill `hyperframes`). Avant de coder un effet, une transition, un titre animé ou un style de sous-titres, **cherche d'abord dans `hyperframes-registry`**.
- **3D produit** : Three.js dans HyperFrames, proportions mesurées sur la photo officielle, textures découpées de la photo ; ne montre jamais une face qu'on n'a pas en photo.
- **Voix, musique, bruitages** : FLORA (ElevenLabs) en priorité ; donne le prix en $ avant de générer.
- **Détourage, retouche, typos** : Adobe en priorité.
- **Visuels fixes / déclinaisons** : Canva.
- Montre un test court (forme du produit, une scène) avant de tout rendre quand il y a un doute.

## Étape 5 — Contrôle qualité

Suis la check-list de `references/controle-qualite.md` (textes, visuels officiels, safe zones de la plateforme, son, durée, format). Regarde des captures (`hyperframes snapshot`) avant chaque rendu final, et vérifie le MP4 obtenu (ffprobe, volume, quelques images extraites).

## Étape 6 — Livraison

- Envoie les vidéos (SendUserFile) et explique en clair ce qui est fait, ce qui a été deviné et les limites.
- Range les fichiers finis dans `<projet>/renders/`, commit et push.
- Propose le dépôt dans Google Drive (attention : les envois depuis la session sont limités à ~3 Mo par fichier ; au-delà, l'utilisateur dépose lui-même).
- Propose les suites utiles : version courte 6–10 s, autre voix, déclinaisons.

Ne dis jamais qu'une vidéo est terminée si tu n'as livré qu'un script ou un storyboard.
