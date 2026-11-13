---
name: verificar
description: Verifica un módulo (docs, lint, tests) antes de declarar terminado. Úsala al cerrar cualquier tarea.
---

# Verificar

```bash
uv run python .agents/skills/verificar/scripts/check.py <modulo>
```

| Salida | Estado | Acción |
|---|---|---|
| 0 | PASS | se puede declarar terminado |
| 1 | FAIL | corregir lo que indica y repetir |
| 2 | INCOMPLETE | falta evidencia (docs o tests): completarla |

Reporta el estado tal como sale. Nunca digas PASS sin haberlo visto.
