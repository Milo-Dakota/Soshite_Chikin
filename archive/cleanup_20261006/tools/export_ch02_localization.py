"""Check chapter 2 localization mappings and export a bilingual reading copy.

Only the Japanese script and its translation are read. No game files are changed.
"""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build' / 'deps'))
import yaml


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def export():
    ja_raw = (ROOT / 'script_ja/ch02.yaml').read_bytes()
    zh_raw = (ROOT / 'script_zh/ch02.json').read_bytes()
    ja = yaml.safe_load(ja_raw.decode('utf-8'))
    zh = json.loads(zh_raw.decode('utf-8-sig'), object_pairs_hook=unique_object)
    ja_hash = hashlib.sha256(ja_raw).hexdigest()
    zh_hash = hashlib.sha256(zh_raw).hexdigest()
    require(ja['chapter_id'] == zh['chapter_id'] == 'ch02', 'Wrong chapter')
    require(zh['source_ja_sha256'].lower() == ja_hash, 'Translation source is stale')
    require(isinstance(zh.get('chapter_title_zh'), str) and zh['chapter_title_zh'].strip(), 'Missing chapter title')
    entries = [e for s in ja['scenes'] for e in s['entries'] if e['type'] != 'direction']
    source_ids = [e['id'] for e in entries]
    require(len(source_ids) == len(set(source_ids)), 'Duplicate source ID')
    require(isinstance(zh['lines'], dict), 'Expected lines mapping')
    require(set(source_ids) == set(zh['lines']),
            f'ID mismatch: missing={set(source_ids)-set(zh["lines"])} extra={set(zh["lines"])-set(source_ids)}')
    long_lines = []
    for lid, text in zh['lines'].items():
        require(isinstance(text, str) and text.strip() == text and text, f'{lid}: empty/padded translation')
        require(not any(c in text for c in '〖〗｜{}'), f'{lid}: display tags in Chinese')
        require(not re.search('[\u3040-\u30ff]', text), f'{lid}: untranslated kana')
        if len(text) > 70:
            long_lines.append({'line_id': lid, 'characters': len(text)})
    names = {
        'qixing': '徐启星', 'chinatsu': '千夏', 'maxi': '马皙', 'wengang': '文钢',
        'theatre_staff': '剧院工作人员', 'house_driver': '司机', 'beidai': '梅川备代',
        'house_servant': '佣人', 'unknown_caller': '电话里的声音', 'external': '外部行为视点',
    }
    types = {'dialogue': '对白', 'protagonist_dialogue': '对白·无配音',
             'thought': '内心·无配音', 'document_text': '书面文字·无配音'}
    md = [f'# 第二章双语阅读稿｜{zh["chapter_title_zh"]}', '',
          f'日语章名：{ja["title_ja"]}', '',
          '本稿从正式日语与中文文件生成，用于阅读核对；未接入游戏，不代表排版或整章验收通过。', '',
          '来源：`script_ja/ch02.yaml`、`script_zh/ch02.json`。修改时先改对应正式源，再重新导出。', '',
          f'日语 SHA-256：`{ja_hash}`', '', f'中文 SHA-256：`{zh_hash}`', '',
          '保留全部显示文本；演出备注不作为正文。Ruby 以台本标记保留在日语栏，中文不带该标记。', '']
    for scene in ja['scenes']:
        md += [f'## {scene["id"]}', '',
               f'场景类型：{scene["scene_kind"]}；叙事视点：{names[scene["narrative_pov"]]}。', '']
        for entry in scene['entries']:
            if entry['type'] == 'direction':
                continue
            speaker = names.get(entry.get('speaker'), '寻人启事')
            md += [f'### {entry["id"]}｜{speaker}｜{types[entry["type"]]}', '',
                   '日：' + entry['ja'], '', '中：' + zh['lines'][entry['id']], '']
    report = {
        'chapter_id': 'ch02', 'source_ja_sha256': ja_hash, 'translation_sha256': zh_hash,
        'scenes': len(ja['scenes']), 'translated_lines': len(entries),
        'text_counts': dict(Counter(e['type'] for e in entries)),
        'checks': ['json_parse', 'unique_json_keys', 'source_hash_binding', 'exact_id_coverage',
                   'nonempty_text', 'no_display_tags_or_kana', 'all_document_text_included'],
        'length_review_threshold': 70, 'long_lines_for_layout_review': long_lines,
        'not_checked': ['RenPy runtime', 'bilingual layout', 'font glyph coverage', 'voice playback'],
        'note': 'Structural check only. Translation and semantic review are performed in the isolated localization context.',
    }
    destination = ROOT / 'docs/ch02'
    destination.mkdir(exist_ok=True)
    (destination / 'ch02_bilingual_script.md').write_text('\n'.join(md), encoding='utf-8')
    (ROOT / 'docs/reports/ch02_localization_check.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True))


if __name__ == '__main__':
    export()
