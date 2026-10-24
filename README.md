# GARMI RL Lab deployment

This repository packages the GARMI desktop workspace for the Virtual Research Building.
The active deployment branch is **`garmi-rl-native-demo`**.

The Lab combines the original CRAM workspace, remote desktop and NeemHub viewer
with one continuous household task. The bowl and mug start on the left kitchen
counter. GARMI delivers the bowl to the dining table, returns for the mug, opens
the upper drawer with its left hand, places the mug inside with its right hand,
and closes the drawer. The task runs once when the desktop session starts.
The left NeemHub pane follows the measured robot, object and drawer states;
the right desktop displays the running Isaac Sim scene.

The demo selector retains the original GARMI and standalone bowl demos.
The **GARMI RL Counter to Table** desktop entry also retains its ten episodes
with scene reset.

[Open the Lab](https://binder.intel4coro.de/v2/gh/zhiyuan-gao/cram-vrb-lab/garmi-rl-native-demo?urlpath=files%2Fdemos%2Fweb_ui%2Findex.html)
· [Task and training source](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl)
· [Runtime provenance](demos/garmi_rl/source.json)

## Repository roles

- **[garmi-mobile-grasp-rl](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl):** training, evaluation, bowl and mug drawer tasks, and the versioned native runtime sources.
- **This repository:** Binder image, build-time installation, desktop integration, workspace page, and a package pinned to an RL source commit.

The mug-to-drawer task is available in the source repository under
[`demos/mug_drawer/`](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl/tree/main/demos/mug_drawer).
Its guide describes the Isaac Sim 5.1 launcher and the published mug policy.
The native Lab package uses the Isaac Sim 6.1 environment supplied by the pinned
GARMI base image.

## Update the runtime

In a committed checkout of the RL source repository:

```bash
python3 scripts/build_native_runtime.py verify
python3 scripts/build_native_runtime.py build --out /path/to/new-runtime-package
```

Copy `runtime.tar.gz`, `files.sha256.json`, and `source.json` from that output into
`demos/garmi_rl/` here. The image installer verifies the archive hash, file manifest,
and every extracted file. `source.json` records the exact source commit.
See [the deployment package guide](demos/garmi_rl/README.md).

Binder builds `binder/Dockerfile`; the workspace opens at
`files/demos/web_ui/index.html`. Use `binder.intel4coro.de` and
`jupyter.intel4coro.de` for production. The `.dev` Binder endpoint is inaccessible
in this workflow. After validating a deployment, a fixed commit URL can be set
as the VRB introduction page's Enter Lab link through its separate CMS.

## Branches

`garmi-rl-native-demo` is the deployment branch. `garmi-rl-demo` retains the earlier
RL workspace implementation. `main`, `garmi`, `dev`, and `isaac6` preserve upstream
versions. Historical release tags provide fixed references for earlier deployments.

[Original project documentation](README_UPSTREAM.md)
