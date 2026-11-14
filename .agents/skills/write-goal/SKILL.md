---
name: write-goal
description: Escribe un goal (GOAL.md con criterios verificables y RUN.md con tareas ejecutables) cuando el dueño lo pide. Úsala para trabajo largo o de varias sesiones.
---

# write-goal

Uso: `/write-goal <modulo> <objetivo>`

Solo cuando el dueño pide un goal. Si crees que hace falta, sugiérelo en una línea y sigue.

## 1. Descubrir (solo lectura)

Revisa el módulo, su código y sus tests. Luego interroga con el método de `grill-me`
hasta resolver:

- el problema, a quién afecta y qué resultado lo resuelve;
- qué entra, qué queda fuera y qué rutas pueden cambiar;
- criterios: cada uno un resultado observable con un umbral o una verificación;
- límites: lo que el trabajo no debe hacer ni tocar;
- riesgos y dudas sin resolver.

No uses palabras vagas como "rápido" o "preciso" sin umbral. No inventes plazos,
tolerancias ni fuentes: lo no resuelto se escribe como no resuelto.

## 2. Aprobar antes de escribir

Presenta un resumen corto (objetivo, alcance, criterios, decisiones, dudas) y espera
aprobación. Aprobar el goal no autoriza implementarlo.

## 3. Escribir

En `<modulo>/docs/goals/goal-<n>/`:

```markdown
# GOAL.md
**Approved:** pending
## Objetivo
## Alcance        (entra / queda fuera)
## Criterios      C1, C2... cada uno verificable
## Límites        L1, L2...
```

```markdown
# RUN.md
**State:** open
## Tareas
### T01 <resultado>
- Status: pending | in progress | done | blocked
- Files: rutas exactas
- Test: el test que se escribe primero
- Validation: comando exacto y qué criterio cubre
## Decisiones
| ID | Decisión | Fuente |
```

Reglas de las tareas:

- Cada tarea deja un resultado revisable, con su test.
- Dos tareas sin dependencia no tocan los mismos archivos.
- Todo criterio queda cubierto por la `Validation` de al menos una tarea.
- Sin `TBD`, `TODO` ni "igual que la otra tarea".

Solo el dueño cambia `**Approved:** pending` a la fecha de aprobación.
Apunta `goal:` en `RESUME.yaml` al directorio del goal.

## Respuesta

La secuencia de tareas, el alcance, las verificaciones y los riesgos abiertos.

## Antipatrones

- Escribir el goal antes de preguntar.
- Tareas que dicen cómo programar en vez de qué resultado dejar.
- Un criterio sin forma de verificarlo.
