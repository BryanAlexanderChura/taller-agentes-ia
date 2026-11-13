# Reglas del proyecto

Versión lite del harness. Skills en `.agents/skills/`.

## Trabajo

- Antes de cambiar comportamiento: test primero, verlo fallar (skill `tdd`).
- No declares terminado sin `VERIFY PASS`:
  `uv run python .agents/skills/verificar/scripts/check.py <modulo>`.
- Cada cambio va en el `docs/CHANGELOG.md` del módulo.
- Python solo con `uv run`; dependencias en `pyproject.toml`.
- No borres archivos: muévelos a `legacy/`.
- Si algo es ambiguo, pregunta antes de avanzar.

## Sesión

- Al abrir: `/retomar-proyecto <modulo>`.
- Al cerrar: `/yaml-resume <modulo>`.
- Módulo nuevo: `/new-module <ruta>`.
- Antes de integrar un cambio grande: `/revisar-con-pi`.

## Skills

Edita solo `.agents/skills/`. `.claude/skills/` es una copia para Claude Code:
`uv run python .agents/sync_claude.py` la actualiza.
