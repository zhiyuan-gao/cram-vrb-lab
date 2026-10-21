# Use the exact original GARMI image serving the validated Isaac Sim 6.1 demo.
FROM intel4coro/yxzhan-2dcram-2dvrb-2dlab-eb909a@sha256:758b2d8bd2e9f0381a2ae766e341525d001e07a5db567922d9167a38966a366a
USER jovyan
ENV REPO_DIR=/home/jovyan/cram-vrb-lab

# Everything needed by RL is installed during the image build, beside GARMI.
COPY --chown=jovyan:users binder/install_garmi_rl.py binder/install_garmi_rl.sh ${REPO_DIR}/binder/
COPY --chown=jovyan:users demos/garmi_rl/ ${REPO_DIR}/demos/garmi_rl/
COPY --chown=jovyan:users demos/neemhub/ ${REPO_DIR}/demos/neemhub/
COPY --chown=jovyan:users demos/web_ui/index.html ${REPO_DIR}/demos/web_ui/index.html
RUN tar -xzf ${REPO_DIR}/demos/neemhub/garmi_rl_pick_up.tar.gz \
        -C ${REPO_DIR}/cognitive_robot_abstract_machine/cramera/scenes && \
    test -s ${REPO_DIR}/cognitive_robot_abstract_machine/cramera/scenes/garmi_rl_pick_up/trajectory.json && \
    bash ${REPO_DIR}/binder/install_garmi_rl.sh

WORKDIR ${REPO_DIR}
# Preserve the original image's Jupyter/desktop entrypoint and default command.
