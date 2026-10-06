"""Validate the Japanese chapter and export its voiced lines, without touching game files."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
for output_folder in ('.build/reports', '.build/exports'):
    (ROOT / output_folder).mkdir(parents=True, exist_ok=True)
import yaml

SOURCE = ROOT / 'scripts/ja' / 'ch02.yaml'
RUBY = re.compile(r'〖([^〖〗｜]+)｜([^〖〗｜]+)〗')
NAMES = {
    'chinatsu': '千夏', 'maxi': '马皙', 'wengang': '文钢',
    'theatre_staff': '剧院工作人员', 'house_driver': '梅川家司机',
    'beidai': '梅川备代', 'house_servant': '梅川家佣人',
    'unknown_caller': '身份不明的来电者',
}
SPEAKERS = {'qixing', *NAMES}
EXPECTED_POV = [('main', 'qixing')] * 5 + [
    ('side_scene', 'chinatsu'), ('side_scene', 'chinatsu'),
    ('side_scene', 'external'), ('main', 'qixing'),
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_ruby(text, line_id):
    require(isinstance(text, str) and bool(text.strip()), f'{line_id}: empty text')
    stripped = RUBY.sub(lambda match: match[1], text)
    require(not any(c in stripped for c in '〖〗｜'), f'{line_id}: invalid ruby')


def export():
    raw = SOURCE.read_bytes()
    data = yaml.safe_load(raw.decode('utf-8'))
    require(data['schema_version'] == 1 and data['chapter_id'] == 'ch02', 'Wrong chapter schema')
    require(len(data['scenes']) == 9, 'Expected nine scenes')
    extension = data['text_type_extensions']['document_text']
    require(extension['display'] is True and extension['voiced'] is False, 'Document text contract')
    digest = hashlib.sha256(raw).hexdigest()
    ids, counts, rows = set(), Counter(), []
    scene_counts = []
    documents = []
    for number, (scene, expected) in enumerate(zip(data['scenes'], EXPECTED_POV), 1):
        sid = scene['id']
        require(sid == f'ch02_sc{number:02d}' and sid not in ids, f'Unexpected scene {sid}')
        ids.add(sid)
        require((scene['scene_kind'], scene['narrative_pov']) == expected, f'{sid}: wrong POV')
        require(scene.get('location') and scene.get('time') and scene.get('entries'), f'{sid}: missing fields')
        local_counts = Counter()
        for entry in scene['entries']:
            lid, kind = entry['id'], entry['type']
            require(lid not in ids, f'Duplicate ID: {lid}')
            ids.add(lid)
            is_direction = kind == 'direction'
            suffix = r'dir\d{3}' if is_direction else r'\d{3}'
            require(re.fullmatch(re.escape(sid) + '_' + suffix, lid), f'{lid}: ID namespace')
            counts[kind] += 1
            local_counts[kind] += 1
            if is_direction:
                require(entry.get('action'), f'{lid}: missing action')
                require('ja' not in entry and 'speaker' not in entry, f'{lid}: direction carries dialogue')
                if 'label_ja' in entry:
                    check_ruby(entry['label_ja'], lid)
                continue
            require(kind in {'dialogue', 'protagonist_dialogue', 'thought', 'document_text'}, f'{lid}: unknown type')
            check_ruby(entry.get('ja'), lid)
            if kind == 'document_text':
                require(sid == 'ch02_sc01' and entry.get('source_kind') == 'missing_person_notice', f'{lid}: document source')
                require(entry.get('author') == 'beidai' and 'speaker' not in entry, f'{lid}: document author/speaker')
                require('ja_spoken' not in entry and not entry.get('voice'), f'{lid}: document must be unvoiced')
                documents.append(lid)
                continue
            speaker = entry.get('speaker')
            require(speaker in SPEAKERS, f'{lid}: unknown speaker')
            if kind == 'thought':
                require(speaker == scene['narrative_pov'] and speaker != 'external', f'{lid}: thought POV')
            if kind == 'protagonist_dialogue':
                require(speaker == 'qixing', f'{lid}: protagonist speaker')
            if kind != 'dialogue':
                require('ja_spoken' not in entry and not entry.get('voice'), f'{lid}: unvoiced text has voice')
                continue
            require(speaker != 'qixing', f'{lid}: protagonist must be silent')
            spoken = entry.get('ja_spoken', RUBY.sub(lambda match: match[2], entry['ja']))
            require(spoken.strip() and not any(c in spoken for c in '〖〗｜'), f'{lid}: invalid spoken text')
            for name in ('徐启星', '梅川', '備代', '艾昆', '文鋼', '馬皙', '千夏'):
                require(name not in spoken, f'{lid}: unresolved name reading {name}')
            derived = RUBY.sub(lambda match: match[2], entry['ja']).replace('千夏', 'ちなつ')
            require(spoken == derived.replace('『', '').replace('』', '') or spoken == derived,
                    f'{lid}: spoken text differs beyond declared readings and display quotes')
            performance = entry.get('performance', {})
            require(all(performance.get(k) for k in ('emotion', 'intensity', 'pace', 'note')), f'{lid}: incomplete performance')
            rows.append({
                'line_id': lid, 'scene_id': sid, 'character': speaker,
                'ja_display': entry['ja'], 'ja_spoken': spoken,
                'emotion': performance['emotion'], 'intensity': performance['intensity'],
                'pace': performance['pace'], 'performance_note': performance['note'],
                'output_path': f'audio/voice/{speaker}/{lid}' + ('.wav' if (ROOT / 'audio/voice' / speaker / (lid + '.wav')).is_file() else '.ogg'),
                'spoken_sha256': hashlib.sha256(spoken.encode('utf-8')).hexdigest(),
            })
        scene_counts.append({'scene_id': sid, 'counts': dict(local_counts)})
    require(len(documents) == 4, 'Missing notice text')
    require(len(rows) == counts['dialogue'], 'Voice selection mismatch')
    require(all(row['character'] != 'qixing' for row in rows), 'Protagonist in voice export')
    by_character = Counter(row['character'] for row in rows)
    md = [
        '# 第二章日语录音台本', '',
        '章节：消えた首席と星の救難信号。以下只导出需要配音的日语对白，没有中文译文。', '',
        '只朗读每条的“朗读正文”。角色名、编号、场次、演技说明与路径均不朗读。每条单独输出 Ogg Vorbis 或未压缩 16 位 PCM WAV 文件，勿只修改文件后缀。', '',
        '徐启星全部文字、千夏及其他人物的内心、寻人启事、视点提示和演出指令均不配音。Ruby 已转换为读音；对白里的“パパ”属于台词，不是说话者标记。', '',
        '本稿按角色分组，组内按出场顺序排列。第一章同角色沿用既有声音；电话效果在接入时处理，录音保持干净。琴房段落表现控制、拒绝和恐惧，不加入亲吻、情色喘息或身体接触音。', '',
        f'来源：`scripts/ja/ch02.yaml`，revision {data["revision"]}。本稿仅列录音文字；章节完成状态见 `docs/status.md`。', '',
        f'台本 SHA-256：`{digest}`', '',
        f'配音共 **{len(rows)} 条**。输出路径相对于项目根目录；保持 Line ID 不变。', '',
        '| 角色 | ID | 条数 |', '|---|---|---:|',
    ]
    for character, name in NAMES.items():
        md.append(f'| {name} | `{character}` | {by_character[character]} |')
    md += ['', '修改台词或读法后，先更新正式台本，再重新导出本稿；不要单独改本稿造成文字源分叉。', '']
    for character, name in NAMES.items():
        md += [f'## {name}（{character}）', '']
        for row in rows:
            if row['character'] != character:
                continue
            md += [
                f'### {row["line_id"]}', '', f'场次：`{row["scene_id"]}`', '',
                '**朗读正文**', '', row['ja_spoken'], '',
                '演技：' + ' / '.join(row[k] for k in ('emotion', 'intensity', 'pace')) + '。' + row['performance_note'], '',
                f'保存为：`{row["output_path"]}`', '',
            ]
    recording = '\n'.join(md)
    exported_ids = re.findall(r'^### (ch02_sc\d{2}_\d{3})$', recording, re.M)
    require(len(exported_ids) == len(rows) and set(exported_ids) == {r['line_id'] for r in rows}, 'Markdown line coverage')
    require(not any(c in recording for c in '〖〗｜'), 'Display markup leaked to recording')
    payload = {'chapter_id': 'ch02', 'revision': data['revision'],
               'script_sha256': digest, 'lines': rows}
    summary = {
        'chapter_id': 'ch02', 'script_sha256': digest, 'scenes': 9,
        'text_counts': {k: v for k, v in counts.items() if k != 'direction'},
        'directions': counts['direction'], 'voice_lines': len(rows),
        'voice_by_character': dict(by_character), 'scene_counts': scene_counts,
        'document_text_ids': documents,
        'checks': ['yaml_parse', 'required_fields', 'unique_ids', 'id_namespaces',
                   'scene_pov', 'known_speakers', 'thought_pov', 'protagonist_unvoiced',
                   'documents_unvoiced', 'ruby_pairs', 'spoken_name_readings',
                   'performance_fields', 'markdown_voice_coverage'],
        'not_checked': ['RenPy runtime', 'bilingual layout', 'voice audio', 'image assets', 'localization'],
    }
    output = ROOT / '.build/exports'
    output.mkdir(parents=True, exist_ok=True)
    if '--recording' in sys.argv:
        (output / 'ch02_recording.md').write_text(recording, encoding='utf-8')
    (output / 'ch02_manifest.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    reports = ROOT / '.build' / 'reports'
    reports.mkdir(parents=True, exist_ok=True)
    (reports / 'ch02_static_check.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in summary.items() if k not in {'scene_counts', 'document_text_ids'}}, ensure_ascii=True))


if __name__ == '__main__':
    export()
