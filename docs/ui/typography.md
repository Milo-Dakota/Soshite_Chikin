# 字体与阅读层级

中文正文、日语正文、姓名、Ruby 和标题分别使用适合其文字的样式，避免以同一字体强行替代中日字形。主字幕、副字幕、姓名和注音的层级应清楚；历史界面保留双语及各自字体。

| 要修改的内容 | 实际维护入口 |
|---|---|
| 对白、内心、姓名、正文注音及历史文字 | `game/ch01_runtime.rpy` 中共享 Character 与 style 定义 |
| 主菜单标题、标题注音与按钮 | `game/ch_main_menu.rpy` |
| 章卡、幕间卡文字 | `game/ch_title_cards.rpy` 及其调用的公共样式 |
| 阅读底栏 | `game/ch_reading_bar.rpy` |
| 功能页面与公共界面 | `game/ch_menu_pages.rpy`、`game/screens.rpy` |
| 默认主题参数 | `game/gui.rpy`；具体 screen／style 覆盖优先，不能只读默认值推断正文效果 |

字体文件位于 `game/fonts/`。具体字体文件名、字号和注音大小从实际使用的样式读取；本文件不维护参数镜像。排版原则见 [阅读面板](reading_panel.md)。

修改字体或显示文字后，按受影响范围检查缺字、Ruby、双语换行、长姓名与窗口缩放；字形覆盖检查不等于实际布局检查。
