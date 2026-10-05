# 第二章表情差分交付｜2026-10-03

按用户确认的 19 张清单全部生成并接入游戏，实装画面待用户验收。使用内置 image_gen 编辑现有立绘底图，不覆盖原有底图或第一章差分。19 张均通过 1024×1536 尺寸与 RGBA 文件检查，来源、提示词和摘要已记录。

生成阶段之后，按用户授权接入 19 张并调整通话演出。台词／字幕／稳定 ID 未改。日语台本 revision 2，SHA-256：`fa06b84c2245e33152c419fa7fc3abf503dc6ca34fde0aa2f9403a7f53730e0a`。

[全部预览与底图对比](ch02_expressions_gallery.html) · [完整提示词、参考与来源](../../assets/manifests/ch02_expression_imports.json)

| 编号 | 表情 | 输出文件 | 使用依据 |
|---|---|---|---|
| 01 | 启星室内 · 无奈浅笑 | [qixing_indoor_bemused_v1.png](../../assets/ch02/expressions/qixing_indoor_bemused_v1.png) | sc01 |
| 02 | 启星室内 · 认真关切 | [qixing_indoor_concerned_v1.png](../../assets/ch02/expressions/qixing_indoor_concerned_v1.png) | sc02 |
| 03 | 启星私服 · 克制怒气 | [qixing_casual_restrained_anger_v1.png](../../assets/ch02/expressions/qixing_casual_restrained_anger_v1.png) | sc04 |
| 04 | 千夏室内 · 尴尬垂眼 | [chinatsu_indoor_awkward_v1.png](../../assets/ch02/expressions/chinatsu_indoor_awkward_v1.png) | sc01_003 |
| 05 | 千夏室内 · 淡淡讽刺 | [chinatsu_indoor_wry_v1.png](../../assets/ch02/expressions/chinatsu_indoor_wry_v1.png) | sc01_004 |
| 06 | 千夏室内 · 自然惊讶 | [chinatsu_indoor_surprised_v1.png](../../assets/ch02/expressions/chinatsu_indoor_surprised_v1.png) | sc01_006 |
| 07 | 千夏礼服 · 受辱后的怒视 | [chinatsu_dress_angry_v1.png](../../assets/ch02/expressions/chinatsu_dress_angry_v1.png) | sc07_dir007 |
| 08 | 文钢 · 激动责备 | [wengang_work_indignant_v1.png](../../assets/ch02/expressions/wengang_work_indignant_v1.png) | sc04_005–006 |
| 09 | 文钢 · 怀疑与劝告 | [wengang_work_skeptical_v1.png](../../assets/ch02/expressions/wengang_work_skeptical_v1.png) | sc04_009–011 |
| 10 | 文钢 · 意外惊讶 | [wengang_work_surprised_v1.png](../../assets/ch02/expressions/wengang_work_surprised_v1.png) | sc04_dir006 |
| 11 | 马皙 · 不可置信的惊讶 | [maxi_incredulous_v1.png](../../assets/ch02/expressions/maxi_incredulous_v1.png) | sc05_012 |
| 12 | 备代整齐 · 假慈爱 | [beidai_home_false_tender_v1.png](../../assets/ch02/expressions/beidai_home_false_tender_v1.png) | sc07_002–004 |
| 13 | 备代凌乱 · 盛怒责斥 | [beidai_home_disheveled_furious_v1.png](../../assets/ch02/expressions/beidai_home_disheveled_furious_v1.png) | sc07_dir008 |
| 14 | 备代凌乱 · 冷淡不耐 | [beidai_home_disheveled_curt_v1.png](../../assets/ch02/expressions/beidai_home_disheveled_curt_v1.png) | sc08_001 |
| 15 | 备代持机 · 对外礼貌 | [beidai_home_phone_polite_v1.png](../../assets/ch02/expressions/beidai_home_phone_polite_v1.png) | sc08_003 |
| 16 | 备代持机 · 疑惑不安 | [beidai_home_phone_uneasy_v1.png](../../assets/ch02/expressions/beidai_home_phone_uneasy_v1.png) | sc08_dir003–004 |
| 17 | 备代持机 · 惊恐失色 | [beidai_home_phone_afraid_v1.png](../../assets/ch02/expressions/beidai_home_phone_afraid_v1.png) | sc08_005 |
| 18 | 备代挥退 · 惊恐催退 | [beidai_home_dismiss_afraid_v1.png](../../assets/ch02/expressions/beidai_home_dismiss_afraid_v1.png) | sc08_dir004 |
| 19 | 剧院工作人员 · 正式歉意 | [theatre_staff_apologetic_v1.png](../../assets/ch02/expressions/theatre_staff_apologetic_v1.png) | sc05_008–009 |

差分以对应底图为编辑目标，保持衣着、身体姿态与道具。备代的凌乱状态延续右肩白背带滑落；持机与挥退均保留原电话和手部。惊恐持机与挥退采用相同情绪设计，后者在前者完成后追加脸部参考以统一表现。

当前交付供用户实装画面验收。125 条双语文本顺序／ID、73 个运行资源摘要、19 个表情显示引用及引擎语法检查通过。没有启动游戏检查画面。

## 实装说明

电视演奏 CG 短暂展示后回到居间对白，千夏依台词切换尴尬、讽刺与惊讶；启星在苦笑和关切段落使用室内差分。文钢的责备／质疑及启星克制怒气随对白切换，启星离开时短暂保留文钢的惊讶反应。剧院工作人员使用歉意，马皙使用不可置信的惊讶。

琴房受辱后的近景使用礼服怒视立绘，替代旧 CG 面部裁切；随后转向凌乱、盛怒的备代。原推拒、记忆和起身 CG 保留。

sc08 保持同一夕照背景：冷淡空手→礼貌持机→疑惑不安→惊恐后移→挥退佣人→惊恐持机继续对白。接机省略精细手指交接；佣人轻微靠近后等待，再沿外侧退场。持机／挥退切换统一缩放，并对挥退底图头部偏移作位置补偿。独立递机局部和备代后退 CG 不再播放，原文件保留归档。

## 后续验收修正
第一次回家 sc02_dir001 恢复有鞋玄关 entry_shoes；此前表情演出覆盖了道具演出的背景选择，误用了空玄关，现已修复。sc03 千夏离开后的空玄关继续保留。
千夏说不要问后，sc02_dir004 从抽手 CG 直接暗转，取消抱膝立绘回切。sc08_dir003 佣人在递机后稍候自行离去；dir004 备代仅用惊恐持机立绘后退，不再切惊恐催退姿态。相关旧素材保留归档，当前实际使用 18 张新增表情。文本、字幕、稳定 ID 与音频设置未改。必要的镜头引用检查与引擎语法检查通过，画面由用户验收。

## 剧院与琴房镜头优化
走出剧院的 sc05_dir007—008 使用第一章 qixing_troubled_v1（低落、垂眼）承接内心活动，取消 qixing_street_stopped_v1 CG 播放。sc07_dir007 取消千夏大幅近景，恢复琴房背景下左侧备代／右侧千夏的正常对话站位；备代使用凌乱盛怒、千夏使用礼服怒视。dir008 保持双方同框，直至火焰记忆镜头。台词、字幕、音频与稳定 ID 未改，引用与语法检查通过，画面待用户验收。
