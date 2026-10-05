$ErrorActionPreference = 'Stop'
$root = Split-Path $PSScriptRoot -Parent
$manifestPath = Join-Path $root 'assets/manifests/ch02_pose_sprite_imports.json'
$manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
$cards = @()
foreach ($job in $manifest.images) {
    $file = Join-Path $root $job.output
    $bytes = [IO.File]::ReadAllBytes($file)
    $width = ([int]$bytes[16] -shl 24) + ([int]$bytes[17] -shl 16) + ([int]$bytes[18] -shl 8) + [int]$bytes[19]
    $height = ([int]$bytes[20] -shl 24) + ([int]$bytes[21] -shl 16) + ([int]$bytes[22] -shl 8) + [int]$bytes[23]
    $job | Add-Member -NotePropertyName width -NotePropertyValue $width -Force
    $job | Add-Member -NotePropertyName height -NotePropertyValue $height -Force
    $job | Add-Member -NotePropertyName png_color_type -NotePropertyValue ([int]$bytes[25]) -Force
    $job | Add-Member -NotePropertyName sha256 -NotePropertyValue ((Get-FileHash -LiteralPath $file -Algorithm SHA256).Hash.ToLower()) -Force
    if ([int]$bytes[25] -ne 6) { throw ('PNG has no RGBA channel: '+$job.id) }
    $url = '../../' + $job.output
    $title = [System.Net.WebUtility]::HtmlEncode($job.title)
    $cards += '<article><a href="' + $url + '" target="_blank"><div class="art"><img src="' + $url + '"></div></a><h2>' + $title + '</h2><p>' + $width + '×' + $height + ' · RGBA</p></article>'
}
$manifest | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $manifestPath -Encoding utf8
$html = '<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>第二章姿态与配角立绘</title><style>body{margin:32px;background:#142132;color:#e9e2d4;font:16px/1.6 sans-serif}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px}article{background:#26394c;padding:16px;border-radius:8px}.art{background:repeating-conic-gradient(#34495b 0% 25%,#405569 0% 50%) 0 0/28px 28px}img{display:block;width:100%;height:640px;object-fit:contain}h2{font-size:19px}p{color:#c5ced8}a{color:#dcc999}</style><h1>第二章 · 六项姿态与配角立绘</h1><p>千夏抱膝、备代凌乱／持电话／挥退佣人，以及两名配角。点击查看原图。均为透明PNG；当前只完成姿态与基础神情，正式表情差分留待后续。六项已按既有台本接入游戏，待用户画面验收。</p><main>' + ($cards -join "`n") + '</main></html>'
[IO.File]::WriteAllText((Join-Path $root 'docs/ch02/ch02_pose_sprites_gallery.html'), $html)
Write-Output ('Delivered '+$manifest.images.Count+' RGBA sprites.')
