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
The installer checks the archive and all 260 runtime files. Existing household
assets and checkpoints come from the preceding cached image layers.

This release applies the FR3 nominal arm velocity bounds in the project's CRAM
and Giskard worlds. Base navigation limits retain the previously validated values.
Local run `20261111-133904-4156` completed both physical tasks and fresh RoboKudo
perception checks. Placement, verification and arm parking took 78.65 seconds,
compared with 133.98 seconds in the preceding local run. Total time was 14 minutes
41 seconds including cold startup; machine load and startup affect that total.
The runtime contains the task validator in `demos/robokudo_household/`.

The Binder image requires NVIDIA CUDA and Vulkan access. Platform health alone
does not verify GPU access; check a new Binder session before changing the
public Enter Lab link to this release.
