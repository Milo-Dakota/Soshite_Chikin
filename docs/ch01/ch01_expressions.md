# 第一章表情差分增补 — 2026-09-29

> 当前状态：2026-09-29 用户确认 Demo 完成并已发布。下文按制作过程保留设计细节；其中当时的“待验收”不代表当前待办。最新总交付见 `docs/ch01_handoff.md`。

已使用内置 image_gen 编辑现有立绘，新增 11 张透明 PNG 并接入演出。没有修改日语正文、汉化、语音、Line ID 或人物显示位置。原图保留。

台本 SHA-256：`99c9e2f74d61272fee0878fd615d04472b31aed59ec1fafa0c717112ded643cd`。

## 交付与来源

- 游戏文件：`game/images/ch01/`，下表名称加 `.png`。
- 生成原图归档：`assets/ch01/expressions/`，名称加 `_v1.png`。
- 完整提示词、参考图、工具输出路径与归档映射：`assets/manifests/ch01_expression_imports.json`。
- 参考底图：`qixing_neutral.png`、`chinatsu_guarded.png`、`maxi_neutral.png`。
- 新增表情声明：`game/ch01_runtime.rpy`；演出源：`tools/build_ch01.py`；六场脚本已重新导出。

## 使用位置

| 文件名 | 表情 | 接入点 |
|---|---|---|
| qixing_troubled | 心事、回避 | ch01_sc02_dir006 起，父母话题；ch01_sc04_dir001 起，犹豫打电话 |
| qixing_bemused | 困惑、无奈 | ch01_sc02_010；ch01_sc05_007、020、031 |
| qixing_serious | 认真、关切 | ch01_sc01_012；ch01_sc04_014；ch01_sc05_010、024，以及 dir010 的餐后询问 |
| qixing_soft | 温和、浅笑 | ch01_sc04_018；ch01_sc05_030、032、035 |
| qixing_surprised | 惊讶、抗议 | ch01_sc06_005，二十岁抗议 |
| chinatsu_embarrassed | 羞涩、脸红 | ch01_sc04_dir006，搀扶 CG 后开始同行，保留短暂停顿 |
| chinatsu_downcast | 低落、疲惫 | ch01_sc04_014 起；ch01_sc05_010 起 |
| chinatsu_surprised | 惊讶、迟疑 | ch01_sc05_dir012，收留提议后；036 答应时再切回已有微笑 |
| maxi_enthusiastic | 热情、得意 | ch01_sc02_008；ch01_sc03_dir001 起 |
| maxi_concerned | 试探、担心 | ch01_sc02_dir006 起，听到家事后收起笑意，延续到 018 询问 |
| maxi_annoyed | 佯怒、不满 | ch01_sc03_dir002 后，发现朋友离开并拿走水 |

话题转折使用短溶解；保留现有 CG，不在 CG 上叠加全身立绘。没有为新增差分更改角色缩放和站位。台本已有演出指令对应表情具体化，额外反应沿用生成器的逐句演出映射。

## 检查与验收边界

11 张均为 1024×1536 RGBA，透明通道存在，全部有游戏引用，归档与游戏文件摘要一致。头部以下的半透明轮廓重合度约 98.2%—99.4%；生成编辑仍有少量衣纹和边缘变化，不宣称逐像素完全锁定。生成输出已逐张目视检查，人物、服装与姿态保持一致。

`docs/reports/ch01_expression_check.json` 记录各图摘要、身体轮廓对照与引用检查；`docs/reports/ch01_resource_check.json` 核对新增后共 33 张章节图片、双语与语音接口。全部静态检查通过。

未启动 Ren'Py，实际过渡、面部可读性和微小衣纹变化是否显眼仍待用户试玩确认。建议重点看父母电话、扶起后的同行、马皙幕间、收留提议和章末抗议。
