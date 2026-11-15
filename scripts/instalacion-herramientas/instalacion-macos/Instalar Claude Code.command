#!/bin/bash

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
INSTALLER="$SCRIPT_DIR/instalar_claude_mac.sh"

if [ ! -f "$INSTALLER" ]; then
    echo "ERROR: No se encontro instalar_claude_mac.sh."
    echo "Mantenga ambos archivos dentro de la misma carpeta."
    echo ""
    printf "Presiona Enter para cerrar..."
    IFS= read -r _
    exit 1
fi

exec /bin/bash "$INSTALLER"
