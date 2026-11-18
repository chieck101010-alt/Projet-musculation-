#!/usr/bin/env bash
# Télécharge les sorties FLORA listées dans assets/audio/runs.json (ignore celles pas encore prêtes).
cd "$(dirname "$0")/.." || exit 1
python3 - <<'PY'
import json, subprocess, os
runs = json.load(open("assets/audio/runs.json"))
base = "https://media.flora.ai/node-inputs/2026/11/18/px7fmc6g6ehdetkyae0gdjabq58jbc18/gen-{}-0.{}"
for name, rid in runs.items():
    out_dir = "assets/audio/vo" if name.startswith("vo") else "assets/audio"
    if any(os.path.exists(f"{out_dir}/{name}.{e}") for e in ("wav", "mp3")):
        continue
    for ext in ("wav", "mp3"):
        dst = f"{out_dir}/{name}.{ext}"
        r = subprocess.run(["curl", "-sfL", "-o", dst, base.format(rid.replace("run_", ""), ext)])
        if r.returncode == 0 and os.path.getsize(dst) > 1000:
            print("ok", dst); break
        if os.path.exists(dst): os.remove(dst)
PY
