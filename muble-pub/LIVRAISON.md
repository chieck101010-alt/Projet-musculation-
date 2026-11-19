# Muble — livraison

## Fichiers

| Fichier | Format | Durée | Pour |
|---|---|---|---|
| `renders/muble-pub-72s-9x16.mp4` | 1080×1920, 30 i/s, H.264 + AAC | 72 s | TikTok, Reels, Snapchat (version complète et pédagogique) |
| `v25/renders/muble-pub-25s-9x16.mp4` | 1080×1920, 30 i/s, H.264 + AAC | 25 s | Snap / TikTok (version courte, plus commerciale) |
| `v09/renders/muble-pub-09s-9x16.mp4` | 1080×1920, 30 i/s, H.264 + AAC | 9 s | « Démo éclair » : pub non désactivable / Snap Ads, rappel de marque |

## Ce qui est réel

- **Interface Muble** : reconstruite à l'identique d'après les captures du site (textes, champs, couleurs, police Plus Jakarta Sans).
- **Logo** : logo officiel extrait des captures et vectorisé avec Adobe (pas redessiné).
- **Vidéos** : plans réels Adobe Stock (licence gratuite), recadrés en 9:16 et étalonnés.
- **Parcours après l'envoi** : repris du site (formulaire « on vous rappelle avec le prix exact », FAQ « prix figé avant votre validation », « paiement en ligne par carte, Apple Pay ou Google Pay », « informations du chauffeur avant la prise en charge »).
- **Voix off** : Gemini « Achird » (via FLORA), choisie par le client. **Musique** : Stable Audio 3 (via FLORA). **Bruitages** : bibliothèque HyperFrames (licence Pixabay, usage commercial libre).

## Hypothèses à confirmer

1. Le libellé du bouton d'envoi du formulaire (« Réserver mon trajet ») : non visible sur les captures.
2. Les choix « 2 passagers » et « 2 bagages » : options réelles des listes inconnues.
3. Les catégories : seules Éco et Berline sont montrées (vues sur le site).
4. Données d'exemple fictives : Thomas Martin, 06 12 34 56 78, thomas.martin@email.fr, Gare de Lyon → Aéroport Paris-CDG, 12 déc. 2026 à 06:30.
5. L'adresse du site n'est pas affichée à la fin (site encore en prévisualisation). Elle se règle avec la variable `site_url` de la scène finale (`compositions/s6-cta.html`).
6. La prononciation de « Muble » par la voix de synthèse varie légèrement d'une phrase à l'autre : à vérifier à l'écoute.

## Refaire un élément

- Voix / musique / sous-titres : `python3 shared/build_audio.py` puis `python3 shared/build_captions.py assets/audio/vo-words.json 72 compositions/captions.html --skip 0:5 66.3:72`
- Version courte : `python3 shared/build_v25.py` (après un rendu 72 s sans sous-titres copié dans `v25/assets/footage/clean72.mp4`)
- Démo éclair 9 s : `python3 shared/build_v09.py` (réutilise le même rendu sans sous-titres)
- Plans vidéo : `shared/prep_footage.sh <dossier des .mov Adobe Stock> assets/footage`
