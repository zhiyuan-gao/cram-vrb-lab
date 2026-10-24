# Bowl and Mug Workspace

The extra Workspace task toolbar is removed. Inside Semantic Digital Twin Scene,
the existing Task picker replaces `garmi rl pick up` with `Bowl and Mug`. Start,
Stop and progress use the scene's existing playback area. Other tasks and the
original Workspace tabs remain available.

This build layer applies only the text files listed in `source.json` after
the existing frozen runtime has been installed. It checks each previous and new
hash, then verifies all 192 runtime files against `files.sha256.json` before
installing the Workspace integration. Simulation code, policies and assets are
unchanged. `source.json` records the source commit, source map and the rebuilt
full-runtime archive hash; `demos/garmi_rl` retains the base archive so its
expensive installation can use the existing Docker cache.

The build writes `household-workspace-source.json` into the installed runtime.
For provenance and verification of this image, use this layer's manifest in
addition to the base package's metadata.
