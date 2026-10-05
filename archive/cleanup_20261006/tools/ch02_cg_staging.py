"""Chapter 2 approved CG cues and native layered displayables."""
import hashlib
import json
import shutil


def configure(stage, shot):
    def cg(name, transition='dissolve'):
        return f'window hide None\nscene ch02_cg {name}\nwith {transition}'

    indoor = 'show ch02_qixing indoor at ch_left\nshow ch02_chinatsu indoor at ch02_indoor_seated\nwith dissolve'
    stage(1, 2, cg('television'), '人物表情和所有声音仍暂缓。')
    stage(1, 3, shot('living') + '\n' + indoor, '点头及表情差分暂缓。')
    stage(2, 2, cg('chinatsu_bruise_detail_v3'))
    stage(2, 3, cg('qixing_take_hand_v6') + '\npause 0.65\n' + cg('chinatsu_withdraw_hand_v1'))
    stage(2, 4, shot('living') + '\nshow ch02_qixing indoor at ch_left\nshow ch02_chinatsu knees at ch02_indoor_seated\nwith dissolve\npause 0.7\nwindow hide None\nscene black\nwith fade', '电视及所有声音仍暂缓。')
    stage(4, 4, cg('qixing_files_detail_v1'))
    stage(4, 5, 'window hide None\npause 0.3')
    stage(5, 4, shot('theatre_intermission') + '\nshow ch02_theatre_staff neutral at ch02_service_right\nwith dissolve', '工作人员歉意表情及所有声音仍暂缓。')
    stage(5, 5, cg('voucher'))
    stage(5, 6, shot('theatre_side') + '\nshow ch_qixing neutral at ch_left\nshow ch_maxi neutral at ch_maxi_position(1690)\nwith dissolve', '后续表情差分暂缓。')
    stage(5, 8, cg('qixing_street_stopped_v1') + '\npause 0.8')
    stage(6, 1, 'call ch_card("ch02_chinatsu_home") from ch02_chinatsu_home_return\n' + cg('chinatsu_limo_interior_v2', 'fade'))
    stage(6, 2, cg('limo_arrival_umekawa_v1') + '\npause 0.9\n' + shot('foyer') + '\nshow ch_chinatsu downcast at ch_right\nwith dissolve')
    stage(6, 3, cg('beidai_welcome_chinatsu_v2'))
    stage(6, 4, cg('chinatsu_corridor_escort_v3'), '所有音频暂缓。')
    stage(6, 5, 'window hide None\npause 0.3')
    stage(6, 6, cg('restaurant_memory', 'Dissolve(0.6)'))
    stage(7, 4, cg('piano_forced_turn_v1'))
    stage(7, 5, cg('piano_push_away_v1'))
    stage(7, 6, cg('empty_keys', 'Dissolve(0.15)'))
    stage(7, 7, cg('chinatsu_angry_close'), '备代起身及独立怒视差分仍暂缓；使用拒绝 CG 的千夏面部裁切。')
    stage(7, 8, shot('piano') + '\nshow ch02_beidai disheveled at ch_left\nwith dissolve', '千夏震颤及人物表情差分仍暂缓；镜头转向失态的备代。')
    stage(7, 9, cg('memory_flames_v1', 'Dissolve(0.6)') + '\nshow ch02_memory_arm at ch02_memory_sway\nwith Dissolve(0.4)')
    stage(7, 10, cg('chinatsu_piano_stand_fear_v1', 'Dissolve(0.25)'))
    stage(8, 1, 'call ch_card("ch02_phone") from ch02_phone_return\n' + shot('phone_dusk') + '\nshow ch02_beidai disheveled at ch_left\nshow ch02_house_servant neutral at ch02_service_right\nwith dissolve', '人物表情差分及所有声音仍暂缓。')
    stage(8, 2, 'window hide None\nhide ch02_beidai\nhide ch02_house_servant\nshow ch02_handover\nwith dissolve\npause 0.45\nhide ch02_handover\nshow ch02_beidai phone at ch_left\nshow ch02_house_servant neutral at ch02_service_right\nwith dissolve', '通话礼貌表情仍暂缓。')
    stage(8, 4, cg('beidai_phone_recoil_v1') + '\npause 0.65\n' + shot('phone_dusk') + '\nshow ch02_beidai dismiss at ch_left\nshow ch02_house_servant neutral at ch02_service_right\nwith dissolve\npause 0.35\nhide ch02_house_servant\nwith dissolve', '通话惊恐表情仍暂缓；保留后退 CG，随后挥退佣人。')
    stage(9, 2, cg('qixing_stargaze_side_v1'))
    stage(9, 3, shot('sky') + '\nshow ch02_star help', '揉眼动作立绘暂缓。')
    stage(9, 6, 'hide ch02_star\n' + cg('chinatsu_bruise_detail_v3', 'Dissolve(0.5)'))
    stage(9, 7, cg('qixing_stargaze_side_v1', 'Dissolve(0.6)') + '\npause 0.7\nwindow hide None\nscene black\nwith fade\ncall ch_card("ch02_ending") from ch02_ending_return')


def build_runtime(root, ja_hash):
    manifest = json.loads((root/'assets/manifests/ch02_cg_imports.json').read_text(encoding='utf-8-sig'))
    assert manifest['script_sha256'] == ja_hash
    target = root/'game/images/ch02/cg'
    target.mkdir(parents=True, exist_ok=True)
    lines, copies = [], []
    for item in manifest['images']:
        if not item['selected']:
            continue
        source = root/item['output']
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        assert digest == item['sha256'], item['id']
        dest = target/source.name
        shutil.copyfile(source, dest)
        copies.append({'source': item['output'], 'runtime': dest.relative_to(root).as_posix(), 'sha256': digest})
        lines.append(f'image ch02_cg {item["id"]} = Transform("images/ch02/cg/{source.name}", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)')
    # Compose PNG + outlined voucher directly; SDL SVG cannot reliably load
    # the embedded raster image in the gallery's self-contained SVG.
    lines += [
        'image ch02_cg voucher = Transform(Composite((1672, 941), (0, 0), "images/ch02/cg/theatre_voucher_handover_base_v1.png", (620, 356), Transform("images/ch02/props/theatre_voucher_v1.svg", xysize=(400, 165))), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))',
        'image ch02_cg television = Composite((1920, 1080), (0, 0), Solid("#101722"), (40, 24), Transform("images/ch02/cg/tv_beidai_recital_v1.png", xysize=(1840, 1032)), (80, 55), Text("テレビ放送", font="fonts/SourceHanSansJP-Regular.otf", size=28, color="#e9edf2", outlines=[(2, "#17202a", 0, 0)]))',
        'image ch02_cg restaurant_memory = Transform("images/ch01/cg_table.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0))',
        # Crop the source pixels before resizing. Nested Transform geometry
        # can retain the uncropped child bounds and enlarge the wrong region.
        'image ch02_cg empty_keys = Transform(im.Crop("images/ch02/umekawa_piano_room_v1.png", (335, 420, 440, 248)), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))',
        'image ch02_cg chinatsu_angry_close = Transform(im.Crop("images/ch02/cg/piano_push_away_v1.png", (815, 140, 750, 422)), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))',
        'image ch02_memory_arm = Transform("images/ch02/cg/memory_mother_arm_layer_v1.png", xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))',
        '', 'transform ch02_memory_sway:',
        '    anchor (0.0, 0.0)', '    pos (0, 0)', '    xoffset 0', '    yoffset 0',
        '    ease 1.6 xoffset 12 yoffset -5', '    ease 1.6 xoffset 0 yoffset 0', '    repeat',
    ]
    return lines, copies
