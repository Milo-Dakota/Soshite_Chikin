$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$projectRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$runtimePython = Join-Path $projectRoot '.venv/Scripts/python.exe'
if (-not (Test-Path -LiteralPath $runtimePython)) {
    throw 'Project Python environment missing. Create .venv with uv and install the root requirements.txt first.'
}
& $runtimePython (Join-Path $PSScriptRoot 'import_audio.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
