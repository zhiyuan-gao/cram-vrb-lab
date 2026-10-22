import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import hashlib

spec = importlib.util.spec_from_file_location('rl_installer', Path(__file__).resolve().parents[1] / 'binder/install_garmi_rl.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class SourceTests(unittest.TestCase):
    def test_bundled_source_is_valid(self):
        payload = Path(__file__).resolve().parents[1] / 'demos/garmi_rl'
        self.assertEqual(installer.verify_source(payload)['file_count'], 146)

    def test_tampered_artifact_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            for name in ('runtime.tar.gz', 'files.sha256.json'):
                (p / name).write_bytes(b'original')
            digest = hashlib.sha256(b'original').hexdigest()
            source = dict(repository='https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl',
                          commit='a' * 40, archive_sha256=digest, files_manifest_sha256=digest)
            (p / 'source.json').write_text(json.dumps(source))
            installer.verify_source(p)
            (p / 'runtime.tar.gz').write_bytes(b'changed')
            with self.assertRaises(ValueError):
                installer.verify_source(p)

    def test_mutable_branch_name_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'source.json').write_text(json.dumps(dict(
                repository='https://github.com/zhiyuan-gao/garmi-mobile-grasp-rl', commit='main')))
            with self.assertRaises(ValueError):
                installer.verify_source(p)


if __name__ == '__main__':
    unittest.main()
