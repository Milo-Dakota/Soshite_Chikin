# 素材来源与许可记录

状态更新：2026-09-29，用户确认 Demo 已完成并发布。本次整理按已有材料记录，不进行新的授权核查，也不把发布状态等同于许可字段已齐全。

| 类别 | 当前来源及记录 |
|---|---|
| 章节美术 | 项目使用内置 image_gen 生成；提示词、参考图和导入映射在 `assets/prompts/`、`assets/manifests/` |
| 主菜单背景 | 内置 image_gen；提示词在 `docs/design/main_menu_design.md`，运行图与归档在素材索引中对应 |
| 厂牌图案 | 现有 `game/images/ui/chikurin_soft_logo.png`；保留文件与摘要，不推测未记录的创作来源 |
| 音乐、音效、环境声、厂牌朗读 | 用户提供，已接入 `game/audio/`；曲目作者、具体来源及许可未在现有交付记录中完整提供，沿用此前暂缓核对的状态 |
| 33 条角色语音 | 用户提供；录音清单与原件在 `voice/`，游戏副本在 `game/audio/voice/`。具体模型权重、授权条款及署名要求未提供 |
| 五种现用字体 | 用户提供，位于 `game/fonts/`；字体分工见 `docs/design/typography.md`。现有许可附件见 `game/licenses/`，不据通用字体名称宣称每个文件均已单独核实 |
| 原工程字体 | `game/SourceHanSansLite.ttf`；已提取版权与摘要至 `game/licenses/SourceHanSansLite-NOTICE.txt`，已有 OFL 文本 `game/licenses/SourceHanSans-OFL.txt` |
| 原工程 GUI | 保留 `game/gui/` 与原工程内容；阅读面板 `reading_panel_a.svg` 为项目实装文件 |

## 历史素材

早期 Easy Lemon、Gymnopedie No. 1 曾记录为 Kevin MacLeod 录音、CC BY 4.0，未接入当前演出；当前 `game/audio/bgm/` 只有 4 个实际使用的 OGG，两首旧 MP3 不在当前目录。历史目录、FAQ 与曲目材料保留在 `assets/licenses/`，旧记录见 [整理前版本](archive/pre_release_cleanup_20260929/docs/asset_licenses.md)。这份历史许可不套用到后来用户提供的音乐上。

## 维护

后续若补充来源信息，应逐项记录素材名、作者、来源、适用许可证、署名、修改与再分发权限。只补真实取得的信息，不修改素材本身。当前文件摘要和来源副本见 `assets/inventory.json`。
