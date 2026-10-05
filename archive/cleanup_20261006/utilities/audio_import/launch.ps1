$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$runtimePython = Join-Path $env:USERPROFILE '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe'
if (-not (Test-Path -LiteralPath $runtimePython)) {
    $runtimeCommand = Get-Command python -ErrorAction SilentlyContinue
    if (-not $runtimeCommand) { throw 'Python 3 is required. Install Python or edit launch.ps1 to set its path.' }
    $runtimePython = $runtimeCommand.Source
}
& $runtimePython (Join-Path $PSScriptRoot 'import_audio.py')
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
