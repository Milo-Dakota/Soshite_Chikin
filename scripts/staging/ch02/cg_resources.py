"""Chapter 2 approved CG cues and native layered displayables."""
import hashlib
import json
import shutil




def build_runtime(root, ja_hash):
    manifest = json.loads((root / 'assets/records/ch02.json').read_text(encoding='utf-8-sig'))['collections']['ch02_cg_imports']
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
