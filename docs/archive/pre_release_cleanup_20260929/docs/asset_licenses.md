# 当前外部素材记录

记录日期：2026-09-28。用户要求先收尾，音乐不再继续选曲或试听。下列文件已下载但**未接入游戏演出、未完成试听验收**。

## 已下载配乐

| 名称／文件 | 作者 | 来源与录音编号 | 许可证 | 署名／修改／随游戏分发 |
|---|---|---|---|---|
| Easy Lemon／`game/audio/bgm/easy_lemon.mp3` | Kevin MacLeod | [作者目录](https://incompetech.com/music/royalty-free/music.html)，USUAN1200076 | CC BY 4.0 | 必须署名并链接许可证；允许修改及随游戏分发；文件未编辑，未来使用淡入淡出应如实记录 |
| Gymnopedie No. 1／`game/audio/bgm/gymnopedie_no1.mp3` | 作曲 Erik Satie；本录音 Kevin MacLeod | [作者目录](https://incompetech.com/music/royalty-free/music.html)，USUAN1100787 | CC BY 4.0（录音） | 同上；不可因作曲古老就认为录音无版权 |

依据：[作者音乐使用 FAQ](https://incompetech.com/music/royalty-free/faq.html)、[作者许可页](https://incompetech.com/music/royalty-free/licenses/)、[CC BY 4.0 条款](https://creativecommons.org/licenses/by/4.0/)。作者说明游戏中应提供可找到的署名页面，许可允许修改；CC BY 要求保留署名、许可链接并说明修改。

官网目录、曲目 JSON 和 FAQ 已存于 `assets/licenses/`；完整许可证已下载到 `game/licenses/CC-BY-4.0.txt`。两首文件从作者目录确定的 `mp3-royaltyfree` 链接下载。

未来实际使用时在游戏 Credits 写入：

```text
Easy Lemon — Kevin MacLeod (incompetech.com)
Gymnopedie No. 1 — Kevin MacLeod (incompetech.com); composed by Erik Satie
Licensed under Creative Commons: By Attribution 4.0
https://creativecommons.org/licenses/by/4.0/
Source: https://incompetech.com/music/royalty-free/music.html
```

## 现有字体

`game/SourceHanSansLite.ttf` 为原工程已有字体，本项目未修改或重新下载该字体。内嵌记录：Adobe 2014—2019，Reserved Font Name “Source”，SIL Open Font License 1.1。本章正文、姓名和标题字形检查无缺字。文件自身的版权原文及 SHA-256 已导出到 `game/licenses/SourceHanSansLite-NOTICE.txt`；其直接来源记录为本项目原有文件，不冒称已与上游最新二进制逐字节匹配。

已从 [Adobe 官方 Source Han Sans 仓库](https://github.com/adobe-fonts/source-han-sans/blob/release/LICENSE.txt) 补齐 OFL 1.1 正文，保存为 `game/licenses/SourceHanSans-OFL.txt`。该上游文本当前署名年份为 2014—2025，与项目字体内嵌的较早年份分别保留。许可允许随软件附带分发及修改，要求保留版权与许可，不可单独出售字体；修改字体须遵守 Reserved Font Name 条款。本项目不修改字体名称或内容。关于页面含字体署名，打包保留许可附件。

## 本轮生成美术

来源：内置 imagegen，本项目生成；文件与 prompt 见 `assets/README.md` 及 `assets/prompts/`。不套用上述音乐或字体许可证，不伪称第三方作者授权。未使用现实人物照片或第三方角色图作为参考。

## 语音与音效

语音由用户后续提供，模型及成品使用许可届时补记。本轮没有生成或下载 SE，没有引入许可不明的音效。
