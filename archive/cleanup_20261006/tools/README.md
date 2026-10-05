# 制作工具

在项目根目录使用具备现有依赖的 Python 运行。项目此前使用 `.build/deps` 中的 PyYAML／fontTools，部分检查还需要 Pillow 与 NumPy；它们不属于游戏依赖。无需因资料整理重新安装。

音频处理的新入口为 `utilities/audio_import/import_audio.cmd`：根目录 `audio/` 的BGM／配音归一化后导入，环境音／音效原样复制。以后补交或替换语音使用此入口；旧 `import_ch02_voice.py` 只作为历史原样导入工具保留，不要用它覆盖已处理的游戏音频。详细配置见 `utilities/audio_import/README.md`。

| 命令 | 作用与输出 |
|---|---|
| `python tools/import_ch02_voice.py` | 按当前日语台本和录音清单校验第二章WAV角色／台词ID、16位PCM及完整音频帧，原样复制到游戏；更新 `docs/reports/ch02_voice_check.json`，支持部分交付 |
| `python tools/export_ch01.py` | 从日语源导出 `voice/` 清单、录音稿及 `docs/reports/ch01_static_check.json` |
| `python tools/export_ch02.py` | 核对第二章日语源、视点、书面文字及配音筛选，导出 `voice/ch02_recording.md`、CSV／JSON 清单及 `docs/reports/ch02_static_check.json`；不写入 game，不运行第一章构建 |
| `python tools/export_ch02_localization.py` | 核对第二章中文与日语摘要、逐条 ID 及书面文字覆盖，导出 `docs/ch02/ch02_bilingual_script.md` 和 `docs/reports/ch02_localization_check.json`；不读取小说，不修改台本或游戏 |
| `python tools/build_ch02.py` | 从正式日语／中文源生成第二章九场、资源声明及静音入口，复制 15 个背景文件；只接入背景和双语，不接立绘／CG／音频；暂缓演出逐项写入构建报告 |
| `python tools/check_ch02.py` | 核对第二章 ID／字幕顺序、图片摘要、字体覆盖和无音频／立绘指令；可选引擎测试稿仅写入 `.build/testcases/`，不启动引擎、不打包进游戏 |
| `python tools/build_ch01.py` | 调用上述导出器，生成游戏六场及入口、`docs/ch01/ch01_bilingual_script.md`、构建报告；会写入 game，发布后仅在修改正式源／演出时运行 |
| `python tools/check_ch01_assets.py` | 图片引用、双语、字体、语音接口替身检查；写报告及字体 NOTICE |
| `python tools/check_ch01_fonts.py` | 文字覆盖，报告在 `docs/reports/` |
| `python tools/check_ch01_expressions.py` | 11 张表情、归档摘要、位置与 CG 分离；读取 `assets/manifests/` |
| `python tools/check_menu_pages.py` | 菜单屏幕与动作引用的静态检查 |
| `python tools/check_delivery.py` | 文档链接、素材来源与副本摘要、工具路径、整理前后游戏文件摘要；输出 `docs/reports/organization_check.json` |

导入 JSON 已移至 `assets/manifests/`。所有报告写入 `docs/reports/`，不会重新散落在 docs 根目录。游戏内效果依然通过 Ren'Py 运行验收。

本次整理的工具原稿已保存到 `docs/archive/pre_release_cleanup_20260929/tools/`；它们只用于追溯，不从归档目录执行。

`check_delivery.py` 的运行摘要比对针对本次整理基准；以后正式修改游戏后出现差异是预期结果，不应为了消除差异而恢复旧游戏文件。发布新版本时应另建对应版本基准。
