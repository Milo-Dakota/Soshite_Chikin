# 制作工具

在项目根目录使用具备现有依赖的 Python 运行。项目此前使用 `.build/deps` 中的 PyYAML／fontTools，部分检查还需要 Pillow 与 NumPy；它们不属于游戏依赖。无需因资料整理重新安装。

| 命令 | 作用与输出 |
|---|---|
| `python tools/export_ch01.py` | 从日语源导出 `voice/` 清单、录音稿及 `docs/reports/ch01_static_check.json` |
| `python tools/build_ch01.py` | 调用上述导出器，生成游戏六场及入口、`docs/ch01/ch01_bilingual_script.md`、构建报告；会写入 game，发布后仅在修改正式源／演出时运行 |
| `python tools/check_ch01_assets.py` | 图片引用、双语、字体、语音接口替身检查；写报告及字体 NOTICE |
| `python tools/check_ch01_fonts.py` | 文字覆盖，报告在 `docs/reports/` |
| `python tools/check_ch01_expressions.py` | 11 张表情、归档摘要、位置与 CG 分离；读取 `assets/manifests/` |
| `python tools/check_menu_pages.py` | 菜单屏幕与动作引用的静态检查 |
| `python tools/check_delivery.py` | 文档链接、素材来源与副本摘要、工具路径、整理前后游戏文件摘要；输出 `docs/reports/organization_check.json` |

导入 JSON 已移至 `assets/manifests/`。所有报告写入 `docs/reports/`，不会重新散落在 docs 根目录。游戏内效果依然通过 Ren'Py 运行验收。

本次整理的工具原稿已保存到 `docs/archive/pre_release_cleanup_20260929/tools/`；它们只用于追溯，不从归档目录执行。

`check_delivery.py` 的运行摘要比对针对本次整理基准；以后正式修改游戏后出现差异是预期结果，不应为了消除差异而恢复旧游戏文件。发布新版本时应另建对应版本基准。
