# 本轮图片交付与验收状态

## Demo 0.2 最新交付

在此前 18 张接入图片上新增 4 张：`ch01/cg/cg_sleeve_v1.png`（拉袖口）、`cg_table_v1.png`（餐桌对坐）、`cg_two_fingers_v1.png`（竖两指）、`cg_walk_v2.png`（转头藏笑）。已通过内置 imagegen 实际生成、目视检查并复制至 `game/images/ch01/` 对应文件，合计 22 张；最终 prompt 在 `assets/prompts/`，新增导入映射在 `tools/ch01_demo02_asset_imports.json`。章末 v2 已纠正男主转头方向。未调用 CLI/API 回退。

本轮接入及静态检查完成，更新画面的游戏内效果待用户验收。以下 18 张记录为前版历史。

## 2026-09-28 最新集成状态

本轮已通过内置 imagegen 补齐并归档：餐厅及空盘差分、更衣室无水瓶差分、马皙立绘、千夏害怕差分、备代灰发鞠躬立绘，以及递面包、递水、搀扶、借沐浴露、礼宾车、模仿拉琴、钢琴演奏 7 张剧情图。连同先前素材，`game/images/ch01/` 共接入 18 张 PNG。备代参考图为 `reference/beidai_casual_v2.png`。

新增原图到归档及游戏路径的映射见 `tools/ch01_asset_imports.json`；全部最终生成说明在 `assets/prompts/`，未删除工具原始输出。未使用 CLI/API 回退。

静态检查见 `docs/ch01_resource_check.json`：图片路径齐全、六张立绘含透明通道。已逐图目视检查构图；尚未进行游戏内合成、边缘与表情切换验收。灰发参考规则不变，暖光 CG 的实际观感也列入用户验收。

以下首批记录保留为历史，不代表最新接入状态。原始分辨率限制仍适用，不将放大显示称为高清细节达标。

全部图片由内置 imagegen 实际生成，未使用 API／CLI 回退。最终生成说明保存在 `assets/prompts/`；原始输出已复制进本项目，未删除工具原始文件。当前为首批候选素材，尚未接入游戏，不等于整章美术验收通过。

| 文件 | 尺寸 | 当前状态 |
|---|---|---|
| `reference/beidai_casual_v2.png` | 1536×1024 | 备代中性灰发修订 Reference；按用户要求去除棕色色偏，后续备代素材以此版为准 |
| `reference/qixing_casual_v1.png` | 1536×1024 | 启星正侧面、面部与常服 Reference；已目视检查 |
| `reference/chinatsu_casual_v1.png` | 1536×1024 | 千夏正侧面、面部与常服 Reference；已目视检查 |
| `ch01/sprites/qixing_casual_neutral_v1.png` | 1024×1536 RGBA | 中性表情，全身透明立绘候选；来源为透明边缘复核后的第二次输出 |
| `ch01/sprites/chinatsu_casual_guarded_v1.png` | 1024×1536 RGBA | 戒备表情，全身透明立绘候选 |
| `ch01/sprites/chinatsu_casual_smile_v1.png` | 1024×1536 RGBA | 微笑差分候选；与上一张同尺寸，尚未做游戏内叠合和切换检查 |
| `ch01/backgrounds/street_day_v1.png` | 1672×941 RGB | 街道与健身馆外观候选；偏写实的质感需与立绘合成核对 |
| `ch01/backgrounds/gym_locker_v1.png` | 1672×941 RGB | 更衣室候选；含长凳上的一瓶水，尚缺水被顺走后的对应变化 |

透明通道检查：三张立绘含 alpha；千夏戒备图已抽查空白区域 alpha=0。预览中看到的暗底不应直接当成不透明黑背景；仍需在实际场景合成后检查边缘。不能因此声称所有边缘均已逐像素合格。

生成尺寸未达到视觉规范提出的背景 1920×1080、立绘 1600×2400 目标。保留原始尺寸，不通过插值放大冒充细节达标；下次先判断显示需求与构图，再决定重生成或调整规范，不直接作为已验收正式高清素材。

待补：主角并排比例确认、马皙与备代设计、本章餐厅及必要动作画面、需要的表情／服装差分、所有素材与 Ren'Py 界面的合成核验。主角 Reference 已有，不要从零另起一套设计。
