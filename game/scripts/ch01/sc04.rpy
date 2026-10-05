# Generated from scripts/ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source scripts/zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in scripts/staging/ch01/directions.json.

label ch01_sc04:
    # ch01_sc04_dir001
    $ ch_voice(None, "")
    call ch_card("ch01_walk") from ch01_walk_return
    window hide None
    scene ch_bg street
    show ch_qixing troubled at ch_left
    show screen ch_phone("父さん")
    with Dissolve(0.6)
    $ ch_audio("street_room")

    # ch01_sc04_001
    window show None
    $ ch_line_id = "ch01_sc04_001"
    $ ch_voice(None, "ch01_sc04_001")
    ch_thought "爸。……明明只要再按一下就好了。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}父さん。……あと一回、押すだけなんだよな。{/font}{/color}{/size}") id ch01_sc04_001

    # ch01_sc04_002
    window show None
    $ ch_line_id = "ch01_sc04_002"
    $ ch_voice(None, "ch01_sc04_002")
    ch_thought "一年半了。像这样犹豫不决，已经有过多少次了呢。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}一年半。こんなふうに迷ったことなら、何度もある。{/font}{/color}{/size}") id ch01_sc04_002

    # ch01_sc04_003
    window show None
    $ ch_line_id = "ch01_sc04_003"
    $ ch_voice(None, "ch01_sc04_003")
    ch_thought "当初说着非要闯出个样子来，就这么跑了出来。事到如今，实在不知道该怎么开口。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}一人前になってやる、なんて飛び出してきた手前、どんな顔で話せばいいのか分からない。{/font}{/color}{/size}") id ch01_sc04_003

    # ch01_sc04_dir002
    $ ch_voice(None, "")
    hide screen ch_phone
    window hide None
    scene ch_cg water
    with dissolve

    # ch01_sc04_004
    window show None
    $ ch_line_id = "ch01_sc04_004"
    $ ch_voice(None, "ch01_sc04_004")
    ch_qixing "……你还在这里啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……まだ、ここにいたのか。{/font}{/color}{/size}") id ch01_sc04_004

    # ch01_sc04_dir003
    $ ch_voice(None, "")
    pause 0.5

    # ch01_sc04_005
    window show None
    $ ch_line_id = "ch01_sc04_005"
    $ ch_voice(None, "ch01_sc04_005")
    ch_qixing "不回家吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}家に帰らないの？{/font}{/color}{/size}") id ch01_sc04_005

    # ch01_sc04_006
    window show None
    $ ch_line_id = "ch01_sc04_006"
    $ ch_voice(None, "ch01_sc04_006")
    ch_qixing "……离家出走？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……家出？{/font}{/color}{/size}") id ch01_sc04_006

    # ch01_sc04_dir004
    $ ch_voice(None, "")
    pause 0.7

    # ch01_sc04_007
    window show None
    $ ch_line_id = "ch01_sc04_007"
    $ ch_voice(None, "ch01_sc04_007")
    ch_thought "露出这种表情，让人怎么放着不管啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}その顔じゃ、放っておけないだろ。{/font}{/color}{/size}") id ch01_sc04_007

    # ch01_sc04_008
    window show None
    $ ch_line_id = "ch01_sc04_008"
    $ ch_voice(None, "ch01_sc04_008")
    ch_qixing "能站起来吗？走，去吃点东西吧。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}立てる？　何か食べに行こう。{/font}{/color}{/size}") id ch01_sc04_008

    # ch01_sc04_009
    window show None
    $ ch_line_id = "ch01_sc04_009"
    $ ch_voice('chinatsu', "ch01_sc04_009")
    ch_girl "……好。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……はい。{/font}{/color}{/size}") id ch01_sc04_009

    # ch01_sc04_dir005
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_cg support
    with dissolve
    $ ch_audio("warm")
    pause 0.6

    # ch01_sc04_010
    window show None
    $ ch_line_id = "ch01_sc04_010"
    $ ch_voice(None, "ch01_sc04_010")
    ch_qixing "小心！" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}危ない！{/font}{/color}{/size}") id ch01_sc04_010

    # ch01_sc04_011
    window show None
    $ ch_line_id = "ch01_sc04_011"
    $ ch_voice(None, "ch01_sc04_011")
    ch_thought "手臂上传来一丝温热。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}腕に、かすかな温かさが伝わってくる。{/font}{/color}{/size}") id ch01_sc04_011

    # ch01_sc04_012
    window show None
    $ ch_line_id = "ch01_sc04_012"
    $ ch_voice('chinatsu', "ch01_sc04_012")
    ch_girl "……谢、谢谢。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……ありがとう、ございます。{/font}{/color}{/size}") id ch01_sc04_012

    # ch01_sc04_dir006
    $ ch_voice(None, "")
    window hide None
    scene ch_bg street
    show ch_qixing neutral at ch_left
    show ch_chinatsu embarrassed at ch_right
    with dissolve
    pause 0.5

    # ch01_sc04_013
    window show None
    $ ch_line_id = "ch01_sc04_013"
    $ ch_voice(None, "ch01_sc04_013")
    ch_qixing "为什么离家出走？啊，只是一个路过的人随口问问。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}どうして家を出たんだ？　ああ、ただの通りすがりの質問だよ。{/font}{/color}{/size}") id ch01_sc04_013

    # ch01_sc04_014
    show ch_chinatsu downcast at ch_right
    show ch_qixing serious at ch_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc04_014"
    $ ch_voice('chinatsu', "ch01_sc04_014")
    ch_girl "从小，大家就说我有音乐天赋……妈妈是舞者，爸爸是钢琴家。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}小さい頃から、音楽の才能があるって言われて……。母は踊り手で、父はピアニストなんです。{/font}{/color}{/size}") id ch01_sc04_014

    # ch01_sc04_015
    window show None
    $ ch_line_id = "ch01_sc04_015"
    $ ch_voice('chinatsu', "ch01_sc04_015")
    ch_girl "他们都希望我也走音乐这条路，所以一直让我学小提琴……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}二人とも、私にも音楽の道に進んでほしくて。ずっと、ヴァイオリンを……。{/font}{/color}{/size}") id ch01_sc04_015

    # ch01_sc04_016
    window show None
    $ ch_line_id = "ch01_sc04_016"
    $ ch_voice('chinatsu', "ch01_sc04_016")
    ch_girl "明明已经十七岁了，每天却只有练习和演奏。我实在喘不过气……就什么也没带，跑出来了。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}もう十七なのに、練習と演奏ばかり。息が詰まって……何も持たずに、飛び出してきちゃいました。{/font}{/color}{/size}") id ch01_sc04_016

    # ch01_sc04_017
    window show None
    $ ch_line_id = "ch01_sc04_017"
    $ ch_voice(None, "ch01_sc04_017")
    ch_thought "……这样啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……そうか。{/font}{/color}{/size}") id ch01_sc04_017

    # ch01_sc04_018
    show ch_qixing soft at ch_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc04_018"
    $ ch_voice(None, "ch01_sc04_018")
    ch_qixing "附近有家不错的西餐厅。光吃面包，肯定不够吧。剩下的，到那里再说。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}近くに、うまい洋食屋があるんだ。パンだけじゃ足りないだろ。続きは、そこで。{/font}{/color}{/size}") id ch01_sc04_018

    # ch01_sc04_019
    window show None
    $ ch_line_id = "ch01_sc04_019"
    $ ch_voice(None, "ch01_sc04_019")
    ch_thought "离家出走的事，待会儿再谈。先填饱肚子才行。……何况，我还有那家的会员卡。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}家出の話は、あとだ。まずは腹を満たさないと。……あそこの会員カードも、あることだし。{/font}{/color}{/size}") id ch01_sc04_019

    return
