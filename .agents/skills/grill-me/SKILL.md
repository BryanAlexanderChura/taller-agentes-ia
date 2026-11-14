---
name: grill-me
description: Cuestiona una propuesta con preguntas basadas en evidencia hasta que el alcance, los tradeoffs y los criterios de aceptación queden claros. Úsala antes de un cambio no trivial.
---

# grill-me

Uso: `/grill-me <propuesta>`

Antes de programar, el agente te interroga. Cada pregunta que responde ahora es un
supuesto que no tiene que adivinar después.

## Método

1. Mira primero la evidencia: el código, los tests y los docs del módulo afectado.
2. Resume la propuesta y separa los hechos de los supuestos.
3. Si la propuesta mezcla piezas independientes, dilo antes de entrar en detalle:
   nombra las piezas, en qué orden construirlas, y sigue solo con la primera.
4. Cuestiona lo que tiene consecuencias: límites, fallos posibles, dependencias y lo que
   queda fuera. No inventes objeciones a detalles menores o ya decididos.
5. Una pregunta por turno. Si hay alternativas, da 2 o 3 opciones con tu recomendación.
6. No repitas una pregunta ya respondida con otras palabras.
7. Para cuando estén claros objetivo, alcance, lo que no se hará, criterios y tradeoffs,
   o cuando avanzar dependa de algo que nadie puede responder ahora.

## Respuesta

Un registro de decisiones corto:

- objetivo y límites confirmados;
- decisiones aceptadas y sus tradeoffs;
- criterios de aceptación medibles;
- dudas o bloqueantes sin resolver;
- evidencia revisada.

`write-goal` puede usar este registro como punto de partida. Interrogar no autoriza editar.

## Antipatrones

- Diez preguntas de golpe.
- Preguntar lo que el código ya responde.
- Discutir el nombre de una variable mientras el alcance sigue abierto.
