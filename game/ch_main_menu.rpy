# Central cinematic title / two-tier menu. Separate from in-game navigation.
image ch_menu_theatre = Transform("images/ui/menu_theatre_v1.png", xysize=(1920, 1080), fit="cover")

transform ch_menu_reveal(delay=0.0, rise=0):
    alpha 0.0
    yoffset rise
    pause delay
    ease 0.8 alpha 1.0
    yoffset 0

transform ch_menu_title_reveal:
    alpha 0.0
    yoffset 10
    pause 1.2
    ease 1.0 alpha 1.0 yoffset 0

style ch_menu_ruby is ch_ruby:
    size 22
    yoffset -74
    color "#e6dac1"

style ch_menu_primary is button:
    xsize 250
    ysize 70
    padding (12, 10)
    background None
    hover_background None
    foreground None
    hover_foreground Transform(Solid("#cbb581"), xsize=210, ysize=1, xalign=0.5, yalign=1.0)

style ch_menu_primary_text is default:
    font "fonts/SourceHanSerifSC-Medium.otf"
    size 34
    color "#ded9cf"
    hover_color "#fff3d9"
    insensitive_color "#777b83"
    xalign 0.5
    yalign 0.5
    kerning 3
    outlines [(1, "#101621b0", 0, 1)]

style ch_menu_secondary is ch_menu_primary:
    xsize 150
    ysize 56
    hover_foreground Transform(Solid("#cbb581"), xsize=100, ysize=1, xalign=0.5, yalign=1.0)

style ch_menu_secondary_text is ch_menu_primary_text:
    font "fonts/SourceHanSansSC-Regular.otf"
    size 24
    kerning 2
    color "#b5bac3"

screen ch_theatre_menu(animate=False, interactive=True):
    $ can_continue = Continue().get_sensitive()
    add "ch_menu_theatre"
    add Solid("#10162320")

    fixed:
        at (ch_menu_title_reveal if animate else Transform())

        # Separate title lines preserve the intentional 只因 / チキン reading.
        text "そして":
            font "fonts/ShipporiMincho-SemiBold.ttf"
            size 36
            kerning 9
            color "#e0d6c3"
            xalign 0.5
            ypos 106
        text "{rb}只因{/rb}{rt}チキン{/rt}もいなくなった":
            font "fonts/ShipporiMincho-SemiBold.ttf"
            size 70
            kerning 5
            color "#f3eee3"
            ruby_style style.ch_menu_ruby
            line_leading 30
            adjust_spacing False
            outlines [(1, "#101621a0", 0, 2)]
            xalign 0.5
            ypos 174
    fixed:
        at (ch_menu_reveal(1.5) if animate else Transform())
        add Solid("#baa27480") xpos 865 ypos 305 xsize 190 ysize 1
        text "无只因生还":
            font "fonts/SourceHanSerifSC-Medium.otf"
            size 25
            kerning 10
            color "#c8b792"
            xalign 0.5
            ypos 329

    fixed:
        at (ch_menu_reveal(2.4) if animate else Transform())
        hbox:
            xalign 0.5
            ypos 806
            spacing 50
            textbutton "开始故事":
                style "ch_menu_primary"
                action (Start() if interactive else Return())
                default_focus not can_continue
                text_color ("#ded9cf" if can_continue else "#e7cf9c")
            textbutton "继续阅读":
                style "ch_menu_primary"
                action (Continue() if interactive else Return())
                default_focus can_continue
                text_color ("#e7cf9c" if can_continue else "#777b83")

    fixed:
        at (ch_menu_reveal(2.6) if animate else Transform())
        hbox:
            xalign 0.5
            ypos 905
            spacing 28
            textbutton "读取存档" style "ch_menu_secondary" action (ShowMenu("load") if interactive else Return())
            textbutton "设置" style "ch_menu_secondary" action (ShowMenu("preferences") if interactive else Return())
            textbutton "关于" style "ch_menu_secondary" action (ShowMenu("about") if interactive else Return())
            textbutton "退出" style "ch_menu_secondary" action (Show("ch_exit_confirm") if interactive else Return())

# Played only from splashscreen. Completion and skipping both return to the
# ordinary fully visible menu; the input that skips cannot start the story.
screen ch_lobby_intro():
    modal True
    use ch_theatre_menu(animate=True, interactive=False)
    key "dismiss" action Return()
    key "game_menu" action Return()
    timer 3.5 action Return()

screen ch_lobby_background():
    add "ch_menu_theatre"
    add Solid("#10162320")
