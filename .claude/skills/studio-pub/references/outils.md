# Besoin → meilleur outil

Vérifie toujours qu'un outil est réellement connecté et capable (liste ses modèles/fonctions) avant de le proposer.

| Besoin | 1er choix | Alternative | Remarques |
|---|---|---|---|
| Voix off naturelle | FLORA → ElevenLabs v3 (`t2a-elevenlabs-tts-v3`) ou Eleven v4 | Scenario → ElevenLabs, Minimax Speech 2.8 HD (41 langues, 10 émotions), Qwen Audio 3 ; enregistrement de l'utilisateur (le plus authentique pour un accent précis) | HeyGen : voix françaises payantes (abonnement HyperFrames). Piper (local) = dépannage, voix robotique. |
| Musique | FLORA → ElevenLabs Music / Lyria / Stable Audio | Scenario → Minimax Music 3.0, ElevenLabs Music, Lyria ; catalogue HeyGen (via `media-use`, nécessite le CLI `heygen`) | La synthèse maison (`numpy`) n'est qu'un dernier recours. Compare le prix FLORA / Scenario. |
| Bruitages isolés | FLORA → ElevenLabs Sound Effects | Scenario → Sonilo Text→SFX ; Openverse (crédit CC BY) | |
| Bruitages calés sur la vidéo montée | Scenario → Sonilo Video→SFX (`model_sonilo-v1-1-video-to-sound-effects`) ou Kling Video→Audio | Placement à la main des sons FLORA | Il écoute la vidéo finie et place les sons sur les impacts. Vérifier ensuite le mixage avec la voix off. |
| Images / vidéos IA | FLORA ou Scenario (Veo 3.1, Seedance 2.5, Kling V3 jusqu'en 4K, Runway Gen-4.5, Luma Ray 3.2, FLUX.3 première/dernière image) — compare le prix | Canva `generate-image` | Ne jamais remplacer le produit officiel par une image générée. |
| Retouche / détourage / agrandissement vidéo | Scenario → Runway Aleph 2 (retouche par description), Pixelcut Video Background Removal, Topaz / Magnific Video Upscale | | |
| Avatar qui parle, synchro labiale | Scenario → Kling AI Avatar 2 Pro, Sync-3, Veed Fabric | | Jamais le visage d'une vraie personne sans son accord. |
| 3D depuis une photo, squelette, animation | Scenario → Tripo 3.1, Hunyuan 3D 3.1 Pro, Meshy, Cartwheel / Uthana (animation) | FLORA (3D) | Pour le produit officiel, la 3D Three.js mesurée sur la photo reste prioritaire : un modèle généré peut inventer des faces. |
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
- **Prix** : FLORA affiche des estimations en $ — annonce-les avant de générer et attends l'accord.
- **Scenario** :
  - Le prix est compté en « Creative Units ». Lance d'abord `model_run` avec `dry_run=true` (gratuit), annonce le prix et attends l'accord.
  - Toujours lire `model_schema_get` avant `model_run`.
  - L'équipe et le projet se récupèrent avec `teams_list` (compte gratuit, projet « Default Project »).
  - `models_list` renvoie des listes énormes : filtre par modalité (`video`, `audio`, `image`, `3d`) et ignore les modèles marqués `Deprecated`.
  - Beaucoup d'outils (crédits restants, analyse d'image, contrôle qualité…) ne s'appellent qu'à travers `scenario_tool_execute_read` / `_write` : la liste complète s'obtient avec `scenario_tools_list`.
