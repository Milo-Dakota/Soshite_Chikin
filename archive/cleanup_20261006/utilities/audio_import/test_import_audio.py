"""Isolated end-to-end checks with generated audio, never current game files."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
FFMPEG = json.loads((HERE / 'config.json').read_text(encoding='utf-8'))['ffmpeg']


class ImportAudioTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='audio-import-test-')
        self.root = Path(self.temp.name)
        for directory in ('audio/voice/maxi', 'audio/bgm', 'audio/ambience', 'audio/sfx', 'voice', 'script_ja'):
            (self.root / directory).mkdir(parents=True)
        raw = b'schema_version: 1\nchapter_id: ch02\n'
        (self.root / 'script_ja/ch02.yaml').write_bytes(raw)
        (self.root / 'voice/ch02_manifest.json').write_text(json.dumps(dict(chapter_id='ch02', script_sha256=hashlib.sha256(raw).hexdigest(),
            lines=[dict(line_id='ch02_sc01_016', character='maxi')])), encoding='utf-8')
        self.voice = self.root / 'audio/voice/maxi/ch02_sc01_016.wav'
        self.generate(self.voice)
        self.generate(self.root / 'audio/bgm/test.ogg')
        for category in ('sfx', 'ambience'):
            self.generate(self.root / f'audio/{category}/test.wav')

    def tearDown(self):
        self.temp.cleanup()

    def generate(self, path, volume='0.5'):
        subprocess.run([FFMPEG, '-v', 'error', '-nostdin', '-y', '-f', 'lavfi', '-i', 'sine=frequency=440:sample_rate=22050:duration=2',
                        '-af', f'volume={volume}', str(path)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    def invoke(self, *args):
        return subprocess.run([sys.executable, str(HERE / 'import_audio.py'), '--root', str(self.root), *args],
                              capture_output=True, text=True, encoding='utf-8', errors='replace')

    def report(self):
        return json.loads((self.root / 'docs/reports/audio_import.json').read_text(encoding='utf-8'))

    def test_real_processing_incremental_and_atomic_failures(self):
        originals = {p: p.read_bytes() for p in (self.root / 'audio').rglob('*') if p.is_file()}
        dry = self.invoke('--dry-run')
        self.assertEqual(dry.returncode, 0, dry.stderr)
        self.assertFalse((self.root / 'game').exists())
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stderr)
        report = self.report()
        self.assertEqual(report['counts'], dict(normalized=2, copied=2, skipped=0))
        for relative in ('bgm/test.ogg', 'voice/maxi/ch02_sc01_016.wav'):
            item = report['files'][relative]
            self.assertLessEqual(item['after']['input_tp'], -1.7)
            self.assertLess(abs(item['after']['input_i'] - item['requested_lufs']), 1.0)
            self.assertAlmostEqual(item['before']['duration_seconds'], item['after']['duration_seconds'], delta=0.15)
        for category in ('sfx', 'ambience'):
            self.assertEqual((self.root / f'audio/{category}/test.wav').read_bytes(), (self.root / f'game/audio/{category}/test.wav').read_bytes())
        for path, content in originals.items():
            self.assertEqual(path.read_bytes(), content)
        self.assertEqual(self.invoke().returncode, 0)
        self.assertEqual(self.report()['counts']['skipped'], 4)
        # Tampered runtime output is regenerated even with unchanged originals.
        destination = self.root / 'game/audio/voice/maxi/ch02_sc01_016.wav'
        destination.write_bytes(b'broken')
        self.assertEqual(self.invoke().returncode, 0)
        self.assertEqual(self.report()['counts'], dict(normalized=1, copied=0, skipped=3))
        # Source changes trigger only the affected output.
        self.generate(self.voice, '0.9')
        self.assertEqual(self.invoke().returncode, 0)
        self.assertEqual(self.report()['counts'], dict(normalized=1, copied=0, skipped=3))
        # Invalid input cannot replace the last working game clip.
        good_output = destination.read_bytes()
        self.voice.write_bytes(b'invalid audio')
        self.assertNotEqual(self.invoke().returncode, 0)
        self.assertEqual(destination.read_bytes(), good_output)

    def test_preflight_ids_and_format_collisions(self):
        self.voice.rename(self.voice.with_name('ch02_sc01_999.wav'))
        self.assertNotEqual(self.invoke().returncode, 0)
        self.assertFalse((self.root / 'game').exists())
        self.voice.with_name('ch02_sc01_999.wav').rename(self.voice)
        self.voice.with_suffix('.ogg').write_bytes(b'collision')
        self.assertNotEqual(self.invoke().returncode, 0)
        self.assertFalse((self.root / 'game').exists())


if __name__ == '__main__':
    unittest.main()
