"""Import supplied chapter 2 PCM WAV clips by authoritative dialogue ID."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import shutil
import sys
import wave

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build/deps'))
import yaml


def main():
    raw = (ROOT / 'script_ja/ch02.yaml').read_bytes()
    data = yaml.safe_load(raw.decode('utf-8'))
    dialogue = {e['id']: e for s in data['scenes'] for e in s['entries'] if e['type'] == 'dialogue'}
    manifest = json.loads((ROOT / 'voice/ch02_manifest.json').read_text(encoding='utf-8'))
    assert manifest['script_sha256'] == hashlib.sha256(raw).hexdigest(), 'Re-export stale recording manifest first'
    rows = {r['line_id']: r for r in manifest['lines']}
    files = []
    # Validate the whole delivery before copying any clip.
    for source in sorted((ROOT / 'voice').glob('*/ch02*.wav')):
        lid, speaker = source.stem, source.parent.name
        assert lid in dialogue and dialogue[lid]['speaker'] == speaker and speaker != 'qixing', source
        with wave.open(str(source), 'rb') as audio:
            assert audio.getcomptype() == 'NONE' and audio.getsampwidth() == 2, source
            frames = audio.getnframes()
            assert frames > 0 and len(audio.readframes(frames)) == frames * audio.getnchannels() * 2, source
            info = dict(codec='pcm_s16le', sample_rate=audio.getframerate(), channels=audio.getnchannels(), duration_seconds=round(frames / audio.getframerate(), 3))
        target = ROOT / 'game/audio/voice' / speaker / source.name
        files.append(dict(line_id=lid, character=speaker, source=source.relative_to(ROOT).as_posix(), output=target.relative_to(ROOT).as_posix(),
                          sha256=hashlib.sha256(source.read_bytes()).hexdigest(), bytes=source.stat().st_size,
                          spoken_sha256=rows[lid]['spoken_sha256'], **info))
    assert files, 'No supplied chapter 2 WAV files'
    for item in files:
        target = ROOT / item['output']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / item['source'], target)
        assert hashlib.sha256(target.read_bytes()).hexdigest() == item['sha256']
    imported = {item['line_id'] for item in files}
    report = dict(chapter_id='ch02', date='2026-10-05', revision=data['revision'], script_sha256=manifest['script_sha256'],
                  voice_lines=len(files), voice_by_character=dict(Counter(item['character'] for item in files)),
                  pending_lines=[dict(line_id=lid, character=e['speaker']) for lid, e in dialogue.items() if lid not in imported],
                  checks=['current_manifest_hash', 'dialogue_speaker_ids', 'pcm_16_bit_complete_frames', 'copied_file_hashes'],
                  audio_listened=False, runtime_tested=False, license_status='user_supplied_preview_model_licenses_not_verified', files=files)
    (ROOT / 'docs/reports/ch02_voice_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('voice_lines', 'voice_by_character', 'script_sha256')}, ensure_ascii=True))


if __name__ == '__main__':
    main()
