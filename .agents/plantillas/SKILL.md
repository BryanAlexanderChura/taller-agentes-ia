---
name: nombre-de-la-skill
description: Qué hace y cuándo usarla, en una frase. El agente decide con esto si la carga.
---

# nombre-de-la-skill

<!--
Plantilla para crear una skill nueva: cópiala a .agents/skills/<nombre>/SKILL.md
y corre `uv run python .agents/sync_claude.py`.

Cómo crece una skill:
1. Empieza con los pasos mínimos (versión 1).
2. Úsala en un caso real y observa dónde falla el agente.
3. Agrega una regla por cada fallo observado, y anota cuál fue.
4. Si una regla no evitó ningún fallo real, sobra: quítala.
Una skill larga que nadie justificó es más ruido que método.
-->

Uso: `/nombre-de-la-skill <argumento>`

## Reglas

- Lo que nunca debe hacer (por ejemplo: solo lectura, no hacer commit).

## Pasos

1. Primer paso, con el comando exacto si lo hay.
2. Segundo paso.
3. Cierre: cómo se verifica (skill `verificar`).

## Respuesta

El formato que debe devolver: viñetas, tabla, veredicto.

## Antipatrones

- El error típico que esta skill evita.

## Historial de reglas

| Regla | Fallo que la motivó |
| --- | --- |
| (ejemplo) Mirar git después de `head` | El agente tomó `next` como pendiente cuando ya estaba hecho. |
