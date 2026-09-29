# Studio introduction. Kept outside generated chapter scripts.
# The supplied 1280x720 artwork is displayed intact on the 16:9 canvas.
image ch_studio_white = Solid("#ffffff")

# The splash now ends on the exact main-menu composition.
define config.end_splash_transition = None

screen ch_studio_logo():
    add "images/ui/chikurin_soft_logo.png" xysize (1920, 1080)

screen ch_studio_name():
    text "竹林ソフト":
        font "fonts/ShipporiMincho-SemiBold.ttf"
        size 42
        color "#202735"
        xalign 0.5
        ypos 710
    text "CHIKURIN SOFT":
        font "fonts/SourceHanSansJP-Regular.otf"
        size 18
        color "#72777d"
        xalign 0.5
        ypos 774

style ch_notice_ja is default:
    font "fonts/SourceHanSerifJP-Medium.otf"
    size 24
    color "#303944"
    line_spacing 6
    text_align 0.5
    xalign 0.5

style ch_notice_zh is default:
    font "fonts/SourceHanSerifSC-Medium.otf"
    size 19
    color "#737b83"
    line_spacing 5
    text_align 0.5
    xalign 0.5

screen ch_startup_notice():
    modal True
    add Solid("#ffffff")
    key "dismiss" action Return()

    vbox:
        xalign 0.5
        ypos 190
        xsize 1520
        spacing 44

        vbox:
            xalign 0.5
            spacing 16
            text "本作品はフィクションです。\n作中に登場する人物・団体・地名・事件等は架空のものであり、\n実在のものとは関係ありません。" style "ch_notice_ja"
            text "本作品纯属虚构。\n作品中出现的人物、团体、地名及事件等均为虚构，\n与现实中的同名对象无关。" style "ch_notice_zh"

        vbox:
            xalign 0.5
            spacing 16
            text "本作品に登場する人物は、すべて18歳以上です。" style "ch_notice_ja"
            text "本作品登场人物均已年满18周岁。" style "ch_notice_zh"

        vbox:
            xalign 0.5
            spacing 16
            text "本作品には、暴力的な表現および死亡に関する描写が含まれます。\nあらかじめご了承ください。" style "ch_notice_ja"
            text "本作品包含暴力及涉及死亡的描写，敬请知悉。" style "ch_notice_zh"

    text "クリックで進む / 点击继续":
        font "fonts/SourceHanSansSC-Regular.otf"
        size 18
        color "#92989f"
        xalign 0.5
        ypos 956

label splashscreen:
    window hide None
    $ quick_menu = False
    scene ch_studio_white
    with None
    pause 0.4
    show screen ch_studio_logo
    with Dissolve(0.9)
    pause 0.5
    show screen ch_studio_name
    # Optional user-supplied brand call. Start with the name's fade-in;
    # keep it separate from the later main-menu music and story voices.
    if renpy.loadable("audio/sfx/chikurin_soft_call.ogg"):
        play sound "audio/sfx/chikurin_soft_call.ogg"
    with Dissolve(0.8)
    pause 3.0
    stop sound fadeout 0.3
    hide screen ch_studio_name
    hide screen ch_studio_logo
    with Dissolve(0.7)
    pause 0.2
    call screen ch_startup_notice with Dissolve(0.6)
    # Keep the same music file/channel as config.main_menu_music so Ren'Py
    # continues playback when control passes to the normal menu.
    if renpy.loadable(config.main_menu_music):
        $ renpy.music.play(config.main_menu_music, channel="music", loop=True, fadein=0.8)
    show screen ch_lobby_background
    with Dissolve(0.8)
    call screen ch_lobby_intro
    hide screen ch_lobby_background
    $ quick_menu = True
    return
