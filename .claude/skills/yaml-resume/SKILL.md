---
name: yaml-resume
description: Cierra la sesión de un módulo: actualiza RESUME.yaml y CHANGELOG, y guarda el resumen en Engram.
---

# yaml-resume

Uso: `/yaml-resume <modulo>`

1. Revisa lo hecho en la sesión: `git status`, `git diff`, `git log` desde el último cierre.
2. Actualiza `<modulo>/docs/RESUME.yaml`:
   - `current_focus`: en qué quedó el trabajo, en una línea.
   - `next`: siguiente acción concreta primero.
   - `open`: pendientes con fecha (`AAAA-MM-DD: texto`).
   - `blockers`: lo que impide avanzar, con fecha; vacío si no hay.
3. Agrega lo hecho al `docs/CHANGELOG.md` si falta.
4. Si hay Engram: guarda un resumen de sesión (`mem_session_summary`) con objetivo, hecho, descubrimientos y siguiente paso.
5. Di qué quedó sin verificar. No declares terminado lo que el checker no confirmó.
