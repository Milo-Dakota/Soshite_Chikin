# Chapter 2 non-voice audio. Source files remain unchanged.
init python:
    renpy.music.register_channel("ch_diegetic", mixer="music", loop=False)

    CH02_AUDIO = {
        "mystery_low": ("audio/bgm/ch02_mystery_low.ogg", "music", True, 0.50),
        "mystery_dark": ("audio/bgm/ch02_mystery_dark.ogg", "music", True, 0.25),
        "ensemble": ("audio/bgm/ch02_theater_ensemble.ogg", "ch_diegetic", False, 0.45),
        "tv": ("<from 80>audio/bgm/ch02_tv_piano.ogg", "ch_diegetic", True, 0.32),
        "tv_return": ("<from 145>audio/bgm/ch02_tv_piano.ogg", "ch_diegetic", True, 0.32),
        "room": ("audio/ambience/ch02_room_quiet.ogg", "ch_ambience", True, 0.08),
        "office": ("audio/ambience/ch02_office_room.ogg", "ch_ambience", True, 0.10),
        "audience": ("audio/ambience/ch02_theater_audience.ogg", "ch_ambience", True, 0.12),
        "car": ("audio/ambience/ch02_car_interior.ogg", "ch_ambience", True, 0.12),
        "night": ("audio/ambience/ch02_street_night.ogg", "ch_ambience", True, 0.12),
        "shower": ("audio/sfx/ch01_shower_loop.ogg", "ch_ambience", True, 0.18),
        "phone_ring": ("audio/sfx/ch01_phone_ring.ogg", "sound", False, 0.40),
        "notification": ("audio/sfx/ch02_phone_notification.ogg", "sound", False, 0.40),
        "door_open": ("audio/sfx/ch02_door_open.ogg", "sound", False, 0.22),
        "door_close": ("audio/sfx/ch02_door_close.ogg", "sound", False, 0.12),
        "mansion_open": ("audio/sfx/ch02_mansion_door_open.ogg", "sound", False, 0.30),
        "paper": ("audio/sfx/ch02_paper_shuffle.ogg", "sound", False, 0.30),
        "heels": ("audio/sfx/ch02_heels_wood.ogg", "sound", False, 0.85),
        "sleeve": ("audio/sfx/ch02_sleeve_pull.ogg", "sound", False, 0.22),
    }

    def ch02_audio_stop(channel, fadeout=0.6):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    def ch02_audio(key):
        path, channel, loop, volume = CH02_AUDIO[key]
        file_path = path.split(">", 1)[-1]
        # Keep a missing file from interrupting reading during asset changes.
        if not renpy.loadable(file_path):
            return
        if channel == "music":
            renpy.music.set_audio_filter(channel, None, replace=True)
        if loop and renpy.music.get_playing(channel=channel) == path:
            return
        if channel == "ch_diegetic":
            af = renpy.audio.filter
            # Narrow, steep band for the small television speaker.
            renpy.music.set_audio_filter(channel,
                [af.Highpass(450), af.Lowpass(2200), af.Lowpass(2200)] if key.startswith("tv") else None,
                replace=True)
        renpy.music.play(path, channel=channel, loop=loop,
                         fadeout=0.6 if channel in ("music", "ch_ambience", "ch_diegetic") else 0,
                         fadein=0.8 if loop and channel != "sound" else 0,
                         relative_volume=volume)

    def ch02_audio_end(keep_music=False):
        for channel in ("music", "sound", "ch_ambience", "ch_diegetic"):
            if keep_music and channel == "music":
                continue
            ch02_audio_stop(channel, 0.6)

    def ch02_audio_scene(scene_id):
        # Keep search music into the office and the home cue through side scenes.
        for channel in ("sound", "ch_diegetic", "voice"):
            ch02_audio_stop(channel, 0)
        renpy.music.set_audio_filter("voice", None)
        ch02_audio_stop("ch_ambience", 0)
        if scene_id not in ("ch02_sc04", "ch02_sc07", "ch02_sc08"):
            ch02_audio_stop("music", 0)
