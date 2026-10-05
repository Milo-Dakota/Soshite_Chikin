# Generated from scripts/ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source scripts/zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in scripts/staging/ch01/directions.json.

label ch01_sc01:
    # ch01_sc01_dir001
    $ ch_voice(None, "")
    window hide None
    scene ch_bg street
    show ch_qixing neutral at ch_left
    with Dissolve(0.6)
    $ ch_audio("daily")
    $ ch_audio("street_room")

    # ch01_sc01_001
    window show None
    $ ch_line_id = "ch01_sc01_001"
    $ ch_voice(None, "ch01_sc01_001")
    ch_thought "二月里，倒是挺暖和。习惯了北方的冷天，穿着这件外套甚至有点热。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}二月にしては、暖かい。北の寒さに慣れた身には、このコートも少し暑いくらいだ。{/font}{/color}{/size}") id ch01_sc01_001

    # ch01_sc01_002
    window show None
    $ ch_line_id = "ch01_sc01_002"
    $ ch_voice(None, "ch01_sc01_002")
    ch_thought "两个月的假期，也快结束了。就算在休假，当警察的也不能荒废锻炼。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}二か月の休暇も、もう終わる。休みだからって、警察官が体をなまらせるわけにはいかない。{/font}{/color}{/size}") id ch01_sc01_002

    # ch01_sc01_003
    window show None
    $ ch_line_id = "ch01_sc01_003"
    $ ch_voice(None, "ch01_sc01_003")
    ch_thought "到健身房要走十分钟。每天来回散步二十分钟，也已经成了习惯。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}ジムまでは歩いて十分。往復二十分の散歩も、すっかり日課になった。{/font}{/color}{/size}") id ch01_sc01_003

    # ch01_sc01_004
    window show None
    $ ch_line_id = "ch01_sc01_004"
    $ ch_voice(None, "ch01_sc01_004")
    ch_thought "再拐过前面的路口……啊，忘带水杯了。待会儿买两瓶水吧。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}次の角を曲がれば……あ、水筒を忘れた。あとで水を二本買うか。{/font}{/color}{/size}") id ch01_sc01_004

    # ch01_sc01_005
    window show None
    $ ch_line_id = "ch01_sc01_005"
    $ ch_voice(None, "ch01_sc01_005")
    ch_thought "这块面包也不好办。早上吃的碳水已经够多了啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}このパンも、どうしよう。朝の炭水化物は、もう十分とったんだけどな。{/font}{/color}{/size}") id ch01_sc01_005

    # ch01_sc01_dir002
    $ ch_voice(None, "")
    window hide None
    scene ch_cg sleeve
    with dissolve

    # ch01_sc01_006
    window show None
    $ ch_line_id = "ch01_sc01_006"
    $ ch_voice('chinatsu', "ch01_sc01_006")
    ch_girl "那个……这个，可以给我吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}あの……それ、もらってもいいですか？{/font}{/color}{/size}") id ch01_sc01_006

    # ch01_sc01_007
    window show None
    $ ch_line_id = "ch01_sc01_007"
    $ ch_voice(None, "ch01_sc01_007")
    ch_thought "脸色不太好。嘴唇干得厉害，眼睛里也满是血丝。……哭过吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}顔色が悪い。唇も乾いてるし、目も充血している。……泣いていたのか？{/font}{/color}{/size}") id ch01_sc01_007

    # ch01_sc01_008
    window show None
    $ ch_line_id = "ch01_sc01_008"
    $ ch_voice(None, "ch01_sc01_008")
    ch_qixing "身体不舒服吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}具合、悪いのか？{/font}{/color}{/size}") id ch01_sc01_008

    # ch01_sc01_009
    window show None
    $ ch_line_id = "ch01_sc01_009"
    $ ch_voice(None, "ch01_sc01_009")
    ch_thought "也许没怎么吃东西。看着也像没睡好。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}ろくに食べていないのかもしれない。寝不足もありそうだ。{/font}{/color}{/size}") id ch01_sc01_009

    # ch01_sc01_010
    window show None
    $ ch_line_id = "ch01_sc01_010"
    $ ch_voice('chinatsu', "ch01_sc01_010")
    ch_girl "不、不是……不是那个意思。求你，把那个……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}ち、違……そうじゃなくて。お願い、それを……。{/font}{/color}{/size}") id ch01_sc01_010

    # ch01_sc01_dir003
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_cg bread
    with dissolve
    pause 1.2

    # ch01_sc01_011
    window show None
    $ ch_line_id = "ch01_sc01_011"
    $ ch_voice(None, "ch01_sc01_011")
    ch_thought "啊……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}あ……。{/font}{/color}{/size}") id ch01_sc01_011

    # ch01_sc01_012
    window hide None
    scene ch_bg street
    show ch_qixing serious at ch_left
    with dissolve
    window show None
    $ ch_line_id = "ch01_sc01_012"
    $ ch_voice(None, "ch01_sc01_012")
    ch_thought "左臂内侧有一片发青。是……淤青吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}左腕の裏、青くなっていた。あざ……だろうか。{/font}{/color}{/size}") id ch01_sc01_012

    # ch01_sc01_dir004
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_bg street
    show ch_qixing neutral at ch_left
    with dissolve
    pause 0.5

    return
