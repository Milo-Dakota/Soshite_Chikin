# Chapter 1 配音交付

`ch01_manifest.csv` 适合表格查看，`ch01_manifest.json` 适合批量生产。二者由 `script_ja/ch01.yaml` 导出，内容相同。

当前台本为已复核的 Demo 录音版（revision 2 / `demo_reviewed`）。33 条已交付、接入并随 Demo 验收发布。清单中的 `ready_for_recording` 是导出器保留的录音文本就绪字段，不代表音频仍未制作；文件实况见 `assets/inventory.json`。后续改词仅复核受影响的配音。

- 只录 `ja_spoken`，不录 `ja_display` 中的 Ruby 分隔符、角色名、演技备注。
- 按 `output_path` 输出 OGG；稳定 ID 不因台词顺序改变而重编号。
- 情绪、强度与节奏是人类可读演技提示，不保证是语音软件直接支持的参数。
- 徐启星对白和所有内心均不在清单中，无需配音。
- 单句朗读变化可通过 `spoken_sha256` 对比；演技变化也需人工确认是否重录。
- 2026-09-29：用户交付的全部 33 条配音已由本目录复制到 `game/audio/voice/<character>/`，按稳定 ID 接入已有播放代码。清单仍作为录音文本依据保留；实际导入状态及文件摘要见 `docs/reports/ch01_voice_check.json`。文件及映射检查通过；用户已确认 Demo 完成并发布，Agent 未进行游戏内试听。

直接阅读和录音请用 `ch01_recording.md`，其中逐句列出朗读正文、演技及准确文件路径。

重新导出：用已安装 PyYAML 的 Python 执行 `tools/export_ch01.py`。本次辅助库位于 `.build/deps`；它们不是游戏依赖，不要打包进游戏。
