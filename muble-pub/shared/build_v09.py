#!/usr/bin/env python3
"""Version « Démo éclair » 9 s (projet HyperFrames muble-pub/v09), montée comme la 25 s
à partir du rendu 72 s sans sous-titres. Usage : python3 shared/build_v09.py (depuis muble-pub/)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_v25 as b

b.V = os.path.join(b.ROOT, "v09")
b.NAME, b.TITLE = "muble-pub-09s", "Muble — démo éclair (9 s)"
b.TOTAL = 9.0
b.SEG = [  # (nom, début version courte, début dans le film 72 s, durée)
    ("A", 0.00, 3.15, 1.40),   # Champs-Élysées + « Besoin d'un chauffeur à Paris ? » déjà lisible à l'image 0
    ("B", 1.40, 19.50, 0.90),  # étape 1 : saisie de l'adresse de départ
    ("C", 2.30, 24.60, 0.80),  # étape 2 : heure, 2 passagers
    ("D", 3.10, 30.90, 0.80),  # étape 3 : tap sur Berline
    ("E", 3.90, 38.60, 2.05),  # étape 5 : envoi, chrono 1:48 ✓, « Demande envoyée », « On vous rappelle avec le prix exact »
    ("F", 5.95, 66.95, 3.05),  # logo, signature, bouton
]
b.VO = [  # (nom, fichier, début, fin, placement)
    ("e01", "vo04", 0.0, None, 1.30),  # « Réservez votre chauffeur simplement, en quelques étapes. »
    ("e02", "vo12", 0.0, 1.05, 5.95),  # « Muble. »
    ("e03", "vo13", 0.0, None, 6.85),  # « Réservez dès maintenant. »
]
b.WORDS = [("vo04", 1.30 - 12.90, None)]
b.MUSIC_OFFSET = 68.665  # la fin naturelle de la musique tombe vers 8,4 s
b.SFX = [
    ("impact-bass-1", 0.02, 0.4, 0, None), ("whoosh-short", 1.38, 0.5, 0, None), ("typing", 1.42, 0.28, 0, 0.85),
    ("whoosh", 2.28, 0.4, 0, None), ("click-soft", 2.90, 0.55, 0, None), ("whoosh-short", 3.08, 0.4, 0, None),
    ("click-soft", 3.60, 0.55, 0, None), ("whoosh", 3.88, 0.4, 0, None), ("click", 4.15, 0.7, 0, None),
    ("pop", 4.27, 0.5, 0, None), ("riser", 3.45, 0.22, 1.8, 2.5), ("pop", 5.50, 0.28, 0, None), ("impact-bass-1", 5.95, 0.55, 0, None),
    ("sparkle", 6.00, 0.4, 0, None),
]
b.main()
