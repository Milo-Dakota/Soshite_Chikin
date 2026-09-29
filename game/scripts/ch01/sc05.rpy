# Generated from script_ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source script_zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in tools/build_ch01.py.

label ch01_sc05:
    # ch01_sc05_dir001
    $ ch_voice(None, "")
    window hide None
    scene ch_cg table
    with fade
    $ ch_audio("daily")
    $ ch_audio("restaurant_room")

    # ch01_sc05_001
    window show None
    $ ch_line_id = "ch01_sc05_001"
    $ ch_voice(None, "ch01_sc05_001")
    ch_thought "……真安静。虽然我吃饭时也不怎么说话，可这也太……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……静かだ。食事中はあまり話さないほうだけど、さすがにこれは。{/font}{/color}{/size}") id ch01_sc05_001

    # ch01_sc05_002
    window show None
    $ ch_line_id = "ch01_sc05_002"
    $ ch_voice(None, "ch01_sc05_002")
    ch_thought "说“到那里再聊”的人，可是我啊。总得说点什么……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}『続きは、そこで』なんて言ったの、俺だしな。何か……。{/font}{/color}{/size}") id ch01_sc05_002

    # ch01_sc05_003
    window show None
    $ ch_line_id = "ch01_sc05_003"
    $ ch_voice(None, "ch01_sc05_003")
    ch_qixing "姓名？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}名前は？{/font}{/color}{/size}") id ch01_sc05_003

    # ch01_sc05_004
    window show None
    $ ch_line_id = "ch01_sc05_004"
    $ ch_voice('chinatsu', "ch01_sc05_004")
    ch_girl "千夏……我叫岛田千夏。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}千夏……島田千夏です。{/font}{/color}{/size}") id ch01_sc05_004

    # ch01_sc05_005
    window show None
    $ ch_line_id = "ch01_sc05_005"
    $ ch_voice(None, "ch01_sc05_005")
    ch_qixing "年龄……不，不对。刚才那句——" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}年齢は……いや、違う。今のは――{/font}{/color}{/size}") id ch01_sc05_005

    # ch01_sc05_dir002
    $ ch_voice(None, "")
    window hide None
    scene ch_bg restaurant
    show ch_qixing neutral at ch_seated_left
    show ch_chinatsu smile at ch_seated_right
    with dissolve
    pause 0.5
    show ch_chinatsu guarded at ch_seated_right
    with dissolve

    # ch01_sc05_006
    window show None
    $ ch_line_id = "ch01_sc05_006"
    $ ch_voice('chinatsu', "ch01_sc05_006")
    ch_chinatsu "十……七岁。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}じゅう……七です。{/font}{/color}{/size}") id ch01_sc05_006

    # ch01_sc05_007
    show ch_qixing bemused at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_007"
    $ ch_voice(None, "ch01_sc05_007")
    ch_thought "刚才不是才听她说过吗。职业病也该有个限度。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}さっき聞いたばかりじゃないか。職業病にもほどがある。{/font}{/color}{/size}") id ch01_sc05_007

    # ch01_sc05_008
    window show None
    $ ch_line_id = "ch01_sc05_008"
    $ ch_voice('chinatsu', "ch01_sc05_008")
    ch_chinatsu "……您说话的样子，像警察一样。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……おまわりさんみたいな、話し方ですね。{/font}{/color}{/size}") id ch01_sc05_008

    # ch01_sc05_009
    window show None
    $ ch_line_id = "ch01_sc05_009"
    $ ch_voice(None, "ch01_sc05_009")
    ch_qixing "是吗？说不定，我还真是警察呢？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}そう？　実は本当に警察官だ、って可能性もあるんじゃない？{/font}{/color}{/size}") id ch01_sc05_009

    # ch01_sc05_010
    show ch_chinatsu downcast at ch_seated_right
    show ch_qixing serious at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_010"
    $ ch_voice('chinatsu', "ch01_sc05_010")
    ch_chinatsu "……希望不是。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……そうじゃないと、いいな。{/font}{/color}{/size}") id ch01_sc05_010

    # ch01_sc05_011
    window show None
    $ ch_line_id = "ch01_sc05_011"
    $ ch_voice('chinatsu', "ch01_sc05_011")
    ch_chinatsu "如果是警察，就会把离家出走的孩子送回父母身边吧？我不要那样。……至少，现在还不想。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}おまわりさんなら、家出した子は親のところへ連れて帰るでしょう？　それは嫌。……今は、まだ。{/font}{/color}{/size}") id ch01_sc05_011

    # ch01_sc05_012
    window show None
    $ ch_line_id = "ch01_sc05_012"
    $ ch_voice(None, "ch01_sc05_012")
    ch_thought "话到了嘴边，又咽了回去。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}言いかけた言葉を、飲み込んだ。{/font}{/color}{/size}") id ch01_sc05_012

    # ch01_sc05_013
    window show None
    $ ch_line_id = "ch01_sc05_013"
    $ ch_voice(None, "ch01_sc05_013")
    ch_qixing "可是，像你这么大的孩子，不靠父母生活，会很辛苦吧。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}でも、君くらいの子が、親を頼らずに暮らすのは大変だろ。{/font}{/color}{/size}") id ch01_sc05_013

    # ch01_sc05_dir003
    $ ch_voice(None, "")
    window hide None
    scene ch_cg two_fingers
    with dissolve
    pause 0.4

    # ch01_sc05_014
    window show None
    $ ch_line_id = "ch01_sc05_014"
    $ ch_voice('chinatsu', "ch01_sc05_014")
    ch_chinatsu "首先，请不要把我当小孩子。其次，养活自己这点事，我还是做得到的。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}まず、子ども扱いしないでください。それから、自分で食べていくくらい、できます。{/font}{/color}{/size}") id ch01_sc05_014

    # ch01_sc05_015
    window show None
    $ ch_line_id = "ch01_sc05_015"
    $ ch_voice('chinatsu', "ch01_sc05_015")
    ch_chinatsu "别看我这样，我也是个小有名气的小提琴手哦。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}私、これでも少しは名の知られたヴァイオリニストなんですよ。{/font}{/color}{/size}") id ch01_sc05_015

    # ch01_sc05_016
    window show None
    $ ch_line_id = "ch01_sc05_016"
    $ ch_voice('chinatsu', "ch01_sc05_016")
    ch_chinatsu "要不是一直被那样逼着练……我想，我应该还挺喜欢拉琴的。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}あんなに無理にやらされなかったら……弾くの、けっこう好きだったと思うんです。{/font}{/color}{/size}") id ch01_sc05_016

    # ch01_sc05_dir004
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_cg violin
    with dissolve
    pause 0.8

    # ch01_sc05_017
    window show None
    $ ch_line_id = "ch01_sc05_017"
    $ ch_voice(None, "ch01_sc05_017")
    ch_thought "跟刚才，简直判若两人。……原来，她也会这样笑啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}さっきまでとは、まるで違う顔だ。……こんなふうにも、笑うんだな。{/font}{/color}{/size}") id ch01_sc05_017

    # ch01_sc05_dir005
    $ ch_voice(None, "")
    stop music fadeout 0.8
    window hide None
    scene ch_cg car
    with dissolve
    pause 0.8

    # ch01_sc05_018
    window show None
    $ ch_line_id = "ch01_sc05_018"
    $ ch_voice(None, "ch01_sc05_018")
    ch_qixing "……怎么了？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……どうした？{/font}{/color}{/size}") id ch01_sc05_018

    # ch01_sc05_019
    window hide None
    scene ch_bg restaurant
    show ch_qixing neutral at ch_seated_left
    show ch_chinatsu afraid at ch_seated_right
    with dissolve
    window show None
    $ ch_line_id = "ch01_sc05_019"
    $ ch_voice('chinatsu', "ch01_sc05_019")
    ch_chinatsu "啊……是我爸爸。梅川备代……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}あ……父です。{rb}梅川備代{/rb}{rt}サスペンダーなし{/rt}……。{/font}{/color}{/size}") id ch01_sc05_019

    # ch01_sc05_020
    show ch_qixing bemused at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_020"
    $ ch_voice(None, "ch01_sc05_020")
    ch_qixing "没穿背带？可他明明穿着啊……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}サスペンダー、なし？　いや、してるけど……。{/font}{/color}{/size}") id ch01_sc05_020

    # ch01_sc05_021
    window show None
    $ ch_line_id = "ch01_sc05_021"
    $ ch_voice('chinatsu', "ch01_sc05_021")
    ch_chinatsu "不是啦。那是我爸爸的名字。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}違いますっ。父の、名前です。{/font}{/color}{/size}") id ch01_sc05_021

    # ch01_sc05_022
    window show None
    $ ch_line_id = "ch01_sc05_022"
    $ ch_voice(None, "ch01_sc05_022")
    ch_thought "原来是名字。……也太容易听错了。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}名前だったのか。……紛らわしいな。{/font}{/color}{/size}") id ch01_sc05_022

    # ch01_sc05_023
    window show None
    $ ch_line_id = "ch01_sc05_023"
    $ ch_voice(None, "ch01_sc05_023")
    ch_qixing "那，梅川小姐——" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}じゃあ、梅川さん――{/font}{/color}{/size}") id ch01_sc05_023

    # ch01_sc05_024
    show ch_qixing serious at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_024"
    $ ch_voice('chinatsu', "ch01_sc05_024")
    ch_chinatsu "请别这样叫我。我就是想逃离那个家，才说自己叫千夏的。叫我千夏就好了。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}その呼び方はやめてください。家から逃げたくて、千夏って名乗ったんです。千夏で、いいですから。{/font}{/color}{/size}") id ch01_sc05_024

    # ch01_sc05_025
    window show None
    $ ch_line_id = "ch01_sc05_025"
    $ ch_voice(None, "ch01_sc05_025")
    ch_qixing "……知道了。千夏。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……分かった。千夏。{/font}{/color}{/size}") id ch01_sc05_025

    # ch01_sc05_026
    window show None
    $ ch_line_id = "ch01_sc05_026"
    $ ch_voice(None, "ch01_sc05_026")
    ch_thought "按理说，应该把她送到父亲身边才对。可现在，要是被她知道我是警察……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}本来なら、父親のところへ連れていくべきなんだろう。でも今、警察官だと知られたら……。{/font}{/color}{/size}") id ch01_sc05_026

    # ch01_sc05_dir006
    $ ch_voice(None, "")
    window hide
    $ ch_audio("door")
    window hide None
    scene ch_bg restaurant_public
    show ch_beidai bow at ch_beidai_public
    with Dissolve(0.6)
    pause 5.0
    stop sound fadeout 0.15

    # ch01_sc05_027
    window show None
    $ ch_line_id = "ch01_sc05_027"
    $ ch_voice('beidai', "ch01_sc05_027")
    ch_beidai "正在用餐的各位，大家好。我是拥有二十年半演奏经历的钢琴家，梅川备代。我的爱好是——" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}お食事中の皆さま、こんにちは。演奏歴二十年半、ピアニストの{rb}梅川備代{/rb}{rt}サスペンダーなし{/rt}です。好きなものは――{/font}{/color}{/size}") id ch01_sc05_027

    # ch01_sc05_dir007
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_cg recital
    with dissolve
    $ ch_audio("recital")
    $ renpy.music.set_volume(0.35, delay=0.5, channel="ch_ambience")
    if renpy.loadable(CH_AUDIO["recital"][0]):
        show screen ch_recital_hint
        pause 18.0
    else:
        pause 2.0
    hide screen ch_recital_hint
    with None
    stop music fadeout 1.3
    $ renpy.music.set_volume(1.0, delay=0.8, channel="ch_ambience")
    window hide None
    scene ch_bg restaurant_public
    show ch_beidai bow at ch_beidai_public
    with dissolve
    pause 1.0
    window hide None
    scene ch_bg restaurant
    show ch_qixing bemused at ch_seated_left
    show ch_chinatsu afraid at ch_seated_right
    with Dissolve(0.5)
    $ ch_audio("door")
    pause 5.0
    stop sound fadeout 0.15

    # ch01_sc05_028
    window show None
    $ ch_line_id = "ch01_sc05_028"
    $ ch_voice(None, "ch01_sc05_028")
    ch_thought "……走了。刚才那算什么啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……帰った。今のは、何だったんだ。{/font}{/color}{/size}") id ch01_sc05_028

    # ch01_sc05_dir008
    $ ch_voice(None, "")
    show ch_qixing neutral at ch_seated_left
    show ch_chinatsu guarded at ch_seated_right
    with dissolve
    $ ch_audio("warm")

    # ch01_sc05_029
    window show None
    $ ch_line_id = "ch01_sc05_029"
    $ ch_voice('chinatsu', "ch01_sc05_029")
    ch_chinatsu "对不起，让您看笑话了。我爸爸，他有点……爱出风头。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}すみません。変なところ、見せちゃって。父、ちょっと……目立ちたがりで。{/font}{/color}{/size}") id ch01_sc05_029

    # ch01_sc05_030
    show ch_qixing soft at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_030"
    $ ch_voice(None, "ch01_sc05_030")
    ch_qixing "没事，不用在意。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}いや、気にしなくていいよ。{/font}{/color}{/size}") id ch01_sc05_030

    # ch01_sc05_dir009
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_bg restaurant_empty
    with dissolve
    pause 1.0
    show ch_qixing neutral at ch_seated_left
    show ch_chinatsu smile at ch_seated_right
    with dissolve

    # ch01_sc05_031
    show ch_qixing bemused at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_031"
    $ ch_voice(None, "ch01_sc05_031")
    ch_thought "什么时候吃了这么多？我才刚吃了几口……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}いつの間に、こんなに食べたんだ。俺、まだ少ししか……。{/font}{/color}{/size}") id ch01_sc05_031

    # ch01_sc05_032
    show ch_qixing soft at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_032"
    $ ch_voice(None, "ch01_sc05_032")
    ch_thought "算了，也好。看她吃得这么香，连我的心情都好了起来。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}まあ、いいか。これだけ食べてくれると、こっちまで気分がいい。{/font}{/color}{/size}") id ch01_sc05_032

    # ch01_sc05_033
    window show None
    $ ch_line_id = "ch01_sc05_033"
    $ ch_voice(None, "ch01_sc05_033")
    ch_qixing "吃饱了吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}お腹、いっぱいになった？{/font}{/color}{/size}") id ch01_sc05_033

    # ch01_sc05_dir010
    $ ch_voice(None, "")
    show ch_qixing serious at ch_seated_left
    with Dissolve(0.2)
    pause 0.5

    # ch01_sc05_034
    window show None
    $ ch_line_id = "ch01_sc05_034"
    $ ch_voice(None, "ch01_sc05_034")
    ch_qixing "那，我只问一句。……你打算什么时候回家？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}じゃあ、一つだけ。……いつ、家に帰るつもり？{/font}{/color}{/size}") id ch01_sc05_034

    # ch01_sc05_dir011
    $ ch_voice(None, "")
    show ch_chinatsu guarded at ch_seated_right
    with dissolve
    pause 0.4

    # ch01_sc05_035
    show ch_qixing soft at ch_seated_left
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_035"
    $ ch_voice(None, "ch01_sc05_035")
    ch_qixing "如果还不想回去，也可以先在我那里住一阵子。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}まだ帰りたくないなら、しばらく俺のところにいてもいいよ。{/font}{/color}{/size}") id ch01_sc05_035

    # ch01_sc05_dir012
    $ ch_voice(None, "")
    show ch_chinatsu surprised at ch_seated_right
    with Dissolve(0.2)
    pause 0.6

    # ch01_sc05_036
    show ch_chinatsu smile at ch_seated_right
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc05_036"
    $ ch_voice('chinatsu', "ch01_sc05_036")
    ch_chinatsu "……好。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……はい。{/font}{/color}{/size}") id ch01_sc05_036

    # ch01_sc05_037
    window show None
    $ ch_line_id = "ch01_sc05_037"
    $ ch_voice(None, "ch01_sc05_037")
    ch_qixing "那，等我一下。我去结账。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}じゃ、ちょっと待ってて。会計してくる。{/font}{/color}{/size}") id ch01_sc05_037

    return
