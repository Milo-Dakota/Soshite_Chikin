# 第二章 CG 交付｜2026-10-03

范围：首批 9 组、11 个静态状态，以及后续补充 6 张 CG／过场图，共 17 个画面状态。使用内置 image_gen 生成；成对动作以第一状态为参考编辑。图片归档在 `assets/ch02/cg/`，完整提示词、参考文件、原始生成路径、尺寸和摘要记录在 `assets/manifests/ch02_cg_imports.json`。

状态：已接入游戏，画面由用户验收。台词、翻译与音频未变。预览见 [CG 画廊](ch02_cg_gallery.html)。

绑定日语台本 revision 1，SHA-256：`cc519c970d6136c03532af71c158277590f93c753f1a9dcbe49940b3f90e3cb4`。

## 首批

| 场次 | 画面 | 文件前缀 |
|---|---|---|
| sc01、02 | 电视节目内备代演奏 | tv_beidai_recital |
| sc02、09 | 千夏左小臂淤青，末场复用 | chinatsu_bruise_detail_v3 |
| sc02 | 启星抓手／千夏抽回 | qixing_take_hand、chinatsu_withdraw_hand |
| sc04 | 凌乱文件与启星手部 | qixing_files_detail |
| sc05 | 工作人员递补偿券 | theatre_voucher_handover |
| sc06 | 千夏在礼宾车窗旁 | chinatsu_limo_interior |
| sc06 | 备代迎接、千夏僵住 | beidai_welcome_chinatsu |
| sc07 | 强制转身／明确推拒 | piano_forced_turn、piano_push_away |
| sc07 | 火焰与母亲手臂的碎片 | memory_flames、memory_mother_arm_layer |

淤青 v1 衣袖出现不连续结构，修订为 v2；保留旧版但不选用。2026-10-03 按用户修正，当前改用 v3：淤青位于左小臂外侧，不新增伤口或致伤过程。抓手画面不额外规定原台本未明确的被握手侧。

兑换券：PNG 是留白纸面的手部底图；交付的 `theatre_voucher_handover_v1.svg` 将已有正式券面嵌入其内部，保留纸边和手指。嵌入位置为 1672×941 画布上的 x=620、y=356、宽400、高165；正式字形使用既有矢量轮廓。后续接入需沿用合成结果，不能展示空白底图。

火焰记忆：底图与真正透明的手臂层分开交付，组成一个画面状态；画廊可切换手臂层。它是主观、不完整的记忆，不明确建筑、起火原因或死亡过程。手臂层保留独立透明画布，接入时可按完整画布同比例缩放并调整轻微挥动。

琴房画面只呈现抓臂、推拒与恐惧。强吻瞬间继续按计划切至无人琴键，不新增接触特写。第一章餐厅演奏回忆复用 `game/images/ch01/cg_table.png`，没有重画。

## 后续补充

| 场次 | 画面 | 文件前缀 |
|---|---|---|
| sc05 | 启星街头停住全景 | qixing_street_stopped |
| sc06 | 礼宾车驶入梅川宅 | limo_arrival_umekawa |
| sc06 | 千夏沿走廊被带走 | chinatsu_corridor_escort |
| sc07 | 千夏在琴房突然站起 | chinatsu_piano_stand_fear |
| sc08 | 备代接听后后退 | beidai_phone_recoil |
| sc09 | 启星仰望星空侧面 | qixing_stargaze_side |

补充镜头增加叙事角度，首批主体画面继续保留。备代起身和接电话镜头保持灰裤、白背带、右肩背带滑落和凌乱头发的连续性。接听 CG 不能代替尚缺的持机礼貌／惊恐立绘差分。

已接入本章全部 CG。Ren’Py lint、125 条双语 ID／顺序和 48 项运行资源摘要检查通过；未启动游戏画面通读，构图和演出由用户验收。票面使用游戏原生 Composite 合成，不依赖 SVG 内嵌 PNG。独立立绘表情、持机礼貌状态及挥退动作仍待后续差分。

## 验收修正
当前抓手、车内、走廊及迎接图均使用v2，旧版保留不选用；琴房面部裁切修正。详见[ch02_cg_revision_20261003.md](ch02_cg_revision_20261003.md)。

## 2026-10-03 左小臂修正版
当前淤青采用 chinatsu_bruise_detail_v3，两处出现均已接入；v1／v2 保留但不选用。使用内置 image_gen 参考引导重构，提示词与来源见 assets/manifests/ch02_bruise_forearm_revision_20261003.json。通话调整只提交方案，见 ch02_phone_staging_proposal.md，当前递机与后退演出仍未改动。
