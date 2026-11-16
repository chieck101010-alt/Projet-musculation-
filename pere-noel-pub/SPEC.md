# SPEC — « Un seul cadeau » · Père Noël & Cie

GOAL:    le spectateur suit UN cadeau de l'usine au sapin et finit convaincu que la livraison du Père Noël
         est une machine logistique parfaite (et que ce studio sait faire du motion design 3D).
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps
TIME:    48.4 s x 30 = 1452 frames. Musique ~121.5 BPM (≈ 14.8 frames / temps). Voix off = horloge.

LOOK:    3D isométrique, caméra orthographique, élévation 35.26°, azimut 45° (± 15° max).
         Sol neige #EEF3FB, horizon/nuit #2A3A6B (seulement aux bords du plan large, via le sol).
         Rouge marque #D7263D, or #F2B33D (accent : ruban, routes, étoile, 1 mot par titre), marine #1B2A4A (encre).
         Volumes en boîtes à faces planes, 3 tons par volume (dessus clair, gauche moyen, droite sombre)
         donnés par 1 soleil (0.35, 1, 0.75) + ciel hémisphérique ; ombres portées douces (PCF, 4096).
         Fenêtres : éteintes #3E4E78 → allumées #FFC965 (le récit : chaque livraison allume une maison).
         Titres : Montserrat 900, 120–150 px, tracking -2 % ; textes secondaires Montserrat 700, 36–48 px.
OBJECTS: cadeau héros (cube rouge, ruban or croisé, nœud 2 boucles) ; usine à tapis roulant, arche d'emballage,
         portique scanner (barre verte), bras aiguilleur, toboggan rouge/blanc à tremplin ; traîneau rouge à patins or,
         sac en toile, Père Noël, 4 rennes ; ville 8×6 îlots de maisons à toits enneigés et cheminées ;
         maison héros en coupe : murs avant qui se rabattent, toit qui s'envole, conduit de cheminée ouvert,
         cheminée à chaussettes, sapin à 20 ampoules + étoile, enfant endormi ; carte du monde : villages, routes or.
MOTION:  arrivées expo.out / power4.out ; caméra power2/3.inOut ; zooms en espace log ; sorties power3.in.
         Ressorts : atterrissages de cadeaux (squash 0.75 / stretch 1.15, amortissement ~0.5).
         Titres posés puis immobiles. Rotation de monde ≤ 1.5°/s.
SHOTS:   0.0–4.3   macro : le ruban se noue sur le cadeau (0.3–1.6), le tapis démarre (1.8), recul sur l'usine.
         4.3–9.3   « Emballé / Vérifié / Trié » : caméra suit le cadeau ; scanner vert 5.65 ; bras 6.88 ;
                   compteur « 2 000 000 000 » 7.85 ; montée sur l'usine entière.
         9.3–13.6  toboggan → tremplin → saut dans le sac 10.55–11.1 ; gros plan traîneau ; « le ciel » 13.73 décollage.
         13.6–23.4 survol de la ville (suivi traîneau), 6 cadeaux largués sur les temps, chaque maison s'allume.
         23.4–31.0 plongée sur la maison héros ; murs/toit s'ouvrent 23.9 ; cadeau dans le conduit 25.85 ;
                   sauts jusqu'au sapin 26.6–27.95 ; guirlande 28.3 ; étoile 29.0 ; la maison se referme 30.2.
         31.0–37.6 dézoom log 6.5 → 150 : toutes les fenêtres s'allument en vague, routes or depuis le Pôle Nord ;
                   titre « 24 fuseaux horaires. 1 nuit » 35.0.
         37.6–38.12 iris blanc depuis le centre.
         38.12–48.4 carte de fin : le cadeau géant tombe (38.6), le couvercle saute (39.1), un mini-traîneau en sort
                   et « tire » le logotype qui s'essuie (39.6) ; slogan 41.5 ; tenue jusqu'à la fin.
BANNED:  fond vide sombre avec petits objets ; glow, bloom, néon, particules décoratives (la neige qui tombe = météo,
         désactivée sur la carte de fin) ; dégradés violets ; tout centré ; tout en fondu/montée ;
         textes qui bougent pendant la lecture ; labels de coin, HUD ; trois cartes ; logo dans un coin ;
         UI produit inventée.
QA:      0.0 (vignette : cadeau + machine, jamais noir), 1.6 (nœud fini), 5.7 (scanner vert), 8.5 (compteur lisible),
         10.8 (saut dans le sac), 14.0 (décollage), 19 (largage + fenêtre allumée), 24.6 (maison ouverte),
         26.2 (cadeau dans le conduit), 28.9 (sapin allumé), 33 (dézoom), 36 (titre réseau), 40.5 (logotype), 47 (fin).
