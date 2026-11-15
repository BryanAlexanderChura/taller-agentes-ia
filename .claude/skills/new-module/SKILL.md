---
name: new-module
description: Crea un módulo nuevo con data/ (fuera de git), scripts/ con etapas medallion (a extraer, b procesar, c reporte), tests/, docs/ y config/.
---

# New module

```bash
uv run python .agents/skills/new-module/scripts/new_module.py <ruta> "<propósito>"
```

Crea:

```text
<ruta>/
  .gitignore            ignora data/
  data/                 datos (fuera de git)
  scripts/
    a01_extraer.py      bronze: leer el dato crudo
    b01_procesar.py     silver: limpiar y validar
    c01_reporte.py      gold: dejar listo para consumo
  tests/                un test por etapa: test_b01_procesar.py
  docs/RESUME.yaml      estado del módulo
  docs/CHANGELOG.md     historial de cambios
  config/config.yaml    rutas y reglas, fuera del código
```

Crea `tests/` vacía: el checker dará INCOMPLETE hasta que escribas el primer test con la skill `tdd`.
Cada etapa tiene su test con el mismo nombre: `scripts/b01_procesar.py` y `tests/test_b01_procesar.py`.
Nunca sobrescribe una ruta existente.
