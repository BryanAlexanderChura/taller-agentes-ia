@echo off
setlocal
title Instalador de Claude Code
set "INSTALLER_FILE=%~f0"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$m='#PS'+'_START#'; $s=Get-Content -LiteralPath $env:INSTALLER_FILE -Raw; $i=$s.IndexOf($m); if($i -lt 0){Write-Host 'Archivo corrupto.' -ForegroundColor Red; exit 1}; Invoke-Expression $s.Substring($i+$m.Length)"
set "INSTALL_RESULT=%ERRORLEVEL%"

echo.
if not "%INSTALL_RESULT%"=="0" (
    echo La instalacion termino con errores. Revisa los mensajes anteriores.
    pause
    exit /b %INSTALL_RESULT%
)
pause
exit /b 0

#PS_START#
# ============================================================
#  INSTALADOR DE CLAUDE CODE - WINDOWS
#  - No requiere permisos de administrador
#  - No requiere winget (usa Git portable como alternativa)
#  - Instala VS Code, Git + Git Bash, Claude Code y OpenCode
#  - Ademas: uv, gh, lazygit, Node.js, pi, Engram (conectado) y herdr
#  - Configura automaticamente todas las variables de entorno
# ============================================================

$ErrorActionPreference = 'Stop'
try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch { }
$ProgressPreference = 'SilentlyContinue'

# API_KEYS_START
$apiKeysIntegradas = @(
    'APIKEYS PLaceholder'
 
)
# API_KEYS_END

function Titulo($texto) {
    Write-Host ''
    Write-Host $texto -ForegroundColor Cyan
}

function Update-SessionPath {
    $maquina = [Environment]::GetEnvironmentVariable('Path','Machine')
    $usuario = [Environment]::GetEnvironmentVariable('Path','User')
    $env:Path = ($maquina, $usuario | Where-Object { $_ }) -join ';'
}

function Add-UserPath([string]$dir) {
    if ([string]::IsNullOrWhiteSpace($dir)) { return }
    if (-not (Test-Path -LiteralPath $dir)) { return }
    $actual = [Environment]::GetEnvironmentVariable('Path','User')
    if ($null -eq $actual) { $actual = '' }
    foreach ($p in $actual.Split(';')) {
        if ($p -and ($p.TrimEnd('\') -ieq $dir.TrimEnd('\'))) {
            Write-Host ('    Ya estaba en PATH: ' + $dir) -ForegroundColor DarkGray
            return
        }
    }
    $nuevo = ($actual.TrimEnd(';') + ';' + $dir).Trim(';')
    [Environment]::SetEnvironmentVariable('Path', $nuevo, 'User')
    Write-Host ('    + Agregado al PATH: ' + $dir) -ForegroundColor Green
    Update-SessionPath
}

function Find-GitRoot {
    $candidatas = New-Object System.Collections.ArrayList
    $cmd = Get-Command git.exe -ErrorAction SilentlyContinue
    if ($cmd) { [void]$candidatas.Add((Split-Path (Split-Path $cmd.Source))) }
    foreach ($base in @($env:LOCALAPPDATA, $env:ProgramFiles, ${env:ProgramFiles(x86)}, $env:USERPROFILE)) {
        if (-not $base) { continue }
        [void]$candidatas.Add((Join-Path $base 'Programs\Git'))
        [void]$candidatas.Add((Join-Path $base 'Git'))
    }
    foreach ($r in $candidatas) {
        if ($r -and (Test-Path -LiteralPath (Join-Path $r 'cmd\git.exe'))) { return $r }
    }
    return $null
}

function Find-VSCodeRoot {
    foreach ($root in @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Microsoft VS Code'),
        (Join-Path $env:ProgramFiles 'Microsoft VS Code'),
        $(if (${env:ProgramFiles(x86)}) { Join-Path ${env:ProgramFiles(x86)} 'Microsoft VS Code' })
    )) {
        if ($root -and (Test-Path -LiteralPath (Join-Path $root 'Code.exe') -PathType Leaf)) { return $root }
    }
    $cmd = Get-Command code.cmd -CommandType Application -ErrorAction SilentlyContinue
    if ($cmd) { return (Split-Path (Split-Path $cmd.Source)) }
    return $null
}

Write-Host '======================================================' -ForegroundColor White
Write-Host '   INSTALADOR DE CLAUDE CODE (WINDOWS)' -ForegroundColor White
Write-Host '======================================================' -ForegroundColor White
Write-Host '   Sin permisos de administrador. Sin winget obligatorio.'

# ------------------------------------------------------------
# PASO 0: SISTEMA Y ARQUITECTURA
# ------------------------------------------------------------
Titulo '[0] Verificando el sistema...'
$windows = Get-ItemProperty -LiteralPath 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
$windowsMajor = if ($null -ne $windows.CurrentMajorVersionNumber) {
    [int]$windows.CurrentMajorVersionNumber
} else {
    [int]($windows.CurrentVersion.Split('.')[0])
}
if ($windowsMajor -lt 10) {
    Write-Host ''
    Write-Host '  ERROR: VS Code actual requiere Windows 10 o Windows 11.' -ForegroundColor Red
    Write-Host '  No se instalara nada. Contacta al instructor.' -ForegroundColor Red
    exit 1
}
if (-not [Environment]::Is64BitOperatingSystem) {
    Write-Host ''
    Write-Host '  ERROR: Este equipo es de 32 bits.' -ForegroundColor Red
    Write-Host '  Este instalador requiere Windows x64.' -ForegroundColor Red
    Write-Host '  No se instalara nada. Contacta al instructor.' -ForegroundColor Red
    exit 1
}
$arquitectura = if ($env:PROCESSOR_ARCHITEW6432) { $env:PROCESSOR_ARCHITEW6432 } else { $env:PROCESSOR_ARCHITECTURE }
if ($arquitectura -ine 'AMD64') {
    Write-Host ''
    Write-Host ('  ERROR: Arquitectura no compatible: ' + $arquitectura) -ForegroundColor Red
    Write-Host '  Este instalador solo admite equipos x64. ARM no esta permitido.' -ForegroundColor Red
    Write-Host '  No se instalara nada. Contacta al instructor.' -ForegroundColor Red
    exit 1
}
$nombreWindows = if ([int]$windows.CurrentBuildNumber -ge 22000) { 'Windows 11' } else { 'Windows 10' }
Write-Host ('    OK - ' + $nombreWindows + ' x64, compilacion ' + $windows.CurrentBuildNumber) -ForegroundColor Green
Update-SessionPath

# ------------------------------------------------------------
# PASO 1: VISUAL STUDIO CODE
# ------------------------------------------------------------
Titulo '[1] Verificando Visual Studio Code...'
$vscodeRoot = Find-VSCodeRoot
if ($vscodeRoot) {
    Write-Host ('    OK - VS Code ya esta instalado en: ' + $vscodeRoot) -ForegroundColor Green
} else {
    $vscodeUrl = 'https://update.code.visualstudio.com/latest/win32-x64-user/stable'
    $vscodeInstaller = Join-Path $env:TEMP ('VSCodeUserSetup-' + [IO.Path]::GetRandomFileName() + '.exe')
    try {
        Write-Host '    Descargando VS Code oficial para Windows x64...' -ForegroundColor Cyan
        Invoke-WebRequest -Uri $vscodeUrl -OutFile $vscodeInstaller -UseBasicParsing -TimeoutSec 900
        if (-not (Test-Path -LiteralPath $vscodeInstaller -PathType Leaf)) { throw 'La descarga no creo el instalador.' }
        if ((Get-Item -LiteralPath $vscodeInstaller).Length -lt 1MB) { throw 'El instalador descargado esta incompleto.' }

        Write-Host '    Verificando la firma digital de Microsoft...' -ForegroundColor Cyan
        $firma = Get-AuthenticodeSignature -LiteralPath $vscodeInstaller
        if ($firma.Status -ne 'Valid') { throw ('Firma digital no valida: ' + $firma.Status) }
        if ($firma.SignerCertificate.Subject -notmatch '(?i)(^|,\s*)O=Microsoft Corporation(,|$)') {
            throw ('El instalador no fue firmado por Microsoft Corporation: ' + $firma.SignerCertificate.Subject)
        }

        Write-Host '    Instalando VS Code para el usuario actual...' -ForegroundColor Yellow
        $procesoVSCode = Start-Process -FilePath $vscodeInstaller -ArgumentList '/VERYSILENT', '/NORESTART', '/MERGETASKS=!runcode' -Wait -PassThru
        if ($procesoVSCode.ExitCode -ne 0) { throw ('El instalador de VS Code termino con codigo ' + $procesoVSCode.ExitCode) }
        $vscodeRoot = Find-VSCodeRoot
        if (-not $vscodeRoot) { throw 'La instalacion termino, pero no se encontro Code.exe.' }
        Write-Host ('    OK - VS Code instalado en: ' + $vscodeRoot) -ForegroundColor Green
    } catch {
        Write-Host ('    ERROR al instalar VS Code: ' + $_.Exception.Message) -ForegroundColor Red
        Write-Host '    No se instalara ningun otro componente.' -ForegroundColor Red
        exit 1
    } finally {
        if (Test-Path -LiteralPath $vscodeInstaller -PathType Leaf) {
            Remove-Item -LiteralPath $vscodeInstaller -Force -ErrorAction SilentlyContinue
        }
    }
}
Add-UserPath (Join-Path $vscodeRoot 'bin')

# ------------------------------------------------------------
# PASO 2: GIT + GIT BASH
# ------------------------------------------------------------
Titulo '[2] Verificando Git y Git Bash...'
$gitRoot = Find-GitRoot

if ($gitRoot) {
    Write-Host ('    OK - Git ya esta instalado en: ' + $gitRoot) -ForegroundColor Green
} else {
    $instalado = $false

    # Opcion A: winget, solo si realmente esta disponible
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host '    Instalando Git con winget (perfil de usuario)...' -ForegroundColor Yellow
        try {
            winget install --id Git.Git -e --source winget --scope user --accept-package-agreements --accept-source-agreements --override '/VERYSILENT /NORESTART /PathOption=CmdTools' | Out-Null
            Update-SessionPath
            $gitRoot = Find-GitRoot
            if ($gitRoot) { $instalado = $true }
        } catch {
            Write-Host '    winget fallo. Se usara el metodo alternativo.' -ForegroundColor Yellow
        }
    } else {
        Write-Host '    winget no esta disponible en este equipo.' -ForegroundColor Yellow
    }

    # Opcion B: Git portable (no necesita admin ni winget)
    if (-not $instalado) {
        Write-Host '    Instalando Git portable en tu carpeta de usuario...' -ForegroundColor Yellow
        $destino = Join-Path $env:LOCALAPPDATA 'Programs\Git'
        $url = $null
        try {
            $rel = Invoke-RestMethod -Uri 'https://api.github.com/repos/git-for-windows/git/releases/latest' -Headers @{ 'User-Agent' = 'instalador-claude' } -TimeoutSec 30
            $asset = $rel.assets | Where-Object { $_.name -like 'PortableGit-*-64-bit.7z.exe' } | Select-Object -First 1
            if ($asset) { $url = $asset.browser_download_url }
        } catch { }
        if (-not $url) {
            $url = 'https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/PortableGit-2.47.1-64-bit.7z.exe'
        }
        $tmp = Join-Path $env:TEMP 'PortableGit-instalador.exe'
        try {
            Write-Host '    Descargando Git (puede tardar 1-3 minutos)...' -ForegroundColor Cyan
            Invoke-WebRequest -Uri $url -OutFile $tmp -UseBasicParsing -TimeoutSec 900
            Write-Host '    Extrayendo archivos...' -ForegroundColor Cyan
            $procesoGit = Start-Process -FilePath $tmp -ArgumentList ('-o"' + $destino + '"'), '-y' -Wait -PassThru
            if ($procesoGit.ExitCode -ne 0) { throw ('El extractor de Git termino con codigo ' + $procesoGit.ExitCode) }
            Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
            $gitRoot = Find-GitRoot
            if (-not $gitRoot -and (Test-Path -LiteralPath (Join-Path $destino 'cmd\git.exe'))) { $gitRoot = $destino }
            if ($gitRoot) {
                Write-Host ('    OK - Git portable instalado en: ' + $gitRoot) -ForegroundColor Green
            } else {
                Write-Host '    ERROR: No se pudo instalar Git.' -ForegroundColor Red
            }
        } catch {
            Write-Host ('    ERROR al descargar Git: ' + $_.Exception.Message) -ForegroundColor Red
            Write-Host '    Descargalo manualmente desde https://git-scm.com/download/win' -ForegroundColor White
        }
    }
}

# ------------------------------------------------------------
# PASO 3: VARIABLES DE ENTORNO DE GIT
# ------------------------------------------------------------
Titulo '[3] Configurando las variables de entorno de Git...'
if ($gitRoot) {
    Add-UserPath (Join-Path $gitRoot 'cmd')          # git.exe
    Add-UserPath (Join-Path $gitRoot 'usr\bin')      # ls, grep, sed, awk...
    Add-UserPath (Join-Path $gitRoot 'mingw64\bin')  # utilidades adicionales

    $bash = Join-Path $gitRoot 'bin\bash.exe'
    if (Test-Path -LiteralPath $bash) {
        [Environment]::SetEnvironmentVariable('CLAUDE_CODE_GIT_BASH_PATH', $bash, 'User')
        $env:CLAUDE_CODE_GIT_BASH_PATH = $bash
        Write-Host ('    + CLAUDE_CODE_GIT_BASH_PATH = ' + $bash) -ForegroundColor Green
    } else {
        Write-Host '    AVISO: no se encontro bash.exe dentro de Git.' -ForegroundColor Yellow
    }
} else {
    Write-Host '    Git no disponible, se omite esta configuracion.' -ForegroundColor Yellow
}

# ------------------------------------------------------------
# PASO 4: CLAUDE CODE
# ------------------------------------------------------------
Titulo '[4] Instalando Claude Code...'
$claudeOk = $false

# Si Claude Code ya esta instalado, no se reinstala
$claudeExistente = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claudeExistente) {
    $exeLocal = Join-Path $env:USERPROFILE '.local\bin\claude.exe'
    if (Test-Path -LiteralPath $exeLocal -PathType Leaf) { $claudeExistente = Get-Item -LiteralPath $exeLocal }
}
if ($claudeExistente) {
    $rutaClaude = if ($claudeExistente.Source) { $claudeExistente.Source } else { $claudeExistente.FullName }
    Write-Host ('    OK - Claude Code ya esta instalado en: ' + $rutaClaude) -ForegroundColor Green
    $claudeOk = $true
}

if (-not $claudeOk) {
Write-Host '    Metodo 1: instalador nativo de PowerShell...' -ForegroundColor Cyan
try {
    $script = Invoke-RestMethod -Uri 'https://claude.ai/install.ps1' -UseBasicParsing -TimeoutSec 120
    $global:LASTEXITCODE = 0
    & ([scriptblock]::Create($script))
    if ($LASTEXITCODE -ne 0) { throw ('El instalador nativo termino con codigo ' + $LASTEXITCODE) }
    $claudeOk = $true
    Write-Host '    OK - Instalacion nativa completada.' -ForegroundColor Green
} catch {
    Write-Host ('    El metodo 1 fallo: ' + $_.Exception.Message) -ForegroundColor Yellow
}
}

if (-not $claudeOk) {
    Write-Host '    Metodo 2 (alternativo): instalador para CMD...' -ForegroundColor Cyan
    try {
        $carpeta = Join-Path $env:TEMP 'claude-instalador'
        if (-not (Test-Path -LiteralPath $carpeta)) { New-Item -ItemType Directory -Path $carpeta -Force | Out-Null }
        $cmdFile = Join-Path $carpeta 'install.cmd'
        Invoke-WebRequest -Uri 'https://claude.ai/install.cmd' -OutFile $cmdFile -UseBasicParsing -TimeoutSec 120
        Push-Location $carpeta
        cmd.exe /c install.cmd
        $cmdExitCode = $LASTEXITCODE
        Pop-Location
        if ($cmdExitCode -ne 0) { throw ('El instalador CMD termino con codigo ' + $cmdExitCode) }
        Remove-Item -LiteralPath $carpeta -Recurse -Force -ErrorAction SilentlyContinue
        $claudeOk = $true
        Write-Host '    OK - Instalacion alternativa completada.' -ForegroundColor Green
    } catch {
        Write-Host ('    El metodo 2 tambien fallo: ' + $_.Exception.Message) -ForegroundColor Red
        Write-Host '    Revisa tu conexion a internet o el antivirus corporativo.' -ForegroundColor White
    }
}

# ------------------------------------------------------------
# PASO 5: VARIABLES DE ENTORNO DE CLAUDE CODE
# ------------------------------------------------------------
Titulo '[5] Configurando las variables de entorno de Claude Code...'
Update-SessionPath
$ubicaciones = @(
    (Join-Path $env:USERPROFILE '.local\bin'),
    (Join-Path $env:LOCALAPPDATA 'Programs\claude'),
    (Join-Path $env:LOCALAPPDATA 'claude\bin'),
    (Join-Path $env:USERPROFILE '.claude\bin'),
    (Join-Path $env:APPDATA 'npm')
)
$encontrado = $false
foreach ($u in $ubicaciones) {
    if ((Test-Path -LiteralPath (Join-Path $u 'claude.exe')) -or (Test-Path -LiteralPath (Join-Path $u 'claude.cmd'))) {
        Add-UserPath $u
        $encontrado = $true
    }
}
if (-not $encontrado) {
    $cc = Get-Command claude -ErrorAction SilentlyContinue
    if ($cc) {
        Add-UserPath (Split-Path $cc.Source)
        $encontrado = $true
    }
}
if (-not $encontrado) {
    Write-Host '    AVISO: no se localizo el ejecutable de Claude Code.' -ForegroundColor Yellow
    Write-Host '    Cierra y abre una terminal nueva y escribe: claude' -ForegroundColor White
}

# ------------------------------------------------------------
# PASO 6: ACTIVACION DE LA API (settings.json) - DESACTIVADO
#  Comentado a proposito: por ahora cada alumno inicia sesion con su cuenta.
#  Para reactivarlo, quita los marcadores de bloque de abajo.
# ------------------------------------------------------------
<#
Titulo '[6] Configurando el acceso a la API...'
$carpetaClaude = Join-Path $env:USERPROFILE '.claude'
if (-not (Test-Path -LiteralPath $carpetaClaude -PathType Container)) {
    Write-Host '    ERROR: la instalacion oficial no creo la carpeta .claude.' -ForegroundColor Red
    Write-Host ('    Ruta esperada: ' + $carpetaClaude) -ForegroundColor Red
    exit 1
}
$destinoSettings = Join-Path $carpetaClaude 'settings.json'

$apiKey = $null
$modoApi = $null
while (-not $modoApi) {
    Write-Host '    Elige como configurar el acceso:' -ForegroundColor White
    Write-Host '      [1] Automaticamente (recomendado)' -ForegroundColor Cyan
    Write-Host '      [2] Pegar una API key manualmente' -ForegroundColor White
    Write-Host '    Presiona Enter para usar la opcion recomendada.' -ForegroundColor DarkGray
    $respuestaApi = (Read-Host '    Opcion [1]').Trim()
    if ([string]::IsNullOrWhiteSpace($respuestaApi) -or $respuestaApi -eq '1') {
        $modoApi = 'automatico'
    } elseif ($respuestaApi -eq '2') {
        $modoApi = 'manual'
    } else {
        Write-Host '    Opcion no valida. Escribe 1 o 2.' -ForegroundColor Yellow
    }
}

if ($modoApi -eq 'automatico') {
    if ($apiKeysIntegradas.Count -eq 0) {
        throw 'No hay API keys integradas. Ejecuta actualizar_api_keys.py antes de distribuir el instalador.'
    }
    foreach ($claveIntegrada in $apiKeysIntegradas) {
        if ($claveIntegrada -notmatch '^sk-ant-[A-Za-z0-9_-]+$') {
            throw 'La lista integrada contiene una API key no valida.'
        }
    }
    $indiceApiKey = [int]((Get-Date).Ticks % $apiKeysIntegradas.Count)
    $apiKey = $apiKeysIntegradas[$indiceApiKey]
    Write-Host '    OK - Se asigno automaticamente una credencial temporal.' -ForegroundColor Green
    Write-Host '    La seleccion usa la fecha y hora actuales para distribuir las credenciales.' -ForegroundColor DarkGray
} else {
    Write-Host '    Pega la API key entregada por el instructor.' -ForegroundColor White
    Write-Host '    Por seguridad, los caracteres no se mostraran en pantalla.' -ForegroundColor DarkGray
    while (-not $apiKey) {
        $apiKeySegura = Read-Host '    API key' -AsSecureString
        $punteroApiKey = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($apiKeySegura)
        try {
            $apiKeyIngresada = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($punteroApiKey)
        } finally {
            [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($punteroApiKey)
        }

        $apiKeyIngresada = $apiKeyIngresada.Trim()
        if ($apiKeyIngresada -notmatch '^sk-ant-[A-Za-z0-9_-]+$') {
            Write-Host '    La API key no es valida. Debe comenzar con sk-ant- y no contener espacios.' -ForegroundColor Yellow
            $apiKeyIngresada = $null
            continue
        }
        $apiKey = $apiKeyIngresada
    }
}

if (Test-Path -LiteralPath $destinoSettings -PathType Leaf) {
    $marcaTiempo = Get-Date -Format 'yyyyMMdd-HHmmss'
    $respaldoSettings = Join-Path $carpetaClaude ('settings.json.bak.' + $marcaTiempo)
    Copy-Item -LiteralPath $destinoSettings -Destination $respaldoSettings -ErrorAction Stop
    Write-Host ('    Copia de seguridad creada: ' + (Split-Path $respaldoSettings -Leaf)) -ForegroundColor DarkGray
}

# Fusiona con el settings.json existente: solo agrega/actualiza apiKeyHelper
$configuracion = New-Object PSObject
if (Test-Path -LiteralPath $destinoSettings -PathType Leaf) {
    $textoActual = Get-Content -LiteralPath $destinoSettings -Raw
    if (-not [string]::IsNullOrWhiteSpace($textoActual)) {
        try {
            $configuracion = $textoActual | ConvertFrom-Json -ErrorAction Stop
        } catch {
            throw 'settings.json existente no es JSON valido; no se modifico. Corrigelo y vuelve a ejecutar.'
        }
    }
}
$configuracion | Add-Member -NotePropertyName 'apiKeyHelper' -NotePropertyValue ('echo ' + $apiKey) -Force
$json = $configuracion | ConvertTo-Json -Depth 50
[IO.File]::WriteAllText($destinoSettings, $json, (New-Object Text.UTF8Encoding($false)))

$configuracionGuardada = Get-Content -LiteralPath $destinoSettings -Raw -ErrorAction Stop | ConvertFrom-Json -ErrorAction Stop
if ($configuracionGuardada.apiKeyHelper -ne ('echo ' + $apiKey)) {
    throw 'La verificacion de settings.json fallo despues de guardar la API key.'
}
Write-Host ('    OK - API key configurada en: ' + $destinoSettings) -ForegroundColor Green
$apiKey = $null
$apiKeyIngresada = $null
#>

# ------------------------------------------------------------
# PASO 7: OPENCODE (APOYO)
# ------------------------------------------------------------
Titulo '[7] Instalando OpenCode como herramienta de apoyo...'
$openCodeBin = Join-Path $env:USERPROFILE '.opencode\bin'
$openCodeExe = Join-Path $openCodeBin 'opencode.exe'
$openCodeOk = $false

if (Test-Path -LiteralPath $openCodeExe -PathType Leaf) {
    Write-Host ('    OK - OpenCode ya esta instalado en: ' + $openCodeExe) -ForegroundColor Green
    $openCodeOk = $true
} else {
    $openCodeCmd = Get-Command opencode.exe -CommandType Application -ErrorAction SilentlyContinue
    if ($openCodeCmd) {
        $openCodeBin = Split-Path $openCodeCmd.Source
        Write-Host ('    OK - OpenCode ya esta instalado en: ' + $openCodeCmd.Source) -ForegroundColor Green
        $openCodeOk = $true
    } elseif ($bash -and (Test-Path -LiteralPath $bash -PathType Leaf)) {
        Write-Host '    OpenCode sirve como apoyo si se agota el acceso de Claude.' -ForegroundColor White
        Write-Host '    Ejecutando el instalador oficial dentro de Git Bash...' -ForegroundColor Cyan
        & $bash -lc 'curl -fsSL https://opencode.ai/install | OPENCODE_INSTALL_DIR="$HOME/.opencode/bin" bash'
        if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $openCodeExe -PathType Leaf)) {
            Write-Host ('    OK - OpenCode instalado en: ' + $openCodeExe) -ForegroundColor Green
            $openCodeOk = $true
        } else {
            Write-Host '    ERROR: El instalador oficial no dejo disponible opencode.exe.' -ForegroundColor Red
        }
    } else {
        Write-Host '    ERROR: Git Bash no esta disponible para instalar OpenCode.' -ForegroundColor Red
    }
}

if ($openCodeOk) { Add-UserPath $openCodeBin }

# ------------------------------------------------------------
# PASO 7B: HERRAMIENTAS DEL TALLER (rescatado de scripts\windows\instalar.ps1)
#  Hibrido: winget si existe; si no, descarga a la carpeta del usuario.
# ------------------------------------------------------------
function Test-Cmd($n) { [bool](Get-Command $n -ErrorAction SilentlyContinue) }

function Try-Winget($id) {
    if (-not (Test-Cmd 'winget')) { return }
    try {
        winget install --id $id -e --source winget --scope user --accept-package-agreements --accept-source-agreements | Out-Null
    } catch { }
    Update-SessionPath
}

function Get-Zip($url, $destino) {
    $zip = Join-Path $env:TEMP ([IO.Path]::GetRandomFileName() + '.zip')
    Invoke-WebRequest -Uri $url -OutFile $zip -UseBasicParsing -TimeoutSec 900
    Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
    [IO.File]::Delete($zip)
}

function Install-GitHubZip($repo, $patron, $destino) {
    $rel = Invoke-RestMethod -Uri ('https://api.github.com/repos/' + $repo + '/releases/latest') -Headers @{ 'User-Agent' = 'instalador-taller' } -TimeoutSec 30
    $asset = $rel.assets | Where-Object { $_.name -like $patron } | Select-Object -First 1
    if (-not $asset) { throw ('No hay asset ' + $patron + ' en ' + $repo) }
    Get-Zip $asset.browser_download_url $destino
}

function Add-ExeDir($destino, $exe) {
    $e = Get-ChildItem -LiteralPath $destino -Filter $exe -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($e) { Add-UserPath $e.DirectoryName }
}

function Instalar($cmd, $accion) {
    if (Test-Cmd $cmd) { Write-Host ('    OK - ' + $cmd + ' ya esta instalado') -ForegroundColor Green; return }
    Write-Host ('    Instalando ' + $cmd + '...') -ForegroundColor Yellow
    try { & $accion; Update-SessionPath } catch { Write-Host ('    ERROR ' + $cmd + ': ' + $_.Exception.Message) -ForegroundColor Red }
    if (Test-Cmd $cmd) { Write-Host ('    OK - ' + $cmd) -ForegroundColor Green }
}

Titulo '[7B] Instalando herramientas del taller...'
if (-not (Test-Cmd 'winget')) { Write-Host '    winget no disponible: se usan descargas directas.' -ForegroundColor DarkGray }

Instalar 'uv' {
    Try-Winget 'astral-sh.uv'
    if (-not (Test-Cmd 'uv')) { Invoke-RestMethod https://astral.sh/uv/install.ps1 | Invoke-Expression }
    Add-UserPath (Join-Path $env:USERPROFILE '.local\bin')
}

Instalar 'gh' {
    Try-Winget 'GitHub.cli'
    if (-not (Test-Cmd 'gh')) {
        $d = Join-Path $env:LOCALAPPDATA 'Programs\gh'
        Install-GitHubZip 'cli/cli' 'gh_*_windows_amd64.zip' $d
        Add-ExeDir $d 'gh.exe'
    }
}

Instalar 'lazygit' {
    Try-Winget 'JesseDuffield.lazygit'
    if (-not (Test-Cmd 'lazygit')) {
        $d = Join-Path $env:LOCALAPPDATA 'Programs\lazygit'
        Install-GitHubZip 'jesseduffield/lazygit' 'lazygit_*_Windows_x86_64.zip' $d
        Add-ExeDir $d 'lazygit.exe'
    }
}

Instalar 'node' {
    Try-Winget 'OpenJS.NodeJS.LTS'
    if (-not (Test-Cmd 'node')) {
        $idx = Invoke-RestMethod https://nodejs.org/dist/index.json -TimeoutSec 30
        $v = ($idx | Where-Object { $_.lts -and [int]($_.version.TrimStart('v').Split('.')[0]) -ge 22 } | Select-Object -First 1).version
        $d = Join-Path $env:LOCALAPPDATA 'Programs\node'
        Get-Zip ('https://nodejs.org/dist/' + $v + '/node-' + $v + '-win-x64.zip') $d
        Add-ExeDir $d 'node.exe'
    }
}
if (Test-Cmd 'node') {
    $nodeMajor = [int]((node --version).TrimStart('v').Split('.')[0])
    if ($nodeMajor -lt 22) { Write-Host ('    AVISO: Node ' + $nodeMajor + '; pi requiere 22+.') -ForegroundColor Yellow }
    $npmGlobal = Join-Path $env:APPDATA 'npm'
    if (-not (Test-Path -LiteralPath $npmGlobal)) { New-Item -ItemType Directory -Path $npmGlobal -Force | Out-Null }
    Add-UserPath $npmGlobal
}

Instalar 'pi' {
    if (-not (Test-Cmd 'npm')) { throw 'npm no disponible (falta Node).' }
    npm install -g --ignore-scripts '@earendil-works/pi-coding-agent'
}

Instalar 'engram' {
    $d = Join-Path $env:LOCALAPPDATA 'engram'
    Install-GitHubZip 'Gentleman-Programming/engram' '*windows_amd64.zip' $d
    Add-ExeDir $d 'engram.exe'
}
if (Test-Cmd 'engram') {
    foreach ($par in @(@('claude', 'claude-code'), @('opencode', 'opencode'), @('codex', 'codex'))) {
        if (Test-Cmd $par[0]) {
            Write-Host ('    Conectando engram con ' + $par[1] + '...') -ForegroundColor Cyan
            try { engram setup $par[1] } catch { Write-Host ('    AVISO: engram setup ' + $par[1] + ' fallo.') -ForegroundColor Yellow }
        }
    }
}

Instalar 'herdr' {
    Invoke-RestMethod https://herdr.dev/install.ps1 | Invoke-Expression
}

# Entorno Python del taller: solo si el instalador vive dentro del repo
$raiz = Split-Path -Parent $env:INSTALLER_FILE
while ($raiz -and -not (Test-Path -LiteralPath (Join-Path $raiz 'pyproject.toml'))) { $raiz = Split-Path -Parent $raiz }
if ($raiz -and (Test-Cmd 'uv')) {
    Write-Host ('    uv sync en ' + $raiz) -ForegroundColor Cyan
    try { uv sync --directory $raiz } catch { Write-Host '    AVISO: uv sync fallo.' -ForegroundColor Yellow }
} else {
    Write-Host '    Repo no encontrado: al clonarlo ejecuta  uv sync' -ForegroundColor DarkGray
}

# ------------------------------------------------------------
# PASO 8: VERIFICACION FINAL
# ------------------------------------------------------------
Titulo '--- RESULTADOS ---'
Update-SessionPath

function Verificar($comando, $etiqueta) {
    $c = Get-Command $comando -ErrorAction SilentlyContinue
    if ($c) {
        Write-Host ('[OK] ' + $etiqueta + ': ' + $c.Source) -ForegroundColor Green
    } else {
        Write-Host ('[X]  ' + $etiqueta + ': no encontrado (abre una terminal nueva)') -ForegroundColor Yellow
    }
}
Verificar 'git'      'Git          '
Verificar 'bash.exe' 'Git Bash     '
Verificar 'ls.exe'   'Comandos Unix'
Verificar 'code.cmd' 'VS Code      '
Verificar 'claude'   'Claude Code  '
Verificar 'opencode' 'OpenCode     '
Verificar 'uv'       'uv           '
Verificar 'gh'       'GitHub CLI   '
Verificar 'lazygit'  'lazygit      '
Verificar 'node'     'Node.js      '
Verificar 'pi'       'pi           '
Verificar 'engram'   'Engram       '
Verificar 'herdr'    'herdr        '

Write-Host ''
if (-not $claudeOk -and -not $encontrado) {
    Write-Host '======================================================' -ForegroundColor Red
    Write-Host '       INSTALACION INCOMPLETA: CLAUDE FALLO' -ForegroundColor Red
    Write-Host '======================================================' -ForegroundColor Red
    Write-Host 'La carpeta .claude y settings.json si fueron preparados.'
    Write-Host 'Revisa los errores de descarga mostrados arriba.'
    exit 1
}
if (-not $openCodeOk) {
    Write-Host '======================================================' -ForegroundColor Red
    Write-Host '       INSTALACION INCOMPLETA: OPENCODE FALLO' -ForegroundColor Red
    Write-Host '======================================================' -ForegroundColor Red
    Write-Host 'Claude Code quedo instalado, pero falta la herramienta de apoyo.'
    Write-Host 'Revisa los errores de descarga mostrados arriba.'
    exit 1
}
Write-Host '======================================================' -ForegroundColor White
Write-Host '         INSTALACION COMPLETADA' -ForegroundColor White
Write-Host '======================================================' -ForegroundColor White
Write-Host 'Ahora se abrira una terminal PowerShell nueva.'
Write-Host 'La nueva terminal carga el PATH actualizado y permite usar'
Write-Host 'Claude Code inmediatamente, sin reiniciar el equipo.'
Write-Host 'Puedes usar cualquiera de estos comandos:'
Write-Host ''
Write-Host '    claude' -ForegroundColor Cyan
Write-Host '    opencode' -ForegroundColor Cyan
Write-Host ''
Write-Host 'Siguiente paso: gh auth login' -ForegroundColor Yellow
Write-Host ''
Write-Host 'Si algo aparecio como [X], reinicia el equipo y vuelve'
Write-Host 'a comprobarlo antes de avisar al instructor.'
Write-Host '======================================================' -ForegroundColor White

try {
    Start-Process -FilePath 'powershell.exe' -WorkingDirectory $PWD.Path -ErrorAction Stop
} catch {
    Write-Host 'AVISO: no se pudo abrir una terminal nueva automaticamente.' -ForegroundColor Yellow
    Write-Host 'Cierra esta ventana y abre PowerShell manualmente.' -ForegroundColor White
}
