# 正式台本与修改联动

日语源为 scripts/ja/chXX.yaml，中文源为 scripts/zh/chXX.json。日语按角色意图、关系、情绪和自然表达重组，保留剧情与梗，不逐字翻译。普通叙事优先画面／动作／声音／自然内心／对白，避免反复「我看到／我发现」。

以下仅为格式示例，章节号不代表当前任务或制作授权。

```yaml
schema_version: 1
chapter_id: ch03
title_ja: "章のタイトル"
revision: 1
scenes:
  - id: ch03_sc01
    scene_kind: main
    narrative_pov: qixing
    location: location_id
    time: time_description
    entries: []
```

scene_kind 为 main 或 side_scene。普通视点 qixing，特殊视点填写角色 ID 或 external（仅外部行为）。内心不能无提示切换人物，镜头不受此约束。

示例只展示层级；正式文件还须满足对应导出器的字段检查。既有台本的 `status` 是历史导出标签，不代表图片、配音或整章的当前完成状态；不要据此重开已完成工作，也不要仅为同步进度修改它而改变台本摘要。当前进度读取 `docs/status.md`，新增格式不另设整章进度副本。正式汉化只读取提供的日语内容及汉化指南，不自行读取状态文件。

| type | 规则 |
|---|---|
| dialogue | speaker、ja；非徐启星说出口对白，默认日语配音 |
| protagonist_dialogue | speaker: qixing、ja；不配音 |
| thought | speaker 与视点角色一致、ja；所有内心不配音 |
| direction | action 与必要参数；不显示、不配音、不汉化 |
| document_text | 明确载体／作者的书面文字，无 speaker、无 voice，保留显示 ID；载体在 text_type_extensions 中声明，寻人启事为既有用法 |

新增书面载体须先声明来源和配音规则，不伪装成对白。普通 Scene 不引入 narrator。关键信息不能只写在演出备注中。

## ID、Ruby 与配音

- 显示 ID 为 chXX_scXX_001，演出独立使用 chXX_scXX_dir001。播放顺序由 entries 决定。
- 插入用新 ID，删除不回收；拆分／合并改变身份时分配新 ID，检查所有旧引用。
- ja 使用 `〖表记｜读音〗`；实装转换为 Ren'Py Ruby，不能显示分隔符。
- 有声台词可填 ja_spoken；缺省从 ja 推导，Ruby 取读音。两者表达同一台词，不分别改写剧情。
- 配音前检查 Ruby 成对、读音非空、专名一致、无残留显示标记、徐启星及所有内心无 voice。performance 记录情绪／强度／节奏，仅作为人类演技提示。

## 中文与修改

中文 JSON 包含 chapter_id、source_ja_sha256、lines（Line ID → 中文），沿用既有章名等字段。中文主字幕、日语副字幕，徐启星也显示双语。

汉化必须在未读原文的独立上下文，输入仅日语、汉化指南、ID 与显示限制。不输入小说、故事研究、原句对照或含这些内容的历史对话。

改 ja/type/speaker 复核中文／实装／朗读和语音；改 ja_spoken／演技复核语音；只改排版且读音不变不强制重录；改 direction 检查资源与语境。ID／路径变化更新所有引用。日语修改后先做剧情核验，再依据日语更新中文，不能拿小说原句回填。

结构检查覆盖解析、字段、角色、ID 唯一、视点、Ruby、中文覆盖、源摘要。正式文字不在生成 rpy 或交接稿中独立修改。
