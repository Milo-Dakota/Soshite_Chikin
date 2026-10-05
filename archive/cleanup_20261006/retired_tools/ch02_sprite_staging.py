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


def configure(staging, deferred):
    def append(scene, number, commands, reason=None):
        key = f'ch02_sc{scene:02}_dir{number:03}'
        staging[key] += commands.splitlines()
        if reason is not None:
            if reason:
                deferred[key] = reason
            else:
                deferred.pop(key, None)

    indoor = 'show ch02_qixing indoor at ch_left\nshow ch02_chinatsu indoor at ch02_indoor_seated\nwith dissolve'
    outdoor = 'show ch_qixing neutral at ch_left\nwith dissolve'
    office = 'show ch_qixing neutral at ch_left\nshow ch02_wengang work at ch02_colleague_right\nwith dissolve'
    append(1, 1, indoor, '电视节目 CG 与所有声音暂缓；本轮仅基础表情。')
    append(1, 4, outdoor)
    append(2, 1, indoor, '电视节目 CG 与声音暂缓；抱膝姿态另需制作。')
    append(3, 1, outdoor)
    append(4, 1, office)
    append(4, 3, office)
    append(5, 1, 'show ch_qixing neutral at ch_left\nshow ch_maxi neutral at ch_maxi_position(1690)\nwith dissolve')
    append(5, 6, 'show ch_qixing neutral at ch_left\nshow ch_maxi neutral at ch_maxi_position(1690)\nwith dissolve', '本轮基础表情，后续恢复本场表情演出。')
    append(5, 7, outdoor)
    append(6, 2, 'show ch_chinatsu downcast at ch_right\nwith dissolve', '礼宾车、迎接双人 CG 与佣人群像暂缓。')
    append(6, 4, 'show ch_chinatsu downcast at ch_right\nwith dissolve', '护臂动作及音频暂缓。')
    append(7, 1, 'show ch02_chinatsu dress at ch_right\nshow ch02_beidai home at ch_left\nwith dissolve', '本轮仅入室站姿和基础表情。')
    # Standing baselines cannot stand in for the required seated action art.
    append(7, 3, 'hide ch02_chinatsu\nhide ch02_beidai\nwith dissolve', '礼服／备代坐姿及琴房动作画面待制作；不以站姿冒充坐姿。')
    # Do not use the tidy, empty-handed baseline during the dishevelled call.
    append(9, 1, outdoor)


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
