# Generated from script_ja/ch01.yaml SHA256 99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd
# Chinese source script_zh/ch01.json SHA256 e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907
# Edit Japanese text in YAML; staging in tools/build_ch01.py.

label ch01_sc02:
    # ch01_sc02_dir001
    $ ch_voice(None, "")
    $ ch_audio("gym_room")
    window hide None
    scene ch_bg locker
    with fade

    # ch01_sc02_001
    window show None
    $ ch_line_id = "ch01_sc02_001"
    $ ch_voice(None, "ch01_sc02_001")
    ch_thought "今天也都是熟面孔。如今人人都讲究节能，肯特意跑来流汗的人，实在不多。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}今日も、いつもの顔ぶれだ。世の中は省エネ一色。わざわざ汗をかきに来る物好きは、そう多くない。{/font}{/color}{/size}") id ch01_sc02_001

    # ch01_sc02_dir002
    $ ch_voice(None, "")
    window hide
    window hide None
    scene ch_cg shower
    with dissolve
    $ ch_audio("shower")
    pause 0.6

    # ch01_sc02_002
    window show None
    $ ch_line_id = "ch01_sc02_002"
    $ ch_voice(None, "ch01_sc02_002")
    ch_thought "又忘带了？……不对，那家伙什么时候自己带过吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}また忘れたのか。……いや、あいつが自分で持ってきたこと、あったか？{/font}{/color}{/size}") id ch01_sc02_002

    # ch01_sc02_003
    window show None
    $ ch_line_id = "ch01_sc02_003"
    $ ch_voice(None, "ch01_sc02_003")
    ch_thought "马皙。在这里认识的朋友。据他自己说，这不叫邋遢，叫艺术家气质。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}{rb}馬皙{/rb}{rt}マー・シー{/rt}。ここで知り合った友人だ。本人いわく、だらしないんじゃなくて芸術家気質、らしい。{/font}{/color}{/size}") id ch01_sc02_003

    # ch01_sc02_004
    window show None
    $ ch_line_id = "ch01_sc02_004"
    $ ch_voice(None, "ch01_sc02_004")
    ch_thought "他很得意自己在艾昆剧院工作，不过我还一次都没去过。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}{rb}艾昆{/rb}{rt}アイクン{/rt}劇場で働いているのが自慢だけど、俺はまだ一度も行ったことがない。{/font}{/color}{/size}") id ch01_sc02_004

    # ch01_sc02_005
    window show None
    $ ch_line_id = "ch01_sc02_005"
    $ ch_voice('maxi', "ch01_sc02_005")
    ch_maxi "哎，你锻炼的时候，都听些什么啊？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}なあ、お前さ。トレーニング中、いつも何聴いてんの？{/font}{/color}{/size}") id ch01_sc02_005

    # ch01_sc02_006
    window show None
    $ ch_line_id = "ch01_sc02_006"
    $ ch_voice(None, "ch01_sc02_006")
    ch_qixing "也没什么……舒缓的钢琴曲之类的吧。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}さあ……落ち着くピアノ曲とか、そのへん。{/font}{/color}{/size}") id ch01_sc02_006

    # ch01_sc02_dir003
    $ ch_voice(None, "")
    $ ch_audio("gym_room")
    window hide None
    scene ch_bg locker
    show ch_qixing neutral at ch_left
    show ch_maxi neutral at ch_maxi_position(1690)
    with fade

    # ch01_sc02_007
    window show None
    $ ch_line_id = "ch01_sc02_007"
    $ ch_voice(None, "ch01_sc02_007")
    ch_thought "平时光是工作，就已经忙不过来了。至少听音乐的时候，想什么也不去考虑。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}普段は仕事だけで手いっぱいだ。音楽くらい、何も考えずに聴いていたい。{/font}{/color}{/size}") id ch01_sc02_007

    # ch01_sc02_008
    show ch_maxi enthusiastic at ch_maxi_position(1690)
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc02_008"
    $ ch_voice('maxi', "ch01_sc02_008")
    ch_maxi "这样啊。难得放假，培养点爱好呗。比如听听现场演奏什么的。我可以——" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}へえ。せっかく休みなんだし、趣味でもつくれよ。生の演奏とかさ。俺が――{/font}{/color}{/size}") id ch01_sc02_008

    # ch01_sc02_009
    window show None
    $ ch_line_id = "ch01_sc02_009"
    $ ch_voice(None, "ch01_sc02_009")
    ch_thought "也不错。反正时间有的是。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}悪くない。時間だけは、たっぷりある。{/font}{/color}{/size}") id ch01_sc02_009

    # ch01_sc02_dir004
    $ ch_voice(None, "")
    $ ch_audio("phone")
    show screen ch_phone("鄭局長", True)
    with dissolve

    # ch01_sc02_010
    show ch_qixing bemused at ch_left
    show ch_maxi neutral at ch_maxi_position(1690)
    with Dissolve(0.2)
    window show None
    $ ch_line_id = "ch01_sc02_010"
    $ ch_voice(None, "ch01_sc02_010")
    ch_qixing "……我可还在休假啊。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……今、休暇中なんだけどな。{/font}{/color}{/size}") id ch01_sc02_010

    # ch01_sc02_011
    stop sound
    hide screen ch_phone
    with dissolve
    window show None
    $ ch_line_id = "ch01_sc02_011"
    $ ch_voice('zheng', "ch01_sc02_011")
    ch_zheng "哟，看来这假休得挺舒服啊。什么时候回来？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}おう、いい休みを過ごしてるみたいだな。いつ戻る？{/font}{/color}{/size}") id ch01_sc02_011

    # ch01_sc02_012
    window show None
    $ ch_line_id = "ch01_sc02_012"
    $ ch_voice(None, "ch01_sc02_012")
    ch_qixing "再过两三天吧。还有点事没办完。倒是局长您，什么时候变得这么热爱工作了？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}あと二、三日です。ちょっと用事が残ってて。局長こそ、いつからそんなに仕事熱心に？{/font}{/color}{/size}") id ch01_sc02_012

    # ch01_sc02_013
    window show None
    $ ch_line_id = "ch01_sc02_013"
    $ ch_voice('zheng', "ch01_sc02_013")
    ch_zheng "还挺敢说。等你回来，看我怎么收拾你。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}言うじゃないか。戻ってきたら覚えてろよ。{/font}{/color}{/size}") id ch01_sc02_013

    # ch01_sc02_dir005
    $ ch_voice(None, "")
    pause 0.5

    # ch01_sc02_014
    window show None
    $ ch_line_id = "ch01_sc02_014"
    $ ch_voice('zheng', "ch01_sc02_014")
    ch_zheng "……过年回家了吗？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……正月は、実家に帰ったのか？{/font}{/color}{/size}") id ch01_sc02_014

    # ch01_sc02_dir006
    $ ch_voice(None, "")
    stop music fadeout 1.0
    show ch_qixing troubled at ch_left
    show ch_maxi concerned at ch_maxi_position(1690)
    with Dissolve(0.2)
    pause 0.7

    # ch01_sc02_015
    window show None
    $ ch_line_id = "ch01_sc02_015"
    $ ch_voice(None, "ch01_sc02_015")
    ch_qixing "没有……我跟家里说，要工作……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}いえ……仕事だって、言ってあるので……。{/font}{/color}{/size}") id ch01_sc02_015

    # ch01_sc02_016
    window show None
    $ ch_line_id = "ch01_sc02_016"
    $ ch_voice('zheng', "ch01_sc02_016")
    ch_zheng "我就知道。别一直这么犟着了，回去好好谈一次。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}やっぱりな。いつまでも意地を張ってないで、一度ちゃんと話してこい。{/font}{/color}{/size}") id ch01_sc02_016

    # ch01_sc02_017
    window show None
    $ ch_line_id = "ch01_sc02_017"
    $ ch_voice(None, "ch01_sc02_017")
    ch_qixing "……嗯。我知道。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……はい。分かってます。{/font}{/color}{/size}") id ch01_sc02_017

    # ch01_sc02_dir007
    $ ch_voice(None, "")
    hide screen ch_phone
    with dissolve

    # ch01_sc02_018
    window show None
    $ ch_line_id = "ch01_sc02_018"
    $ ch_voice('maxi', "ch01_sc02_018")
    ch_maxi "……跟家里闹矛盾了？" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}……家と、もめてんの？{/font}{/color}{/size}") id ch01_sc02_018

    # ch01_sc02_dir008
    $ ch_voice(None, "")
    hide ch_maxi
    with dissolve
    pause 0.5

    # ch01_sc02_019
    window show None
    $ ch_line_id = "ch01_sc02_019"
    $ ch_voice(None, "ch01_sc02_019")
    ch_thought "其实，连电话都没打。只是发了条简短的消息，拜了个年。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}本当は、電話さえしていない。新年の挨拶を、短いメッセージで送っただけだ。{/font}{/color}{/size}") id ch01_sc02_019

    # ch01_sc02_020
    window show None
    $ ch_line_id = "ch01_sc02_020"
    $ ch_voice(None, "ch01_sc02_020")
    ch_thought "跟父母吵了一架，一时冲动就跑来了杏城。工作和生活，好不容易才安定下来。" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}親とぶつかって、勢いで{rb}杏城{/rb}{rt}シンチェン{/rt}まで来た。仕事も、暮らしも、ようやく落ち着いた。{/font}{/color}{/size}") id ch01_sc02_020

    # ch01_sc02_021
    window show None
    $ ch_line_id = "ch01_sc02_021"
    $ ch_voice(None, "ch01_sc02_021")
    ch_thought "早就不生气了。可一说要回去，就……" (show_ja_text="{size=24}{color=#aebdce}{font=fonts/SourceHanSerifJP-Medium.otf}もう、怒ってなんかいない。それなのに、帰るとなると……。{/font}{/color}{/size}") id ch01_sc02_021

    return
