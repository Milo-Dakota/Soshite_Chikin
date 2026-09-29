# 主菜单 B：中央片名

用户批准方案 B。上方中央两行日文标题，下方中文译名；钢琴位于中央；底部两层纯文字菜单。深蓝与暗金，模拟正式演出开场的庄重感，不改变正文的搞怪气质。

- 开始故事：新开局。
- 继续阅读：Ren'Py Continue 动作，载入最新普通／快速／自动存档；无存档时不可用。有存档时默认聚焦继续，否则聚焦开始。
- 读取存档／设置／关于：进入现有功能页面。
- 退出：带确认。
- 选中效果：文字提亮、底部细金线，支持按钮原生键盘焦点。
- lobby 音乐保持原配置，进入剧情仍按既有流程淡出。

实装：game/ch_main_menu.rpy；screens.rpy 的 main_menu 使用新界面，游戏内导航不替换。gui.main_menu_background 同步为新舞台背景。对话、语音和存档 ID 未变。

背景：game/images/ui/menu_theatre_v1.png。由内置 imagegen 生成，未用 CLI 或安装依赖。原图 1672×941，在游戏中适配 1920×1080；文字及交互不是图片的一部分。

静态检查只验证字体覆盖、资源、入口与按钮引用。未启动引擎；用户检查标题 Ruby、鼠标／键盘焦点、无存档状态、继续阅读、子菜单返回与 lobby 播放。

## 背景最终生成提示

Use case: stylized-concept. Asset: 16:9 landscape main-menu background for a polished 2010–2016 Japanese PC visual novel. Hand-painted anime background, refined quiet theatrical atmosphere, muted midnight navy and charcoal with warm antique gold. View straight toward an empty small elegant theatre stage from audience level, nearly symmetrical dark velvet curtains framing the sides. A black grand piano with open lid sits in the middle distance around horizontal center, entirely between 43% and 68% image height, warmly lit by a single subtle overhead spotlight. A plain wooden chair next to piano with dark suspenders draped discreetly over its back. No people. Upper central 15–40% stays very dark and uncluttered, usable for a large game title; bottom 72–100% very dark unobtrusive auditorium silhouettes for centered menu controls. Painterly craftsmanship, delicate wood and piano reflections, subtle atmospheric dust, convincing architecture and piano proportions. Serious formal concert opening used as deadpan comedy, not horror. No text, letters, logos, menu controls, watermark, chickens, blood or spooky imagery. Wide 16:9 composition.

