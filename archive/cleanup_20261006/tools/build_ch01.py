"""Build only Chapter 1 from validated Japanese source. Does not launch Ren'Py."""
from pathlib import Path
import hashlib
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
exported = runpy.run_path(str(ROOT / 'tools/export_ch01.py'))
data = exported['data']
ruby = exported['ruby']
source_hash = hashlib.sha256(exported['source'].read_bytes()).hexdigest()
translation_path = ROOT / 'script_zh/ch01.json'
translation = json.loads(translation_path.read_text(encoding='utf-8-sig'))
assert translation['chapter_id'] == data['chapter_id']
assert translation['source_ja_sha256'].lower() == source_hash, 'Chinese translation needs Japanese source review'
expected_ids = {e['id'] for s in data['scenes'] for e in s['entries'] if e['type'] != 'direction'}
assert set(translation['lines']) == expected_ids, 'Missing or stale Chinese line IDs'
assert all(isinstance(t, str) and t.strip() and not any(c in t for c in '{}〖〗\n')
           for t in translation['lines'].values()), 'Chinese must be nonempty plain text'
translation_hash = hashlib.sha256(translation_path.read_bytes()).hexdigest()

# Explicit staging for every direction; no unhandled instruction is silently dropped.
# Text always comes from YAML. Compact gesture approximations are tracked in handoff.
staging = {}
def stage(scene, number, commands):
    staging[f'ch01_sc{scene:02}_dir{number:03}'] = commands.strip().splitlines()

stage(1, 1, '''scene ch_bg street
show ch_qixing neutral at ch_left
with Dissolve(0.6)
$ ch_audio("daily")
$ ch_audio("street_room")''')
stage(1, 2, '''scene ch_cg sleeve
with dissolve''')
stage(1, 3, '''window hide
scene ch_cg bread
with dissolve
pause 1.2''')
stage(1, 4, '''window hide
scene ch_bg street
show ch_qixing neutral at ch_left
with dissolve
pause 0.5''')

stage(2, 1, '''$ ch_audio("gym_room")
scene ch_bg locker
with fade''')
stage(2, 2, '''window hide
scene ch_cg shower
with dissolve
$ ch_audio("shower")
pause 0.6''')
stage(2, 3, '''$ ch_audio("gym_room")
scene ch_bg locker
show ch_qixing neutral at ch_left
show ch_maxi neutral at ch_maxi_position(1690)
with fade''')
stage(2, 4, '''$ ch_audio("phone")
show screen ch_phone("鄭局長", True)
with dissolve''')
stage(2, 5, 'pause 0.5')
stage(2, 6, '''stop music fadeout 1.0
show ch_qixing troubled at ch_left
show ch_maxi concerned at ch_maxi_position(1690)
with Dissolve(0.2)
pause 0.7''')
stage(2, 7, '''hide screen ch_phone
with dissolve''')
stage(2, 8, '''hide ch_maxi
with dissolve
pause 0.5''')

stage(3, 1, '''$ ch_stop_audio()
call ch_card("ch01_interlude") from ch01_interlude_return
scene ch_bg locker_empty
show ch_maxi enthusiastic at ch_maxi_position(320)
with Dissolve(0.6)
$ ch_audio("gym_room")''')
stage(3, 2, '''window hide
hide ch_maxi
with dissolve
pause 0.9
show ch_maxi annoyed at ch_maxi_position(320)
with dissolve''')

stage(4, 1, '''call ch_card("ch01_walk") from ch01_walk_return
scene ch_bg street
show ch_qixing troubled at ch_left
show screen ch_phone("父さん")
with Dissolve(0.6)
$ ch_audio("street_room")''')
stage(4, 2, '''hide screen ch_phone
scene ch_cg water
with dissolve''')
stage(4, 3, 'pause 0.5')
stage(4, 4, 'pause 0.7')
stage(4, 5, '''window hide
scene ch_cg support
with dissolve
$ ch_audio("warm")
pause 0.6''')
stage(4, 6, '''scene ch_bg street
show ch_qixing neutral at ch_left
show ch_chinatsu embarrassed at ch_right
with dissolve
pause 0.5''')

stage(5, 1, '''scene ch_cg table
with fade
$ ch_audio("daily")
$ ch_audio("restaurant_room")''')
stage(5, 2, '''scene ch_bg restaurant
show ch_qixing neutral at ch_seated_left
show ch_chinatsu smile at ch_seated_right
with dissolve
pause 0.5
show ch_chinatsu guarded at ch_seated_right
with dissolve''')
stage(5, 3, '''scene ch_cg two_fingers
with dissolve
pause 0.4''')
stage(5, 4, '''window hide
scene ch_cg violin
with dissolve
pause 0.8''')
stage(5, 5, '''stop music fadeout 0.8
scene ch_cg car
with dissolve
pause 0.8''')
stage(5, 6, '''window hide
$ ch_audio("door")
scene ch_bg restaurant_public
show ch_beidai bow at ch_beidai_public
with Dissolve(0.6)
pause 5.0
stop sound fadeout 0.15''')
stage(5, 7, '''window hide
scene ch_cg recital
with dissolve
$ ch_audio("recital")
$ renpy.music.set_volume(0.35, delay=0.5, channel="ch_ambience")
if renpy.loadable(CH_AUDIO["recital"][0]):
    show screen ch_recital_hint
    pause 18.0
else:
    pause 2.0
hide screen ch_recital_hint
with None
stop music fadeout 1.3
$ renpy.music.set_volume(1.0, delay=0.8, channel="ch_ambience")
scene ch_bg restaurant_public
show ch_beidai bow at ch_beidai_public
with dissolve
pause 1.0
scene ch_bg restaurant
show ch_qixing bemused at ch_seated_left
show ch_chinatsu afraid at ch_seated_right
with Dissolve(0.5)
$ ch_audio("door")
pause 5.0
stop sound fadeout 0.15''')
stage(5, 8, '''show ch_qixing neutral at ch_seated_left
show ch_chinatsu guarded at ch_seated_right
with dissolve
$ ch_audio("warm")''')
stage(5, 9, '''window hide
scene ch_bg restaurant_empty
with dissolve
pause 1.0
show ch_qixing neutral at ch_seated_left
show ch_chinatsu smile at ch_seated_right
with dissolve''')
stage(5, 10, '''show ch_qixing serious at ch_seated_left
with Dissolve(0.2)
pause 0.5''')
stage(5, 11, '''show ch_chinatsu guarded at ch_seated_right
with dissolve
pause 0.4''')
stage(5, 12, '''show ch_chinatsu surprised at ch_seated_right
with Dissolve(0.2)
pause 0.6''')

stage(6, 1, '''scene ch_bg street
show ch_qixing neutral at ch_left
show ch_chinatsu smile at ch_right
with fade
$ ch_audio("warm")
$ ch_audio("street_room")''')
stage(6, 2, '''scene ch_cg walk
with dissolve
pause 0.5''')
stage(6, 3, '''window hide
pause 1.0
$ ch_stop_audio()
scene black
with fade
call ch_card("ch01_ending") from ch01_ending_return''')

# Line-specific cues refine the matching direction without duplicating Japanese text.
before = {
    'ch01_sc01_012': ['scene ch_bg street', 'show ch_qixing serious at ch_left', 'with dissolve'],
    'ch01_sc02_011': ['stop sound', 'hide screen ch_phone', 'with dissolve'],
    'ch01_sc05_019': ['scene ch_bg restaurant', 'show ch_qixing neutral at ch_seated_left',
                       'show ch_chinatsu afraid at ch_seated_right', 'with dissolve'],
    'ch01_sc06_005': ['scene ch_bg street', 'show ch_qixing surprised at ch_left',
                       'show ch_chinatsu smile at ch_right', 'with dissolve'],
}
# Facial acting at topic changes. Existing CG shots retain their composition.
# These cues never introduce a hidden sprite on top of a CG.
expression_cues = {
    'ch01_sc02_008': ['show ch_maxi enthusiastic at ch_maxi_position(1690)'],
    'ch01_sc02_010': ['show ch_qixing bemused at ch_left',
                      'show ch_maxi neutral at ch_maxi_position(1690)'],
    'ch01_sc04_014': ['show ch_chinatsu downcast at ch_right',
                      'show ch_qixing serious at ch_left'],
    'ch01_sc04_018': ['show ch_qixing soft at ch_left'],
    'ch01_sc05_007': ['show ch_qixing bemused at ch_seated_left'],
    'ch01_sc05_010': ['show ch_chinatsu downcast at ch_seated_right',
                      'show ch_qixing serious at ch_seated_left'],
    'ch01_sc05_020': ['show ch_qixing bemused at ch_seated_left'],
    'ch01_sc05_024': ['show ch_qixing serious at ch_seated_left'],
    'ch01_sc05_030': ['show ch_qixing soft at ch_seated_left'],
    'ch01_sc05_031': ['show ch_qixing bemused at ch_seated_left'],
    'ch01_sc05_032': ['show ch_qixing soft at ch_seated_left'],
    'ch01_sc05_035': ['show ch_qixing soft at ch_seated_left'],
    'ch01_sc05_036': ['show ch_chinatsu smile at ch_seated_right'],
}
for line_id, commands in expression_cues.items():
    before.setdefault(line_id, []).extend(commands + ['with Dissolve(0.2)'])
destination = ROOT / 'game/scripts/ch01'
destination.mkdir(parents=True, exist_ok=True)
used = set()
all_lines = []
voice_lines = []
def quote(text):
    return json.dumps(text, ensure_ascii=False)

def stage_lines(commands):
    # Dialogue remains visible during pauses and expression changes. Hide it
    # only for an actual shot change or an explicit clean-image performance.
    result = []
    for command in commands:
        if command.startswith('scene '):
            result.append('    window hide None')
        result.append('    ' + command)
    return result

for scene in data['scenes']:
    lines = [f'# Generated from script_ja/ch01.yaml SHA256 {source_hash}',
             f'# Chinese source script_zh/ch01.json SHA256 {translation_hash}',
             '# Edit Japanese text in YAML; staging in tools/build_ch01.py.', '',
             f"label {scene['id']}:"]
    for entry in scene['entries']:
        line_id = entry['id']
        lines += [f'    # {line_id}']
        if entry['type'] == 'direction':
            assert line_id in staging, f'Unhandled direction: {line_id}'
            used.add(line_id)
            lines += ['    $ ch_voice(None, "")']
            lines += stage_lines(staging[line_id])
        else:
            all_lines.append(line_id)
            lines += stage_lines(before.get(line_id, []))
            character = 'ch_thought' if entry['type'] == 'thought' else 'ch_' + entry['speaker']
            if entry.get('display_name') == '少女':
                character = 'ch_girl'
            voice = entry['speaker'] if entry['type'] == 'dialogue' else None
            if voice:
                voice_lines.append(line_id)
            text = entry['ja'].replace('[', '[[')
            text = ruby.sub(lambda m: '{rb}' + m[1] + '{/rb}{rt}' + m[2] + '{/rt}', text)
            assert not any(c in text for c in '〖〗｜'), line_id
            chinese = translation['lines'][line_id].replace('[', '[[')
            # Native what is Chinese in full; Japanese is a screen argument.
            # Ren'Py snapshots show arguments in each HistoryEntry for history.
            text = '{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}' + text + '{/font}{/color}{/size}'
            lines += ['    window show None', f'    $ ch_line_id = {quote(line_id)}',
                      f'    $ ch_voice({repr(voice)}, {quote(line_id)})',
                      f'    {character} {quote(chinese)} (show_ja_text={quote(text)}) id {line_id}']
        lines += ['']
    lines += ['    return', '']
    (destination / (scene['id'].split('_')[1] + '.rpy')).write_text('\n'.join(lines), encoding='utf-8')
reading = ['# 第一章：' + translation['chapter_title_zh'], '',
           '中文主字幕 / 日语副字幕。中文仅依据日语台本及译名指南制作；配音仍使用既有日语清单。', '',
           '日语源 SHA-256：`' + source_hash + '`', '',
           '中文源 SHA-256：`' + translation_hash + '`', '']
for scene in data['scenes']:
    reading += ['## ' + scene['id'], '']
    for entry in scene['entries']:
        if entry['type'] == 'direction':
            continue
        reading += ['### ' + entry['id'] + ' · ' + entry['speaker'], '',
                    translation['lines'][entry['id']], '', entry['ja'], '']
(ROOT / 'docs/ch01/ch01_bilingual_script.md').write_text('\n'.join(reading), encoding='utf-8')
assert used == set(staging), 'Staging contains a stale direction ID'
assert set(voice_lines) == {r['line_id'] for r in exported['rows']}
entrypoint = ['# Chapter 1 entry. Generated by tools/build_ch01.py.', 'label start:',
              '    $ ch_chapter_label = "第一章"',
              '    $ ch_stop_audio()', '    call ch_card("ch01_title") from ch01_title_return']
entrypoint += [f"    call {scene['id']} from entry_{scene['id']}_return" for scene in data['scenes']]
entrypoint += ['    $ ch_stop_audio()', '    call ch02_start from entry_ch02_return', '    return', '']
(ROOT / 'game/script.rpy').write_text('\n'.join(entrypoint), encoding='utf-8')
report = {'script_sha256': source_hash, 'scenes': len(data['scenes']), 'texts': len(all_lines),
          'translation_sha256': translation_hash, 'translated_lines': len(translation['lines']),
          'subtitle_order': ['zh_primary', 'ja_secondary'],
          'directions': len(used), 'voice_lines': len(voice_lines),
          'checks': ['all_directions_mapped', 'stable_say_ids', 'voice_manifest_match', 'ruby_conversion'],
          'runtime_tested': False, 'runtime_owner': 'user'}
(ROOT / 'docs/reports/ch01_build_check.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report))
