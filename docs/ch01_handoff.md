# 第一章 Demo 0.3 — 当前交付

状态：用户于 2026-09-29 确认 Demo 完成并已发布。此次仅整理制作资料与归档；没有重新发布，也没有改动游戏运行文件。发布地址、发行包与包摘要未在本会话提供。

## 已交付

- 6 场线性剧情、97 条双语正文：28 条启星对白、36 条内心、33 条其他人物对白。
- 中文主字幕 36 px／日语副字幕 24 px，同时开始逐字显示；姓名 26 px。一体式阅读面板、历史、存读档及设置页。
- 34 张章节图片：17 张立绘及表情、6 张背景及状态差分、11 张 CG。另有主菜单背景与厂牌图案。
- 33 条日语配音：千夏 22、马皙 6、郑局长 4、备代 1。启星与所有内心无配音。
- 4 段音乐、3 段环境声、3 段章节音效，以及厂牌朗读。钢琴演奏有“点击跳过演奏”提示。
- 标题卡平滑退出与下一场淡入；备代采用公共区域致意、双人反应镜头和画外门声离场。

## 权威源与再生成

| 内容 | 维护位置 |
|---|---|
| 日语正式文字 | `script_ja/ch01.yaml` |
| 中文译文 | `script_zh/ch01.json`，保持与日语摘要绑定 |
| 本章研究与计划 | `script_plan/ch01.md` |
| 演出编排 | `tools/build_ch01.py` |
| 通用画面、资源定义、音频接口 | `game/ch01_runtime.rpy` |
| 录音清单与用户交付 | `voice/` |
| 游戏最终素材 | `game/images/`、`game/audio/`、`game/fonts/` |

日语 SHA-256：`99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd`。

中文 SHA-256：`e46e1759ba58bf39ef9538d5681a4c79ae911ea23181186da715c490e80b9907`。

Scene／Line ID 不重编号，已发布的编译脚本与存档保留。正文先改正式源，再沿语音、汉化与实装依赖更新；不要仅编辑生成的 `.rpy`。

## 设计与素材说明

- [音频](ch01/ch01_audio.md)、[人物构图](ch01/ch01_portrait_layout.md)、[11 张表情](ch01/ch01_expressions.md)、[备代入退场](ch01/ch01_beidai_staging.md)。
- [双语阅读稿](ch01/ch01_bilingual_script.md)，由正式源生成。
- [字体](design/typography.md)、[阅读面板](design/reading_panel_design.md)、[主菜单](design/main_menu_design.md)、[功能页面](design/menu_pages_design.md)、[启动演出](design/startup_presentation.md)。
- [素材总索引](../assets/README.md)、[工具与检查](../tools/README.md)。

## 验收与后续范围

用户已完成游戏验收并发布；Agent 完成素材与脚本静态核对，没有把静态测试记为引擎实测。检查原始字段保留在 `docs/reports/`。

本 Demo 沿用已验收的原始素材尺寸：背景／CG 1672×941、立绘 1024×1536，运行画布 1920×1080。生成表情存在少量边缘和衣纹差异，不宣称逐像素锁定。素材许可记录仍按已有证据保留，发布事实不补齐未知授权信息。

后续优先处理已发布 Demo 的反馈；第二章尚未启动。没有当前必须继续制作的第一章待办。

旧交接全文：[整理前快照](archive/pre_release_cleanup_20260929/docs/ch01_handoff.md)。其中逐轮“待验收／暂缓”均为历史状态。
