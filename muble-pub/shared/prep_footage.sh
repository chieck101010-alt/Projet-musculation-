#!/usr/bin/env bash
# Recadre les plans Adobe Stock en 1080x1920 (9:16), 30 i/s, avec un étalonnage commun « nuit parisienne ».
# Usage : prep_footage.sh <dossier_raw> <dossier_sortie>
set -euo pipefail
RAW="$1"; OUT="$2"; mkdir -p "$OUT"
GRADE="eq=contrast=1.07:saturation=0.96:gamma=0.98,colorbalance=rs=-0.01:gs=-0.015:bs=0.05:rh=0.01:bh=-0.01,vignette=angle=PI/5"
# nom | source | début | durée | expression x du recadrage (largeur source w, hauteur h ; t = temps)
clip() { # $1 sortie $2 source $3 ss $4 durée $5 cropx-expr
  local src="$RAW/$2"
  ffmpeg -v error -y -ss "$3" -t "$4" -i "$src" -an \
    -vf "fps=30,crop=w=ih*9/16:h=ih:x='$5':y=0,scale=1080:1920:flags=lanczos,$GRADE,format=yuv420p" \
    -c:v libx264 -preset slow -crf 19 -movflags +faststart "$OUT/$1.mp4" </dev/null
  echo "ok $1"
}
vert() { # plans déjà verticaux
  ffmpeg -v error -y -ss "$3" -t "$4" -i "$RAW/$2" -an \
    -vf "fps=30,scale=1080:1920:flags=lanczos,$GRADE,format=yuv420p" \
    -c:v libx264 -preset slow -crf 19 -movflags +faststart "$OUT/$1.mp4" </dev/null
  echo "ok $1"
}
clip rdv-business-seat     482289372.mov  0.0  6.0  "1900-ih*9/32"
vert avion-voyageur        1270012406.mov 0.0  6.0
clip champs-elysees-nuit   557621523.mov  1.0  7.0  "1720-ih*9/32"
clip chauffeur-marche      chauffeur-eiffel_264564019.mov 5.5 4.7 "min(iw-ih*9/16,max(0,700-ih*9/32))"
clip chauffeur-portiere    chauffeur-eiffel_264564019.mov 16.8 3.4 "min(iw-ih*9/16,max(0,(780-25*t)-ih*9/32))"
clip passager-nuit         596558039.mov  0.0  7.0  "min(iw-ih*9/16,2950-ih*9/32)"
clip smartphone-voiture    440314317.mov  1.0  7.0  "2250-ih*9/32"
vert valise-avion          746098855.mov  0.0  7.0
clip gare-de-lyon          526417762.mov  2.0  7.0  "min(iw-ih*9/16,max(0,(1250+25*t)-ih*9/32))"
clip sorties-amies         226798580.mov 18.0  7.0  "min(iw-ih*9/16,max(0,930-ih*9/32))"
clip paris-nuit-alexandre3 178022166.mov  0.0 10.0  "min(iw-ih*9/16,max(0,(1150-20*t)-ih*9/32))"
