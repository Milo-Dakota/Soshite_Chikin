# 素材总索引

第一章 Demo 已由用户验收并发布。本目录保存来源与归档；游戏实际读取 `game/` 中的运行副本。

| 目录 | 内容 |
|---|---|
| `reference/` | 启星、千夏、备代的固定设计参考 |
| `reference/ch02/` | 第二章五套人物／服装 Reference；见 `docs/ch02/ch02_character_references.md`，尚未接入游戏 |
| `ch02/backgrounds/` | 第二章 14 张背景（含 1 张后续补充）与 1 张透明乐团层；已复制到 `game/images/ch02/` 并接入背景＋双语阅读版，待用户运行验收 |
| `ch02/props/`、`ch02/ui/` | 第二章肖像、鞋子、递电话、撤除痕迹与 7 张矢量图形；预览见 `docs/ch02/ch02_props_gallery.html`，已接入第二章，待用户画面验收 |
| `ch02/sprites/` | 第二章五张基础立绘，已接入游戏；预览 `docs/ch02/ch02_sprites_gallery.html`，布局待用户验收，表情差分尚未制作 |
| `ch01/backgrounds/` | 6 张背景与状态差分，已统一原 `bg/` 命名 |
| `ch01/sprites/` | 6 张基础立绘／早期差分 |
| `ch01/expressions/` | 后补 11 张表情差分 |
| `ch01/cg/` | 11 张剧情 CG |
| `ui/` | 当前主菜单和厂牌图案的归档副本 |
| `prompts/` | 早期美术独立提示词 |
| `manifests/` | 原始生成路径、归档、游戏路径；新批次提示词内嵌在 JSON |
| `licenses/` | 历史外部素材来源资料，不能代替当前使用清单 |

统一机器索引：[inventory.json](inventory.json)。列出当前章节图片、UI、音频、字体和各文件 SHA-256，以及已找到的归档或用户交付副本。缺少独立来源记录的条目明确标注，不推测作者或许可。

## 使用原则

生成美术均使用内置 image_gen。详细来源按 `manifests/` 和 `prompts/` 追溯；背景图、立绘保留原始尺寸，旧版不覆盖。表情修改继续以现有角色为参考。

`voice/` 是用户配音交付原件与录音清单，`game/audio/voice/` 是运行副本，两者保留并按摘要核对。其他用户音频目前直接位于 `game/audio/`，没有虚构额外原件。

原有 Ren'Py GUI、字体、编译文件、缓存与存档未清理。历史未使用素材只记录，不凭文件名删除。旧素材交付文档见 [历史快照](../docs/archive/pre_release_cleanup_20260929/assets/README.md)。


第二章 CG：assets/ch02/cg/。17 个画面状态（含分层记忆），预览 docs/ch02/ch02_cg_gallery.html，来源与提示词 assets/manifests/ch02_cg_imports.json；已生成，待验收和接入。

2026-10-03更新：第二章全部CG已接入game/images/ch02/cg/，生成源tools/ch02_cg_staging.py。

2026-10-03：第二章六项姿态与配角立绘位于 assets/ch02/sprites/，预览 docs/ch02/ch02_pose_sprites_gallery.html，提示词与来源 assets/manifests/ch02_pose_sprite_imports.json。已生成，待用户验收，尚未接入。

2026-10-03：第二章 19 张表情差分已归档 assets/ch02/expressions/，预览 docs/ch02/ch02_expressions_gallery.html，来源与提示词 assets/manifests/ch02_expression_imports.json；待用户画面验收，尚未接入。
