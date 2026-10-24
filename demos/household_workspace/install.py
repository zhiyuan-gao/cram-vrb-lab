"""Apply the hashed Workspace update to the existing frozen runtime."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

PAYLOAD = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def install(lab):
    root = lab / 'garmi-mobile-grasp-rl'
    source = json.loads((PAYLOAD / 'source.json').read_text())
    baseline = json.loads((lab / 'demos/garmi_rl/source.json').read_text())
    if baseline['commit'] != source['base_runtime_commit']:
        raise ValueError('Unexpected base runtime')
    for name, entry in source['files'].items():
        target = root / name
        bundled = PAYLOAD / 'files' / name
        if not target.resolve().is_relative_to(root.resolve()) or not bundled.resolve().is_relative_to((PAYLOAD / 'files').resolve()):
            raise ValueError(f'Unsafe update path: {name}')
        previous = entry['before_sha256']
        if (target.exists() if previous is None else digest(target) != previous) or digest(bundled) != entry['sha256']:
            raise ValueError(f'Workspace update checksum mismatch: {name}')
    for name in source['files']:
        (root / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(PAYLOAD / 'files' / name, root / name)
    expected = json.loads((PAYLOAD / 'files.sha256.json').read_text())
    for name, sha in expected.items():
        if digest(root / name) != sha:
            raise ValueError(f'Final runtime checksum mismatch: {name}')
    subprocess.run([sys.executable, str(root / 'scripts/install_live_workspace.py'),
                    '--workspace', str(lab)], check=True)
    shutil.copy2(PAYLOAD / 'source.json', root / 'household-workspace-source.json')
    print(f'Installed native Task integration from {source["commit"]}; verified {len(expected)} runtime files')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lab', type=Path, required=True)
    install(parser.parse_args().lab.resolve())
