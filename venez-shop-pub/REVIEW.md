# REVIEW — Pub Venez Shop « Cagoule Nike 20€ » (33,6 s, 1080×1920, 30 i/s)

## Scènes
| Temps | Scène | Ressources |
|---|---|---|
| 0–2,1 s | Accroche « WESH, T'AS VU ÇA ? » (zoom sur les yeux, glitch) | photo porté |
| 2,1–6,4 s | Logo Nike + « CAGOULE NIKE » + tampon 20€ | photo produit détourée |
| 6,4–11,6 s | Zooms viseur : tissu, virgule Nike, cache-cou → « Qualité · Confort · Protection » | photo produit |
| 11,6–14,6 s | « Le style au quotidien » (photo coupée en deux qui se rejoint, lumières) | photo porté |
| 14,6–22,3 s | Livraison : carte IDF 75/91/92/93/94/95, +5€ IDF, La Poste 24/48h +5€, retrait dans le 93 | infos du flyer |
| 22,3–24,9 s | Produits testés · Paiement sécurisé · Envoi rapide | flyer |
| 24,9–33,6 s | Écran jaune : Snap naskoo_1ter, « Ajoute-moi !! », TikTok @venez_shop75, « Merci pour la force ! » | flyer |

## Sources
- Voix off : Gemini 3.1 Flash TTS (voix Puck, fr-FR) via FLORA, 7 répliques. Musique : Lyria 3.5 via FLORA.
- Logos Nike, Snapchat, TikTok : paquet simple-icons 13.21.0. Police marqueur : Permanent Marker (Apache 2.0).
- Bruitages : banque HyperFrames (voir assets/audio/sfx/CREDITS.md).

## Mesuré, pas écouté
- `hyperframes check` : 0 erreur. Mix final -12,6 LUFS, crête -1,1 dBTP, aucune saturation.
- La voix n'a pas pu être retranscrite (modèle de transcription bloqué par le réseau) : ses durées collent au texte, mais l'intonation reste à écouter.

## Non intégré
- Liens TikTok et Pinterest : inaccessibles depuis la session.
- Flyer : reçu en aperçu seulement ; ses infos et son style sont repris, pas l'image elle-même.

Régénérer : `python3 tools/gen_scenes.py . && python3 tools/gen_index.py .`
