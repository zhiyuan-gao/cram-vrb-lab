# GARMI Mobile Grasp Lab

Run a trained mobile grasping policy in the complete GARMI apartment:
**CRAM navigation → RL base-and-right-arm approach → fixed close/lift →
CRAM transport and placement on the dining table**.

[Open the interactive Lab](https://binder.dev.intel4coro.de/v2/gh/zhiyuan-gao/cram-vrb-lab/garmi-rl-demo?urlpath=proxy%2F8781%2F)
· [Watch the demos](https://zhiyuan-gao.github.io/franka-tabletop-tasks/demos/garmi/episodes/)
· [Run locally](binder/README.md)

The workspace shows the live Isaac Sim camera, a remote desktop, task progress
and NeemHub's 3D scene. Opening the desktop starts one attempt automatically.
The page also provides start/stop controls, recordings and downloadable results.

This branch is based on the original
[`garmi@41c1032`](https://github.com/yxzhan/cram-vrb-lab/tree/41c103214a0c89899e4c5ee28428b2f31b116307)
with **Isaac Sim 5.1.0**. It includes checkpoint 7500's exported policy, its
observation normalizer, all 40 bowl grasp references and the adapted assets.
The default demonstration uses reference `bowl-r020` on the left counter.

| Location | Purpose |
|---|---|
| `demos/garmi_rl_demo.py` | Desktop/terminal launch entry |
| `integration/` | CRAM/RL handover, simulator and web controls |
| `rl/garmi_rl/` | Frozen policy observation, action and grasp finishing code |
| `runtime/` | Model, references, assets and hash verification |
| `binder/` | Container and VRB startup |

See [deployment instructions](binder/README.md) and
[validation](runtime/fork-validation.md).
The original Lab documentation is preserved in [README_UPSTREAM.md](README_UPSTREAM.md).
Training and expert-data collection remain in
[`garmi-mobile-grasp-rl`](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl).
Third-party sources and licenses are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
