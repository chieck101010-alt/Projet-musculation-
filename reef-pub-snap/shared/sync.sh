#!/usr/bin/env bash
# Copie les ressources partagées (flacon 3D, textures officielles, découpes) dans chaque vidéo.
set -e
cd "$(dirname "$0")/.."
for v in v1-street v2-cinema v3-tiktok; do
  mkdir -p "$v/assets/lib" "$v/assets/tex" "$v/assets/cut" "$v/compositions"
  cp assets/lib/three.module.min.js shared/reef-bottle.js "$v/assets/lib/"
  cp assets/tex/plaque-reef33.png "$v/assets/tex/"
  cp assets/cut/*.png "$v/assets/cut/"
  cp .gitignore hyperframes.json "$v/"
  sed "s/reef-pub-snap/reef-$v/" package.json > "$v/package.json"
  printf '{\n  "id": "reef-%s",\n  "name": "reef-%s",\n  "createdAt": "2026-11-17T20:30:00.000Z"\n}\n' "$v" "$v" > "$v/meta.json"
done
