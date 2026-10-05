"""Build a local audition page from the downloaded, unmodified candidates."""
from pathlib import Path
import json, hashlib, html, re
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / 'assets/ch02/audio_candidates'
items = [
    ('A1','bgm_12704_track1','赤い月の朝','Motoyuki',405,'低强度悬疑','钢琴为主，作者注明旋律克制、适合对白背景。优先比较它能否承托启星寻找千夏时的内心活动。'),
    ('A2','bgm_1548_track1','Flutter','かずち',50,'低强度悬疑','作者描述为安静、孤独、略带可疑感的氛围音乐。用于比较较抽象的空间感与钢琴方案。'),
    ('A3','bgm_13706_track1','残された日記','shimtone',290,'低强度悬疑','作者定位为阴暗、悲伤或恐怖场景。作为偏失落的一版，试听时留意是否太悲伤。'),
    ('B1','bgm_23641_track1','Whispers Between Silence','松浦洋介',426,'家庭压迫','作者描述为简单、安静且令人不安的钢琴曲，适合不穏场景。用于宅内对话，比较低调的心理压力。'),
    ('B2','bgm_21940_track1','廃','shimtone',290,'家庭压迫','作者定位为缓慢、不安的怪谈氛围。作为更阴冷的一版，试听时留意是否过于灵异。'),
    ('B3','bgm_20834_track1','密約','Heitaro Ashibe',452,'家庭压迫','作者明确以不安的交易与对话场景为意象；中速、暗色电子音乐。作为节奏感较明确的对照候选。'),
    ('S1','se_858_track1','穏やかな通知音','ひふみセオリー',138,'补充音效','用于 sc03 手机消息；作者按手机通知音设计。'),
    ('S2','se_1191_track1','紙のページをめくる音','Notzan ACT',357,'补充音效','纸张轻响候选，用于 sc05 递券。原素材是翻页声，需试听确认纸质与动作是否合适，不直接认定为最终递券声。'),
    ('S3','se_1179_track3','急ぐ足音・Track 3','稿屋 隆',3,'补充音效','急促离场脚步候选，用于 sc04、05。素材带悬疑追逐倾向，需试听确认速度与力度是否过强。'),
]
manifest=[]
for code,stem,title,author,creator,group,note in items:
    record=json.loads((DIR/(stem+'.json')).read_text(encoding='utf-8-sig'))
    data=(DIR/(stem+'.mp3')).read_bytes()
    assert len(data)>1000 and (data.startswith(b'ID3') or data[:1]==b'\xff'), stem
    assert hashlib.sha256(data).hexdigest()==record['sha256']
    record.pop('download_url',None)
    record.update(code=code,title=title,author=author,creator_url=f'https://opentracks.com/creator/detail/{creator}',group=group,note=note,selected=False,status='downloaded_pending_user_audition',download_date='2026-10-03',modified=False,license='OpenTracks audio license',license_url='https://opentracks.com/help/articles/license/',attribution='站点许可不强制；项目仍保留作者与出处',editing_allowed=True,game_distribution='允许作为游戏背景；发布时不能让最终用户轻易独立取得音源，详见 game_trpg 条款。禁止独立素材再分发。',loop_declared=any('（ループ/' in s for s in record['download_options']))
    manifest.append(record)
(DIR/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','li','h1','h2','br'): self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,text):
        if not self.skip: self.parts.append(text)
sources=DIR/'sources'
sources.mkdir(exist_ok=True)
urls={i[k] for i in manifest for k in ('source','creator_url','license_url')}
urls.update(['https://opentracks.com/help/articles/terms/','https://opentracks.com/help/articles/game_trpg/'])
for url in sorted(urls):
    key=hashlib.sha256(url.encode()).hexdigest()[:12]
    snapshot=ROOT/'.build/audio_research'/f'{key}.html'
    assert snapshot.is_file(), f'Missing source snapshot: {url}'
    parser=PlainText(); parser.feed(snapshot.read_text(encoding='utf-8'))
    text=re.sub(r'\n\s*\n','\n',''.join(parser.parts))
    (sources/f'{key}.txt').write_text('Source: '+url+'\nCaptured: 2026-10-03\n\n'+text,encoding='utf-8')

sections=[]
for group in ['低强度悬疑','家庭压迫','补充音效']:
    cards=[]
    for item in manifest:
        if item['group']!=group: continue
        src='../../'+item['file']
        loop='官网标注可循环' if item['loop_declared'] else '单次音效'
        cards.append(f'''<article><div class="code">{item['code']} · {loop}</div><h3>{html.escape(item['title'])}</h3><p class="author">{html.escape(item['author'])}</p><p>{html.escape(item['note'])}</p><audio controls preload="metadata" src="{src}"></audio><div class="links"><a href="{src}">打开音频文件</a><a href="{item['source']}" target="_blank" rel="noopener">官方来源</a></div></article>''')
    sections.append(f'<section><h2>{group}</h2><div class="grid">'+''.join(cards)+'</div></section>')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第二章 · 音频候选试听</title><style>
body{margin:0;background:#142130;color:#e9e4da;font:16px/1.65 system-ui,sans-serif}main{max-width:1200px;margin:auto;padding:36px 24px 70px}h1{font-size:30px}h2{margin-top:36px;color:#d7bd89}h3{font-size:21px;margin:8px 0}.intro{max-width:900px;color:#bdcad7}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:18px}article{background:#203247;padding:22px;border:1px solid #3b4d61;border-radius:12px;display:flex;flex-direction:column}.code{color:#d7bd89;font-size:14px}.author{color:#a9b9c9;margin:0}article p{flex:1}audio{width:100%;margin:14px 0}.links{display:flex;gap:20px;font-size:14px}a{color:#dcc28f}.controls{padding:16px;background:#203247;border-radius:8px;display:flex;gap:24px;align-items:center;flex-wrap:wrap}button{background:#d7bd89;border:0;padding:9px 16px;border-radius:5px;color:#142130;cursor:pointer}footer{margin-top:35px;color:#a9b9c9;font-size:14px}</style><main>
<h1>第二章 · 音频候选试听</h1><p class="intro">两类 BGM 各 3 首，另有 3 个补充音效。均已下载到本地，未接入游戏。按作者描述与标签初筛，尚未经主观听感验收；下方说明是入选理由，不代表已经试听认可。听完告诉我编号即可，例如“A1＋B2”。</p>
<div class="controls"><button onclick="document.querySelectorAll('audio').forEach(a=>a.pause())">全部暂停</button><label>试听音量 <input id="volume" type="range" min="0" max="1" step="0.05" value="0.5"></label><label><input type="checkbox" id="loop">循环试听 BGM</label></div>
'''+''.join(sections)+'''<footer>原始文件未剪辑、未归一化，曲目间原始响度可能不同。本页仅用于项目本地选曲。<a href="ch02_audio_candidates.md">来源、许可与待补项目</a></footer></main><script>
const players=[...document.querySelectorAll('audio')];players.forEach(a=>{a.volume=.5;a.addEventListener('play',()=>players.forEach(b=>{if(b!==a)b.pause()}))});document.querySelector('#volume').oninput=e=>players.forEach(a=>a.volume=+e.target.value);document.querySelector('#loop').onchange=e=>players.forEach(a=>a.loop=e.target.checked&&a.getAttribute('src').includes('/bgm_'));
</script></html>'''
(ROOT/'docs/ch02/ch02_audio_audition.html').write_text(page,encoding='utf-8')
md=['# 第二章音频候选｜2026-10-03','','六首 BGM＋三个补充音效已下载，未选定、未接入游戏。基于官方作者描述及标签初筛，实际听感由用户决定。原音未修改。','','| 编号 | 用途 | 曲目／作者 | 试听与来源 |','|---|---|---|---|']
for i in manifest:
    md.append(f"| {i['code']} | {i['group']} | {i['title']}／{i['author']} | [本地音频](../../{i['file']}) · [官网]({i['source']}) |")
md+=['','## 许可与归档','','采用 [OpenTracks 音源许可](https://opentracks.com/help/articles/license/) 及各作者页面条件。允许免费用于商业／非商业游戏背景，允许格式转换、剪辑及滤镜；站点不强制署名，项目仍记录作者与来源。禁止音源独立再分发；正式发布须依照 [游戏使用说明](https://opentracks.com/help/articles/game_trpg/) 处理音源打包，不能将本试听页及候选素材目录作为公开素材包发布。','','かずち的附加条件明确允许含成人表达的作品使用，其余入选作者页面标为遵循站点许可。许可页面与作者条件文本快照归档于 `assets/ch02/audio_candidates/sources/`。原始文件散列、官方下载页面、循环标注及未选定状态见同目录 `manifest.json`。','','## 仍未补齐的可选项','','普通缓慢步行、剧院座椅轻响、拿起／移开电话声、星空短尾奏仍未下载。已搜索到的座椅声音偏明显撞击／粗暴起身，未为凑数量收录。递券纸声及急促脚步只是近似动作候选，需实际试听决定。温暖回忆 BGM 沿用第一章，不重复下载。','','本轮没有下载角色配音，也没有修改游戏播放逻辑。']
(ROOT/'docs/ch02/ch02_audio_candidates.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(f'{len(manifest)} files verified; BGM loop declarations: '+str([i['code'] for i in manifest if i['loop_declared']]))
