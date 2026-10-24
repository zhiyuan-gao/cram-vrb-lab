# GARMI RL recording

`garmi_rl_pick_up.tar.gz` contains the self-contained NeemHub recording of the
successful CRAM navigation → RL grasp → CRAM transport and placement run
`20261020-164101-49d9`. It includes 1327 trajectory frames, the robot and apartment
models, meshes, and the camera configuration. The source project is
`garmi-mobile-grasp-rl`; its recording is under
`results/cram-rl-web/20261020-164101-49d9/cramera/scenes/__recording__`.

The Binder Dockerfile extracts this archive into
`cognitive_robot_abstract_machine/cramera/scenes/garmi_rl_pick_up` during the image
build, alongside `garmi_pick_place`. NeemHub scans this shared scene directory.
The Workspace uses NeemHub's existing Robot / Environment / Task selectors;
there is no additional outer demo bar.

At runtime this replay needs neither `/mnt/dev-tools`, a startup restore command,
nor a running simulation. The original GARMI desktop demo remains available.
In **NeemHub + Desktop**, choose Robot **garmi**, Environment **GarmiApartment**,
and Task **garmi rl pick up**, then **Play NEEM** in NeemHub.

Build and deploy the updated Binder image to retain these files in newly created
containers. Changes to a running container do not update the image it was made from.
