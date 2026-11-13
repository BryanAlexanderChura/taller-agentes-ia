"""Hook PreToolUse (Claude Code y Codex): bloquea comandos destructivos.

Lee el evento JSON por stdin; si `tool_input` coincide con un patrón de
bloqueados.txt, sale con 2 y el motivo en stderr (el agente lo recibe).
"""

import json
import re
import sys
from pathlib import Path

PATRONES = Path(__file__).with_name("bloqueados.txt")
BLOQUEAR = 2


def patrones() -> list[str]:
    lineas = PATRONES.read_text(encoding="utf-8").splitlines()
    return [p for p in lineas if p.strip() and not p.startswith("#")]


def motivo(evento: dict) -> str | None:
    texto = json.dumps(evento.get("tool_input", {}), ensure_ascii=False)
    for patron in patrones():
        if re.search(patron, texto, re.IGNORECASE):
            return patron
    return None


def main() -> int:
    patron = motivo(json.load(sys.stdin))
    if patron:
        print(
            f"Bloqueado por el hook de seguridad (patrón: {patron}). Busca otra forma o pide permiso.",
            file=sys.stderr,
        )
        return BLOQUEAR
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
