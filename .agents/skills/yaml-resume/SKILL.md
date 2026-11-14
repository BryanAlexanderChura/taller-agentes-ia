---
name: yaml-resume
description: Cierra la sesión de un módulo: sincroniza RESUME.yaml y CHANGELOG con lo hecho, y guarda el resumen en Engram.
---

# yaml-resume

Uso: `/yaml-resume <modulo>`

## Reglas

- RESUME es un marcador, no un diario: dice dónde seguir, no todo lo que pasó.
- Cada entrada es una frase corta. El detalle va al CHANGELOG, al goal o a Engram.
- Solo lo observado en la sesión: no inventes avances ni cierres.
- No reescribas criterios de un goal para que coincidan con el código: reporta la diferencia.

## Esquema

```yaml
current_focus: Una línea con en qué quedó el trabajo.
goal: docs/goals/goal-1   # solo con un goal activo; si no, se omite
updated: 2026-11-14       # fecha del cierre
head: 60a432c             # commit corto al cerrar
next:                     # sin fecha; la siguiente acción primero; máximo 5
  - Agregar la etapa silver.
open:                     # pendientes con fecha
  - "2026-11-10: confirmar la fuente de clientes con finanzas"
blockers:                 # lo que impide avanzar, con fecha; [] si no hay
  - "2026-11-12: sin acceso de lectura a la base de ventas"
last_session: 1eed5698    # opcional: ID del resumen de sesión en Engram
```

## Pasos

1. Revisa lo hecho: `git status`, `git diff` y `git log <head>..HEAD -- <modulo>`.
2. CHANGELOG: agrega lo hecho si falta, con lo que se verificó y lo que no.
3. RESUME:
   - Un pendiente resuelto sale de `open` o `blockers` solo después de quedar en el CHANGELOG.
   - Un pendiente que ya no aplica se borra sin más; git guarda la historia.
   - Un pendiente que sigue conserva su fecha original; solo uno nuevo lleva la fecha de hoy.
   - `goal` se mantiene mientras el goal no esté cerrado.
   - Actualiza `updated` y `head` al final, con el commit en que queda la sesión.
4. Verifica: `uv run python .agents/skills/verificar/scripts/check.py <modulo>`.
5. Engram (si está), solo en un cierre real: `mem_session_summary` una vez, con objetivo,
   hecho, descubrimientos y siguiente paso. Guarda su ID en `last_session`.

## Respuesta

Breve: qué cambió en RESUME y CHANGELOG, qué quedó sin verificar y el resultado del checker.
Actualizar el marcador no prueba que el trabajo esté terminado.

## Antipatrones

- Copiar el chat entero en RESUME.
- Marcar como hecho algo que el checker no confirmó.
- Cambiar la fecha de un pendiente viejo: oculta cuánto lleva abierto.
