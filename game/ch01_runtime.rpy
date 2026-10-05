# Shared presentation and optional user-supplied audio for Chapter 1.
# The Japanese YAML is the authoritative text source.

default ch_line_id = ""

# Character supplies the style for the screen's id="what" widget, overriding
# its screen-level style. Bind dialogue explicitly so Ruby offsets take effect.
define ch_qixing = Character("徐启星", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#aebdce")
define ch_thought = Character(None, screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, what_color="#d0d9e1")
define ch_girl = Character("少女", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#e7cbb7")
define ch_chinatsu = Character("千夏", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#e7cbb7")
define ch_maxi = Character("马皙", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#bfccb5")
define ch_zheng = Character("郑局长", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#aebdce")
define ch_beidai = Character("梅川备代", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")

init python:
    renpy.music.register_channel("ch_ambience", mixer="sfx", loop=True)

    CH_AUDIO = {
        "daily": ("audio/bgm/ch01_daily_calm.ogg", "music", True, 0.32),
        "warm": ("audio/bgm/ch01_warm.ogg", "music", True, 0.32),
        "recital": ("audio/bgm/ch01_piano_recital.ogg", "music", False, 0.55),
        "shower": ("audio/sfx/ch01_shower_loop.ogg", "ch_ambience", True, 0.22),
        "phone": ("audio/sfx/ch01_phone_ring.ogg", "sound", False, 0.50),
        "door": ("audio/sfx/ch01_restaurant_door.ogg", "sound", False, 0.40),
        "street_room": ("audio/ambience/ch01_street_day.ogg", "ch_ambience", True, 0.12),
        "gym_room": ("audio/ambience/ch01_gym_room.ogg", "ch_ambience", True, 0.10),
        "restaurant_room": ("audio/ambience/ch01_restaurant_room.ogg", "ch_ambience", True, 0.10),
    }

    def ch_audio(key):
        path, channel, loop, volume = CH_AUDIO[key]
        if renpy.loadable(path):
            if loop and renpy.music.get_playing(channel=channel) == path:
                return
            renpy.music.play(path, channel=channel, loop=loop,
                             fadeout=0.6 if channel in ("music", "ch_ambience") else 0.0,
                             fadein=0.8 if loop else 0.0, relative_volume=volume)
        else:
            renpy.music.stop(channel=channel, fadeout=0.5)

    def ch_voice(speaker, line_id):
        # Stop the previous line even if the next line is a silent thought.
        renpy.music.stop(channel="voice")
        # Telephone dialogue uses the same filter across both chapters.
        # Apply to the next file, then clear on every other line or silence.
        telephone = speaker == "zheng" and line_id in (
            "ch01_sc02_011", "ch01_sc02_013", "ch01_sc02_014", "ch01_sc02_016")
        telephone = telephone or (speaker == "maxi" and line_id in (
            "ch02_sc01_016", "ch02_sc01_017")) or (
            speaker == "unknown_caller" and line_id.startswith("ch02_sc08_"))
        af = renpy.audio.filter
        renpy.music.set_audio_filter("voice", [af.Highpass(300), af.Lowpass(3400)] if telephone else None)
        if speaker and speaker != "qixing":
            for extension in ("wav", "ogg"):
                path = "audio/voice/{}/{}.{}".format(speaker, line_id, extension)
                if renpy.loadable(path):
                    # voice is a store function, not part of renpy.exports.
                    voice(path)
                    break

    def ch_stop_audio():
        for channel in ("music", "sound", "voice", "ch_ambience"):
            renpy.music.stop(channel=channel, fadeout=0.6)
        renpy.music.set_audio_filter("voice", None)

define ch_title_text = "そして{rb}只因{/rb}{rt}チキン{/rt}もいなくなった"

init python:
    def ch_keep_dialogue_window():
        # Non-dialogue interactions must not fall back to the stock narrator
        # textbox. Read the rollback-aware history without adding a new entry.
        entry = _history_list[-1] if _history_list else None
        renpy.show_screen("ch_say",
            who=entry.who if entry else None,
            what=entry.what if entry else "",
            ja_text=((getattr(entry, "show_args", None) or {}).get("ja_text", "") if entry else ""),
            retained=True,
            retained_who_color=((getattr(entry, "who_args", None) or {}).get("color", "#cbb581") if entry else "#cbb581"),
            _transient=True)
        renpy.shown_window()

define config.empty_window = ch_keep_dialogue_window

# screens.rpy uses init offset -1 and resolves this style while rebuilding
# language styles. Define it earlier, including on language changes.
init -2:
    style ch_ruby is default:
        font "fonts/SourceHanSansJP-Regular.otf"
        size 19
        # Ruby shares the base text baseline unless explicitly raised.
        yoffset -38
        color "#f3efe7"
        outlines []

    # Titles use 48–49 px text; history uses 33 px instead of dialogue's 36.
    style ch_title_ruby is ch_ruby:
        yoffset -51

    style ch_history_ruby is ch_ruby:
        yoffset -35

    # Japanese secondary subtitles use a 24 px base in dialogue AND history.
    # Keep title/about Ruby independent from this smaller subtitle size.
    style ch_subtitle_ruby is ch_ruby:
        size 13
        yoffset -26
        color "#aebdce"

style ch_dialogue is default:
    font "fonts/SourceHanSerifSC-Medium.otf"
    size 36
    color "#f3efe7"
    line_spacing 8
    line_leading 18
    ruby_style style.ch_subtitle_ruby
    adjust_spacing False
    outlines []

style ch_name is default:
    font "fonts/SourceHanSerifSC-Medium.otf"
    size 26
    color "#cbb581"
    outlines []

style ch_secondary_dialogue is ch_dialogue:
    font "fonts/SourceHanSerifJP-Medium.otf"
    size 24
    color "#aebdce"

screen ch_say(who, what, ja_text="", retained=False, retained_who_color="#cbb581"):
    window:
        id "window"
        background "gui/reading_panel_a.svg"
        xalign 0.5
        xsize 1776
        yalign 1.0
        yoffset -8
        ysize 350
        padding (0, 0)
        add Solid("#bba47730") xpos 64 ypos 294 xsize 1648 ysize 1
        if who is not None:
            hbox:
                xpos 64
                ypos 32
                spacing 22
                if retained:
                    text who id "who" style "ch_name" color retained_who_color yalign 0.5
                else:
                    text who id "who" style "ch_name" yalign 0.5
                add Solid("#cbb58180") xsize 62 ysize 1 yalign 0.5
        # Keep the same text origin for thoughts and spoken dialogue.
        vbox:
            xpos 64
            ypos 80
            xsize 1648
            spacing 8
            # Ren'Py requires this widget to receive the EXACT what argument.
            text what id "what" style "ch_dialogue" xsize 1648 slow (not retained)
            if ja_text:
                text ja_text:
                    id "ch_japanese"
                    style "ch_secondary_dialogue"
                    xsize 1648
                    slow (not retained and not renpy.is_skipping() and not renpy.in_rollback())
                    slow_cps preferences.text_cps
                    # Only the primary say text handles dismissal clicks.
                    slow_abortable False

screen ch_recital_hint():
    zorder 90
    # Informational only; clicks continue to reach the skippable pause.
    frame:
        xalign 0.97
        yalign 0.95
        padding (18, 10)
        background Solid("#151c28aa")
        text "点击跳过演奏":
            font "fonts/SourceHanSansSC-Regular.otf"
            size 22
            color "#d0d9e1"

screen ch_caption(title, subtitle=""):
    zorder 100
    add Solid("#202735")
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 32
        text title font "fonts/SourceHanSerifJP-Medium.otf" xalign 0.5 text_align 0.5 size 54 color "#f3efe7" ruby_style style.ch_title_ruby line_leading 18
        if subtitle:
            text subtitle font "fonts/SourceHanSerifSC-Medium.otf" xalign 0.5 text_align 0.5 size 28 color "#b39a68"

# Dialogue portraits use screen-space half-body framing, not a shared floor.
# Explicit center/top anchors keep placement independent of scaled canvas size.
# Keep the original 1024x1536 canvases intact for aligned expression variants.
transform ch_left:
    xpos 320
    xanchor 0.5
    ypos 240
    yanchor 0.0
    yoffset 0
    zoom 1.06

transform ch_right:
    xpos 1690
    xanchor 0.5
    ypos 380
    yanchor 0.0
    yoffset 0
    zoom 0.96

# Maxi keeps the same size and height on either side of the screen.
transform ch_maxi_position(side=320):
    xpos side
    xanchor 0.5
    ypos 240
    yanchor 0.0
    yoffset 0
    zoom 1.06

transform ch_center:
    xalign 0.5
    yalign 1.0
    yoffset 350
    zoom 0.82

# Full-body bow in the restaurant's open aisle, away from the dining table.
transform ch_beidai_public:
    xpos 850
    xanchor 0.5
    ypos 190
    yanchor 0.0
    yoffset 0
    zoom 0.48

transform ch_seated_left:
    xpos 320
    xanchor 0.5
    ypos 270
    yanchor 0.0
    yoffset 0
    zoom 1.06

transform ch_seated_right:
    xpos 1690
    xanchor 0.5
    ypos 410
    yanchor 0.0
    yoffset 0
    zoom 0.96

transform ch_step_away:
    ease 0.35 alpha 0.0 xoffset 65

# Target aspect ratio is maintained by fit=cover; originals are not enlarged on disk.
image ch_bg street = Transform("images/ch01/street_day.png", xysize=(1920, 1080), fit="cover")
image ch_bg locker = Transform("images/ch01/gym_locker.png", xysize=(1920, 1080), fit="cover")
image ch_bg locker_empty = Transform("images/ch01/gym_empty.png", xysize=(1920, 1080), fit="cover")
image ch_bg restaurant = Transform("images/ch01/restaurant_day.png", xysize=(1920, 1080), fit="cover")
image ch_bg restaurant_public = Transform("images/ch01/restaurant_public.png", xysize=(1920, 1080), fit="cover")
image ch_bg restaurant_empty = Transform("images/ch01/restaurant_empty.png", xysize=(1920, 1080), fit="cover")
image ch_cg bread = Transform("images/ch01/cg_bread.png", xysize=(1920, 1080), fit="cover")
image ch_cg support = Transform("images/ch01/cg_support.png", xysize=(1920, 1080), fit="cover")
image ch_cg recital = Transform("images/ch01/cg_recital.png", xysize=(1920, 1080), fit="cover")
image ch_cg shower = Transform("images/ch01/cg_shower.png", xysize=(1920, 1080), fit="cover")
image ch_cg car = Transform("images/ch01/cg_car.png", xysize=(1920, 1080), fit="cover")
image ch_cg water = Transform("images/ch01/cg_water.png", xysize=(1920, 1080), fit="cover")
image ch_cg violin = Transform("images/ch01/cg_violin.png", xysize=(1920, 1080), fit="cover")
image ch_cg sleeve = Transform("images/ch01/cg_sleeve.png", xysize=(1920, 1080), fit="cover")
image ch_cg two_fingers = Transform("images/ch01/cg_two_fingers.png", xysize=(1920, 1080), fit="cover")
image ch_cg walk = Transform("images/ch01/cg_walk.png", xysize=(1920, 1080), fit="cover")
image ch_cg table = Transform("images/ch01/cg_table.png", xysize=(1920, 1080), fit="cover")
image ch_qixing neutral = "images/ch01/qixing_neutral.png"
image ch_qixing troubled = "images/ch01/qixing_troubled.png"
image ch_qixing bemused = "images/ch01/qixing_bemused.png"
image ch_qixing serious = "images/ch01/qixing_serious.png"
image ch_qixing soft = "images/ch01/qixing_soft.png"
image ch_qixing surprised = "images/ch01/qixing_surprised.png"
image ch_chinatsu guarded = "images/ch01/chinatsu_guarded.png"
image ch_chinatsu smile = "images/ch01/chinatsu_smile.png"
image ch_chinatsu afraid = "images/ch01/chinatsu_afraid.png"
image ch_chinatsu embarrassed = "images/ch01/chinatsu_embarrassed.png"
image ch_chinatsu downcast = "images/ch01/chinatsu_downcast.png"
image ch_chinatsu surprised = "images/ch01/chinatsu_surprised.png"
image ch_maxi neutral = "images/ch01/maxi_neutral.png"
image ch_maxi enthusiastic = "images/ch01/maxi_enthusiastic.png"
image ch_maxi concerned = "images/ch01/maxi_concerned.png"
image ch_maxi annoyed = "images/ch01/maxi_annoyed.png"
image ch_beidai bow = "images/ch01/beidai_bow.png"

screen ch_phone(contact, incoming=False, mode=None):
    frame:
        xalign 0.5
        ypos 170
        yanchor 0.0
        xsize 430
        padding (35, 38)
        background Solid("#202735f0")
        vbox:
            spacing 26
            xalign 0.5
            text ("通知" if mode == "notification" else "通話" if mode == "call" else "着信" if incoming else "連絡先") size 25 color "#b39a68" xalign 0.5
            text contact size 40 color "#f3efe7" xalign 0.5
            text ("新しい通知" if mode == "notification" else "通話中" if mode == "call" else "通話" if incoming else "発信") size 25 color "#aebdce" xalign 0.5

label ch_card(card_id):
    $ title, subtitle = CH_CARDS[card_id]
    window hide
    stop ch_ambience fadeout 0.6
    $ quick_menu = False
    show screen ch_caption(title, subtitle)
    with dissolve
    pause
    # Clear the old scene while the opaque title still covers it.
    scene black
    hide screen ch_caption
    # Fade the whole card out instead of dropping it in a single frame.
    with Dissolve(0.6)
    $ quick_menu = True
    return
