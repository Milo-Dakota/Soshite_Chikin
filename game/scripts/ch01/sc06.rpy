# Generated from script_ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source script_zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in tools/build_ch01.py.

label ch01_sc06:
    # ch01_sc06_dir001
    $ ch_voice(None, "")
    window hide None
    scene ch_bg street
    show ch_qixing neutral at ch_left
    show ch_chinatsu smile at ch_right
    with fade
    $ ch_audio("warm")
    $ ch_audio("street_room")

    # ch01_sc06_001
    window show None
    $ ch_line_id = "ch01_sc06_001"
    $ ch_voice('chinatsu', "ch01_sc06_001")
    ch_chinatsu "……谢谢你。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……ありがとう。{/font}{/color}{/size}") id ch01_sc06_001

    # ch01_sc06_002
    window show None
    $ ch_line_id = "ch01_sc06_002"
    $ ch_voice(None, "ch01_sc06_002")
    ch_qixing "嗯。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}ん。{/font}{/color}{/size}") id ch01_sc06_002

    # ch01_sc06_003
    window show None
    $ ch_line_id = "ch01_sc06_003"
    $ ch_voice(None, "ch01_sc06_003")
    ch_thought "……啊，是在对我说啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……ああ、俺に言ってるのか。{/font}{/color}{/size}") id ch01_sc06_003

    # ch01_sc06_dir002
    $ ch_voice(None, "")
    window hide None
    scene ch_cg walk
    with dissolve
    pause 0.5

    # ch01_sc06_004
    window show None
    $ ch_line_id = "ch01_sc06_004"
    $ ch_voice('chinatsu', "ch01_sc06_004")
    ch_chinatsu "总觉得，你像个捡了流浪猫回家的大叔。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}なんだか、野良猫を拾ったおじさんみたい。{/font}{/color}{/size}") id ch01_sc06_004

    # ch01_sc06_005
    window hide None
    scene ch_bg street
    show ch_qixing surprised at ch_left
    show ch_chinatsu smile at ch_right
    with dissolve
    window show None
    $ ch_line_id = "ch01_sc06_005"
    $ ch_voice(None, "ch01_sc06_005")
    ch_qixing "大叔……我才二十岁啊！" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}おじさんって……俺、まだ二十歳なんだけど！{/font}{/color}{/size}") id ch01_sc06_005

    # ch01_sc06_dir003
    $ ch_voice(None, "")
    window hide
    pause 1.0
    $ ch_stop_audio()
    window hide None
    scene black
    with fade
    call ch_card("第一章・終", "パンと、家出少女") from ch01_ending_return

    return
