# Run the GARMI RL Lab

The Lab executes the trained grasp policy and Giskard online in the complete
GARMI apartment. The default task picks a bowl from the left kitchen counter
and places it on the dining table.

## VRB

[Open the Lab](https://binder.dev.intel4coro.de/v2/gh/zhiyuan-gao/cram-vrb-lab/garmi-rl-demo?urlpath=proxy%2F8781%2F).

The launch URL selects branch `garmi-rl-demo`, builds `binder/Dockerfile` and
opens `proxy/8781/`. The first tab contains the live Isaac Sim camera and the
remote desktop. Opening the desktop starts `demos/garmi_rl_demo.py`, which
requests the first task through the local demo service.

The page's **开始一次运行** button starts another attempt after the current one
finishes. **停止本次运行** stops its simulator and controller. Reopening the
desktop preserves the current or completed attempt. NeemHub, VS Code and
JupyterLab are available in the other tabs.

The original `demos/garmi_demo.py` and `demos/web_ui/index.html` remain in the
repository. The derived image replaces only the desktop's automatic demo
selection with `GARMI-RL-autostart.desktop`.

## Local GPU container

```bash
git clone --branch garmi-rl-demo --single-branch https://github.com/zhiyuan-gao/cram-vrb-lab.git
cd cram-vrb-lab
docker build -t garmi-rl-lab -f binder/Dockerfile .
docker run --rm --runtime=nvidia --gpus all --shm-size=1g \
  -p 127.0.0.1:8891:8888 --name garmi-rl-lab garmi-rl-lab \
  jupyter lab --ip=0.0.0.0 --port=8888 --no-browser \
  --IdentityProvider.token= --ServerApp.password=
```

Open <http://127.0.0.1:8891/proxy/8781/>. This local command exposes the workspace
only on the host's loopback interface. VRB sessions use JupyterHub authentication.
For a remote workstation, forward port 8891 over SSH.

The container supplies Isaac Sim 5.1, Isaac Lab, the trained policy and all
runtime data. The host supplies an NVIDIA GPU, compatible driver and NVIDIA
Container Toolkit. Both CUDA and Vulkan must be accessible inside the session.
Submodules need not be fetched for this Docker build; their tested installations
and the original apartment assets come from the pinned base image.

## Run from a terminal

Inside the running Lab:

```bash
python3 /home/jovyan/cram-vrb-lab/demos/garmi_rl_demo.py
```

This starts the first run or observes the existing one. It prints progress and
the result directory. The web service is started by `binder/rl-entrypoint.sh`.

## Results

Each attempt saves its video, state trace and task report to
`/workspace/results/cram-rl-web/<run-id>/`. Successful placement requires physical
release, support and stability, followed by the task's completion event.

Before stopping a local container, save its results:

```bash
docker cp garmi-rl-lab:/workspace/results/cram-rl-web ./garmi-demo-results
```

For VRB, download the result directory through JupyterLab.

## Platform status

The original High-Fidelity Lab uses `binder.dev.intel4coro.de`. On 20 October
2026 its `/health` endpoint returned HTTP 500. The earlier production Binder
test could open a workspace but did not receive a GPU. These are separate from
the local GPU-container tests recorded in [fork-validation.md](../runtime/fork-validation.md).

Platform resource configuration lives in
[`IntEL4CoRo/binder.intel4coro.de-deploy`](https://github.com/IntEL4CoRo/binder.intel4coro.de-deploy).
Publishing this repository does not modify that platform or the VRB introduction
page.
