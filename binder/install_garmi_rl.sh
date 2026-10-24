#!/usr/bin/env bash
# Build-time installation only; no startup recovery and no dev-tools mount.
set -euo pipefail
lab_dir="${REPO_DIR:-/home/jovyan/cram-vrb-lab}"
demo_dir="$lab_dir/garmi-mobile-grasp-rl"
/opt/conda/bin/python "$lab_dir/binder/install_garmi_rl.py" \
  --lab "$lab_dir" --desktop-home /home/jovyan
# Frozen policy assets and USD references use this canonical path.
if [[ ! -e /workspace && ! -L /workspace ]]; then
  sudo ln -s "$demo_dir" /workspace
fi
test "$(readlink -f /workspace)" = "$demo_dir"
cd "$demo_dir"
/opt/conda/bin/python runtime/unpack.py
export PATH="/home/jovyan/.local/bin:$PATH"
# Apply the bundled setuptools constraint to every isolated source build,
# including flatdict in the initial requirements installation.
UV_BUILD_CONSTRAINT="$demo_dir/rl/build-constraints.txt" bash scripts/setup_isaac61.sh
"$lab_dir/cognitive_robot_abstract_machine/.venv/bin/python" integration/prepare_full_scene.py
# Validate the frozen bundle and camera math without starting GPU simulation.
PYTHONPATH="$demo_dir/integration:$demo_dir/rl" .venv61/bin/python -c \
  'from pathlib import Path; from garmi_cram_rl.contract import Bundle; Bundle(Path("results/cram-rl-integration/policy-7500"), Path.cwd()); print("Frozen RL bundle validated.")'
test -s integration/assets/apartment.usda
test -x /home/jovyan/Desktop/GARMI_RL_pick_up.desktop
# Install the single continuous task alongside the existing bowl demo.
/opt/conda/bin/python demos/household_sequence/fetch_assets.py
/opt/conda/bin/python scripts/install_live_workspace.py \
  --workspace "$lab_dir" --desktop-home /home/jovyan
/opt/conda/bin/python demos/household_sequence/install.py \
  --lab "$lab_dir" --home /home/jovyan
