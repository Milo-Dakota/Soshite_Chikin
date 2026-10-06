# 制作工具

使用项目根目录的 `.venv`（Python 3.11+），依赖统一见 [requirements.txt](../requirements.txt)。环境与依赖由人类使用 uv 安装；工具不自动安装，也不再读取 `.build/deps` 或 Codex 专用 Python。FFmpeg 单独安装并加入系统 PATH。

激活 `.venv` 后执行以下命令，或将 `python` 替换为 `.venv\Scripts\python.exe`。子工具沿用同一 Python 解释器。

```text
python tools/project.py export ch02
python tools/project.py recording ch02
python tools/project.py reading ch02
python tools/project.py build ch02
python tools/project.py check ch02
python tools/project.py check-ui
python tools/project.py audit
```

| 操作 | 输出及用途 |
|---|---|
| export chXX | 检查日语，只生成 .build/exports 中的 JSON 录音清单及 .build/reports 中的报告 |
| recording chXX | 生成机器清单与录音稿，再复制录音稿为 handoff/chXX/voice.md，仅确需人类录音时执行 |
| reading chXX | 校验双语绑定并生成 .build/exports/chXX_bilingual_script.md，仅阅读核对时执行 |
| build chXX | 正式双语＋演出源生成本章 game 脚本；ch01 同时更新总入口，ch02 复制图片副本 |
| check chXX | 台本、字幕、图片、字体及语音路由检查，不启动引擎、不修改音频 |
| check-ui | 菜单静态引用检查 |
| audit | 当前链接、文件映射、正式文本绑定检查，不比较旧发布快照 |

章节专用校验由统一入口调度；支持的章节参数以 `python tools/project.py --help` 为准。新增章节时按授权范围扩展导出、构建与检查，不要假定只换章节参数就能处理新章。演出在 scripts/staging，工具不维护临时镜头覆盖。公共 UI／声音配置直接维护 game 对应文件。

唯一日常音频入口为根目录 import_audio.cmd，见 [音频工具](audio_import/README.md)。旧原样导入器、HTML 试听和一次性交付脚本已清理，不再使用。

build_ch02_props.py 按日语源重建矢量道具，不生成画廊，修改道具时单独运行并复核。check_voice_levels.py 为按需测量，不必每次运行。报告／导出可重建，不替代 docs/status.md。

日语导出与 Ren'Py 构建保留章节专用工具，以维护不同的视点、书面文字与演出约定；双语校验／阅读稿统一由 export_localization.py 处理。第一章资源检查内部调用字体检查，入口不重复调用。音频导入、道具生成与响度测量用途不同，分别保留。

常规 build／check 不生成录音稿、双语阅读稿或引擎测试脚本，也不写入 handoff。确需第二章引擎测试脚本时运行 `python tools/check_ch02.py --prepare-runtime-test`，输出到 .build/testcases；生成脚本本身不代表已运行引擎测试。
