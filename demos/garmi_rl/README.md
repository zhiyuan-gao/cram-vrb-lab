# GARMI RL runtime bundled with CRAM Lab

The current image runs the continuous bowl-and-mug household task. Its entry is
in NeemHub's existing Task selector, replacing `garmi rl pick up`; no outer task
toolbar is added. `demos/household_workspace/source.json` records the UI integration
source and `demos/household_workspace/files.sha256.json` verifies the final installed
runtime. The archive and descriptions below record the base runtime retained for
the cached installation layer.

`runtime.tar.gz` is the live counter-to-table demo snapshot. It includes the PPO
inference policy, frozen reference data, source code, Isaac Sim 6.1 compatibility
patch, pinned Python requirements and an English desktop launcher. The source
project is <https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl>, with the desktop,
scene reset, live viewer and camera fixes maintained in its `deployment/isaac61/`
directory. `source.json` pins the source commit and artifact hashes;
`files.sha256.json` identifies every file in this snapshot.

`binder/install_garmi_rl.sh` installs it during the image build into
`/home/jovyan/cram-vrb-lab/garmi-mobile-grasp-rl`, with `/workspace` as the frozen
asset alias. It creates the **GARMI RL Counter to Table** desktop entry beside
original GARMI. No persistent development mount or startup recovery is needed.

The launcher runs 10 complete counter-to-table episodes, retaining Isaac Sim and
its streaming window between episodes. Each episode resets the robot, bowl and
RL control state. The existing bowl starts on the left counter at `(0.2, 7.4)`.
Mouse speeds use Isaac Sim defaults with the corrected camera pivot.

The original GARMI program and environment are preserved. Stop an already
running original GARMI demo before starting RL. The existing NeemHub Workspace
page automatically follows the RL live bridge on port 8765; the saved RL replay
is installed separately from `demos/neemhub/garmi_rl_pick_up.tar.gz`.

Licenses and asset provenance are retained inside the archive in `LICENSE`,
`THIRD_PARTY_NOTICES.md` and `runtime/data-manifest.json`. Regenerate this archive
from a committed source checkout with `python3 scripts/build_native_runtime.py build
--out /path/to/new-package`, then copy the three generated files into this directory.
