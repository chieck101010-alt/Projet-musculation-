# Organisation du studio LOFTUS-CHEEK

## Arborescence
```
loftus-cheek/
├── PROJET.md              ← brief officiel (référence)
├── INSTRUCTIONS.md        ← règles de travail (depuis Google Drive)
├── ORGANISATION.md        ← ce fichier
├── identite/              ← logo LC, polices, palette (communs à toutes les pubs)
├── commercial/            ← offres, tarifs, messages DM, suivi clients
├── portfolio/             ← sélection des meilleurs rendus finaux
├── _modele-pub/           ← dossier vierge à copier pour chaque nouvelle pub
├── pubs/
│   └── LC-AAAAMMJJ-client-produit-v1/
│       ├── BRIEF.md        (étape 1)
│       ├── STORYBOARD.md   (étapes 2–3, à valider)
│       ├── SUIVI.md        (fait / reste à faire — mis à jour à chaque étape)
│       ├── assets/         (fichiers client, images)
│       ├── audio/voix · audio/musique · audio/sfx   (chaque son dans son fichier)
│       ├── compositions/   (une scène HyperFrames = un fichier → on ne retouche que la scène concernée)
│       └── renders/apercus (brouillons légers) · renders/final (MP4 livrés)
└── suivi/
    ├── point-de-reprise.md       ← où on en est, prochaine action
    └── journal-apprentissage.md  ← une technique apprise par pub + erreurs à ne pas refaire
```

## Règles d'économie (Claude Pro + crédits FLORA)
1. **Une étape = une session courte.** Brief → storyboard → validation → production scène par scène → audio → rendu.
2. **Commit + push après chaque étape** : rien n'est perdu si la session s'arrête.
3. **SUIVI.md + point-de-reprise.md** toujours à jour : on reprend sans tout relire.
4. **Aperçus d'abord** : captures d'images clés et rendu basse qualité avant le rendu final.
5. **Audio généré une seule fois** : on réutilise les fichiers de `audio/`, on ne régénère que la phrase à corriger.
6. **Prix annoncé avant toute génération payante** (FLORA), validation obligatoire.
7. **Éléments communs réutilisés** : logo, ouverture/fermeture LC, palette et polices dans `identite/`.
