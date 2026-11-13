---
name: new-module
description: Crea un módulo nuevo con etapas medallion (a extraer, b procesar, c reporte) y sus docs.
---

# New module

```bash
uv run python .agents/skills/new-module/scripts/new_module.py <ruta> "<propósito>"
```

Crea:

```text
<ruta>/
  a01_extraer.py    bronze: leer el dato crudo
  b01_procesar.py   silver: limpiar y validar
  c01_reporte.py    gold: dejar listo para consumo
  docs/RESUME.yaml  estado del módulo
  docs/CHANGELOG.md historial de cambios
```

No crea tests: el checker dará INCOMPLETE hasta que escribas el primero con la skill `tdd`.
Nunca sobrescribe una ruta existente.
