# Generated resource declarations; staging/text source: tools/build_ch02.py.
default ch_chapter_label = "第一章"

init python:
    def ch02_silence():
        # Immediate stop also prevents first-chapter/menu audio leaking in.
        for channel in ("music", "sound", "voice", "ch_ambience", "ch_diegetic"):
            renpy.music.stop(channel=channel, fadeout=0)
        renpy.music.set_audio_filter("voice", None)
        renpy.music.set_audio_filter("ch_diegetic", None)

define ch02_wengang = Character("文钢", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")
define ch02_theatre_staff = Character("剧院工作人员", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")
define ch02_house_driver = Character("司机", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")
define ch02_house_servant = Character("佣人", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")
define ch02_unknown_caller = Character("电话里的声音", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")
define ch02_notice = Character("寻人启事", screen="ch_say", what_style="ch_dialogue", who_style="ch_name", who_size=26, who_color="#cbb581")

image ch02_bg living = Transform("images/ch02/qixing_living_morning_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg entry = Transform("images/ch02/qixing_entry_morning_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg office = Transform("images/ch02/police_office_day_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg theatre_exterior = Transform("images/ch02/theatre_exterior_day_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg theatre_intermission = Transform("images/ch02/theatre_hall_intermission_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg theatre_side = Transform("images/ch02/theatre_audience_side_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg mansion = Transform("images/ch02/umekawa_exterior_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg foyer = Transform("images/ch02/umekawa_foyer_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg corridor = Transform("images/ch02/umekawa_corridor_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg bathroom = Transform("images/ch02/umekawa_bathroom_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg piano = Transform("images/ch02/umekawa_piano_room_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg phone_dusk = Transform("images/ch02/umekawa_phone_dusk_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg night = Transform("images/ch02/street_night_v1.png", xysize=(1920, 1080), fit="cover")
image ch02_bg sky = Transform("images/ch02/starry_sky_v1.png", xysize=(1920, 1080), fit="cover")
# Props: native composition retains embedded raster art on SDL SVG loaders.
image ch02_notice_art = Composite((1200, 1700), (0, 0), "images/ch02/props/missing_notice_paper_runtime.svg", (416, 267), Transform("images/ch02/props/chinatsu_notice_portrait_v1.png", xysize=(368, 491), fit="cover"))
# Explicit anchors override the show default (bottom-center). Match ch_phone top placement.
image ch02_notice = Transform("ch02_notice_art", xysize=(450, 638), xalign=0.5, yanchor=0.0, ypos=32, xoffset=0, yoffset=0)
image ch02_voucher = Transform("images/ch02/props/theatre_voucher_v1.svg", xysize=(900, 435), xalign=0.5, yanchor=0.0, ypos=155, xoffset=0, yoffset=0)
image ch02_handover = Transform("images/ch02/props/servant_phone_handover_v3.png", xysize=(1000, 667), anchor=(0.0, 0.0), xpos=850, ypos=90, xoffset=0, yoffset=0, fit="contain")
image ch02_bg street_posted = Transform(Composite((1672, 941), (0, 0), "images/ch01/street_day.png", (1450, 315), Transform("ch02_notice_art", xysize=(102, 145)), (593, 335), Transform("ch02_notice_art", xysize=(48, 68))), xysize=(1920, 1080))
image ch02_bg street_removed = Transform(Composite((1672, 941), (0, 0), "images/ch01/street_day.png", (1450, 315), Transform("images/ch02/props/notice_removed_layer_v1.png", xysize=(102, 145)), (593, 335), Transform("images/ch02/props/notice_removed_layer_v1.png", xysize=(48, 68))), xysize=(1920, 1080))
image ch02_bg entry_shoes = Transform(Composite((1672, 941), (0, 0), "images/ch02/qixing_entry_morning_v1.png", (840, 640), Transform("images/ch02/props/chinatsu_shoes_layer_v1.png", xysize=(215, 215), fit="contain")), xysize=(1920, 1080))

image ch02_star help:
    "images/ch02/props/signal_star_v1.svg"
    xysize (34, 34)
    anchor (0.5, 0.5)
    pos (0.66, 0.36)
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 1.54
    repeat

image ch02_star coordinates:
    "images/ch02/props/signal_star_v1.svg"
    xysize (34, 34)
    anchor (0.5, 0.5)
    pos (0.66, 0.36)
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.66
    alpha 1.0
    pause 0.22
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 0.22
    alpha 1.0
    pause 0.66
    alpha 0.0
    pause 1.54
    alpha 0.0

image ch02_qixing indoor = "images/ch02/sprites/qixing_indoor_neutral_v1.png"
image ch02_chinatsu indoor = "images/ch02/sprites/chinatsu_indoor_seated_neutral_v1.png"
image ch02_chinatsu dress = "images/ch02/sprites/chinatsu_dress_neutral_v1.png"
image ch02_wengang work = "images/ch02/sprites/wengang_work_neutral_v1.png"
image ch02_beidai home = "images/ch02/sprites/beidai_home_neutral_v1.png"
image ch02_chinatsu knees = "images/ch02/sprites/chinatsu_indoor_knees_closed_v1.png"
image ch02_beidai disheveled = "images/ch02/sprites/beidai_home_disheveled_v1.png"
image ch02_beidai phone = "images/ch02/sprites/beidai_home_phone_neutral_v1.png"
image ch02_beidai dismiss = "images/ch02/sprites/beidai_home_phone_dismiss_v1.png"
image ch02_theatre_staff neutral = "images/ch02/sprites/theatre_staff_halfbody_neutral_v1.png"
image ch02_house_servant neutral = "images/ch02/sprites/umekawa_servant_partial_neutral_v1.png"

transform ch02_indoor_seated:
    xpos 1690
    xanchor 0.5
    ypos 380
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 0.96

transform ch02_colleague_right:
    xpos 1690
    xanchor 0.5
    ypos 240
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 1.06

transform ch02_service_right:
    xpos 1500
    xanchor 0.5
    ypos 220
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 0.60

image ch02_cg tv_beidai_recital_v1 = Transform("images/ch02/cg/tv_beidai_recital_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg qixing_files_detail_v1 = Transform("images/ch02/cg/qixing_files_detail_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg theatre_voucher_handover_base_v1 = Transform("images/ch02/cg/theatre_voucher_handover_base_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg chinatsu_withdraw_hand_v1 = Transform("images/ch02/cg/chinatsu_withdraw_hand_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg piano_forced_turn_v1 = Transform("images/ch02/cg/piano_forced_turn_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg memory_flames_v1 = Transform("images/ch02/cg/memory_flames_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg memory_mother_arm_layer_v1 = Transform("images/ch02/cg/memory_mother_arm_layer_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg piano_push_away_v1 = Transform("images/ch02/cg/piano_push_away_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg qixing_street_stopped_v1 = Transform("images/ch02/cg/qixing_street_stopped_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg limo_arrival_umekawa_v1 = Transform("images/ch02/cg/limo_arrival_umekawa_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg chinatsu_piano_stand_fear_v1 = Transform("images/ch02/cg/chinatsu_piano_stand_fear_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg beidai_phone_recoil_v1 = Transform("images/ch02/cg/beidai_phone_recoil_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg qixing_stargaze_side_v1 = Transform("images/ch02/cg/qixing_stargaze_side_v1.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg chinatsu_limo_interior_v2 = Transform("images/ch02/cg/chinatsu_limo_interior_v2.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg beidai_welcome_chinatsu_v2 = Transform("images/ch02/cg/beidai_welcome_chinatsu_v2.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg chinatsu_corridor_escort_v3 = Transform("images/ch02/cg/chinatsu_corridor_escort_v3.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg qixing_take_hand_v6 = Transform("images/ch02/cg/qixing_take_hand_v6.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg chinatsu_bruise_detail_v3 = Transform("images/ch02/cg/chinatsu_bruise_detail_v3.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0), xoffset=0, yoffset=0)
image ch02_cg voucher = Transform(Composite((1672, 941), (0, 0), "images/ch02/cg/theatre_voucher_handover_base_v1.png", (620, 356), Transform("images/ch02/props/theatre_voucher_v1.svg", xysize=(400, 165))), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))
image ch02_cg television = Composite((1920, 1080), (0, 0), Solid("#101722"), (40, 24), Transform("images/ch02/cg/tv_beidai_recital_v1.png", xysize=(1840, 1032)), (80, 55), Text("テレビ放送", font="fonts/SourceHanSansJP-Regular.otf", size=28, color="#e9edf2", outlines=[(2, "#17202a", 0, 0)]))
image ch02_cg restaurant_memory = Transform("images/ch01/cg_table.png", xysize=(1920, 1080), fit="cover", anchor=(0.0, 0.0), pos=(0, 0))
image ch02_cg empty_keys = Transform(im.Crop("images/ch02/umekawa_piano_room_v1.png", (335, 420, 440, 248)), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))
image ch02_cg chinatsu_angry_close = Transform(im.Crop("images/ch02/cg/piano_push_away_v1.png", (815, 140, 750, 422)), xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))
image ch02_memory_arm = Transform("images/ch02/cg/memory_mother_arm_layer_v1.png", xysize=(1920, 1080), anchor=(0.0, 0.0), pos=(0, 0))

transform ch02_memory_sway:
    anchor (0.0, 0.0)
    pos (0, 0)
    xoffset 0
    yoffset 0
    ease 1.6 xoffset 12 yoffset -5
    ease 1.6 xoffset 0 yoffset 0
    repeat

image ch02_qixing indoor_bemused = "images/ch02/expressions/qixing_indoor_bemused_v1.png"
image ch02_qixing indoor_concerned = "images/ch02/expressions/qixing_indoor_concerned_v1.png"
image ch02_qixing casual_anger = "images/ch02/expressions/qixing_casual_restrained_anger_v1.png"
image ch02_chinatsu indoor_awkward = "images/ch02/expressions/chinatsu_indoor_awkward_v1.png"
image ch02_chinatsu indoor_wry = "images/ch02/expressions/chinatsu_indoor_wry_v1.png"
image ch02_chinatsu indoor_surprised = "images/ch02/expressions/chinatsu_indoor_surprised_v1.png"
image ch02_chinatsu dress_angry = "images/ch02/expressions/chinatsu_dress_angry_v1.png"
image ch02_wengang work_indignant = "images/ch02/expressions/wengang_work_indignant_v1.png"
image ch02_wengang work_skeptical = "images/ch02/expressions/wengang_work_skeptical_v1.png"
image ch02_wengang work_surprised = "images/ch02/expressions/wengang_work_surprised_v1.png"
image ch02_maxi incredulous = "images/ch02/expressions/maxi_incredulous_v1.png"
image ch02_beidai home_tender = "images/ch02/expressions/beidai_home_false_tender_v1.png"
image ch02_beidai disheveled_furious = "images/ch02/expressions/beidai_home_disheveled_furious_v1.png"
image ch02_beidai disheveled_curt = "images/ch02/expressions/beidai_home_disheveled_curt_v1.png"
image ch02_beidai phone_polite = "images/ch02/expressions/beidai_home_phone_polite_v1.png"
image ch02_beidai phone_uneasy = "images/ch02/expressions/beidai_home_phone_uneasy_v1.png"
image ch02_beidai phone_afraid = "images/ch02/expressions/beidai_home_phone_afraid_v1.png"
image ch02_beidai dismiss_afraid = "images/ch02/expressions/beidai_home_dismiss_afraid_v1.png"
image ch02_theatre_staff apologetic = "images/ch02/expressions/theatre_staff_apologetic_v1.png"
transform ch02_chinatsu_face:
    xpos 1000
    xanchor 0.5
    ypos -40
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 2.0

transform ch02_phone_left:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset 0
    yoffset 0
    zoom 0.85

transform ch02_phone_recoil:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    zoom 0.85
    xoffset 0
    yoffset 0
    ease 0.18 xoffset -55

transform ch02_phone_back:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset -55
    yoffset 0
    zoom 0.85

transform ch02_phone_dismiss:
    xpos 600
    xanchor 0.5
    ypos 150
    yanchor 0.0
    xoffset -98
    yoffset -21
    zoom 0.85

transform ch02_servant_offer:
    xpos 1500
    xanchor 0.5
    ypos 220
    yanchor 0.0
    zoom 0.60
    xoffset 0
    yoffset 0
    ease 0.25 xoffset -45

transform ch02_servant_exit:
    xpos 1500
    xanchor 0.5
    ypos 220
    yanchor 0.0
    zoom 0.60
    xoffset -45
    yoffset 0
    alpha 1.0
    ease 0.4 xoffset 420 alpha 0.0

image ch02_bg street_day = Transform("images/ch01/street_day.png", xysize=(1920, 1080), fit="cover")
image ch02_bg restaurant = Transform("images/ch01/restaurant_day.png", xysize=(1920, 1080), fit="cover")
# Composite before screen scaling so the two states share identical architecture.
image ch02_bg theatre_performance = Transform(Composite((1672, 941), (0, 0), "images/ch02/theatre_hall_intermission_v1.png", (125, 50), Transform("images/ch02/theatre_orchestra_layer_v1.png", zoom=0.84)), xysize=(1920, 1080), fit="cover")

label ch02_start:
    $ ch02_silence()
    $ ch_chapter_label = "第二章"
    $ ch_line_id = ""
    window hide None
    scene black
    hide screen ch_phone
    hide screen ch_recital_hint
    call ch_card("ch02_title") from ch02_title_return
    call ch02_sc01 from entry_ch02_sc01_return
    call ch02_sc02 from entry_ch02_sc02_return
    call ch02_sc03 from entry_ch02_sc03_return
    call ch02_sc04 from entry_ch02_sc04_return
    call ch02_sc05 from entry_ch02_sc05_return
    call ch02_sc06 from entry_ch02_sc06_return
    call ch02_sc07 from entry_ch02_sc07_return
    call ch02_sc08 from entry_ch02_sc08_return
    call ch02_sc09 from entry_ch02_sc09_return
    $ ch02_silence()
    return
