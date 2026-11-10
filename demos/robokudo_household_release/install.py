"""Install the verified RoboKudo household runtime after cached Lab layers."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

PAYLOAD = Path(__file__).resolve().parent


def install(lab):
    root = lab / 'garmi-mobile-grasp-rl'
    if not (root / 'household/assets/garmi_dual_preserved.usda').is_file():
        raise RuntimeError('Install the original household runtime and assets first')
    sys.path.insert(0, str(lab / 'binder'))
    from install_garmi_rl import verify_source
    source = verify_source(PAYLOAD)
    expected = json.loads((PAYLOAD / 'files.sha256.json').read_text())
    if len(expected) != source['file_count']:
        raise ValueError('Unexpected runtime file count')
    with tarfile.open(PAYLOAD / 'runtime.tar.gz', 'r:gz') as archive:
        members = archive.getmembers()
        if len(members) != len(expected) or {m.name for m in members} != set(expected):
            raise ValueError('Archive members differ from the manifest')
        for member in members:
            if not member.isfile() or not (root / member.name).resolve().is_relative_to(root.resolve()):
                raise ValueError(f'Unsafe archive member: {member.name}')
            if hashlib.sha256(archive.extractfile(member).read()).hexdigest() != expected[member.name]:
                raise ValueError(f'Runtime checksum mismatch: {member.name}')
        archive.extractall(root, filter='data')
    shutil.copytree(root / 'runtime/cram_vrb_lab', root / 'cram-vrb-lab/cram_vrb_lab', dirs_exist_ok=True)
    subprocess.run([sys.executable, str(root / 'scripts/install_live_workspace.py'),
                    '--workspace', str(lab), '--desktop-home', str(Path.home())], check=True)
    subprocess.run([sys.executable, str(root / 'demos/robokudo_household/install_preview.py')],
                   env={**os.environ, 'GARMI_PERCEPTION_HOUSEHOLD': '1'}, check=True)
    for name, sha in expected.items():
        if hashlib.sha256((root / name).read_bytes()).hexdigest() != sha:
            raise ValueError(f'Installed runtime checksum mismatch: {name}')
    web = (lab / 'demos/web_ui/index.html').read_text()
    for required in ('openPath:', 'layout=workspace', 'robokudo-workspace.js'):
        if required not in web:
            raise RuntimeError(f'Missing Workspace entry: {required}')
    shutil.copy2(PAYLOAD / 'source.json', root / 'robokudo-household-source.json')
    print(f'Installed RoboKudo household source {source["commit"]}; verified {len(expected)} files')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lab', type=Path, required=True)
    install(parser.parse_args().lab.resolve())
