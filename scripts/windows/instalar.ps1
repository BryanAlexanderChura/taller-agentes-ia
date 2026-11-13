# Verifica e instala las herramientas del taller. Idempotente: solo instala lo que falta.
# Uso: powershell -ExecutionPolicy Bypass -File scripts\windows\instalar.ps1
# Archivo en ASCII a proposito: PowerShell 5.1 lee sin BOM como ANSI.

$ErrorActionPreference = 'Stop'

function Test-Cmd($Name) {
    [bool](Get-Command $Name -ErrorAction SilentlyContinue)
}

function Update-SessionPath {
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine') + ';' +
                [Environment]::GetEnvironmentVariable('Path', 'User')
}

function Add-UserPath($Dir) {
    $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
    if ($userPath -notlike "*$Dir*") {
        [Environment]::SetEnvironmentVariable('Path', "$userPath;$Dir", 'User')
    }
    Update-SessionPath
}

function Install-Winget($Cmd, $Id) {
    if (Test-Cmd $Cmd) { Write-Host "[ok] $Cmd"; return }
    Write-Host "[instalando] $Cmd ($Id)"
    winget install --id $Id -e --accept-source-agreements --accept-package-agreements
    Update-SessionPath
}

function Install-Npm($Cmd, [string[]]$NpmArgs) {
    if (Test-Cmd $Cmd) { Write-Host "[ok] $Cmd"; return }
    Write-Host "[instalando] $Cmd (npm $NpmArgs)"
    npm install -g @NpmArgs
}

# 1. Base del entorno
Install-Winget 'git'  'Git.Git'
Install-Winget 'gh'   'GitHub.cli'
Install-Winget 'lazygit' 'JesseDuffield.lazygit'
Install-Winget 'uv'   'astral-sh.uv'
Install-Winget 'node' 'OpenJS.NodeJS.LTS'

$nodeMajor = [int]((node --version).TrimStart('v').Split('.')[0])
if ($nodeMajor -lt 22) {
    Write-Warning "Node $nodeMajor detectado; pi requiere Node 22 o superior. Actualiza: winget upgrade OpenJS.NodeJS.LTS"
}

# 2. Agentes
if (Test-Cmd 'claude') {
    Write-Host '[ok] claude'
} else {
    Write-Host '[instalando] claude (instalador nativo)'
    Invoke-RestMethod https://claude.ai/install.ps1 | Invoke-Expression
    Add-UserPath (Join-Path $env:USERPROFILE '.local\bin')
}
Install-Npm 'codex'    @('@openai/codex')
Install-Npm 'opencode' @('opencode-ai')
Install-Npm 'pi'       @('--ignore-scripts', '@earendil-works/pi-coding-agent')

# 3. Memoria: engram (binario de GitHub Releases)
if (Test-Cmd 'engram') {
    Write-Host '[ok] engram'
} else {
    Write-Host '[instalando] engram (GitHub Releases)'
    $arch = if ($env:PROCESSOR_ARCHITECTURE -eq 'ARM64') { 'arm64' } else { 'amd64' }
    $release = Invoke-RestMethod https://api.github.com/repos/Gentleman-Programming/engram/releases/latest
    $asset = $release.assets | Where-Object { $_.name -like "*windows_$arch.zip" } | Select-Object -First 1
    $dest = Join-Path $env:LOCALAPPDATA 'engram'
    $zip = Join-Path $env:TEMP $asset.name
    Invoke-WebRequest $asset.browser_download_url -OutFile $zip
    Expand-Archive $zip -DestinationPath $dest -Force
    Remove-Item $zip
    Add-UserPath $dest
}

# Conectar engram como MCP en cada agente instalado (claude-code pregunta por permisos)
if (Test-Cmd 'engram') {
    foreach ($pair in @(@('codex', 'codex'), @('opencode', 'opencode'), @('claude', 'claude-code'))) {
        if (Test-Cmd $pair[0]) {
            Write-Host "[engram] setup $($pair[1])"
            engram setup $pair[1]
        }
    }
}

# 4. Herdr (preview beta en Windows): un fallo no detiene el resto
if (Test-Cmd 'herdr') {
    Write-Host '[ok] herdr'
} else {
    Write-Host '[instalando] herdr (preview beta)'
    try {
        Invoke-RestMethod https://herdr.dev/install.ps1 | Invoke-Expression
        Update-SessionPath
    } catch {
        Write-Warning "herdr no se instalo: $($_.Exception.Message). El taller sigue sin el."
    }
}

# 5. Entorno Python del taller
$root = Resolve-Path (Join-Path $PSScriptRoot '..\..')
uv sync --directory $root

# 6. Resumen
Write-Host ''
Write-Host 'Resumen:'
foreach ($cmd in 'git', 'gh', 'lazygit', 'uv', 'node', 'claude', 'codex', 'opencode', 'pi', 'engram', 'herdr') {
    $state = if (Test-Cmd $cmd) { 'ok' } else { 'FALTA' }
    Write-Host ("  {0,-9} {1}" -f $cmd, $state)
}
Write-Host ''
Write-Host 'Siguiente: gh auth login, y abre una terminal nueva para refrescar el PATH.'
