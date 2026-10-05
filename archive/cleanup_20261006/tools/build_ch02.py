"""Build chapter 2 backgrounds, bilingual subtitles and approved props.

Authoritative text stays in YAML/JSON. Approved baseline sprites are active;
Approved visuals and audio are active; supplied voice files are optional.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build/deps'))
import yaml
from ch02_prop_staging import configure as configure_props, build_runtime as build_props
from ch02_sprite_staging import configure as configure_sprites, build_runtime as build_sprites
from ch02_cg_staging import configure as configure_cg, build_runtime as build_cg
from ch02_expression_staging import configure as configure_expressions, build_runtime as build_expressions, LINE_CUES
from ch02_audio_staging import configure as configure_audio, LINE_CUES as AUDIO_LINE_CUES

RUBY = re.compile(r'〖([^〖〗｜]+)｜([^〖〗｜]+)〗')
NAMES = {'wengang': '文钢', 'theatre_staff': '剧院工作人员',
         'house_driver': '司机', 'house_servant': '佣人', 'unknown_caller': '电话里的声音'}
STAGING = {}
DEFERRED = {}


def stage(scene, number, commands='', deferred=''):
    key = f'ch02_sc{scene:02}_dir{number:03}'
    STAGING[key] = commands.strip().splitlines() if commands.strip() else ['pass']
    DEFERRED.pop(key, None)
    if deferred:
        DEFERRED[key] = deferred


def shot(name, transition='dissolve'):
    return f'window hide None\nscene ch02_bg {name}\nwith {transition}'


def card(suffix):
    return f'call ch_card("ch02_{suffix}") from ch02_{suffix}_return'


stage(1, 1, shot('living'), '人物、电视节目与所有声音暂缓。')
stage(1, 2, deferred='电视演奏 CG 与人物表情暂缓。')
stage(1, 3, deferred='启星动作暂缓。')
stage(1, 4, shot('street_day'), '寻人启事覆盖层暂缓；四条书面文字全部保留。')
stage(1, 5, deferred='手机图形和铃声暂缓，电话对白正常显示。')
stage(1, 6, 'pause 0.3', '挂断动作暂缓。')
stage(2, 1, shot('entry', 'fade') + '\npause 0.5\n' + shot('living'), '人物和电视声音暂缓。')
for n, reason in [(2, '淤青特写暂缓。'), (3, '抓手与抽回 CG 暂缓。'), (4, '人物动作暂缓。')]:
    stage(2, n, 'window hide None\nscene black\nwith fade' if n == 4 else '', reason)
stage(3, 1, card('morning') + '\n' + shot('street_day'), '启事撤除层暂缓。')
stage(3, 2, deferred='手机通知图形暂缓。')
stage(3, 3, shot('entry'), '鞋子有／无差分暂缓；保留空玄关。')
stage(3, 4, shot('street_day') + '\npause 0.4\n' + shot('living'), '撤除痕迹及人物呼吸演出暂缓。')
stage(3, 5, 'window hide None\nscene black\nwith fade', '人物离场和门声暂缓。')
stage(4, 1, shot('office', 'fade'))
stage(4, 2, deferred='落座和人物动作暂缓。')
stage(4, 3, 'window hide None\nscene black\nwith dissolve\npause 0.3\n' + shot('office'))
stage(4, 4, deferred='文件与手部 CG 暂缓。')
stage(4, 5, 'pause 0.3', '手部动作暂缓。')
stage(4, 6, 'window hide None\nscene black\nwith fade', '人物奔离和门声暂缓。')
stage(5, 1, shot('theatre_exterior', 'fade'))
stage(5, 2, shot('theatre_performance'), '画内合奏及所有音频暂缓。')
stage(5, 3, deferred='人物视线动作暂缓，保留乐团背景。')
stage(5, 4, shot('theatre_intermission'), '工作人员及音频暂缓；只移除乐团层。')
stage(5, 5, shot('theatre_side'), '递券 CG 和票面暂缓。')
stage(5, 6, deferred='马皙表情暂缓。')
stage(5, 7, shot('theatre_exterior', 'fade'), '离席人物动作和音频暂缓。')
stage(5, 8, 'pause 0.5')
stage(6, 1, card('chinatsu_home'), '车内 CG 未制作，此句在黑底显示，不能用宅外冒充车内。')
stage(6, 2, shot('mansion') + '\npause 0.7\n' + shot('foyer'), '礼宾车与佣人暂缓。')
stage(6, 3, deferred='迎接双人 CG 暂缓。')
stage(6, 4, shot('corridor'), '人物动作及音频暂缓。')
stage(6, 5, deferred='人物脚步画面暂缓，保留走廊背景。')
stage(6, 6, shot('restaurant'), '只复用餐厅背景，不接入人物 CG。')
stage(6, 7, shot('bathroom'), '水声暂缓。')
stage(6, 8, deferred='哭声暂缓，求救对白以双语显示。')
stage(6, 9, 'window hide None\nscene black\nwith fade')
stage(7, 1, card('chinatsu_piano') + '\n' + shot('piano'), '礼服人物暂缓。')
stage(7, 2, deferred='人物立绘暂缓，保留琴房空间。')
for n, reason in [(3, '坐姿与佣人退出暂缓。'), (4, '强制转身 CG 暂缓。'), (5, '推拒动作暂缓。'),
                  (6, '人物接触不出图，本轮保持无人琴房；事实由原有内心文字说明。'),
                  (7, '人物表情与起身暂缓。'), (8, '背带及发型差分暂缓。'),
                  (9, '火焰记忆 CG 暂缓，不拿宅邸背景当母亲死亡画面。'), (10, '突然起身 CG 暂缓。')]:
    stage(7, n, deferred=reason)
stage(7, 11, 'window hide None\nscene black\nwith fade')
stage(8, 1, card('phone') + '\n' + shot('phone_dusk'), '外部行为视点；电话及人物层暂缓。')
stage(8, 2, deferred='接电话动作暂缓。')
stage(8, 3, 'pause 0.7')
stage(8, 4, deferred='后退与挥退佣人的动作暂缓。')
stage(8, 5, 'window hide None\nscene black\nwith Dissolve(0.8)')
stage(9, 1, card('qixing_night') + '\n' + shot('night'))
stage(9, 2, shot('sky'))
stage(9, 3, deferred='揉眼与目标星独立图层暂缓。')
stage(9, 4, deferred='HELP 精确星光闪烁暂缓，解码台词全部显示。')
stage(9, 5, deferred='89N64W 精确星光闪烁暂缓，坐标台词全部显示。')
stage(9, 6, deferred='淤青回忆 CG 暂缓；不使用启星未亲历的幕间画面。')
stage(9, 7, 'window hide None\npause 0.5\nscene black\nwith fade\n' + card('ending'))

configure_props(stage, shot)
configure_sprites(STAGING, DEFERRED)
configure_cg(stage, shot)
configure_expressions(stage, shot)
configure_audio(STAGING, DEFERRED)

BACKGROUNDS = {
    'living': 'qixing_living_morning_v1', 'entry': 'qixing_entry_morning_v1',
    'office': 'police_office_day_v1', 'theatre_exterior': 'theatre_exterior_day_v1',
    'theatre_intermission': 'theatre_hall_intermission_v1', 'theatre_side': 'theatre_audience_side_v1',
    'mansion': 'umekawa_exterior_v1', 'foyer': 'umekawa_foyer_v1',
    'corridor': 'umekawa_corridor_v1', 'bathroom': 'umekawa_bathroom_v1',
    'piano': 'umekawa_piano_room_v1', 'phone_dusk': 'umekawa_phone_dusk_v1',
    'night': 'street_night_v1', 'sky': 'starry_sky_v1',
}


def quote(text):
    return json.dumps(text, ensure_ascii=False)


def build():
    ja_path, zh_path = ROOT / 'script_ja/ch02.yaml', ROOT / 'script_zh/ch02.json'
    ja_hash = hashlib.sha256(ja_path.read_bytes()).hexdigest()
    zh_hash = hashlib.sha256(zh_path.read_bytes()).hexdigest()
    data = yaml.safe_load(ja_path.read_text(encoding='utf-8'))
    zh = json.loads(zh_path.read_text(encoding='utf-8-sig'))
    assert data['chapter_id'] == zh['chapter_id'] == 'ch02'
    assert zh['source_ja_sha256'] == ja_hash, 'Stale translation'
    entries = [e for s in data['scenes'] for e in s['entries']]
    assert len({e['id'] for e in entries}) == len(entries), 'Duplicate IDs'
    texts = [e for e in entries if e['type'] != 'direction']
    assert set(zh['lines']) == {e['id'] for e in texts}, 'Translation coverage'
    assert set(STAGING) == {e['id'] for e in entries if e['type'] == 'direction'}, 'Direction coverage'
    dest = ROOT / 'game/scripts/ch02'
    dest.mkdir(parents=True, exist_ok=True)
    for s in data['scenes']:
        lines = [f'# Generated by tools/build_ch02.py; JA SHA256 {ja_hash}',
                 f'# ZH SHA256 {zh_hash}', '# Approved visual staging and audio; supplied voices are optional.',
                 f'label {s["id"]}:', f'    $ ch02_audio_scene("{s["id"]}")']
        for e in s['entries']:
            lid = e['id']
            lines += ['', f'    # {lid}']
            if e['type'] == 'direction':
                if lid in DEFERRED:
                    lines += ['    # Deferred: ' + DEFERRED[lid]]
                lines += ['    ' + c for c in STAGING[lid]]
                continue
            assert e['type'] in ('dialogue', 'protagonist_dialogue', 'thought', 'document_text')
            if lid in LINE_CUES:
                lines += ['    ' + c for c in LINE_CUES[lid].splitlines()]
            if lid in AUDIO_LINE_CUES:
                lines += ['    ' + c for c in AUDIO_LINE_CUES[lid].splitlines()]
            if lid == 'ch02_sc01_011':
                lines += ['    show ch02_notice', '    with dissolve']
            if lid == 'ch02_sc01_016':
                lines += ['    show screen ch_phone("馬皙", mode="call")']
            character = ('ch_thought' if e['type'] == 'thought' else
                         'ch02_notice' if e['type'] == 'document_text' else
                         ('ch02_' if e['speaker'] in NAMES else 'ch_') + e['speaker'])
            ja = RUBY.sub(lambda m: '{rb}' + m[1] + '{/rb}{rt}' + m[2] + '{/rt}', e['ja'].replace('[', '[['))
            assert not any(c in ja for c in '〖〗｜'), lid
            ja = '{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}' + ja + '{/font}{/color}{/size}'
            chinese = zh['lines'][lid]
            assert chinese and not any(c in chinese for c in '{}〖〗\n'), lid
            speaker = e['speaker'] if e['type'] == 'dialogue' else None
            lines += ['    window show None', f'    $ ch_line_id = {quote(lid)}',
                      f'    $ ch_voice({repr(speaker)}, {quote(lid)})',
                      f'    {character} {quote(chinese.replace("[", "[["))} (show_ja_text={quote(ja)}) id {lid}']
        lines += ['', '    return', '']
        (dest / (s['id'].split('_')[1] + '.rpy')).write_text('\n'.join(lines), encoding='utf-8')

    images = ROOT / 'game/images/ch02'
    images.mkdir(parents=True, exist_ok=True)
    copies = []
    for stem in [*BACKGROUNDS.values(), 'theatre_orchestra_layer_v1']:
        source = ROOT / 'assets/ch02/backgrounds' / (stem + '.png')
        target = images / source.name
        shutil.copyfile(source, target)
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        assert hashlib.sha256(target.read_bytes()).hexdigest() == digest
        copies.append({'source': source.relative_to(ROOT).as_posix(), 'runtime': target.relative_to(ROOT).as_posix(), 'sha256': digest})
    prop_runtime, prop_copies = build_props(ROOT, ja_hash)
    copies.extend(prop_copies)
    sprite_runtime, sprite_copies = build_sprites(ROOT)
    copies.extend(sprite_copies)
    cg_runtime, cg_copies = build_cg(ROOT, ja_hash)
    copies.extend(cg_copies)
    expression_runtime, expression_copies = build_expressions(ROOT, ja_hash)
    copies.extend(expression_copies)
    runtime = ['# Generated resource declarations; staging/text source: tools/build_ch02.py.',
               'default ch_chapter_label = "第一章"', '', 'init python:',
               '    def ch02_silence():',
               '        # Immediate stop also prevents first-chapter/menu audio leaking in.',
               '        for channel in ("music", "sound", "voice", "ch_ambience", "ch_diegetic"):',
               '            renpy.music.stop(channel=channel, fadeout=0)',
               '        renpy.music.set_audio_filter("voice", None)',
               '        renpy.music.set_audio_filter("ch_diegetic", None)', '']
    for key, name in {**NAMES, 'notice': '寻人启事'}.items():
        runtime.append(f'define ch02_{key} = Character({quote(name)}, screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")')
    runtime += ['']
    for key, stem in BACKGROUNDS.items():
        runtime.append(f'image ch02_bg {key} = Transform("images/ch02/{stem}.png", xysize=(1920, 1080), fit="cover")')
    runtime += prop_runtime + [''] + sprite_runtime + [''] + cg_runtime + [''] + expression_runtime + ['']
    runtime += ['image ch02_bg street_day = Transform("images/ch01/street_day.png", xysize=(1920, 1080), fit="cover")',
                'image ch02_bg restaurant = Transform("images/ch01/restaurant_day.png", xysize=(1920, 1080), fit="cover")',
                '# Composite before screen scaling so the two states share identical architecture.',
                'image ch02_bg theatre_performance = Transform(Composite((1672, 941), (0, 0), "images/ch02/theatre_hall_intermission_v1.png", (125, 50), Transform("images/ch02/theatre_orchestra_layer_v1.png", zoom=0.84)), xysize=(1920, 1080), fit="cover")', '',
                'label ch02_start:', '    $ ch02_silence()', '    $ ch_chapter_label = "第二章"',
                '    $ ch_line_id = ""', '    window hide None', '    scene black',
                '    hide screen ch_phone', '    hide screen ch_recital_hint',
                '    call ch_card("ch02_title") from ch02_title_return']
    runtime += [f'    call {s["id"]} from entry_{s["id"]}_return' for s in data['scenes']]
    runtime += ['    $ ch02_silence()', '    return', '']
    (ROOT / 'game/ch02_runtime.rpy').write_text('\n'.join(runtime), encoding='utf-8')
    report = {'scope': 'approved_visuals_bilingual_subtitles_and_optional_voice_audio', 'ja_sha256': ja_hash, 'zh_sha256': zh_hash,
              'expression_variants': 18, 'retired_phone_shots': ['ch02_handover', 'beidai_phone_recoil_v1', 'ch02_beidai dismiss_afraid'],
              'scenes': len(data['scenes']), 'display_lines': len(texts), 'directions': len(STAGING),
              'audio_play_calls': sum(c.startswith(('$ ch02_audio(', '$ ch_audio(')) for commands in STAGING.values() for c in commands), 'character_sprite_show_calls': sum(c.startswith(('show ch02_qixing', 'show ch02_chinatsu', 'show ch02_wengang', 'show ch02_beidai', 'show ch_qixing', 'show ch_chinatsu', 'show ch_maxi')) for commands in STAGING.values() for c in commands), 'assets': copies,
              'deferred_directions': DEFERRED, 'runtime_tested': False}
    (ROOT / 'docs/reports/ch02_build_check.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Built {len(data["scenes"])} scenes, {len(texts)} bilingual lines, {len(copies)} images. Non-voice audio enabled.')


if __name__ == '__main__':
    build()
