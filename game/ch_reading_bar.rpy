# Quiet reading controls, independent of subtitle layout.
style ch_reading_button is button:
    xsize 84
    ysize 44
    padding (8, 7)
    background None
    foreground None
    hover_foreground Transform(Solid("#cbb581"), ysize=1, yalign=1.0)
    selected_foreground Transform(Solid("#cbb58180"), ysize=1, yalign=1.0)

style ch_reading_button_text is default:
    font "fonts/SourceHanSansSC-Regular.otf"
    size 20
    color "#a5b0bf"
    hover_color "#fff0ce"
    selected_color "#d9c18e"
    insensitive_color "#596677"
    xalign 0.5
    yalign 0.5
    kerning 2

screen ch_reading_bar(compact=False):
    fixed:
        xalign 0.5
        yalign 1.0
        yoffset -8
        xsize 1776
        ysize 48
        text ch_chapter_label:
            font "fonts/SourceHanSerifSC-Medium.otf"
            size 18
            kerning 5
            color "#9c947f"
            xpos 64
            yalign 0.5
        hbox:
            xalign 1.0
            xoffset -56
            yalign 0.5
            spacing 10
            textbutton "回退" style "ch_reading_button" action Rollback()
            textbutton "历史" style "ch_reading_button" action ShowMenu("history")
            textbutton "快进" style "ch_reading_button" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton "自动" style "ch_reading_button" action Preference("auto-forward", "toggle")
            null width 20
            textbutton "保存" style "ch_reading_button" action ShowMenu("save")
            textbutton "读取" style "ch_reading_button" action ShowMenu("load")
            if not compact:
                textbutton "快存" style "ch_reading_button" action QuickSave()
                textbutton "快读" style "ch_reading_button" action QuickLoad()
            null width 20
            textbutton "设置" style "ch_reading_button" action ShowMenu("preferences")
