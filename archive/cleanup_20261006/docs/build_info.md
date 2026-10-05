# 当前构建信息

更新：2026-10-05。当前为开发预览配置，本轮没有生成或发布新的发行包。

| 项目 | 当前值 |
|---|---|
| 日文正式标题 | 『そして〖只因｜チキン〗もいなくなった』 |
| 中文标题 | 《无只因生还》 |
| 窗口标题 | `そして只因もいなくなった`（窗口标题不支持游戏内 Ruby 排版） |
| 版本号 | `0.4.0-dev` |
| 版本说明 | 第一、二章开发预览版 |
| 构建简称 | `soshite_chikin` |
| Windows 启动程序 | `soshite_chikin.exe` |
| 配布目录名 | `soshite_chikin-0.4.0-dev` |
| 默认选择的平台 | Windows，Ren'Py 包标识 `win` |
| 默认 Windows 包文件名 | `soshite_chikin-0.4.0-dev-win.zip` |
| 默认输出文件夹 | 项目同级的 `soshite_chikin-0.4.0-dev-dists`，即 `C:/Users/craft/Desktop/soshite_chikin-0.4.0-dev-dists/`；启动器指定其他输出位置时以指定位置为准 |
| 本地引擎 | Ren'Py 8.5.3.26051504 |
| 游戏画面 | 1920×1080，16:9 |
| 内容范围 | 第一章与第二章，完全线性剧情 |
| 字幕 | 中文主字幕、日语副字幕 |
| 配音状态 | 第一章已收录；第二章36条WAV全部接入（8位角色），听感待验收 |
| 存档标识 | `soshite_chikin-1790527487`，沿用现有标识 |

## 信息维护

- `game/options.rpy`：`config.version` 是唯一版本号源；`build.version` 引用它，避免页面版本与打包版本分叉。作品名、窗口标题、构建简称和版本说明也在此维护。
- `game/ch_menu_pages.rpy`：关于页读取版本号与版本说明，显示当前两章范围和配音状态。
- `project.json`：启动器上次选择的打包平台已从 `mac` 调整为 `win`。平台可以在启动器中改选；该值是默认选择，不限制项目只能导出 Windows。
- `docs/ch01_handoff.md`：保留已发布的第一章 Demo 0.3 历史交付，不作为当前工程版本。

此前的 `build.version = 0.3`、`config.version = 0.3 — Chapter 1 Bilingual Demo` 与只介绍第一章的关于页已统一。`-dev` 明确表示开发预览，第二章配音已补齐，仍待试听验收。发布时再按实际完成内容更新 `config.version` 与版本说明。

打包配置排除小说原文、制作文档、台本源、候选素材、制作工具和 `.build/` 等制作资料；运行资源位于 `game/`。本轮不核对外部素材来源及许可，继续沿用用户指定的待核验状态。
