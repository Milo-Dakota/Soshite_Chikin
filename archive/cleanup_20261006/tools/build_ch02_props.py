"""Build chapter 2 vector props. Raster originals are embedded unchanged."""
from pathlib import Path
import sys, json, re, base64, hashlib
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.build/deps'))
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

OUT = ROOT / 'assets/ch02/ui'
OUT.mkdir(parents=True, exist_ok=True)
font = TTFont(ROOT / 'game/fonts/SourceHanSerifJP-Medium.otf')
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
upem = font['head'].unitsPerEm
cache = {}

def glyph(ch):
    if ch not in cache:
        name = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        cache[ch] = (pen.getCommands(), glyphs[name].width)
    return cache[ch]

def width(s, size):
    return sum(glyph(c)[1] for c in s) * size / upem

def text(s, x, y, size, color='#34312d', center=False):
    if center:
        x -= width(s, size) / 2
    result = f'<g aria-label="{escape(s)}" fill="{color}">'
    for c in s:
        d, advance = glyph(c)
        result += f'<path d="{d}" transform="translate({x:.3f},{y}) scale({size/upem},-{size/upem})"/>'
        x += advance * size / upem
    return result + '</g>'

def rich(s, x, y, size, limit=1000):
    result = ''
    origin = x
    for part in re.split(r'(〖[^〗]+〗)', s):
        tokens = [part] if part.startswith('〖') else list(part)
        for token in tokens:
            if not token:
                continue
            if token.startswith('〖'):
                base, reading = token[1:-1].split('｜')
            else:
                base, reading = token, None
            w = width(base, size)
            if x + w > origin + limit:
                x, y = origin, y + size * 1.85
            result += text(base, x, y, size)
            if reading:
                small = min(size * .43, w / max(width(reading, 1), 1))
                result += text(reading, x + w/2, y-size*.98, small, center=True)
            x += w
    return result, y

def uri(path):
    return 'data:image/png;base64,' + base64.b64encode(path.read_bytes()).decode()

def svg(w, h, body, title):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{escape(title)}</title>{body}</svg>'

def write(name, content):
    (OUT/name).write_text(content, encoding='utf-8')

source = (ROOT/'script_ja/ch02.yaml').read_text(encoding='utf-8')
def line(id):
    row = next(r for r in source.splitlines() if 'id: '+id+',' in r)
    return json.loads(re.search(r'ja: ("(?:[^"\\]|\\.)*")', row)[1])

ids = [f'ch02_sc01_{i:03}' for i in range(11,15)]
notice = [line(id) for id in ids]
paper = '<rect x="20" y="20" width="1160" height="1660" fill="#ded6c5"/><rect x="25" y="25" width="1150" height="1650" fill="#f2eddf"/><rect x="61" y="61" width="1078" height="1578" fill="none" stroke="#aaa18d" stroke-width="2"/>'
paper += text('尋ね人',600,177,82,center=True)
paper += '<path d="M360 209H840" stroke="#8c826d" stroke-width="2"/>'
paper += f'<image x="416" y="267" width="368" height="491" preserveAspectRatio="xMidYMid slice" xlink:href="{uri(ROOT/"assets/ch02/props/chinatsu_notice_portrait_v1.png")}"/>'
paper += '<rect x="408" y="259" width="384" height="507" fill="none" stroke="#a79b85" stroke-width="2"/>'
y = 890
for s in notice:
    part, end = rich(s, 112, y, 41, 976)
    paper += part
    y = end + 126
poster = svg(1200,1700,paper,'尋ね人 — '+''.join(notice))
write('missing_notice_v1.svg',poster)

spots = [{'x':1450,'y':315,'width':102,'height':145}, {'x':593,'y':335,'width':48,'height':68}]
posted = ''
removed = ''
for p in spots:
    x,y,w,h = [p[k] for k in ('x','y','width','height')]
    posted += f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 1200 1700">{paper}</svg>'
    for tx,ty in [(x+2,y+1),(x+w-12,y+1),(x+2,y+h-5),(x+w-12,y+h-5)]:
        posted += f'<rect x="{tx}" y="{ty}" width="10" height="4" fill="#d4c5a7" opacity=".65"/>'
    removed += f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="none" xlink:href="{uri(ROOT/"assets/ch02/props/notice_removed_layer_v1.png")}"/>'
write('street_notices_posted_v1.svg',svg(1672,941,posted,'張り出された尋ね人の紙'))
write('street_notices_removed_v1.svg',svg(1672,941,removed,'同じ位置に残った剥がし跡'))

# A restrained proscenium emblem, not a character or an additional story clue.
ticket = '<rect x="8" y="8" width="1184" height="564" rx="5" fill="#ece3cb"/><rect x="25" y="25" width="1150" height="530" fill="none" stroke="#927342" stroke-width="3"/><rect x="40" y="40" width="1120" height="500" fill="none" stroke="#b9a274"/>'
ticket += '<g fill="none" stroke="#8a6938" stroke-width="5"><path d="M95 335V226Q167 128 239 226V335M111 335V232Q167 159 223 232V335M95 335H239M130 335V254M204 335V254"/><path d="M120 224Q167 248 214 224"/></g>'
part,_=rich('〖艾昆｜アイクン〗劇場',335,165,46,800)
ticket += part + text('無料引換券',335,275,70)
detail = line('ch02_sc05_009').split('。')[1]+'。'
part,_=rich(detail,335,382,29,760)
ticket += part
write('theatre_voucher_v1.svg',svg(1200,580,ticket,'艾昆劇場 無料引換券 — '+detail))

# Phone mockups are retired. ch_phone renders these states in the game.

star = '<defs><radialGradient id="g"><stop stop-color="#f8fcff" stop-opacity=".85"/><stop offset=".23" stop-color="#c7e8ff" stop-opacity=".5"/><stop offset="1" stop-color="#afd7ff" stop-opacity="0"/></radialGradient></defs><circle cx="32" cy="32" r="31" fill="url(#g)"/><path d="M32 12L34 29L49 32L34 34L32 52L30 34L15 32L30 29Z" fill="#e6f3ff" opacity=".65"/><circle cx="32" cy="32" r="2.4" fill="#fff"/>'
write('signal_star_v1.svg',svg(64,64,star,'共通の信号星'))
morse={'H':'....','E':'.','L':'.-..','P':'.--.','8':'---..','9':'----.','N':'-.','6':'-....','4':'....-','W':'.--'}
def timeline(word):
    events=[]
    for i,c in enumerate(word):
        for j,mark in enumerate(morse[c]):
            events.append({'on':True,'units':1 if mark=='.' else 3})
            if j < len(morse[c])-1: events.append({'on':False,'units':1})
        events.append({'on':False,'units':3 if i<len(word)-1 else 7})
    return events
layout={'chapter':'ch02','ja_sha256':hashlib.sha256((ROOT/'script_ja/ch02.yaml').read_bytes()).hexdigest(),'canvas':[1672,941], 'notice_line_ids':ids,'notice_text':notice,'street_notices':spots,'shoes':{'x':840,'y':640,'width':215,'height':215},'phone_ui':{'canvas':[1920,1080],'x':745,'y':170,'width':430,'height':276},'signal':{'anchor':[.66,.36],'display_size':30,'unit_seconds':.22,'sequences':{s:timeline(s) for s in ['HELP','89N64W']}},'status':'Produced; visual acceptance and game integration pending'}
write('ch02_props_layout.json',json.dumps(layout,ensure_ascii=False,indent=2))

page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第二章 · 道具与覆盖层</title><style>
body{background:#151a22;color:#e8e2d6;font:16px system-ui;margin:36px auto;max-width:1250px;padding:0 24px}h1{font-size:28px}h2{font-size:21px;color:#cfb986;margin-top:40px}p{color:#b8c1ce;line-height:1.7}.grid{display:flex;gap:28px;align-items:start;flex-wrap:wrap}.card{background:#222a35;padding:20px;border:1px solid #3c4655}.poster{width:360px}.ticket{width:660px;max-width:100%}.stage{position:relative;width:100%;aspect-ratio:1672/941;background:#26313d}.stage>img{position:absolute;width:100%;height:100%;object-fit:fill}.stage .shoes{left:50.239%;top:68.012%;width:12.859%;height:22.848%;object-fit:contain}.stage .hand{left:40%;top:8%;width:60%;height:92%;object-fit:contain}.stage>.star{position:absolute;left:66%;top:36%;width:1.794%;height:auto;transform:translate(-50%,-50%)}button{background:#303c4d;border:1px solid #72829a;color:#f2ecdf;padding:10px 18px;margin:12px 8px 12px 0;cursor:pointer}.check{background:repeating-conic-gradient(#3b4350 0 25%,#29313e 0 50%) 0/24px 24px}.label{font-size:13px;color:#aeb9c9}
</style><h1>第二章 · 道具、覆盖层与界面图形</h1><p>本页供画面验收。素材尚未接入游戏；启事正文来自正式日语台本，文字已转为字形轮廓，图中没有 AI 生成的文字。</p>
<h2>寻人启事与兑换券</h2><div class="grid"><a href="../../assets/ch02/ui/missing_notice_v1.svg"><img class="poster" src="../../assets/ch02/ui/missing_notice_v1.svg"></a><div><img class="ticket" src="../../assets/ch02/ui/theatre_voucher_v1.svg"><p>票面未添加日期、座位、编号或额外线索。</p></div></div>
<h2>街边张贴／撤除</h2><button onclick="document.getElementById('notices').src='../../assets/ch02/ui/street_notices_posted_v1.svg'">张贴</button><button onclick="document.getElementById('notices').src='../../assets/ch02/ui/street_notices_removed_v1.svg'">撤除</button><div class="stage"><img src="../../game/images/ch01/street_day.png"><img id="notices" src="../../assets/ch02/ui/street_notices_posted_v1.svg"></div>
<h2>玄关鞋子层</h2><button onclick="let s=document.getElementById('shoes');s.hidden=!s.hidden">鞋子显隐</button><div class="stage"><img src="../../assets/ch02/backgrounds/qixing_entry_morning_v1.png"><img class="shoes" id="shoes" src="../../assets/ch02/props/chinatsu_shoes_layer_v1.png"></div>
<h2>来电／通知</h2><div class="grid"><img width="344" src="../../assets/ch02/ui/phone_incoming_maxi_v1.svg"><img width="344" src="../../assets/ch02/ui/phone_notification_maxi_v1.svg"></div><p>沿用现有 ch_phone 的深灰面板、金色状态字和联系人层级。通知不附加聊天内容。</p>
<h2>佣人递电话局部</h2><div class="stage"><img src="../../assets/ch02/backgrounds/umekawa_phone_dusk_v1.png"><img class="hand" src="../../assets/ch02/props/servant_phone_handover_v3.png"></div>
<h2>同一星点 · 两段信号</h2><button onclick="signal('HELP')">HELP</button><button onclick="signal('89N64W')">89N64W</button><button onclick="stopSignal()">停止</button><span id="signalLabel">未播放</span><div class="stage"><img src="../../assets/ch02/backgrounds/starry_sky_v1.png"><img class="star" id="star" hidden src="../../assets/ch02/ui/signal_star_v1.svg"></div><p>预览按钮仅供验收，不是游戏解谜界面；闪烁没有音频。信号结束后回到原有星空。</p><h2>沿用现有素材</h2><p>章节卡、三场幕间、返回主视点提示、解码正文、双语阅读面板及历史／存读档／菜单继续复用现有实现。</p><script>
const sequences=SEQUENCES;let timer=null;function stopSignal(){clearTimeout(timer);document.getElementById('star').hidden=true;document.getElementById('signalLabel').textContent='未播放'}function signal(word){stopSignal();document.getElementById('signalLabel').textContent=word;let i=0;function tick(){if(i>=sequences[word].length){document.getElementById('star').hidden=true;return}let e=sequences[word][i++];document.getElementById('star').hidden=!e.on;timer=setTimeout(tick,e.units*220)}tick()}
</script></html>'''
page=page.replace('SEQUENCES',json.dumps(layout['signal']['sequences']))
(ROOT/'docs/ch02/ch02_props_gallery.html').write_text(page,encoding='utf-8')
print('Built 5 SVG assets, layout/timing JSON, and review gallery (legacy phone mockups retained for historical reference).')

