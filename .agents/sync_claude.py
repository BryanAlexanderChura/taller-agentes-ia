"""Copia .agents/skills a .claude/skills (Claude Code no lee .agents/skills).

Copia en vez de symlink: en Windows los symlinks piden permisos especiales.
Uso: uv run python .agents/sync_claude.py
"""

import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / ".agents" / "skills"
DESTINO = RAIZ / ".claude" / "skills"


def main() -> int:
    shutil.copytree(
        ORIGEN, DESTINO, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__")
    )
    print(f"copiado: {ORIGEN} -> {DESTINO}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
