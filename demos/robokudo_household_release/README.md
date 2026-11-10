# RoboKudo household Lab

This release runs one continuous GARMI task in Isaac Sim: perceive and grasp a
bowl on the kitchen counter, carry it to the dining table, return to perceive
and grasp a mug, then open a drawer, place the mug inside and close the drawer.
The trained policies coordinate the base and right arm during grasping.

The Workspace keeps the live NeemHub scene on the left and Isaac Sim desktop
on the right. NeemHub's arrow opens Knowledge, Plan, Statechart, Kinematics and
Transforms. The RoboKudo arrow opens the actual RGB-D observations, fitted
object geometry and perception results used by the policies.

`Start task` runs the sequence once. Starting again cleans up the previous
simulation and task processes and reloads the initial scene. The final scene
stays visible after completion.

The runtime is built from the commit pinned in `source.json` in
[garmi-mobile-grasp-rl](https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl/tree/codex/robokudo-household-release-20261110).
The installer checks the archive and all 259 runtime files. Existing household
assets and checkpoints come from the preceding cached image layers.

Local validation completed both physical tasks in 11 minutes 39 seconds,
including startup. Simulator RSS remained around 9 GB. The runtime contains
the full validation and performance records in `demos/robokudo_household/`.

The Binder image requires NVIDIA CUDA and Vulkan access. Platform health alone
does not verify GPU access; check a new Binder session before changing the
public Enter Lab link to this release.
