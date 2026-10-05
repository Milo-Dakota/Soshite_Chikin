"""Chapter 2 prop integration; no audio or full character sprites."""
import hashlib
import json
import re
import shutil


def configure(stage, shot):
    stage(1, 4, shot('street_posted'))
    stage(1, 5, 'hide ch02_notice\nshow screen ch_phone("馬皙", incoming=True)\nwith dissolve', '铃声暂缓。')
    stage(1, 6, 'hide screen ch_phone\nwith dissolve\npause 0.3')
    stage(2, 1, shot('entry_shoes', 'fade') + '\npause 1.0\n' + shot('living'), '人物和电视声音暂缓。')
    stage(3, 1, 'call ch_card("ch02_morning") from ch02_morning_return\n' + shot('street_removed'))
    stage(3, 2, 'show screen ch_phone("馬皙", mode="notification")\nwith dissolve')
    stage(3, 3, 'hide screen ch_phone\n' + shot('entry'))
    stage(3, 4, shot('street_removed') + '\npause 0.8\n' + shot('living'), '人物呼吸演出暂缓。')
    stage(5, 5, shot('theatre_side') + '\nshow ch02_voucher\nwith dissolve', '递券手部 CG 暂缓；展示正式票面。')
    stage(5, 6, 'hide ch02_voucher\nwith dissolve', '马皙表情暂缓。')
    stage(8, 1, 'call ch_card("ch02_phone") from ch02_phone_return\n' + shot('phone_dusk') + '\nshow ch02_handover\nwith dissolve', '外部行为视点；备代立绘暂缓。')
    stage(8, 2, 'hide ch02_handover\nwith dissolve', '备代持电话立绘暂缓。')
    stage(9, 3, 'show ch02_star help', '揉眼人物动作暂缓。')
    stage(9, 4, 'show ch02_star help')
    stage(9, 5, 'hide ch02_star\nshow ch02_star coordinates')


def build_runtime(root, ja_hash):
    layout = json.loads((root/'assets/ch02/ui/ch02_props_layout.json').read_text(encoding='utf-8'))
    assert layout['ja_sha256'] == ja_hash, 'Stale prop text'
    target = root/'game/images/ch02/props'
    target.mkdir(parents=True, exist_ok=True)
    copies = []
    for directory, suffix in [('props','*.png'),('ui','*.svg')]:
        for source in sorted((root/'assets/ch02'/directory).glob(suffix)):
            if source.name in ('phone_incoming_maxi_v1.svg', 'phone_notification_maxi_v1.svg'):
                continue  # Retired mockups; phone UI is rendered by ch_phone.
            dest = target/source.name
            shutil.copyfile(source, dest)
            copies.append({'source':source.relative_to(root).as_posix(), 'runtime':dest.relative_to(root).as_posix(), 'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
    # SDL SVG loaders need not support embedded raster <image>. Keep the
    # original vector lettering and compose its unchanged portrait in Ren'Py.
    original = (target/'missing_notice_v1.svg').read_text(encoding='utf-8')
    paper = re.sub(r'<image\b[^>]*/>', '', original)
    assert paper != original
    dest = target/'missing_notice_paper_runtime.svg'
    dest.write_text(paper, encoding='utf-8')
    copies.append({'source':'assets/ch02/ui/missing_notice_v1.svg', 'runtime':dest.relative_to(root).as_posix(), 'derivation':'Remove embedded portrait; compose unchanged PNG using native displayables', 'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
    prefix = 'images/ch02/props/'
    lines = [
        '# Props: native composition retains embedded raster art on SDL SVG loaders.',
        f'image ch02_notice_art = Composite((1200, 1700), (0, 0), "{prefix}missing_notice_paper_runtime.svg", (416, 267), Transform("{prefix}chinatsu_notice_portrait_v1.png", xysize=(368, 491), fit="cover"))',
        '# Explicit anchors override the show default (bottom-center). Match ch_phone top placement.',
        'image ch02_notice = Transform("ch02_notice_art", xysize=(450, 638), xalign=0.5, yanchor=0.0, ypos=32, xoffset=0, yoffset=0)',
        f'image ch02_voucher = Transform("{prefix}theatre_voucher_v1.svg", xysize=(900, 435), xalign=0.5, yanchor=0.0, ypos=155, xoffset=0, yoffset=0)',
        f'image ch02_handover = Transform("{prefix}servant_phone_handover_v3.png", xysize=(1000, 667), anchor=(0.0, 0.0), xpos=850, ypos=90, xoffset=0, yoffset=0, fit="contain")',
    ]
    for state in ['posted','removed']:
        parts = ['(0, 0), "images/ch01/street_day.png"']
        for p in layout['street_notices']:
            art = 'ch02_notice_art' if state=='posted' else prefix+'notice_removed_layer_v1.png'
            parts.append(f'({p["x"]}, {p["y"]}), Transform("{art}", xysize=({p["width"]}, {p["height"]}))')
        lines.append(f'image ch02_bg street_{state} = Transform(Composite((1672, 941), '+', '.join(parts)+'), xysize=(1920, 1080))')
    p = layout['shoes']
    lines.append(f'image ch02_bg entry_shoes = Transform(Composite((1672, 941), (0, 0), "images/ch02/qixing_entry_morning_v1.png", ({p["x"]}, {p["y"]}), Transform("{prefix}chinatsu_shoes_layer_v1.png", xysize=({p["width"]}, {p["height"]}), fit="contain")), xysize=(1920, 1080))')
    signal = layout['signal']
    for name, word in [('help','HELP'),('coordinates','89N64W')]:
        lines += ['', f'image ch02_star {name}:', f'    "{prefix}signal_star_v1.svg"',
                  '    xysize (34, 34)', '    anchor (0.5, 0.5)',
                  f'    pos ({signal["anchor"][0]}, {signal["anchor"][1]})']
        for event in signal['sequences'][word]:
            lines += [f'    alpha {1.0 if event["on"] else 0.0}', f'    pause {event["units"]*signal["unit_seconds"]:.2f}']
        lines += ['    repeat'] if word=='HELP' else ['    alpha 0.0']
    return lines, copies
