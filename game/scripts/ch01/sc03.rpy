# Generated from scripts/ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source scripts/zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in scripts/staging/ch01/directions.json.

label ch01_sc03:
    # ch01_sc03_dir001
    $ ch_voice(None, "")
    $ ch_stop_audio()
    call ch_card("ch01_interlude") from ch01_interlude_return
    window hide None
    scene ch_bg locker_empty
    show ch_maxi enthusiastic at ch_maxi_position(320)
    with Dissolve(0.6)
    $ ch_audio("gym_room")

    # ch01_sc03_001
    window show None
    $ ch_line_id = "ch01_sc03_001"
    $ ch_voice('maxi', "ch01_sc03_001")
    ch_maxi "最近的话……就这个吧。明天十点半。哎，这个——" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}近い日だと……これか。明日の十時半。おい、これ――{/font}{/color}{/size}") id ch01_sc03_001

    # ch01_sc03_dir002
    $ ch_voice(None, "")
    window hide
    hide ch_maxi
    with dissolve
    pause 0.9
    show ch_maxi annoyed at ch_maxi_position(320)
    with dissolve

    # ch01_sc03_002
    window show None
    $ ch_line_id = "ch01_sc03_002"
    $ ch_voice('maxi', "ch01_sc03_002")
    ch_maxi "……已经走了啊。咦，连我的水也拿走了！" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……帰ってんのかよ。あれ、俺の水まで！{/font}{/color}{/size}") id ch01_sc03_002

    # ch01_sc03_003
    window show None
    $ ch_line_id = "ch01_sc03_003"
    $ ch_voice('maxi', "ch01_sc03_003")
    ch_maxi "下次我非把你整瓶沐浴露都用光不可！" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}次はボディソープ、一本まるごと使ってやるからな！{/font}{/color}{/size}") id ch01_sc03_003

    return
