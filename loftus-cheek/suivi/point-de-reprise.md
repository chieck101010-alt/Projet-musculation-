# POINT DE REPRISE — LOFTUS-CHEEK

## 2026-11-19 (8)
- **Montage V2 sans son rendu** : `pubs/LC-20261119-loftus-cheek-studio-v2/renders/apercus/montage-v2-sans-son.mp4` (28 s). Structure inspirée de Muble : vraie vidéo → téléphone (story vendeur avant/après) → « l'objet devient le monde » → logo → street (vidéo + photos Scenario) → bascule dorée → luxe (vidéo + Nishane + chrono) → services sur mécanisme → final CTA.
- **Outils actifs** : Scenario (connecteur, gratuit 50 CU/jour, 2 jobs en parallèle) ; Adobe Stock (licences gratuites) ; ElevenLabs direct toujours refusé (en-tête).
- **Manque** : voix off, musique, bruitages ; animation vidéo des produits (formule Scenario payante) ; On blanche (13 CU, demain).

## 2026-11-19 (7) — À LIRE EN PREMIER DANS LA NOUVELLE SESSION
- **Refonte V2 en cours** : plan complet dans `pubs/LC-20261119-loftus-cheek-studio-v2/REFONTE-V2.md` (diagnostic V1, DA « un seul studio, une seule caméra », storyboard, coûts). Direction recommandée : tournage IA (vidéos produits) + réalisation HyperFrames.
- **Skills installés** : Scenario (`.agents/skills/scenario*`) et ElevenLabs officiels (`.agents/skills/text-to-speech`, `music`, `sound-effects`…).
- **ElevenLabs** : clé enregistrée dans les « Network secrets » de l'environnement (hôte api.elevenlabs.io). Dans l'ancienne session, le proxy l'envoyait encore en `Authorization: Bearer` → refus. Première action : `curl -sS https://api.elevenlabs.io/v1/user/subscription` (sans en-tête) ; si refus, vérifier que le secret utilise l'en-tête `xi-api-key` sans préfixe.
- **Scenario** : à connecter comme connecteur claude.ai (`https://mcp.scenario.com/mcp`) → vérifier avec ToolSearch « scenario ».
- **En attente du client** : vidéos de référence + photos (sneaker tendance, parfum, ensemble) EN PIÈCES JOINTES ou Google Drive › LOFTUS-CHEEK ; accord budget.
- **Ne rien générer de payant sans accord.**

## 2026-11-19 (6)
- **Étape atteinte** : montage v1 complet 28 s sans son (accroche Nike + éclats 3D, bascule, logo 3D, 4 plans produits 2D, services, final CTA).
- **Visuels** : Nike TN (logo Nike, choix client), parfum, montre (Canva). Survêtement manquant (quota Canva épuisé ; le client veut un ensemble porté par une autre personne, réf. bleu marine non reçue en fichier).
- **Le client veut un autre parfum** : image non reçue en fichier.
- **Dépenses** : FLORA 0,077 $ ; Canva : limite IA mensuelle épuisée.
- **Prochaine action** : recevoir les photos (parfum, ensemble) en pièce jointe ; budget pour voix/musique/vidéos IA (FLORA Starter ≈18 $/mois ou Canva renouvelé).

## 2026-11-19 (5)
- **Étape atteinte** : projet HyperFrames de la pub créé. Scènes testées (gratuit) : compositions/parfum.html (flacon 3D, verre + liquide + reflet) et compositions/accroche.html (photo → fissures → éclats 3D → version pub).
- **Aperçus** : renders/apercus/test-parfum-v1.mp4, test-accroche-v1.mp4. L'accroche utilise des images de TEST (assets/test/) à remplacer par la sneaker.
- **Dépenses** : 0 $.
- **Prochaine action** : avis client sur les 2 tests ; recharge FLORA → voix, musique, visuels produits ; puis scènes bascule/logo/street/services/final.

## 2026-11-19 (4)
- **Étape atteinte** : script voix off validé. Logo officiel reçu et rangé. Animation 3D du logo (final 5 s) rendue : identite/logo/anim/renders/lc-logo-final-5s.mp4.
- **Dépenses** : 0 $.
- **En attente** : avis sur l'animation du logo + accord budget FLORA (≈0,65–0,86 $).
- **Prochaine action** : version intro 2 s du logo, puis flacon 3D et éclats de verre (gratuit).

## 2026-11-19 (3)
- **Étape atteinte** : PROJET 001 — brief, concept, storyboard, voix off, effets, budget rédigés.
- **Fichiers** : pubs/LC-20261119-loftus-cheek-studio-v1/ (BRIEF, STORYBOARD, SUIVI).
- **Décisions** : signature AI CREATIVE STUDIO · CTA « Contact en DM » · voix 001 homme · voix 002 femme · parfum fictif NOCTIS · aucune dépense sans accord.
- **Prochaine action** : storyboard v2 + VOIX-OFF.md rédigés ; attente accord budget, puis 3 variantes SVG du logo LC (gratuit).

## 2026-11-19 (2)
- **Étape atteinte** : projet officiel enregistré (PROJET.md), outils vérifiés, organisation créée (ORGANISATION.md, _modele-pub/).
- **Constat budget** : FLORA = 0,13 $ disponibles.
- **En attente** : réponses aux infos manquantes, puis prompt du PROJET 001.
- **Prochaine action** : PROJET 001 — brief puis concept et storyboard (rien de généré avant validation).

## 2026-11-19 (1)
- Instructions récupérées depuis Google Drive et installées.
