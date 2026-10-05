"""Approved chapter 2 baseline sprites; explicit top/center portrait anchors."""
import hashlib
import shutil

SPRITES = {
    'qixing indoor': 'qixing_indoor_neutral_v1',
    'chinatsu indoor': 'chinatsu_indoor_seated_neutral_v1',
    'chinatsu dress': 'chinatsu_dress_neutral_v1',
    'wengang work': 'wengang_work_neutral_v1',
    'beidai home': 'beidai_home_neutral_v1',
    'chinatsu knees': 'chinatsu_indoor_knees_closed_v1',
    'beidai disheveled': 'beidai_home_disheveled_v1',
    'beidai phone': 'beidai_home_phone_neutral_v1',
    'beidai dismiss': 'beidai_home_phone_dismiss_v1',
    'theatre_staff neutral': 'theatre_staff_halfbody_neutral_v1',
    'house_servant neutral': 'umekawa_servant_partial_neutral_v1',
}




def build_runtime(root):
    target = root/'game/images/ch02/sprites'
    target.mkdir(parents=True, exist_ok=True)
    lines, copies = [], []
    for key, stem in SPRITES.items():
        source = root/'assets/ch02/sprites'/(stem+'.png')
        dest = target/source.name
        shutil.copyfile(source, dest)
        lines.append(f'image ch02_{key} = "images/ch02/sprites/{source.name}"')
        copies.append({'source':source.relative_to(root).as_posix(), 'runtime':dest.relative_to(root).as_posix(), 'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
    lines += [
        '', 'transform ch02_indoor_seated:',
        '    xpos 1690', '    xanchor 0.5', '    ypos 380',
        '    yanchor 0.0', '    xoffset 0', '    yoffset 0', '    zoom 0.96',
        '', 'transform ch02_colleague_right:',
        '    xpos 1690', '    xanchor 0.5', '    ypos 240',
        '    yanchor 0.0', '    xoffset 0', '    yoffset 0', '    zoom 1.06',
        '', 'transform ch02_service_right:',
        '    xpos 1500', '    xanchor 0.5', '    ypos 220',
        '    yanchor 0.0', '    xoffset 0', '    yoffset 0', '    zoom 0.60',
    ]
    return lines, copies
