"""Crea un módulo con etapas medallion y docs mínimos.

Uso: uv run python .agents/skills/new-module/scripts/new_module.py <ruta> "<propósito>"
"""

import sys
from datetime import date
from pathlib import Path

ETAPAS = {
    "a01_extraer.py": "Bronze: leer el dato crudo, tal como llega.",
    "b01_procesar.py": "Silver: limpiar y validar.",
    "c01_reporte.py": "Gold: dejar listo para consumo.",
}


def crear(ruta: Path, proposito: str) -> None:
    if ruta.exists():
        raise SystemExit(f"ya existe: {ruta}")
    (ruta / "docs").mkdir(parents=True)
    for archivo, doc in ETAPAS.items():
        (ruta / archivo).write_text(
            f'"""{doc}"""\n\n\ndef run():\n    raise NotImplementedError\n',
            encoding="utf-8",
        )
    (ruta / "docs" / "RESUME.yaml").write_text(
        "# Marcador del módulo, no diario. Lo actualiza /yaml-resume; lo lee /retomar-proyecto.\n"
        f"current_focus: {proposito}\n"
        "# goal: docs/goals/goal-1   # solo con un goal activo\n"
        f"updated: {date.today()}\n"
        'head: ""   # commit corto al cerrar la sesión\n'
        "next:\n  - Escribir el primer test (skill tdd).\n"
        "open: []       # AAAA-MM-DD: texto\n"
        "blockers: []   # AAAA-MM-DD: texto\n",
        encoding="utf-8",
    )
    (ruta / "docs" / "CHANGELOG.md").write_text(
        f"# Changelog\n\n## 0.1.0 - {date.today()}\n\n### Added\n\n- Módulo creado: {proposito}\n",
        encoding="utf-8",
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print('uso: new_module.py <ruta> "<propósito>"')
        return 2
    ruta = Path(argv[1])
    crear(ruta, argv[2])
    print(f"creado: {ruta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
