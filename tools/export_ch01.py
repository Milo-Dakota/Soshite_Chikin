"""Export the current Japanese draft for human voice production; no game launch."""
from pathlib import Path
import csv
import hashlib
import json
import re
import sys
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (ROOT / output_folder).mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / '.build' / 'deps'))
import yaml

source = ROOT / 'scripts/ja' / 'ch01.yaml'
data = yaml.safe_load(source.read_text(encoding='utf-8'))
ruby = re.compile(r'〖([^〖〗｜]+)｜([^〖〗｜]+)〗')
ids = set()
rows = []
counts = Counter()
speakers = {'qixing', 'chinatsu', 'maxi', 'zheng', 'beidai'}
defaults = {
    'chinatsu': ('reserved', 'low', 'natural'),
    'maxi': ('casual', 'medium', 'natural'),
    'zheng': ('familiar', 'medium', 'measured'),
    'beidai': ('grandiose', 'medium', 'ceremonial'),
}
for scene in data['scenes']:
    assert scene['id'] not in ids
    ids.add(scene['id'])
    for entry in scene['entries']:
        line_id = entry['id']
        assert line_id not in ids, f'Duplicate: {line_id}'
        ids.add(line_id)
        if entry['type'] == 'direction':
            assert entry.get('action')
            continue
        assert entry['speaker'] in speakers
        assert entry['type'] in {'dialogue', 'protagonist_dialogue', 'thought'}
        text = entry['ja']
        assert text.strip()
        spoken = entry.get('ja_spoken') or ruby.sub(lambda m: m[2], text)
        assert not any(c in spoken for c in '〖〗｜'), line_id
        counts[entry['type']] += 1
        if entry['type'] == 'thought':
            assert entry['speaker'] == scene['narrative_pov'], line_id
        if entry['type'] == 'protagonist_dialogue':
            assert entry['speaker'] == 'qixing'
        if entry['type'] != 'dialogue':
            continue
        speaker = entry['speaker']
        assert speaker != 'qixing'
        emotion, intensity, pace = defaults[speaker]
        performance = entry.get('performance', {})
        row = {
            'line_id': line_id,
            'scene_id': scene['id'],
            'character': speaker,
            'ja_display': text,
            'ja_spoken': spoken,
            'emotion': performance.get('emotion', emotion),
            'intensity': performance.get('intensity', intensity),
            'pace': performance.get('pace', pace),
            'performance_note': performance.get('note', ''),
            'output_path': f'audio/voice/{speaker}/{line_id}.ogg',
            'spoken_sha256': hashlib.sha256(spoken.encode('utf-8')).hexdigest(),
            'status': 'ready_for_recording' if data['status'] == 'demo_reviewed' else 'draft_for_review',
        }
        rows.append(row)
output = ROOT / '.build/exports'
output.mkdir(parents=True, exist_ok=True)
with (output / 'ch01_manifest.csv').open('w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
payload = {
    'chapter_id': 'ch01', 'script_status': data['status'],
    'script_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'note': 'Japanese demo text reviewed. User produces voice; use ja_spoken and output_path.' if data['status'] == 'demo_reviewed' else 'Japanese only. Review the draft before recording.',
    'lines': rows,
}
(output / 'ch01_manifest.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
recording = ['# 第一章日语录音台本', '', '只朗读下列正文。每条单独输出真实 Ogg Vorbis 文件；路径相对于项目根目录。',
             '徐启星及所有内心均不配音。角色姓名的特殊读法已转换。', '',
             '台本 SHA-256：`' + payload['script_sha256'] + '`', '']
for character, name in [('chinatsu', '千夏'), ('maxi', '马皙'), ('zheng', '郑局'), ('beidai', '梅川备代')]:
    recording += ['## ' + name, '']
    for row in rows:
        if row['character'] != character:
            continue
        recording += ['### ' + row['line_id'], '', row['ja_spoken'], '',
                      '演技：' + ' / '.join([row['emotion'], row['intensity'], row['pace']]) + '。' + row['performance_note'], '',
                      '保存为：`' + row['output_path'] + '`', '']
(output / 'ch01_recording.md').write_text('\n'.join(recording), encoding='utf-8')
summary = {
    'script_sha256': payload['script_sha256'],
    'scenes': len(data['scenes']), 'text_counts': dict(counts),
    'voice_lines': len(rows), 'voice_by_character': dict(Counter(r['character'] for r in rows)),
    'checks': ['yaml_parse', 'unique_ids', 'known_speakers', 'thought_pov', 'protagonist_unvoiced', 'ruby_spoken'],
    'not_checked': ['RenPy runtime', 'layout', 'save/load', 'voice audio', 'asset integration'],
}
(ROOT / '.build' / 'reports' / 'ch01_static_check.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=True))
