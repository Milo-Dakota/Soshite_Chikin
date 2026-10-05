# 音频原件入口

人类原件放入 bgm、voice/角色ID、ambience、sfx，保持约定文件名。双击根目录 import_audio.cmd。

BGM／配音归一化到 game/audio，环境音／SE 原样复制。原件不改动，不能拿处理后游戏文件再覆盖原件。

新声音的播放时机由 Agent 接入；配音机器清单通过 tools/project.py export chXX 生成到 .build/exports，台词修改后先更新清单。

详见 [导入说明](../tools/audio_import/README.md)。旧 voice 目录和原样导入器已归档。
