#!/usr/bin/env bash
# Recadre les plans Adobe Stock en 1080x1920 (9:16), 30 i/s, étalonnage commun « noir chrome » LOFTUS-CHEEK.
# Usage : prep_footage.sh <dossier_brut> <dossier_sortie>
set -euo pipefail
RAW="$1"; OUT="$2"; mkdir -p "$OUT"
GRADE="eq=contrast=1.10:saturation=0.85:gamma=0.96,colorbalance=rs=-0.02:gs=-0.01:bs=0.03:rh=0.02:gh=0.01,vignette=angle=PI/4.5"
clip() { # sortie source début durée x-du-recadrage (w=largeur source, ih=hauteur)
  ffmpeg -v error -y -ss "$3" -t "$4" -i "$RAW/$2" -an \
    -vf "fps=30,crop=w=ih*9/16:h=ih:x='$5':y=0,scale=1080:1920:flags=lanczos,$GRADE,format=yuv420p" \
    -c:v libx264 -preset medium -crf 19 -movflags +faststart "$OUT/$1.mp4" </dev/null && echo "ok $1"
}
clip ville-pas        homme-nuit-ville.mov        1.5 4.0 "min(iw-ih*9/16,900+30*t)"
clip sneakers-neon    sneakers-neon.mov           1.0 3.0 "(iw-ih*9/16)/2"
clip homme-marche     homme-marche-travelling.mov 6.0 3.0 "600"
clip parfum-spray     parfum-spray.mov            9.0 4.0 "1100"
clip montre-trotteuse montre-trotteuse.mov        4.0 4.0 "700"
clip montre-meca      montre-mecanisme.mov        2.0 5.0 "850"
clip montre-noir      montre-noir.mov             0.5 4.5 "720"
