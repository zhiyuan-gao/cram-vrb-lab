"""Start the GARMI RL demo once and show its progress in the desktop terminal."""
import argparse
import json
import time
import urllib.error
import urllib.request


def request(path, *, token=None, port=8781):
    headers = {'X-Demo-Token': token} if token else {}
    message = urllib.request.Request(
        f'http://127.0.0.1:{port}/api/{path}',
        method='POST' if token else 'GET', headers=headers)
    with urllib.request.urlopen(message, timeout=5) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8781)
    parser.add_argument('--no-wait', action='store_true')
    args = parser.parse_args()
    for attempt in range(30):
        try:
            status = request('status', port=args.port)
            break
        except (urllib.error.URLError, TimeoutError):
            if attempt == 29:
                raise RuntimeError('GARMI web service is unavailable; check /workspace/results/cram-rl-web/server.log')
            time.sleep(1)
    response = request('start-once', token=status['csrf_token'], port=args.port)
    run_id = response['run_id']
    print(f"GARMI RL run: {run_id} ({'started' if response['started'] else 'already exists'})", flush=True)
    print('Open the GARMI RL tab for live Isaac Sim images, controls and saved results.', flush=True)
    if args.no_wait:
        return 0
    previous = None
    try:
        while True:
            status = request('status', port=args.port)
            if status.get('run_id') != run_id:
                print('Another run has been selected; see the GARMI RL tab.', flush=True)
                return 0
            progress = (status['status'], status.get('stage'), status['message'])
            if progress != previous:
                print(f"{status['status']}: {status['message']}", flush=True)
                previous = progress
            if not status['active']:
                print(f'Results: /workspace/results/cram-rl-web/{run_id}', flush=True)
                return 0 if status['status'] == 'completed' else 1
            time.sleep(1)
    except KeyboardInterrupt:
        status = request('status', port=args.port)
        if response['started'] and status.get('run_id') == run_id and status['active']:
            request('stop', token=status['csrf_token'], port=args.port)
            print('\nStopping this run.', flush=True)
        return 130


if __name__ == '__main__':
    raise SystemExit(main())
