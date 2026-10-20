# GARMI RL Workspace

A separate copy of the CRAM Workspace hosts the counter-to-table demo: CRAM navigation → RL base/right-arm approach → fixed close/lift → CRAM transport and placement.

The first tab shows the live Isaac camera, task stages and remote desktop. Opening the desktop automatically starts one run through `demos/garmi_rl_demo.py`. Reopening it keeps the same run; the page's start button launches another attempt after completion. **NeemHub**, **VS Code**, and **JupyterLab** use the session’s existing proxy.

For container and Binder launch instructions, see [binder/README.md](../../binder/README.md). The original CRAM Lab page remains unchanged.

Each run creates its own directory under `results/cram-rl-web/`. Success requires task completion and a passed physical placement check. Closing a run stops only that run’s processes.
