"""Non-voice audio cues applied after the approved visual staging."""

LINE_CUES = {
    'ch02_sc01_016': '$ ch02_audio_stop("sound", 0)',
}


def configure(staging, deferred):
    def cue(scene, direction, before='', after='', replace=None):
        key = f'ch02_sc{scene:02}_dir{direction:03}'
        commands = '\n'.join(staging[key])
        if replace:
            old, new = replace
            assert old in commands, key
            commands = commands.replace(old, new, 1)
        staging[key] = '\n'.join(x for x in (before, commands, after) if x).splitlines()

    # Keep the television on screen through Chinatsu's first two replies.
    staging['ch02_sc01_dir002'] = [
        'window hide None', 'scene ch02_cg television', 'with dissolve']
    cue(1, 1, after='$ ch02_audio("room")\n$ ch02_audio("tv")')
    cue(1, 4, before='window hide None\n$ ch02_audio_stop("ch_diegetic", 0.35)\n$ ch02_audio_stop("ch_ambience", 0.35)\nscene black\n$ ch02_audio("door_close")\nwith Dissolve(0.35)\npause 0.5',
        after='$ ch_audio("daily")\n$ ch_audio("street_room")')
    cue(1, 5, before='window hide None', after='$ ch02_audio("phone_ring")\npause')
    # Door movement is heard on black before revealing the interior.
    enter = 'window hide None\nscene black\nwith Dissolve(0.3)\n$ ch02_audio("door_open")\npause 1.4'
    cue(2, 1, before=enter, replace=('with fade', 'with dissolve'))
    cue(2, 1, replace=('scene ch02_bg entry_shoes',
        'scene ch02_bg entry_shoes\n$ ch02_audio("room")\n$ ch02_audio("tv_return")'))
    cue(2, 3, replace=('scene ch02_cg chinatsu_withdraw_hand_v1',
        '$ ch02_audio("sleeve")\nscene ch02_cg chinatsu_withdraw_hand_v1'))
    cue(2, 4, before='$ ch02_audio_end()')
    cue(3, 1, after='$ ch_audio("daily")\n$ ch_audio("street_room")')
    cue(3, 2, after='$ ch02_audio("notification")')
    cue(3, 3, before='hide screen ch_phone\n$ ch02_audio_stop("music", 0.3)\n$ ch02_audio_stop("ch_ambience", 0.3)\n' + enter,
        after='$ ch02_audio("room")')
    cue(3, 4, after='$ ch02_audio("mystery_low")')
    cue(3, 5, before='$ ch02_audio("door_close")', after='$ ch02_audio_stop("ch_ambience")')
    cue(4, 1, before=enter, replace=('with fade', 'with dissolve'),
        after='$ ch02_audio("mystery_low")\n$ ch02_audio("office")')
    cue(4, 4, before='$ ch02_audio("paper")')
    cue(4, 6, before='$ ch02_audio("door_close")', after='$ ch02_audio_end()')
    cue(5, 1, after='$ ch_audio("street_room")')
    cue(5, 2, before='$ ch02_audio_stop("music")\n$ ch02_audio_stop("ch_ambience")',
        after='$ ch02_audio("ensemble")')
    cue(5, 4, before='$ ch02_audio_stop("ch_diegetic", 1.2)', after='$ ch02_audio("audience")')
    cue(5, 7, before='$ ch02_audio_stop("music")\n$ ch02_audio_stop("ch_ambience")',
        after='$ ch_audio("street_room")')
    cue(5, 8, after='$ ch02_audio_end()')
    cue(6, 1, after='$ ch02_audio("car")\n$ ch02_audio("mystery_dark")')
    cue(6, 2, before='$ ch02_audio_stop("ch_ambience", 0.8)',
        replace=('scene ch02_bg foyer', '$ ch02_audio("mansion_open")\nscene ch02_bg foyer'),
        after='$ ch02_audio("room")')
    cue(6, 7, after='$ ch02_audio("shower")')
    cue(6, 9, before='$ ch02_audio_end(keep_music=True)')
    staging['ch02_sc07_dir001'] = [
        'call ch_card("ch02_chinatsu_piano") from ch02_chinatsu_piano_return',
        'window hide None', '$ ch02_audio("mansion_open")',
        'scene ch02_bg piano', 'show ch02_beidai home at ch_left',
        'with Dissolve(0.5)', '$ ch02_audio("room")',
        'pause 2.1', '$ ch02_audio("heels")',
        '$ renpy.pause(2.92, hard=True)',
        'show ch02_chinatsu dress at ch_right', 'with Dissolve(0.35)',
    ]
    cue(7, 11, before='$ ch02_audio_end(keep_music=True)')
    cue(8, 1, after='$ ch02_audio("room")')
    cue(8, 3, before='$ ch02_audio_stop("music", 0.6)',
        replace=('hide ch02_house_servant', 'hide ch02_house_servant\n$ ch02_audio("mansion_open")'))
    cue(8, 5, before='$ ch02_audio_end()')
    cue(9, 1, after='$ ch02_audio("night")\n$ ch02_audio("mystery_low")')
    cue(9, 7, replace=('call ch_card("ch02_ending")',
        '$ ch02_audio_end()\ncall ch_card("ch02_ending")'))

    # Remove obsolete audio-deferred claims, retaining outstanding visual notes.
    for key, note in list(deferred.items()):
        if note in ('所有第二章音频仍暂缓。', '画内合奏及所有音频暂缓。', '铃声暂缓。', '水声暂缓。'):
            deferred.pop(key)
        else:
            deferred[key] = note.replace('与音频仍暂缓', '仍暂缓').replace('及所有音频暂缓', '暂缓').replace('；音频仍暂缓', '').replace('与门声仍暂缓', '仍暂缓').replace('所有声音暂缓', '声音已接入').replace('水声暂缓', '水声已接入')
