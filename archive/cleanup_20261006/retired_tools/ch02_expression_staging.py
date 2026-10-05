"""Approved expression variants and continuous chapter 2 phone staging."""
import hashlib
import json
import shutil

EXPRESSIONS = {
    'qixing indoor_bemused': 'qixing_indoor_bemused_v1',
    'qixing indoor_concerned': 'qixing_indoor_concerned_v1',
    'qixing casual_anger': 'qixing_casual_restrained_anger_v1',
    'chinatsu indoor_awkward': 'chinatsu_indoor_awkward_v1',
    'chinatsu indoor_wry': 'chinatsu_indoor_wry_v1',
    'chinatsu indoor_surprised': 'chinatsu_indoor_surprised_v1',
    'chinatsu dress_angry': 'chinatsu_dress_angry_v1',
    'wengang work_indignant': 'wengang_work_indignant_v1',
    'wengang work_skeptical': 'wengang_work_skeptical_v1',
    'wengang work_surprised': 'wengang_work_surprised_v1',
    'maxi incredulous': 'maxi_incredulous_v1',
    'beidai home_tender': 'beidai_home_false_tender_v1',
    'beidai disheveled_furious': 'beidai_home_disheveled_furious_v1',
    'beidai disheveled_curt': 'beidai_home_disheveled_curt_v1',
    'beidai phone_polite': 'beidai_home_phone_polite_v1',
    'beidai phone_uneasy': 'beidai_home_phone_uneasy_v1',
    'beidai phone_afraid': 'beidai_home_phone_afraid_v1',
    'beidai dismiss_afraid': 'beidai_home_dismiss_afraid_v1',
    'theatre_staff apologetic': 'theatre_staff_apologetic_v1',
}

RETIRED_EXPRESSIONS = {'beidai_home_dismiss_afraid_v1'}

# Text IDs are stable; face changes occur immediately before the relevant line.
LINE_CUES = {
    'ch02_sc01_005': 'window hide None\nscene ch02_bg living\nwith dissolve\nshow ch02_qixing indoor at ch_left\nshow ch02_chinatsu indoor_wry at ch02_indoor_seated\nwith dissolve',
    'ch02_sc01_006': 'show ch02_chinatsu indoor_surprised at ch02_indoor_seated\nwith Dissolve(0.2)',
    'ch02_sc04_007': 'hide ch_qixing\nshow ch02_qixing casual_anger at ch_left\nwith Dissolve(0.2)',
    'ch02_sc04_009': 'show ch02_wengang work_skeptical at ch02_colleague_right\nwith Dissolve(0.2)',
}


def configure(stage, shot):
    silent = '所有第二章音频仍暂缓。'
    # Show the recital first, then return to the conversation for Chinatsu's face.
    stage(1, 2, 'window hide None\nscene ch02_cg television\nwith dissolve\npause 0.8\n' + shot('living') + '\nshow ch02_qixing indoor at ch_left\nshow ch02_chinatsu indoor_awkward at ch02_indoor_seated\nwith dissolve', silent)
    stage(1, 3, 'show ch02_qixing indoor_bemused at ch_left\nwith Dissolve(0.2)', '点头身体动作与音频仍暂缓。')
    stage(2, 1, shot('entry_shoes', 'fade') + '\npause 1.0\n' + shot('living') + '\nshow ch02_qixing indoor_concerned at ch_left\nshow ch02_chinatsu indoor at ch02_indoor_seated\nwith dissolve', silent)
    stage(2, 4, 'window hide None\nscene black\nwith fade', silent)
    stage(4, 3, 'window hide None\nscene black\nwith dissolve\npause 0.3\n' + shot('office') + '\nshow ch_qixing serious at ch_left\nshow ch02_wengang work_indignant at ch02_colleague_right\nwith dissolve', silent)
    stage(4, 6, 'window hide None\nscene ch02_bg office\nshow ch02_wengang work_surprised at ch02_colleague_right\nwith None\npause 1.5\nscene black\nwith fade', '启星奔离身体动作仍暂缓；文钢与背景一起直接出现。')
    stage(5, 1, shot('theatre_exterior', 'fade') + '\nshow ch_qixing troubled at ch_left\nshow ch_maxi concerned at ch_maxi_position(1690)\nwith dissolve', silent)
    stage(5, 4, shot('theatre_intermission') + '\nshow ch02_theatre_staff apologetic at ch02_service_right\nwith dissolve', silent)
    stage(5, 6, shot('theatre_side') + '\nshow ch_qixing surprised at ch_left\nshow ch02_maxi incredulous at ch_maxi_position(1690)\nwith dissolve', silent)
    stage(5, 7, shot('theatre_exterior', 'fade') + '\nshow ch_qixing troubled at ch_left\nwith dissolve', '使用第一章低落垂眼差分；离席身体动作与音频仍暂缓。')
    stage(5, 8, 'window hide None\npause 0.8', silent)
    stage(7, 2, 'show ch02_beidai home_tender at ch_left\nwith Dissolve(0.2)', silent)
    stage(7, 7, shot('piano') + '\nshow ch02_chinatsu dress_angry at ch_right\nshow ch02_beidai disheveled_furious at ch_left\nwith dissolve', '两侧正常对话站位；备代起身身体动作与音频仍暂缓。')
    stage(7, 8, 'pause 0.25', '保留两侧人物，不再单独切向备代；千夏震颤身体动作与音频仍暂缓。')
    stage(8, 1, 'call ch_card("ch02_phone") from ch02_phone_return\n' + shot('phone_dusk') + '\nshow ch02_beidai disheveled_curt at ch02_phone_left\nshow ch02_house_servant neutral at ch02_service_right\nwith dissolve', silent)
    stage(8, 2, 'show ch02_house_servant neutral at ch02_servant_offer\npause 0.25\nshow ch02_beidai phone_polite at ch02_phone_left\nwith Dissolve(0.25)', '接机通过姿态切换省略精细手部交接；音频仍暂缓。')
    stage(8, 3, 'window hide None\npause 0.5\nshow ch02_house_servant neutral at ch02_servant_exit\npause 0.4\nhide ch02_house_servant\nshow ch02_beidai phone_uneasy at ch02_phone_left\nwith Dissolve(0.2)\npause 0.7', '佣人递机后稍候自行离去；电话略离耳的手臂动作暂缓。')
    stage(8, 4, 'show ch02_beidai phone_afraid at ch02_phone_recoil\nwith Dissolve(0.15)\npause 0.25', silent)


def build_runtime(root, ja_hash):
    manifest = json.loads((root/'assets/manifests/ch02_expression_imports.json').read_text(encoding='utf-8-sig'))
    assert manifest['ja_sha256'] == ja_hash
    items = {item['id']: item for item in manifest['images']}
    assert set(items) == set(EXPRESSIONS.values())
    target = root/'game/images/ch02/expressions'
    target.mkdir(parents=True, exist_ok=True)
    lines, copies = [], []
    for key, stem in EXPRESSIONS.items():
        item = items[stem]
        source = root/item['output']
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        assert digest == item['sha256'], stem
        dest = target/source.name
        shutil.copyfile(source, dest)
        lines.append(f'image ch02_{key} = "images/ch02/expressions/{source.name}"')
        copies.append({'source': item['output'], 'runtime': dest.relative_to(root).as_posix(), 'sha256': digest})
    # The dismiss pose's head is ~50 px to the right and ~25 px lower in
    # source coordinates; compensate at the same display scale as the phone.
    lines += '''
transform ch02_chinatsu_face:
    xpos 1000
    xanchor 0.5
    ypos -40
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 2.0

transform ch02_phone_left:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 0.85

transform ch02_phone_recoil:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    zoom 0.85
    xoffset 0
    yoffset 0
    ease 0.18 xoffset -55

transform ch02_phone_back:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset -55
    yoffset 0
    zoom 0.85

transform ch02_phone_dismiss:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset -98
    yoffset -21
    zoom 0.85

transform ch02_servant_offer:
    xpos 1500
    xanchor 0.5
    ypos 220
    yanchor 0.0
    zoom 0.60
    xoffset 0
    yoffset 0
    ease 0.25 xoffset -45

transform ch02_servant_exit:
    xpos 1500
    xanchor 0.5
    ypos 220
    yanchor 0.0
    zoom 0.60
    xoffset -45
    yoffset 0
    alpha 1.0
    ease 0.4 xoffset 420 alpha 0.0
'''.strip().splitlines()
    return lines, copies
