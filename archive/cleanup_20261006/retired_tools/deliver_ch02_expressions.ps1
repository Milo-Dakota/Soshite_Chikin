$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$manifestPath = Join-Path $root 'assets/manifests/ch02_expression_imports.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($manifest.images.Count -ne 19) { throw 'Expected 19 expression variants.' }
$cards = @()
foreach ($job in $manifest.images) {
    $file = Join-Path $root $job.output
    $bytes = [IO.File]::ReadAllBytes($file)
    $width = ([int]$bytes[16] -shl 24) + ([int]$bytes[17] -shl 16) + ([int]$bytes[18] -shl 8) + [int]$bytes[19]
    $height = ([int]$bytes[20] -shl 24) + ([int]$bytes[21] -shl 16) + ([int]$bytes[22] -shl 8) + [int]$bytes[23]
    if ($width -ne 1024 -or $height -ne 1536 -or [int]$bytes[25] -ne 6) { throw ('Unexpected PNG geometry/alpha: ' + $job.id) }
    $job | Add-Member -NotePropertyName width -NotePropertyValue $width -Force
    $job | Add-Member -NotePropertyName height -NotePropertyValue $height -Force
    $job | Add-Member -NotePropertyName png_color_type -NotePropertyValue ([int]$bytes[25]) -Force
    $job | Add-Member -NotePropertyName sha256 -NotePropertyValue ((Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLower()) -Force
    $job | Add-Member -NotePropertyName base_sha256 -NotePropertyValue ((Get-FileHash -LiteralPath (Join-Path $root $job.refs[0]) -Algorithm SHA256).Hash.ToLower()) -Force
    $title = [System.Net.WebUtility]::HtmlEncode($job.title)
    $scene = [System.Net.WebUtility]::HtmlEncode($job.scene)
    $url = '../../' + $job.output
    $base = '../../' + $job.refs[0]
    $cards += '<article><h2>' + $job.index + ' · ' + $title + '</h2><div class="frame"><a href="' + $url + '" target="_blank"><img src="' + $url + '" data-diff="' + $url + '" data-base="' + $base + '"></a></div><button onclick="flip(this)">对比底图</button><p>' + $scene + ' · 1024×1536 RGBA</p><a href="' + $url + '" target="_blank">打开差分原图</a></article>'
}
if ($manifest.status -ne 'integrated_pending_user_visual_review') { $manifest.status = 'generated_pending_user_review_not_integrated' }
$manifest | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $manifestPath -Encoding UTF8
$html = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第二章表情差分</title><style>body{margin:28px;background:#142132;color:#e9e2d4;font:16px/1.6 sans-serif}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}article{background:#26394c;padding:16px;border-radius:8px}.frame{background:repeating-conic-gradient(#34495b 0% 25%,#405569 0% 50%) 0 0/28px 28px}img{display:block;width:100%;height:520px;object-fit:contain}h2{font-size:18px}p{color:#c5ced8;font-size:14px}a{color:#dcc999}button{background:#ddceb0;border:0;border-radius:4px;padding:8px 14px;margin-top:12px;cursor:pointer}</style><h1>第二章 · 19 张表情差分</h1><p>19 张均已接入游戏，实装画面待用户验收。每张可切换对应底图进行对比，点击打开原图。</p><main>' + ($cards -join "`n") + '</main><script>function flip(b){const i=b.parentElement.querySelector("img");const base=i.dataset.base;const showing=i.getAttribute("src")===base;i.src=showing?i.dataset.diff:base;b.textContent=showing?"对比底图":"返回表情差分";}</script></html>'
[IO.File]::WriteAllText((Join-Path $root 'docs/ch02/ch02_expressions_gallery.html'),$html)
Write-Output ('Delivered '+$manifest.images.Count+' expression variants, all 1024x1536 RGBA.')
