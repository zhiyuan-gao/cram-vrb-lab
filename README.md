# GARMI RL Lab deployment

This repository packages the interactive GARMI household demo for the
[VLA and RL Lab](https://vrb.ease-crc.org/explore-labs/vla-lab/) in the Virtual Research Building.
The active release branch is `codex/robokudo-household-release-20261110`.

The bowl and mug start on the kitchen counter. RoboKudo localizes the objects,
CRAM selects the bowl approach station, and `RLPickUpAction` runs the trained
whole-body grasp policy. GARMI carries the bowl to the dining table, returns for
the mug, captures a fresh perception result, grasps it, and places it in a drawer
before closing the drawer. **Start task** runs this continuous sequence once.

The left pane shows the live NeemHub world and task progress; the right pane shows
Isaac Sim on the remote desktop. The NeemHub arrow opens Knowledge, Plan,
Statechart, Kinematics and Transforms. **RoboKudo ↗** shows the RGB-D observations,
object point clouds and pose estimates used during the task.

[Open the Lab](https://binder.dev.intel4coro.de/v2/gh/zhiyuan-gao/cram-vrb-lab/codex%2Frobokudo-household-release-20261110?urlpath=files%2Fdemos%2Fweb_ui%2Findex.html)
· [Task and training source](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl/tree/codex/robokudo-household-release-20261110)
· [Runtime provenance](demos/robokudo_household_release/source.json)

## Current release

The runtime uses the FR3 nominal arm velocity bounds through project-level CRAM
and Giskard overrides. Navigation keeps the validated base limits. The full
local task passed with the bowl on the table and the mug inside the closed drawer.
See [the release guide](demos/robokudo_household_release/README.md).

## Repository roles

- **garmi-mobile-grasp-rl:** training, evaluation, checkpoints, task implementations and native runtime sources.
- **cram-vrb-lab:** Binder image, desktop integration, interactive page and a runtime package pinned to a source commit.

## Update the runtime

From a committed checkout of the source repository:

```bash
python3 scripts/build_native_runtime.py verify
python3 scripts/build_native_runtime.py build --out /path/to/new-runtime-package
```

Copy `runtime.tar.gz`, `files.sha256.json`, and `source.json` into
`demos/robokudo_household_release/`. Binder builds `binder/Dockerfile`; the installer
verifies the package and its files. Open `files/demos/web_ui/index.html` in the
authenticated Jupyter session, then select **Start task**.

The GPU deployment uses `binder.dev.intel4coro.de`. The VRB Enter Lab button pins a
specific validated deployment commit. The original GARMI and other task entries
remain available in the demo selector.

[Original project documentation](README_UPSTREAM.md)
