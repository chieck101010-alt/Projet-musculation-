# Besoin → meilleur outil

Vérifie toujours qu'un outil est réellement connecté et capable (liste ses modèles/fonctions) avant de le proposer.

| Besoin | 1er choix | Alternative | Remarques |
|---|---|---|---|
| Voix off naturelle | FLORA → ElevenLabs v3 (`t2a-elevenlabs-tts-v3`) ou Eleven v4 ; **Gemini 3.1 Flash TTS `fr-FR`** (voix « Achird » choisie pour Muble, ≈ 0,013 $ la phrase) | Enregistrement de l'utilisateur (le plus authentique pour un accent précis) | HeyGen : voix françaises payantes (abonnement HyperFrames). Piper (local) = dépannage, voix robotique. |
| Musique | FLORA → ElevenLabs Music / Lyria / Stable Audio | Catalogue HeyGen (via `media-use`, nécessite le CLI `heygen`) | La synthèse maison (`numpy`) n'est qu'un dernier recours. |
| Bruitages | FLORA → ElevenLabs Sound Effects | Bibliothèque HyperFrames `media-use/audio/assets/sfx` (licence Pixabay, gratuite) ; Openverse (crédit CC BY) | Openverse est bloqué par le réseau de l'environnement. |
| Vidéos réelles (lieux, personnes, voitures) | **Adobe Stock, catégorie « free »** (`asset_search` StockAsset + `asset_license_and_download_stock`) | FLORA vidéo IA | Gratuit, licence en un appel, plus crédible que l'IA pour des voitures et des villes réelles. |
| Images / vidéos IA | FLORA (modèles image, vidéo, image→vidéo) | Runway (si connecté), Canva `generate-image` | Ne jamais remplacer le produit officiel par une image générée. |
| Logo en haute définition | Fichier officiel du client | Adobe `image_vectorize` sur la meilleure capture (binarisée avant) | Dire au client que c'est une vectorisation de sa capture. |
| Détourage | Adobe `image_remove_background` / `image_select_subject` | Canva `remove-background` | Le `remove-background` de HyperFrames est pensé pour des personnes, il rend mal les plantes et objets fins. |
| Retouche / extension d'image | Adobe (effets, generative expand, fill) | | |
| Polices | Adobe Fonts (`font_recommend`, `font_search`) | Polices intégrées à HyperFrames | Toute police non intégrée doit être fournie en fichier (`@font-face`). |
| Visuels fixes, déclinaisons | Canva | Adobe Express | |
| Montage, motion, 3D, sous-titres, rendu MP4 | HyperFrames (`hyperframes`, `hyperframes-cli`) | | Effets prêts à l'emploi : `hyperframes-registry` (~450 blocs). |
| Copier une vidéo de référence | `reverse-any-video` | Extraction d'images clés avec ffmpeg | |
| Style éprouvé | `style-sampling` | | |
| Recherche tendances | Recherche web, `firecrawl`, `deep-research` | | |
| Analyse de pubs concurrentes | `apify-ultimate-scraper` | | |
| Fichiers de l'utilisateur / partage | Google Drive | | Envoi depuis la session limité à ~3 Mo par fichier. |
| Présentation client | `slideshow`, `pptx`, `pdf`, `docx` | | |

## Pièges connus

- **Réseau** : un site bloqué se débloque en l'ajoutant aux hôtes autorisés de l'environnement (outil `update_environment`). Les outils Node ont besoin de `NODE_USE_ENV_PROXY=1` pour passer par le proxy.
- **Installations** : l'installation de nouveaux logiciels peut être refusée par la sécurité de la session ; demande l'accord explicite de l'utilisateur, ne contourne pas.
- **Connecteurs qui se déconnectent** : refais un ToolSearch avec le nom du serveur avant de conclure qu'un outil est absent.
- **Prix** : FLORA affiche des estimations en $ — annonce-les avant de générer et attends l'accord. Demande toujours un devis exact (`quote: true`) : l'estimation de la liste vaut pour la durée par défaut.
- **Adobe** : les résultats sont servis par `to.adobe.com` (ajouté au réseau de l'environnement en novembre 2026).
- Voir aussi `methode-validee.md` (leçons du projet Muble).
