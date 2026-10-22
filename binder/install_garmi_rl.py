"""Install the bundled RL source and desktop entry during the image build."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tarfile


def verify_source(payload):
    source = json.loads((payload / 'source.json').read_text())
    if source['repository'] != 'https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl':
        raise ValueError('Unexpected RL source repository')
    commit = source['commit']
    if len(commit) != 40 or any(c not in '0123456789abcdef' for c in commit):
        raise ValueError('RL source must pin a full commit')
    for name, key in [('runtime.tar.gz', 'archive_sha256'),
                      ('files.sha256.json', 'files_manifest_sha256')]:
        if hashlib.sha256((payload / name).read_bytes()).hexdigest() != source[key]:
            raise ValueError(f'RL source artifact mismatch: {name}')
    return source


def install(lab, desktop_home):
    root = lab / 'garmi-mobile-grasp-rl'
    if root.exists():
        raise FileExistsError(f'Refusing to overwrite an existing RL installation: {root}')
    payload = lab / 'demos/garmi_rl'
    source = verify_source(payload)
    expected = json.loads((payload / 'files.sha256.json').read_text())
    if len(expected) != source['file_count']:
        raise ValueError('RL source file count mismatch')
    with tarfile.open(payload / 'runtime.tar.gz', 'r:gz') as archive:
        members = archive.getmembers()
        if len(members) != len(expected) or {m.name for m in members} != set(expected):
            raise ValueError('Runtime archive does not match its file manifest')
        for member in members:
            if not member.isfile() or not (root / member.name).resolve().is_relative_to(root.resolve()):
                raise ValueError(f'Unsafe runtime member: {member.name}')
            if hashlib.sha256(archive.extractfile(member).read()).hexdigest() != expected[member.name]:
                raise ValueError(f'Runtime checksum mismatch: {member.name}')
        archive.extractall(root, filter='data')
    frozen = root / 'cram-vrb-lab'
    shutil.copytree(root / 'runtime/cram_vrb_lab', frozen / 'cram_vrb_lab')
    for name in ('cognitive_robot_abstract_machine', 'ros2_ws'):
        (frozen / name).symlink_to(lab / name, target_is_directory=True)
    # Keep the policy's frozen world.usda, sharing the original image's meshes.
    for source in (lab / 'assets').iterdir():
        destination = frozen / 'assets' / source.name
        if source.name == 'garmi-apartment':
            for child in source.iterdir():
                if child.name != 'world.usda':
                    (destination / child.name).symlink_to(child, target_is_directory=child.is_dir())
        else:
            destination.symlink_to(source, target_is_directory=source.is_dir())
    desktop = (root / 'integration/GARMI_RL_pick_up.desktop').read_text()
    desktop = desktop.replace('/mnt/dev-tools/rl_project/garmi-mobile-grasp-rl', str(root))
    for folder in (lab / 'demos/desktop', desktop_home / 'Desktop'):
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / 'GARMI_RL_pick_up.desktop'
        target.write_text(desktop)
        target.chmod(0o755)
    print(f'Installed the RL source and desktop entry at {root}')
    return root


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lab', type=Path, required=True)
    parser.add_argument('--desktop-home', type=Path, required=True)
    args = parser.parse_args()
    install(args.lab.resolve(), args.desktop_home.resolve())
