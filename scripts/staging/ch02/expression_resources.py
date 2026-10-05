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




def build_runtime(root, ja_hash):
    manifest = json.loads((root / 'assets/records/ch02.json').read_text(encoding='utf-8-sig'))['collections']['ch02_expression_imports']
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
