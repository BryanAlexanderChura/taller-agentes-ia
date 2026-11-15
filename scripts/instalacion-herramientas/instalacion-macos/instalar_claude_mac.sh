#!/bin/bash
# ============================================================
#  INSTALADOR DE CLAUDE CODE - macOS / Linux
#  - No requiere permisos de administrador
#  - Instala VS Code, Git, Claude Code y OpenCode
#  - Configura automaticamente las variables de entorno (PATH)
# ============================================================

CLAUDE_BIN_DIR="$HOME/.local/bin"
MARK_START="# >>> Claude Code (instalador) >>>"
MARK_END="# <<< Claude Code (instalador) <<<"
VSCODE_MARK_START="# >>> Visual Studio Code (instalador) >>>"
VSCODE_MARK_END="# <<< Visual Studio Code (instalador) <<<"
OPENCODE_MARK_START="# >>> OpenCode (instalador) >>>"
OPENCODE_MARK_END="# <<< OpenCode (instalador) <<<"
set -o pipefail

# API_KEYS_START
API_KEYS=(
    'sk-ant-APIKEYS PLaceholder'
)
# API_KEYS_END

echo "======================================================"
echo "   INSTALADOR DE CLAUDE CODE (macOS / Linux)"
echo "======================================================"
echo ""

# ------------------------------------------------------------
# PASO 0: SISTEMA Y ARQUITECTURA
# ------------------------------------------------------------
echo "[0] Verificando el sistema..."
OS_NAME="$(uname -s)"
OS_ARCH="$(uname -m)"
if [ "$OS_NAME" = "Darwin" ] && [ "$(sysctl -n hw.optional.arm64 2>/dev/null)" = "1" ]; then
    OS_ARCH="arm64"
fi

case "$OS_NAME:$OS_ARCH" in
    Darwin:x86_64)
        SYSTEM_DESC="macOS Intel x64"
        VSCODE_PLATFORM="darwin"
        ;;
    Darwin:arm64)
        SYSTEM_DESC="macOS Apple Silicon arm64"
        VSCODE_PLATFORM="darwin-arm64"
        ;;
    Linux:x86_64)
        SYSTEM_DESC="Linux x64"
        VSCODE_PLATFORM="linux-x64"
        ;;
    Darwin:*|Linux:*)
        echo "    ERROR: Arquitectura no compatible: $OS_ARCH"
        echo "    Se admite macOS Intel x64, macOS Apple Silicon arm64 y Linux x64."
        echo "    No se instalara nada. Contacta al instructor."
        exit 1
        ;;
    *)
        echo "    ERROR: Sistema operativo no compatible: $OS_NAME"
        echo "    No se instalara nada. Contacta al instructor."
        exit 1
        ;;
esac

if [ "$OS_NAME" = "Darwin" ]; then
    MACOS_MAJOR="$(sw_vers -productVersion | cut -d. -f1)"
    case "$MACOS_MAJOR" in
        ''|*[!0-9]*)
            echo "    ERROR: No se pudo detectar la version de macOS."
            exit 1
            ;;
    esac
    if [ "$MACOS_MAJOR" -lt 12 ]; then
        echo "    ERROR: Este instalador requiere macOS 12 o posterior."
        echo "    No se instalara nada. Contacta al instructor."
        exit 1
    fi
    echo "    OK - macOS $(sw_vers -productVersion) - $OS_ARCH"
else
    echo "    OK - $SYSTEM_DESC"
fi

# ------------------------------------------------------------
# PASO 1: VISUAL STUDIO CODE
# ------------------------------------------------------------
echo ""
echo "[1] Verificando Visual Studio Code..."
VSCODE_BIN_DIR=""
if command -v code >/dev/null 2>&1; then
    VSCODE_BIN_DIR="$(dirname "$(command -v code)")"
    echo "    OK - VS Code ya esta instalado: $(command -v code)"
elif [ "$OS_NAME" = "Darwin" ]; then
    for VSCODE_APP in "$HOME/Applications/Visual Studio Code.app" "/Applications/Visual Studio Code.app"; do
        if [ -x "$VSCODE_APP/Contents/Resources/app/bin/code" ]; then
            VSCODE_BIN_DIR="$VSCODE_APP/Contents/Resources/app/bin"
            echo "    OK - VS Code ya esta instalado en: $VSCODE_APP"
            break
        fi
    done
elif [ -x "$HOME/.local/opt/vscode/bin/code" ]; then
    VSCODE_BIN_DIR="$HOME/.local/opt/vscode/bin"
    echo "    OK - VS Code ya esta instalado en: $HOME/.local/opt/vscode"
fi

if [ -z "$VSCODE_BIN_DIR" ]; then
    if ! command -v curl >/dev/null 2>&1; then
        echo "    ERROR: curl no esta disponible para descargar VS Code."
        echo "    No se instalara ningun otro componente."
        exit 1
    fi

    VSCODE_TMP="$(mktemp -d "${TMPDIR:-/tmp}/vscode-instalador.XXXXXX")" || exit 1
    if [ "$OS_NAME" = "Darwin" ]; then
        VSCODE_ARCHIVE="$VSCODE_TMP/vscode.zip"
        VSCODE_EXTRACT="$VSCODE_TMP/extract"
        VSCODE_URL="https://update.code.visualstudio.com/latest/$VSCODE_PLATFORM/stable"
        echo "    Descargando VS Code oficial para $SYSTEM_DESC..."
        if ! curl -fL --retry 3 --connect-timeout 30 --max-time 900 "$VSCODE_URL" -o "$VSCODE_ARCHIVE"; then
            echo "    ERROR: No se pudo descargar VS Code."
            exit 1
        fi
        if [ ! -s "$VSCODE_ARCHIVE" ] || [ "$(wc -c < "$VSCODE_ARCHIVE")" -lt 1048576 ]; then
            echo "    ERROR: La descarga de VS Code esta vacia o incompleta."
            exit 1
        fi

        mkdir -p "$VSCODE_EXTRACT"
        if ! ditto -x -k "$VSCODE_ARCHIVE" "$VSCODE_EXTRACT"; then
            echo "    ERROR: No se pudo extraer VS Code."
            exit 1
        fi
        VSCODE_APP="$VSCODE_EXTRACT/Visual Studio Code.app"
        if [ ! -x "$VSCODE_APP/Contents/Resources/app/bin/code" ]; then
            echo "    ERROR: El paquete descargado no contiene VS Code."
            exit 1
        fi
        echo "    Verificando la firma digital de Microsoft..."
        if ! codesign --verify --deep --strict "$VSCODE_APP" >/dev/null 2>&1; then
            echo "    ERROR: La firma digital de VS Code no es valida."
            exit 1
        fi
        VSCODE_SIGNER="$(codesign -dv --verbose=4 "$VSCODE_APP" 2>&1)"
        if ! printf '%s\n' "$VSCODE_SIGNER" | grep -qF 'TeamIdentifier=UBF8T346G9'; then
            echo "    ERROR: VS Code no fue firmado por Microsoft Corporation."
            exit 1
        fi
        if ! spctl --assess --type execute "$VSCODE_APP" >/dev/null 2>&1; then
            echo "    ERROR: macOS no aprobo la firma de VS Code."
            exit 1
        fi

        mkdir -p "$HOME/Applications"
        if [ -e "$HOME/Applications/Visual Studio Code.app" ]; then
            echo "    ERROR: Ya existe una instalacion de VS Code no reconocida en ~/Applications."
            echo "    No se sobrescribira. Contacta al instructor."
            exit 1
        fi
        mv "$VSCODE_APP" "$HOME/Applications/Visual Studio Code.app"
        VSCODE_BIN_DIR="$HOME/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
    else
        VSCODE_ARCHIVE="$VSCODE_TMP/vscode.tar.gz"
        VSCODE_EXTRACT="$VSCODE_TMP/extract"
        VSCODE_URL="https://update.code.visualstudio.com/latest/linux-x64/stable"
        echo "    Descargando VS Code oficial para Linux x64..."
        if ! curl -fL --retry 3 --connect-timeout 30 --max-time 900 "$VSCODE_URL" -o "$VSCODE_ARCHIVE"; then
            echo "    ERROR: No se pudo descargar VS Code."
            exit 1
        fi
        if [ ! -s "$VSCODE_ARCHIVE" ] || [ "$(wc -c < "$VSCODE_ARCHIVE")" -lt 1048576 ]; then
            echo "    ERROR: La descarga de VS Code esta vacia o incompleta."
            exit 1
        fi

        mkdir -p "$VSCODE_EXTRACT"
        if ! tar -xzf "$VSCODE_ARCHIVE" -C "$VSCODE_EXTRACT"; then
            echo "    ERROR: No se pudo extraer VS Code."
            exit 1
        fi
        if [ ! -x "$VSCODE_EXTRACT/VSCode-linux-x64/bin/code" ]; then
            echo "    ERROR: El paquete descargado no contiene VS Code."
            exit 1
        fi
        mkdir -p "$HOME/.local/opt"
        if [ -e "$HOME/.local/opt/vscode" ]; then
            echo "    ERROR: Ya existe una instalacion de VS Code no reconocida en ~/.local/opt/vscode."
            echo "    No se sobrescribira. Contacta al instructor."
            exit 1
        fi
        mv "$VSCODE_EXTRACT/VSCode-linux-x64" "$HOME/.local/opt/vscode"
        VSCODE_BIN_DIR="$HOME/.local/opt/vscode/bin"
    fi
    rm -f "$VSCODE_ARCHIVE"
    rmdir "$VSCODE_EXTRACT" "$VSCODE_TMP" 2>/dev/null || true
    echo "    OK - VS Code instalado para el usuario actual."
fi

add_vscode_path_block() {
    local rc="$1"
    [ -e "$rc" ] || touch "$rc"
    if grep -qF "$VSCODE_MARK_START" "$rc" 2>/dev/null; then
        echo "    VS Code ya configurado en PATH: $rc"
        return
    fi
    {
        echo ""
        echo "$VSCODE_MARK_START"
        echo "export PATH=\"$VSCODE_BIN_DIR:\$PATH\""
        echo "$VSCODE_MARK_END"
    } >> "$rc"
    echo "    VS Code agregado al PATH en: $rc"
}

add_vscode_path_block "$HOME/.zprofile"
add_vscode_path_block "$HOME/.zshrc"
add_vscode_path_block "$HOME/.bash_profile"
add_vscode_path_block "$HOME/.bashrc"
export PATH="$VSCODE_BIN_DIR:$PATH"

# ------------------------------------------------------------
# PASO 2: GIT
# ------------------------------------------------------------
echo ""
echo "[2] Verificando Git..."
if [ "$OS_NAME" = "Darwin" ]; then
    if xcode-select -p >/dev/null 2>&1 && git --version >/dev/null 2>&1; then
        echo "    OK - Herramientas de Apple y Git disponibles: $(git --version)"
    else
        echo "    Faltan las Herramientas de Linea de Comandos de Apple."
        echo "    Se abrira una ventana oficial de macOS para instalarlas."
        echo "    Pulsa Instalar, acepta la licencia y espera a que termine."
        echo "    El instalador continuara automaticamente despues."
        xcode-select --install >/dev/null 2>&1 || true

        printf "    Esperando a que finalice la instalacion"
        INTENTOS_XCODE=0
        while [ "$INTENTOS_XCODE" -lt 180 ]; do
            if xcode-select -p >/dev/null 2>&1 && git --version >/dev/null 2>&1; then
                break
            fi
            printf "."
            sleep 10
            INTENTOS_XCODE=$((INTENTOS_XCODE + 1))
        done
        echo ""

        if xcode-select -p >/dev/null 2>&1 && git --version >/dev/null 2>&1; then
            echo "    OK - Herramientas de Apple instaladas: $(git --version)"
        else
            echo "    ERROR: Las herramientas de Apple no terminaron de instalarse."
            echo "    Completa la ventana de Apple y vuelve a abrir este instalador."
            exit 1
        fi
    fi
elif command -v git >/dev/null 2>&1 && git --version >/dev/null 2>&1; then
    echo "    OK - Git ya esta instalado: $(git --version)"
else
    echo "    ERROR: Git no esta instalado."
    echo "    Instalalo con el gestor de paquetes de tu distribucion y vuelve a intentar."
    exit 1
fi

# ------------------------------------------------------------
# PASO 3: CLAUDE CODE (INSTALADOR NATIVO OFICIAL)
# ------------------------------------------------------------
echo ""
echo "[3] Instalando Claude Code (instalador nativo oficial)..."
if curl -fsSL https://claude.ai/install.sh | bash; then
    echo "    OK - Instalacion nativa finalizada."
else
    echo "    ERROR: No se pudo descargar el instalador."
    echo "    Revisa tu conexion a internet y vuelve a intentarlo."
    exit 1
fi

# ------------------------------------------------------------
# PASO 4: VARIABLES DE ENTORNO (PATH)
# ------------------------------------------------------------
echo ""
echo "[4] Configurando variables de entorno (PATH)..."

# Localizar el binario recien instalado
CLAUDE_PATH=""
for candidato in "$HOME/.local/bin/claude" "$HOME/.claude/bin/claude" "$HOME/bin/claude"; do
    if [ -x "$candidato" ]; then
        CLAUDE_PATH="$candidato"
        CLAUDE_BIN_DIR="$(dirname "$candidato")"
        break
    fi
done

if [ -z "$CLAUDE_PATH" ] && command -v claude >/dev/null 2>&1; then
    CLAUDE_PATH="$(command -v claude)"
    CLAUDE_BIN_DIR="$(dirname "$CLAUDE_PATH")"
fi

if [ -z "$CLAUDE_PATH" ]; then
    echo "    ERROR: La instalacion termino, pero no se encontro Claude Code."
    echo "    Vuelve a ejecutar el instalador o contacta al instructor."
    exit 1
fi

# Escribir el bloque de PATH en todos los archivos de arranque del usuario
add_path_block() {
    local rc="$1"
    [ -e "$rc" ] || touch "$rc"
    if grep -qF "$MARK_START" "$rc" 2>/dev/null; then
        echo "    Ya configurado: $rc"
        return
    fi
    {
        echo ""
        echo "$MARK_START"
        echo "export PATH=\"\$HOME/.local/bin:\$PATH\""
        if [ "$CLAUDE_BIN_DIR" != "$HOME/.local/bin" ] && [ -n "$CLAUDE_BIN_DIR" ]; then
            echo "export PATH=\"$CLAUDE_BIN_DIR:\$PATH\""
        fi
        echo "$MARK_END"
    } >> "$rc"
    echo "    Actualizado: $rc"
}

# zsh (shell por defecto en macOS) y bash, para cubrir todos los casos
add_path_block "$HOME/.zprofile"
add_path_block "$HOME/.zshrc"
add_path_block "$HOME/.bash_profile"
add_path_block "$HOME/.bashrc"

# Aplicar tambien en la sesion actual
export PATH="$HOME/.local/bin:$PATH"
[ -n "$CLAUDE_BIN_DIR" ] && export PATH="$CLAUDE_BIN_DIR:$PATH"

# ------------------------------------------------------------
# PASO 5: ACTIVACION DE LA API (settings.json)
# ------------------------------------------------------------
echo ""
echo "[5] Configurando el acceso a la API..."
if [ ! -d "$HOME/.claude" ]; then
    echo "    ERROR: la instalacion oficial no creo la carpeta ~/.claude."
    exit 1
fi

API_KEY=""
API_MODE=""
while [ -z "$API_MODE" ]; do
    echo "    Elige como configurar el acceso:"
    echo "      [1] Automaticamente (recomendado)"
    echo "      [2] Pegar una API key manualmente"
    echo "    Presiona Enter para usar la opcion recomendada."
    printf "    Opcion [1]: "
    IFS= read -r API_OPTION
    case "$API_OPTION" in
        ""|1) API_MODE="automatico" ;;
        2) API_MODE="manual" ;;
        *) echo "    Opcion no valida. Escribe 1 o 2." ;;
    esac
done

if [ "$API_MODE" = "automatico" ]; then
    if [ "${#API_KEYS[@]}" -eq 0 ]; then
        echo "    ERROR: No hay API keys integradas."
        echo "    Ejecuta actualizar_api_keys.py antes de distribuir el instalador."
        exit 1
    fi
    for EMBEDDED_KEY in "${API_KEYS[@]}"; do
        case "$EMBEDDED_KEY" in
            sk-ant-*) ;;
            *) echo "    ERROR: La lista integrada contiene una API key no valida."; exit 1 ;;
        esac
        case "$EMBEDDED_KEY" in
            *[!A-Za-z0-9_-]*)
                echo "    ERROR: La lista integrada contiene caracteres no validos."
                exit 1
                ;;
        esac
    done
    API_INDEX=$(( $(date +%s) % ${#API_KEYS[@]} ))
    API_KEY="${API_KEYS[$API_INDEX]}"
    echo "    OK - Se asigno automaticamente una credencial temporal."
    echo "    La seleccion usa la fecha y hora actuales para distribuir las credenciales."
else
    echo "    Pega la API key entregada por el instructor."
    echo "    Por seguridad, los caracteres no se mostraran en pantalla."
    while [ -z "$API_KEY" ]; do
        printf "    API key: "
        IFS= read -r -s API_KEY
        echo ""
        case "$API_KEY" in
            sk-ant-*) ;;
            *)
                echo "    La API key no es valida. Debe comenzar con sk-ant-."
                API_KEY=""
                continue
                ;;
        esac
        case "$API_KEY" in
            *[!A-Za-z0-9_-]*)
                echo "    La API key contiene espacios o caracteres no validos."
                API_KEY=""
                ;;
        esac
    done
fi

SETTINGS_FILE="$HOME/.claude/settings.json"
umask 077
if [ -f "$SETTINGS_FILE" ]; then
    BACKUP_FILE="$HOME/.claude/settings.json.bak.$(date +%Y%m%d-%H%M%S)"
    cp "$SETTINGS_FILE" "$BACKUP_FILE"
    echo "    Copia de seguridad creada: $(basename "$BACKUP_FILE")"
fi

printf '{\n  "apiKeyHelper": "echo %s"\n}\n' "$API_KEY" > "$SETTINGS_FILE"
if ! grep -qF "\"apiKeyHelper\": \"echo $API_KEY\"" "$SETTINGS_FILE"; then
    echo "    ERROR: no se pudo verificar settings.json."
    API_KEY=""
    exit 1
fi
echo "    OK - API key configurada en: $SETTINGS_FILE"
API_KEY=""

# ------------------------------------------------------------
# PASO 6: OPENCODE (APOYO)
# ------------------------------------------------------------
echo ""
echo "[6] Instalando OpenCode como herramienta de apoyo..."
OPENCODE_BIN_DIR="$HOME/.opencode/bin"
if command -v opencode >/dev/null 2>&1; then
    OPENCODE_BIN_DIR="$(dirname "$(command -v opencode)")"
    echo "    OK - OpenCode ya esta instalado: $(command -v opencode)"
elif [ -x "$OPENCODE_BIN_DIR/opencode" ]; then
    echo "    OK - OpenCode ya esta instalado en: $OPENCODE_BIN_DIR/opencode"
else
    echo "    OpenCode sirve como apoyo si se agota el acceso de Claude."
    echo "    Ejecutando el instalador oficial..."
    if ! curl -fsSL https://opencode.ai/install | OPENCODE_INSTALL_DIR="$OPENCODE_BIN_DIR" bash; then
        echo "    ERROR: No se pudo instalar OpenCode."
        exit 1
    fi
    if [ ! -x "$OPENCODE_BIN_DIR/opencode" ]; then
        echo "    ERROR: El instalador termino, pero no se encontro OpenCode."
        exit 1
    fi
    echo "    OK - OpenCode instalado en: $OPENCODE_BIN_DIR/opencode"
fi

add_opencode_path_block() {
    local rc="$1"
    [ -e "$rc" ] || touch "$rc"
    if grep -qF "$OPENCODE_MARK_START" "$rc" 2>/dev/null; then
        echo "    OpenCode ya configurado en PATH: $rc"
        return
    fi
    {
        echo ""
        echo "$OPENCODE_MARK_START"
        echo "export PATH=\"$OPENCODE_BIN_DIR:\$PATH\""
        echo "$OPENCODE_MARK_END"
    } >> "$rc"
    echo "    OpenCode agregado al PATH en: $rc"
}

add_opencode_path_block "$HOME/.zprofile"
add_opencode_path_block "$HOME/.zshrc"
add_opencode_path_block "$HOME/.bash_profile"
add_opencode_path_block "$HOME/.bashrc"
export PATH="$OPENCODE_BIN_DIR:$PATH"

# ------------------------------------------------------------
# PASO 7: VERIFICACION FINAL
# ------------------------------------------------------------
echo ""
echo "--- RESULTADOS ---"
check_cmd() {
    if command -v "$1" >/dev/null 2>&1; then
        echo "[OK] $2: $(command -v "$1")"
    else
        echo "[X]  $2: no encontrado (cierra y abre la Terminal)"
    fi
}
check_cmd git    "Git        "
check_cmd code   "VS Code    "
check_cmd claude "Claude Code"
check_cmd opencode "OpenCode   "

echo ""
echo "======================================================"
echo "         INSTALACION COMPLETADA"
echo "======================================================"
echo "Ahora se iniciara un shell nuevo en esta misma ventana."
echo "Esto carga el PATH actualizado y permite usar Claude Code"
echo "inmediatamente, sin cerrar la Terminal ni reiniciar el equipo."
echo "Puedes usar: code, claude y opencode"
echo "======================================================"

case "${SHELL:-}" in
    */zsh|*/bash)
        echo "Abriendo un shell actualizado con todas las variables de entorno..."
        exec "$SHELL" -l
        ;;
    *)
        echo "No se pudo detectar zsh o bash. Abre una Terminal nueva."
        ;;
esac
