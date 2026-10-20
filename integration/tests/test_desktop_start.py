"""A desktop reconnect must not launch a second simulator."""
from concurrent.futures import ThreadPoolExecutor

import pytest

import web_server as web


def test_concurrent_desktop_connections_start_only_one_run(tmp_path, monkeypatch):
    monkeypatch.setattr(web, 'RESULTS', tmp_path)
    controller = web.Controller(services=False)
    launches = []

    def launch():
        launches.append('run')
        controller.run = tmp_path / 'first-run'
        controller.meta = {'run_id': 'first-run', 'status': 'starting'}
        return controller.meta.copy()

    monkeypatch.setattr(controller, 'start', launch)
    with ThreadPoolExecutor(max_workers=8) as executor:
        responses = list(executor.map(lambda _: controller.start_once(), range(8)))

    assert launches == ['run']
    assert sum(response['started'] for response in responses) == 1
    assert {response['run_id'] for response in responses} == {'first-run'}


@pytest.mark.parametrize('status', ['running', 'completed', 'failed', 'stopped', 'interrupted'])
def test_reopening_desktop_preserves_existing_attempt(tmp_path, monkeypatch, status):
    monkeypatch.setattr(web, 'RESULTS', tmp_path)
    controller = web.Controller(services=False)
    controller.run = tmp_path / 'existing-run'
    controller.meta = {'run_id': 'existing-run', 'status': status}
    monkeypatch.setattr(controller, 'start', lambda: pytest.fail('Duplicate simulator launch'))

    response = controller.start_once()

    assert response == {'started': False, 'run_id': 'existing-run', 'status': status}
