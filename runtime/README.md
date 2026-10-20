# GARMI inference bundle

`data.tar.gz` contains the checkpoint 7500 inference policy (`actor.ts` with its
input normalizer), 40 bowl grasp references, the position filter, adapted assets
and the small grasp cache used by the CRAM adapter.

The container build verifies all 22 files against `data-manifest.json` and the
policy's 37 frozen source dependencies. The full apartment and CRAM installation
come from the pinned upstream GARMI image. `integration/prepare_full_scene.py`
constructs the complete scene at build time.

The integration was imported from
[`zhiyuan-gao/garmi-mobile-grasp-rl@9c35c55`](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl/tree/9c35c550c31b689833d6e9df51082232f43e8093).
This fork starts at
[`yxzhan/cram-vrb-lab:garmi@41c1032`](https://github.com/yxzhan/cram-vrb-lab/tree/41c103214a0c89899e4c5ee28428b2f31b116307),
using Isaac Sim 5.1.0. The upstream `dev` / `isaac6` branches are separate.

The original integration's validation is retained in
[previous-validation.md](previous-validation.md). Validation of this fork's new
desktop launcher is recorded in [fork-validation.md](fork-validation.md).
