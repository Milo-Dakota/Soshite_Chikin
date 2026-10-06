"""Build chapter 2 vector props. Raster originals are embedded unchanged."""
from pathlib import Path
import sys, json, re, base64, hashlib
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

OUT = ROOT / 'assets/ch02/props'
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

source = (ROOT/'scripts/ja/ch02.yaml').read_text(encoding='utf-8')
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
layout={'chapter':'ch02','ja_sha256':hashlib.sha256((ROOT/'scripts/ja/ch02.yaml').read_bytes()).hexdigest(),'canvas':[1672,941], 'notice_line_ids':ids,'notice_text':notice,'street_notices':spots,'shoes':{'x':840,'y':640,'width':215,'height':215},'phone_ui':{'canvas':[1920,1080],'x':745,'y':170,'width':430,'height':276},'signal':{'anchor':[.66,.36],'display_size':30,'unit_seconds':.22,'sequences':{s:timeline(s) for s in ['HELP','89N64W']}},'note':'Generated from current Japanese source; chapter status is in docs/status.md'}
(ROOT/'scripts/staging/ch02/props_layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8')

print('Built current SVG props and layout data; no preview page.')
