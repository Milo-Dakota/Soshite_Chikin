# 『そして〖只因｜チキン〗もいなくなった』— Agent 入口

这是中文接龙小说《无只因生还》的 Ren'Py 线性视觉小说工程。Agent 负责改编、隔离汉化、美术与实装；人类提供音频并反馈游戏效果。美术认真遵循日本商业视觉小说气质，荒谬感来自剧情本身。

## 按任务读取

先读 [当前状态](docs/status.md)。第一、二章已完成，第三章未开始；不重复初始化或自行开启下一章。归档、报告、全量素材记录不作为默认上下文。

| 任务 | 读取入口 |
|---|---|
| 开始一章 | [工作流](docs/workflow.md)、[章节计划](docs/story/chapter_plan.md)、[故事总览](docs/story/story_overview.md)、本章原文、[台本规范](docs/rules/script_format.md) |
| 修改台词 | 本章 scripts/ja、docs/chapters、相关原文、[角色语言](docs/rules/character_language.md) |
| 汉化 | 独立且未读原文的上下文；只给日语台本、[汉化指南](docs/rules/localization_guide.md)、必要 ID 与显示限制 |
| 制作美术 | [视觉规范](docs/rules/visual_style.md)、本章 assets.md、对应 Reference；重做时才读 assets/records 中相关条目 |
| 调整演出 | 本章 scripts/staging、docs/chapters/chXX/staging.md、相关 Scene；[工具说明](tools/README.md) |
| 提供／导入音频 | [原件入口](audio/README.md)、[导入说明](tools/audio_import/README.md) |
| 修改 UI | docs/ui 对应文档与 game 中相关代码 |

## 必须保持

- 标题写作「只因」，读作「チキン」：`そして〖只因｜チキン〗もいなくなった`。
- 剧情事实忠实，表现方式自由。source/novel.txt 不可修改；梗、突兀转折、未解矛盾不得合理化。研究区分明示事件、人物说法与改编判断，保留原文定位及版本摘要。
- 普通 Scene 为徐启星中心叙事，无独立第三人称旁白。镜头自由，徐启星可有立绘、CG、同框。非在场剧情明确标记 side_scene，内心与视点一致。
- 徐启星对白、所有内心、系统与书面文字不配音；其他人物说出口对白有日语配音。全部音频由人类提供，Agent 不自行寻找或合成。
- 日语台本是正式文本源；中文仅从日语翻译。汉化上下文不得包含原文、原文研究或已读这些资料的会话历史。
- Scene ID、Line ID 不重排、不回收；Ruby 分离显示与朗读。改正式文字须复核译文、语音和实装，不能只改生成的 rpy。
- 按章节制作、分批接入 Ren'Py，实际生成美术；不能以 prompt 或占位图冒充完成品。
- 当前状态只在 docs/status.md 维护。交接优先聊天，确需清单才写 Markdown，不默认制作 HTML 画廊／试听页。

## 目录职责

| 目录 | 用途 |
|---|---|
| game/ | Ren'Py 运行工程；章节脚本由构建器生成，公共 UI／运行逻辑直接在此维护 |
| source/ | 原小说，只在剧情研究与日语改编阶段读取 |
| scripts/ja、scripts/zh | 正式日语与中文文本 |
| scripts/staging | 当前有效镜头指令、资源声明及布局；公共音频配置仍在 game 中 |
| docs/ | 状态、工作流、规范、剧情研究及章节特殊约定 |
| assets/ | 美术原件、Reference 和必要生成记录 |
| audio/ | 人类音频原件；根目录 import_audio.cmd 是唯一日常导入入口 |
| handoff/ | 确有需要才创建的人类交接 Markdown，完成章节不补建待办 |
| tools/ | 构建、导出、检查及音频导入 |
| .build/ | 可重建导出、报告、依赖和临时文件，不是当前状态来源 |
| archive/ | 历史资料，不默认读取、不执行旧工具 |
