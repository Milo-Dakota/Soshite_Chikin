# Shared theatre programme pages; save/load retain native FileAction semantics.
style ch_page_text is default:
    font "fonts/SourceHanSansSC-Regular.otf"
    size 25
    color "#dce0e5"
    line_spacing 10

style ch_page_heading is ch_page_text:
    font "fonts/SourceHanSerifSC-Medium.otf"
    size 34
    color "#d6be8d"

style ch_page_button is button:
    xminimum 86
    ysize 56
    padding (18, 10)
    background None
    hover_background None
    foreground None
    hover_foreground Transform(Solid("#cbb581"), ysize=1, yalign=1.0)
    selected_foreground Transform(Solid("#cbb581"), ysize=1, yalign=1.0)

style ch_page_button_text is ch_menu_secondary_text:
    selected_color "#e7cf9c"
    insensitive_color "#656e7c"
    kerning 0

style ch_setting_button is ch_page_button:
    xminimum 0
    xsize 410
    selected_foreground Transform(Solid("#cbb581"), xsize=3, ysize=20, yalign=0.5)

style ch_setting_button_text is ch_page_button_text:
    xalign 0.0

style ch_volume is slider:
    xsize 410
    ysize 30
    left_bar Transform(Solid("#cbb581"), ysize=3, yalign=0.5)
    right_bar Transform(Solid("#485363"), ysize=3, yalign=0.5)
    thumb Solid("#f1dfb8", xsize=5, ysize=22)
    thumb_shadow None
    thumb_offset 2

style ch_save_card is button:
    xsize 448
    ysize 302
    padding (12, 10)
    background Solid("#33405280")
    hover_background Solid("#48546a")
    insensitive_background Solid("#33405250")
    foreground None
    hover_foreground Transform(Solid("#cbb581"), ysize=1, yalign=1.0)

style ch_save_card_text is ch_page_text:
    size 20
    hover_color "#fff0cf"

screen ch_page_shell(title):
    if main_menu:
        add "ch_menu_theatre"
    add Solid("#0c1420b0")
    add Solid("#111d2bec") xpos 90 ypos 66 xsize 1740 ysize 948
    add Solid("#bba47770") xpos 90 ypos 66 xsize 1740 ysize 1
    add Solid("#bba47740") xpos 90 ypos 1013 xsize 1740 ysize 1
    add Solid("#cbb581") xpos 160 ypos 110 xsize 4 ysize 48
    text title style "ch_page_heading" xpos 186 ypos 110 size 42
    textbutton "返回" style "ch_page_button" xpos 1624 ypos 104:
        action (ShowMenu("main_menu") if main_menu else Return())
    fixed:
        xpos 180
        ypos 190
        xsize 1560
        ysize 740
        transclude
    if not main_menu:
        hbox:
            xalign 0.5
            ypos 950
            spacing 20
            textbutton "保存" style "ch_page_button" action ShowMenu("save")
            textbutton "读取" style "ch_page_button" action ShowMenu("load")
            textbutton "历史" style "ch_page_button" action ShowMenu("history")
            textbutton "设置" style "ch_page_button" action ShowMenu("preferences")
            textbutton "关于" style "ch_page_button" action ShowMenu("about")
            textbutton "主菜单" style "ch_page_button" action MainMenu()
    else:
        text "无只因生还  /  第一章・第二章":
            style "ch_page_text"
            size 18
            color "#7c8797"
            xalign 0.5
            ypos 966
    key "game_menu" action (ShowMenu("main_menu") if main_menu else Return())

screen ch_file_slots(title):
    use ch_page_shell(title):
        text ("存档页 · " + FilePageName(auto="自动存档", quick="快速存档")) style "ch_page_text" size 22 xalign 0.5
        grid 3 2:
            xalign 0.5
            ypos 38
            spacing 24
            for slot in range(1, 7):
                button:
                    style "ch_save_card"
                    action FileAction(slot)
                    key "save_delete" action FileDelete(slot)
                    fixed:
                        xfill True
                        yfill True
                        add Solid("#131f2e") xsize 424 ysize 282
                        if FileLoadable(slot):
                            add FileScreenshot(slot) xalign 0.5 ypos 4 xsize 400 ysize 225
                        else:
                            text "尚无记录" style "ch_page_text" size 24 color "#637080" xalign 0.5 ypos 104
                            add Solid("#bba47750") xalign 0.5 ypos 153 xsize 50 ysize 1
                        text "[slot:02d]" style "ch_page_text" size 19 color "#d6be8d" xpos 12 ypos 240
                        text FileTime(slot, format="%Y / %m / %d   %H:%M", empty="空白存档"):
                            style "ch_page_text"
                            size 19
                            xpos 65
                            ypos 240
        hbox:
            xalign 0.5
            ypos 681
            spacing 8
            textbutton "上一页" style "ch_page_button" action FilePagePrevious()
            if config.has_autosave:
                textbutton "自动" style "ch_page_button" action FilePage("auto")
            if config.has_quicksave:
                textbutton "快速" style "ch_page_button" action FilePage("quick")
            for page in range(1, 10):
                textbutton "[page]" style "ch_page_button" xminimum 52 action FilePage(page)
            textbutton "下一页" style "ch_page_button" action FilePageNext()
        key "save_page_prev" action FilePagePrevious()
        key "save_page_next" action FilePageNext()

screen ch_preferences():
    use ch_page_shell("设置"):
        hbox:
            xpos 40
            ypos 36
            spacing 90
            vbox:
                xsize 430
                spacing 22
                text "01  /  画面" style "ch_page_heading"
                null height 18
                textbutton "窗口模式" style "ch_setting_button" action Preference("display", "window")
                textbutton "全屏显示" style "ch_setting_button" action Preference("display", "fullscreen")
                null height 28
                text "演出" style "ch_page_text" color "#d6be8d"
                textbutton "显示转场动画" style "ch_setting_button" action Preference("transitions", "toggle")
                text "金色标记表示当前启用的选项。" style "ch_page_text" size 20 color "#8390a1" xmaximum 420
            vbox:
                xsize 430
                spacing 22
                text "02  /  阅读" style "ch_page_heading"
                null height 18
                text "文字显示速度" style "ch_page_text"
                bar value Preference("text speed") style "ch_volume"
                text ("即时显示" if preferences.text_cps == 0 else "每秒约 %d 字" % preferences.text_cps) style "ch_page_text" size 18 color "#8390a1"
                null height 20
                text "自动播放等待时间" style "ch_page_text"
                bar value Preference("auto-forward time") style "ch_volume"
                null height 28
                text "快进" style "ch_page_text" color "#d6be8d"
                textbutton "允许跳过未读文字" style "ch_setting_button" action Preference("skip", "toggle")
                textbutton "选项后继续快进" style "ch_setting_button" action Preference("after choices", "toggle")
            vbox:
                xsize 430
                spacing 22
                text "03  /  声音" style "ch_page_heading"
                null height 18
                if config.has_music:
                    text "背景音乐" style "ch_page_text"
                    bar value Preference("music volume") style "ch_volume"
                if config.has_sound:
                    text "环境与音效" style "ch_page_text"
                    bar value Preference("sound volume") style "ch_volume"
                if config.has_voice:
                    text "角色配音" style "ch_page_text"
                    bar value Preference("voice volume") style "ch_volume"
                null height 18
                textbutton "全部静音" style "ch_setting_button" action Preference("all mute", "toggle")

screen ch_about():
    use ch_page_shell("关于"):
        add Solid("#bba47740") xpos 660 ypos 34 xsize 1 ysize 600
        vbox:
            xpos 20
            ypos 112
            xsize 610
            spacing 28
            text "そして" font "fonts/ShipporiMincho-SemiBold.ttf" size 32 color "#d6be8d" xalign 0.5
            text "{rb}只因{/rb}{rt}チキン{/rt}もいなくなった":
                font "fonts/ShipporiMincho-SemiBold.ttf"
                size 36
                ruby_style style.ch_ruby
                line_leading 24
                color "#efe7d8"
                xalign 0.5
            text "无只因生还" style "ch_page_heading" size 29 xalign 0.5
            null height 32
            text "从一次偶遇，走向失踪与星辰的谜团。" style "ch_page_text" size 23 xalign 0.5
            text "[ch_edition_name]" style "ch_page_text" size 22 color "#a5afbe" xalign 0.5
            text "Version [config.version]" style "ch_page_text" size 18 color "#7c8797" xalign 0.5
        viewport:
            xpos 728
            ypos 30
            xsize 790
            ysize 670
            mousewheel True
            draggable True
            scrollbars "vertical"
            vbox:
                spacing 20
                text "作品介绍" style "ch_page_heading"
                text "将中文接龙小说认真改编为日语视觉小说，\n再以中文汉化呈现。" style "ch_page_text"
                text "完全线性剧情 · 中日双语字幕" style "ch_page_text" color "#d6be8d"
                text "当前收录\n第一章「面包与离家少女」\n第二章「消失的首席与星辰的求救信号」" style "ch_page_text"
                text "第一章、第二章均已接入日语角色配音。" style "ch_page_text" size 22 color "#a5afbe"
                null height 12
                text "制作与素材" style "ch_page_heading"
                text "原作  /  中文接龙小说《无只因生还》" style "ch_page_text"
                text "日语改编 · 中文汉化 · 演出\n本项目制作" style "ch_page_text"
                text "美术\n使用图像生成工具辅助制作" style "ch_page_text"
                text "字体\n思源宋体 / 思源黑体 · Adobe\nShippori Mincho" style "ch_page_text"
                text "游戏引擎\nRen'Py [renpy.version_only]" style "ch_page_text"
                null height 20
                text "引擎许可" style "ch_page_heading" size 26
                text "[renpy.license!t]" style "ch_page_text" size 18 xmaximum 730

screen ch_confirm_panel(message, yes_action, no_action, yes_label="确定", no_label="取消"):
    add Solid("#080f1ad4")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 920
        padding (70, 52)
        background Solid("#152133f5")
        foreground None
        vbox:
            spacing 36
            xfill True
            add Solid("#cbb581") xalign 0.5 xsize 120 ysize 1
            text message style "ch_page_heading" size 32 xalign 0.5 textalign 0.5 xmaximum 760
            hbox:
                xalign 0.5
                spacing 60
                textbutton yes_label style "ch_page_button" action yes_action
                textbutton no_label style "ch_page_button" action no_action default_focus True

screen ch_exit_confirm():
    modal True
    zorder 200
    use ch_confirm_panel("要离开吗？", Quit(confirm=False), Hide("ch_exit_confirm"), "返回桌面", "留在这里")
    key "game_menu" action Hide("ch_exit_confirm")
