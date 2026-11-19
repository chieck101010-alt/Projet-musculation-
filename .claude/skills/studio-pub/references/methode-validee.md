# Méthode validée par l'utilisateur (projet Muble, VTC — novembre 2026)

L'utilisateur a dit à la livraison : « je l'ai très bien aimé et j'aimerais que tu gardes le même mode de fonctionnement ». C'est le déroulé à reproduire sur les prochaines pubs. Le projet complet sert d'exemple : `muble-pub/` (STORYBOARD.md, SPEC.md, VOIX-OFF.md, LIVRAISON.md, scripts dans `shared/`).

## Le déroulé qui a plu

1. **Inventaire réel** des outils (FLORA, Adobe, Canva, Drive, HyperFrames, registry) avec test concret : liste des modèles, solde FLORA, une licence Adobe Stock téléchargée.
2. **Concept avec un fil rouge** tiré de la promesse de la marque (ici « 2 minutes chrono » : un chrono qui se remplit à chaque étape de la démo).
3. **Storyboard complet** dans `STORYBOARD.md` : faits vérifiés sur le site, éléments manquants, inventaire, recherche avec sources, tableau temps / image / texte / voix / son, budget. **Validation par questions à cocher** avant de produire.
4. **Vraies images** : Adobe Stock catégorie « free » (gratuites, licence en un appel, vrais chauffeurs, vrai Paris) plutôt que la vidéo IA. Recadrage 9:16 et étalonnage commun avec `shared/prep_footage.sh` (ffmpeg).
5. **Interface reconstruite à l'identique** en HTML/CSS d'après les captures (mêmes textes, même police, mêmes couleurs), dans un téléphone en perspective 3D CSS, avec saisie lettre par lettre, doigt qui tape, zooms sur le champ actif. Jamais d'écran inventé : ce qui n'est pas vu sur le site est montré en motion design hors du téléphone, ou signalé comme hypothèse.
6. **Logo** : extrait de la meilleure capture, binarisé, vectorisé avec Adobe `image_vectorize`, puis découpé en symbole / lettres pour l'animer.
7. **Voix** : 3–4 essais courts envoyés à l'utilisateur, il choisit à l'oreille. Ensuite **une prise par phrase** (placement précis, reprise d'une seule phrase si besoin), transcription Whisper (`--model small --language fr`) pour caler chaque coupe et chaque texte sur le mot prononcé.
8. **Mixage par script** (`shared/build_audio.py`) : voix normalisées à −16 LUFS, musique calée pour que sa fin naturelle tombe sur le logo final, baisse automatique sous la voix (sidechain), bruitages de la bibliothèque HyperFrames sur chaque action visible.
9. **Sous-titres par script** (`shared/build_captions.py`) : groupes de 30 caractères max, coupés aux phrases et aux virgules, pastille sombre lisible sur l'interface, coupés là où un titre à l'écran dit déjà la même chose.
10. **Contrôle** : `hyperframes check` à 0 erreur, captures aux moments clés de la voix, vérification que le champ actif n'est jamais caché par les sous-titres, mesure du son du MP4 final, images extraites du MP4.
11. **Version courte** montée à partir d'un rendu « sans sous-titres » de la version longue (`shared/build_v25.py`), avec extraits de la même voix coupés aux pauses, nouvelle musique calée sur la durée et sous-titres propres. Coût de génération supplémentaire : 0.
12. **Livraison** : MP4 envoyés dès qu'ils sont prêts, `LIVRAISON.md` (ce qui est réel, les hypothèses à confirmer, comment refaire), commit et push.

## Leçons pratiques

- **Toujours demander un devis FLORA (`quote: true`) avant de générer.** L'estimation de la liste des modèles correspond à la durée par défaut. Une musique de 90 s coûte environ 3 fois le prix affiché pour 30 s.
- Le solde FLORA peut être bas. Solution économique qui a plu : **voix Gemini 3.1 Flash TTS** en `fr-FR` (≈ 0,013 $ la phrase), **musique Stable Audio 3** (≈ 0,04 $ pour 80 s), **bruitages gratuits** de la bibliothèque HyperFrames (licence Pixabay).
- La génération ElevenLabs Music de 90 s a échoué par dépassement de temps (non facturée). Prévoir une alternative.
- Le compte FLORA est limité à 3 projets actifs : générer dans un projet existant avec `add_to_canvas: false`.
- Les résultats Adobe sont servis par `to.adobe.com` : l'hôte a été ajouté au réseau de l'environnement.
- Les vidéos « 4K » d'Adobe Stock arrivent en ProRes (1 à 2 Go) : les garder hors du dépôt (scratchpad) et ne committer que les plans recadrés.
- Un `cd dossier && commande &` ne change le dossier que dans le sous-shell : les téléchargements en parallèle doivent utiliser des chemins absolus.
- La session peut redémarrer en plein travail : committer et pousser souvent, garder les identifiants de génération dans un fichier (`assets/audio/runs.json`).
- La prononciation d'un nom de marque par une voix de synthèse peut varier d'une phrase à l'autre : le signaler et faire valider à l'écoute.
