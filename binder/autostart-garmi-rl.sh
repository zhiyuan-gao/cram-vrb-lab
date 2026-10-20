#!/usr/bin/env bash
set -euo pipefail
command_to_run='python3 -u /home/jovyan/cram-vrb-lab/demos/garmi_rl_demo.py; exec bash'
for terminal in xfce4-terminal gnome-terminal mate-terminal; do
    if command -v "$terminal" >/dev/null 2>&1; then
        exec "$terminal" -- bash -c "$command_to_run"
    fi
done
exec python3 -u /home/jovyan/cram-vrb-lab/demos/garmi_rl_demo.py
