# 制作工具

根目录使用 Python 3.11+，依赖见 requirements.txt。本机已有 .build/deps 的 PyYAML／fontTools；不自动安装依赖。

```text
python tools/project.py export ch02
python tools/project.py recording ch02
python tools/project.py build ch02
python tools/project.py check ch02
python tools/project.py check-ui
python tools/project.py audit
```

| 操作 | 输出及用途 |
|---|---|
| export chXX | 检查日语，录音机器清单／阅读稿到 .build/exports，报告到 .build/reports |
| recording chXX | export 后复制录音稿为 handoff/chXX/voice.md，仅确需人类录音时执行 |
| build chXX | 正式双语＋演出源生成本章 game 脚本；ch01 同时更新总入口，ch02 复制图片副本 |
| check chXX | 台本、字幕、图片、字体及语音路由检查，不启动引擎、不修改音频 |
| check-ui | 菜单静态引用检查 |
| audit | 当前链接、文件映射、正式文本绑定检查，不比较旧发布快照 |

现有章节专用校验保留，统一入口调度；第三章没有启动，不预建其构建器。演出在 scripts/staging，工具不维护临时镜头覆盖。公共 UI／声音配置直接维护 game 对应文件。

唯一日常音频入口为根目录 import_audio.cmd，见 [音频工具](audio_import/README.md)。旧原样导入器、HTML 试听和一次性交付脚本已归档。

build_ch02_props.py 按日语源重建矢量道具，不生成画廊，修改道具时单独运行并复核。check_voice_levels.py 为按需测量，不必每次运行。报告／导出可重建，不替代 docs/status.md。
