---
name: retomar-proyecto
description: Recupera el estado de un módulo al abrir una sesión y detecta si sus fuentes se contradicen. Solo lectura.
---

# retomar-proyecto

Uso: `/retomar-proyecto <modulo>`

## Reglas

- Solo lectura: no edites, no corras tests, no implementes, no hagas commit.
- Lee cada fuente una vez. No recorras el código ni todo el historial.
- Engram explica decisiones pasadas; no prueba que algo esté terminado.
- No digas que los tests pasan: solo que pasaron cuando se cerró la sesión.

## Pasos

1. **RESUME**: lee `<modulo>/docs/RESUME.yaml` (`current_focus`, `goal`, `updated`,
   `head`, `next`, `open`, `blockers`, `last_session`, `engram`). Si no existe, dilo y
   sugiere `/yaml-resume`.
2. **Git**, solo para el módulo:
   - `git status --short <modulo>`: cambios sin commitear.
   - `git log --oneline <head>..HEAD -- <modulo>`: commits después del cierre.
3. **CHANGELOG**: la última entrada de `<modulo>/docs/CHANGELOG.md`. Basta para saber
   si los commits y cambios del paso 2 están registrados.
4. **Goal**: si `goal` existe, lee el estado y las tareas en curso de su `RUN.md`.
5. **Engram** (si está):
   - Abre `last_session` por su ID (`mem_get_observation`): es el resumen de la última sesión.
   - En `engram`, elige por la descripción y abre solo la memoria que responda una
     pregunta concreta; no las leas todas.
   - Sin IDs en RESUME: `mem_context` una vez. Un ID que no existe se reporta, no se adivina.
6. **Edad**: calcula los días desde la fecha de cada `open` y `blockers` hasta hoy.

## Coherencia

| Veredicto | Cuándo |
| --- | --- |
| COHERENTE | RESUME, git, CHANGELOG y RUN.md cuentan la misma historia. |
| REQUIERE VERIFICACIÓN | Hay commits o cambios después de `head` que CHANGELOG o RESUME no reflejan, o falta `head`. |
| CONTRADICCIÓN | Dos fuentes afirman cosas incompatibles: RUN.md cerrado con tareas abiertas, `next` ya hecho según CHANGELOG. |

Ante REQUIERE VERIFICACIÓN o CONTRADICCIÓN, recomienda `/yaml-resume` antes de seguir.

## Respuesta

De 3 a 6 viñetas, citando la fuente de cada dato:

- **Estado**: en qué quedó, el goal si hay, y el veredicto de coherencia.
- **Contexto clave**: solo lo necesario para entender el foco, con la edad en días de cada pendiente.
- **Siguiente acción**: la tarea en curso si hay; si no, la primera de `next`. No la ejecutes.
- **Bloqueantes**: los de `blockers` con su edad, o "ninguno documentado".
- **Preguntas**: solo si queda una duda real.

## Antipatrones

- Retomar leyendo todo el repositorio "para tener contexto".
- Tomar `next` como verdad sin mirar git: puede estar hecho y sin registrar.
- Empezar a trabajar dentro de la retoma.
