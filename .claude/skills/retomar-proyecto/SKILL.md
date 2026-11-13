---
name: retomar-proyecto
description: Recupera el estado de un módulo al abrir una sesión. Solo lectura.
---

# retomar-proyecto

Uso: `/retomar-proyecto <modulo>`

Solo lectura: no edites, no corras tests, no implementes.

1. Lee `<modulo>/docs/RESUME.yaml` y la última entrada de `docs/CHANGELOG.md`.
2. `git status` y `git log --oneline -10`: ¿hay cambios o commits que RESUME no refleja?
3. Si hay Engram: `mem_context` para la última sesión.

Responde en 3 a 5 viñetas:

- **Estado**: en qué quedó; COHERENTE o REQUIERE VERIFICACIÓN si las fuentes no coinciden.
- **Siguiente acción**: la primera de `next`.
- **Bloqueantes**: los de `blockers`, o ninguno.
- **Preguntas**: solo si queda una duda real.
