$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$cgDir = Join-Path $root 'assets/ch02/cg'
$voucher = Get-Content -LiteralPath (Join-Path $root 'assets/ch02/ui/theatre_voucher_v1.svg') -Raw
$ticketBody = $voucher.Substring($voucher.IndexOf('>') + 1)
$ticketBody = $ticketBody.Substring(0, $ticketBody.LastIndexOf('</svg>'))
$base64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $cgDir 'theatre_voucher_handover_base_v1.png')))
$svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1672" height="941" viewBox="0 0 1672 941"><image width="1672" height="941" href="data:image/png;base64,' + $base64 + '"/><svg x="620" y="356" width="400" height="165" viewBox="0 0 1200 580" preserveAspectRatio="none">' + $ticketBody + '</svg></svg>'
[IO.File]::WriteAllText((Join-Path $cgDir 'theatre_voucher_handover_v1.svg'), $svg)
$manifestPath = Join-Path $root 'assets/manifests/ch02_cg_imports.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
$cards = @()
foreach ($job in $manifest.images) {
    $file = Join-Path $root $job.output
    $bytes = [IO.File]::ReadAllBytes($file)
    $width = ([int]$bytes[16] -shl 24) + ([int]$bytes[17] -shl 16) + ([int]$bytes[18] -shl 8) + [int]$bytes[19]
    $height = ([int]$bytes[20] -shl 24) + ([int]$bytes[21] -shl 16) + ([int]$bytes[22] -shl 8) + [int]$bytes[23]
    $job | Add-Member width $width -Force
    $job | Add-Member height $height -Force
    $job | Add-Member sha256 ((Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLower()) -Force
    if (-not $job.selected -or $job.group -eq 'primary_layer') { continue }
    $url = '../../' + $job.output
    if ($job.id -eq 'theatre_voucher_handover_base_v1') { $url = '../../assets/ch02/cg/theatre_voucher_handover_v1.svg' }
    $tag = if ($job.group -eq 'supplement') { '后续补充' } else { '首批' }
    $title = [System.Net.WebUtility]::HtmlEncode($job.title)
    if ($job.id -eq 'memory_flames_v1') {
        $visual = '<div class="layers"><img src="' + $url + '"><img id="arm" src="../../assets/ch02/cg/memory_mother_arm_layer_v1.png"></div><button onclick="document.getElementById(''arm'').hidden=!document.getElementById(''arm'').hidden">显示／隐藏手臂层</button>'
    } else { $visual = '<a href="' + $url + '" target="_blank"><img src="' + $url + '"></a>' }
    $cards += '<article>' + $visual + '<h2>' + $title + '</h2><p>' + $tag + ' · ' + $job.scene + ' · ' + $width + '×' + $height + '</p></article>'
}
$manifest | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $manifestPath -Encoding utf8
$hand = @($manifest.images | Where-Object { $_.selected -and $_.id -like 'qixing_take_hand_*' })[0]
$pair = '<section style="max-width:1000px;margin:24px auto"><h2>抓手／抽回手：联动画面</h2><img id="hand_pair" src="../../' + $hand.output + '"><button onclick="document.getElementById(''hand_pair'').src=''../../' + $hand.output + '''">抓手</button> <button onclick="document.getElementById(''hand_pair'').src=''../../assets/ch02/cg/chinatsu_withdraw_hand_v1.png''">抽回手</button></section>'
$html = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第二章 CG 画廊</title><style>body{margin:32px;background:#111c29;color:#e9e2d4;font:16px/1.6 sans-serif}h1{font-size:28px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(520px,1fr));gap:24px}article{background:#203044;padding:16px;border-radius:8px}img{width:100%;display:block}h2{font-size:19px;margin:12px 0 4px}p{color:#c4c9cc}.layers{position:relative}.layers img:nth-child(2){position:absolute;inset:0;width:100%;height:100%}.layers img[hidden]{display:none}button{margin-top:8px;padding:8px;background:#e0d3b3;border:0;border-radius:4px}a{color:#dcc999}</style><h1>第二章 · 全部 CG</h1><p>首批 9 组／11 状态，加后续补充 6 张：共 17 个画面状态。点击图片查看原图。火焰记忆由底图与透明手臂层组成；兑换券使用已有正式票面。已接入游戏，画面由用户验收。</p><main>' + ($cards -join "`n") + '</main><h2>第一章餐厅回忆复用</h2><a href="../../game/images/ch01/cg_table.png"><img style="max-width:700px" src="../../game/images/ch01/cg_table.png"></a></html>'
$html = $html.Replace('<main>', $pair + '<main>')
[IO.File]::WriteAllText((Join-Path $root 'docs/ch02/ch02_cg_gallery.html'), $html)
Write-Output ('Selected PNG files: ' + @($manifest.images | Where-Object selected).Count)
