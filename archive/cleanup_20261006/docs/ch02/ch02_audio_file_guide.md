# 第二章音频文件放置与命名

范围：第二章非配音音频。按既有 `ch02_audio_remaining.md` 整理。2026-10-03 更新：初稿 15 个新增文件及 5 个第一章复用文件已接入游戏；后续补充项仍可选。

以下目录均相对于项目根目录。正式文件统一采用 OGG；如果下载的是 MP3/WAV，请保留真实扩展名，例如 `ch02_mystery_low.mp3`，不要仅改成 `.ogg`。后续接入时由 Agent 转换。每首／每项选定一个版本；备选曲不要全部放入正式目录。

## 初稿：需要寻找

| 类别 | 要找的素材 | 文件夹 | 正式文件名 | 要求 |
|---|---|---|---|---|
| BGM | 轻悬疑、寻找线索 | `game/audio/bgm/` | `ch02_mystery_low.ogg` | 低强度，适合内心与对白，能循环 |
| BGM | 梅川宅家庭压迫 | `game/audio/bgm/` | `ch02_mystery_dark.ogg` | 克制、压抑，适合对白，能循环 |
| 画内音乐 | 剧院古典器乐合奏 | `game/audio/bgm/` | `ch02_theater_ensemble.ogg` | 有小提琴声部，完整乐句、自然收束 |
| 环境声 | 安静室内 | `game/audio/ambience/` | `ch02_room_quiet.ogg` | 无清楚人声与音乐，可循环 |
| 环境声 | 警局办公室 | `game/audio/ambience/` | `ch02_office_room.ogg` | 轻办公空间声，可循环 |
| 环境声 | 剧院观众 | `game/audio/ambience/` | `ch02_theater_audience.ogg` | 中场低语，可循环，无持续掌声 |
| 环境声 | 行驶中的车内 | `game/audio/ambience/` | `ch02_car_interior.ogg` | 隔窗轮胎／发动机声，可循环 |
| 环境声 | 深夜街道 | `game/audio/ambience/` | `ch02_street_night.ogg` | 稀疏远车、轻风，可循环 |
| SE | 普通室内门打开 | `game/audio/sfx/` | `ch02_door_open.ogg` | 住宅／办公室普通门 |
| SE | 普通室内门关闭 | `game/audio/sfx/` | `ch02_door_close.ogg` | 与打开同类门 |
| SE | 厚重木门打开 | `game/audio/sfx/` | `ch02_mansion_door_open.ogg` | 梅川宅使用 |
| SE | 厚重木门关闭 | `game/audio/sfx/` | `ch02_mansion_door_close.ogg` | 与打开材质统一 |
| SE | 整理文件纸张 | `game/audio/sfx/` | `ch02_paper_shuffle.ogg` | 整理多张文件的声音 |
| SE | 高跟鞋踩木地板 | `game/audio/sfx/` | `ch02_heels_wood.ogg` | 克制、缓慢 |
| SE | 衣袖抽回轻摩擦 | `game/audio/sfx/` | `ch02_sleeve_pull.ogg` | 轻微布料摩擦 |

共 15 个文件。初稿素材是最终素材的一部分。

## 初稿：沿用第一章，无需寻找、复制或改名

| 素材 | 已有完整相对路径 |
|---|---|
| 日常平静 BGM（Easy Lemon） | `game/audio/bgm/ch01_daily_calm.ogg` |
| 备代电视节目（大厅音乐已原样复制、独立管理） | `game/audio/bgm/ch02_tv_piano.ogg` |
| 白天街道环境 | `game/audio/ambience/ch01_street_day.ogg` |
| 浴室流水 | `game/audio/sfx/ch01_shower_loop.ogg` |
| 手机来电铃 | `game/audio/sfx/ch01_phone_ring.ogg` |

## 后续补充：可选，不替代初稿

| 类别 | 要找的素材 | 文件夹 | 正式文件名 |
|---|---|---|---|
| 音乐 | 星空悬念短尾奏 | `game/audio/bgm/` | `ch02_star_revelation_tail.ogg` |
| SE | 普通鞋缓慢步行 | `game/audio/sfx/` | `ch02_footsteps_slow.ogg` |
| SE | 急促离场脚步 | `game/audio/sfx/` | `ch02_footsteps_hurried.ogg` |
| SE | 剧院座椅轻响 | `game/audio/sfx/` | `ch02_theater_seat.ogg` |
| SE | 递券／接券纸声 | `game/audio/sfx/` | `ch02_ticket_handle.ogg` |
| SE | 手机通知轻响 | `game/audio/sfx/` | `ch02_phone_notification.ogg` |
| SE | 电话拿起／移离耳边轻响 | `game/audio/sfx/` | `ch02_phone_handle.ogg` |

温暖回忆配乐沿用 `game/audio/bgm/ch01_warm.ogg`（Gymnopedie No.1），无需另找。

补充项按演出需要接入；如果主悬疑曲足以承担结尾，短尾奏可以省略。电话与电视滤镜由游戏处理，无需额外处理版文件。

## 来源记录

每项保留曲名／素材名、作者、来源网页与许可网页，便于 Agent 接入时更新 `docs/asset_licenses.md`。下载过的试听备选仍放在 `assets/ch02/audio_candidates/`；它们不等于已选定的正式素材。配音使用既有 `game/audio/voice/<角色ID>/<台词ID>.ogg` 规则，另按配音台本交付，不在本表中逐条列出。
