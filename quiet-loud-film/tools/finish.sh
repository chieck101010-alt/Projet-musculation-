#!/usr/bin/env bash
# Finishing pass on a rendered master: light animated film grain, audio untouched.
#   tools/finish.sh renders/raw-FR.mp4 renders/quiet-loud-FR.mp4
set -euo pipefail
in="$1"; out="$2"
ffmpeg -v error -y -i "$in" \
  -vf "noise=c0s=7:c0f=t+u,format=yuv420p" \
  -c:v libx264 -preset slow -crf 17 -profile:v high -movflags +faststart \
  -c:a copy "$out"
