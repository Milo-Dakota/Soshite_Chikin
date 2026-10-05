# Demo 字体分工

使用用户提供的 game/fonts 文件，未下载或安装系统字体。

| 用途 | 字体 | 字号 |
|---|---|---|
| 中文主字幕、内心 | SourceHanSerifSC-Medium.otf | 36 |
| 日语副字幕 | SourceHanSerifJP-Medium.otf | 24 |
| 中文姓名 | SourceHanSerifSC-Medium.otf | 32 |
| 主标题、章间大标题 | ShipporiMincho-SemiBold.ttf | 主菜单 49、章卡 48 |
| 章卡副标题 | SourceHanSerifSC-Medium.otf | 29，兼容中文姓名 |
| 菜单、设置及系统界面 | SourceHanSansSC-Regular.otf | 沿用原界面字号 |
| 日文注音 | SourceHanSansJP-Regular.otf | 副字幕 13，标题 19 |

中文仍为主字幕，日语仍为副字幕。历史保留日文专用字体。内心通过既有颜色区分，不添加斜体；姓名没有单独 SemiBold 文件，使用实有 Medium，不做模拟粗体。注音在小字号下优先使用无衬线 Regular。

字体检查使用 tools/check_ch01_fonts.py，结果存入 docs/ch01_font_check.json；它检查正文、姓名、标题、注音及界面文本的字符覆盖，不代替 Ren'Py 实际排版验收。原有注音偏移和留白保持，换字体后的视觉效果由用户运行确认。

## 阅读界面更新

用户已验收功能页面。正文改为宽 1776、高 282 的两侧留边面板，底部留 68 px；姓名使用上沿铭牌、28 px。正文起点更靠上，中文 36／日语 24 与注音参数不变。底栏独立为低对比度深蓝细带，中文按钮分为阅读、存档、设置；自动／快进选中呈暗金色，保留原动作并增加读取入口。

实装：game/ch01_runtime.rpy、game/ch_reading_bar.rpy；screens.rpy 的桌面与触屏 quick_menu 连接新底栏。字体与屏幕引用静态检查通过，没有 add 填充属性误用。本章最长中文 41 字，正文宽度 1648 px；实际换行、注音与长句排版仍由用户运行确认，未启动 SDK。
