# Fork validation — 20 October 2026

Base: `yxzhan/cram-vrb-lab:garmi@41c1032`.
Imported integration: `zhiyuan-gao/garmi-mobile-grasp-rl@9c35c55`.
Policy: checkpoint 7500, default reference `bowl-r020`.

## Container and automated checks

- The Docker image built successfully with Isaac Sim 5.1.0.
- Bundle verification passed for all 22 runtime files and 37 frozen policy dependencies.
- The integration suite passed **28 tests**, with one optional drawer test skipped.
- The new desktop-start tests cover concurrent starts and reconnecting to running,
  completed, failed, stopped and interrupted attempts.
- The original `demos/garmi_demo.py` and `demos/web_ui/index.html` are unchanged;
  the upstream README is preserved byte for byte in `README_UPSTREAM.md`.

Run the suite inside the prepared container:

```bash
cd /workspace
PYTHONPATH=/workspace/integration:/workspace/rl:/workspace/scripts:/workspace/cram-vrb-lab \
  /isaac-sim/python.sh -m pytest integration/tests -q
```

## Browser and GPU execution

The isolated local container uses an NVIDIA RTX 4070. The browser opens the
GARMI RL panel and an embedded remote desktop. The desktop's XDG startup invokes
`demos/garmi_rl_demo.py` and starts an online simulation without pressing the
page's start button.

Run `20261020-122444-8356` completed CRAM navigation, RL base/right-arm approach,
fixed close/lift, CRAM transport, placement verification and arm retraction.
`transport_result.passed` was true: the bowl was released, supported by the
table, clear of the fingers and stable for two seconds. Horizontal placement
error was **0.007819 m**. Transport used physical grasping without attachment.

The browser verified all four tabs and the connected desktop. Repeated terminal
launch requests during and after the run returned the same run ID. Reloading
the page after completion also preserved the run, without starting another
simulator. The run saved its video and state/task reports.

## Remote VRB status

The new fork has not yet passed a remote GPU execution test.
`https://binder.dev.intel4coro.de/health` returned HTTP 500 during this check.
The repository includes the Binder launch URL and container configuration;
the platform must also supply working CUDA and Vulkan GPU access.
