---
name: presentar-porque
description: Convierte el contenido de una sesión en diapositivas que explican por qué hacemos las cosas así, no cómo se hacen. Úsala al crear o reescribir una presentación del taller.
---

# presentar-porque

Uso: `/presentar-porque sesiones/<sesion>.py`

Las diapositivas dicen **por qué**. El **cómo** (comandos, pasos, configuración) lo
explica el instructor en vivo o se ve en la demo. Una diapositiva que enseña a hacer
algo compite con quien presenta; una que deja el porqué es lo que el alumno recuerda.

## Método

1. **Encuentra la decisión detrás de cada tema.** Para cada sección pregunta: ¿qué
   problema evita?, ¿qué pasaría si no lo hiciéramos? Si no hay respuesta, el tema
   sobra o es un detalle del cómo.
2. **Una pregunta por diapositiva**, como título: `¿Por qué ...?`. Máximo 48
   caracteres. Si no cabe, son dos diapositivas.
3. **Una idea central**, en una frase que se pueda repetir de memoria. Es la respuesta
   a la pregunta. Sin tecnicismos si hay una forma llana de decirlo.
4. **De 2 a 4 tarjetas con las razones.** Cada una: un nombre corto (3 o 4 palabras)
   y una frase. Son consecuencias o beneficios, nunca pasos.
5. **Lo concreto, solo como apoyo:**
   - una demo va en una nota (`Demo: ...`), sin explicar cómo se hace;
   - una conclusión práctica va en una nota (`Por eso: ...`);
   - un artefacto con partes (un YAML, un concepto con vocabulario) va en una
     diapositiva de anatomía: cada parte con su porqué, no con su definición.
6. **Una imagen solo si muestra una relación** (un ciclo, un bucle, un flujo) que en
   texto costaría un párrafo.
7. **Portada**: número de sesión, título corto y una bajada que resuma el porqué de
   toda la sesión.

## Cómo suena

| En vez de (el cómo) | Escribe (el porqué) |
| --- | --- |
| `uv sync`, `uv add`, `uv run` | Si el entorno no se puede reproducir, el error tampoco. |
| RESUME tiene `next`, `open`, `blockers` | Un diario crece hasta que nadie lo lee. Un marcador dice dónde seguir. |
| Correr los tests antes de cerrar | "Terminado" no se afirma: se demuestra. |
| Usa `/clear` entre tareas | La atención es finita: cuanto más le das, menos atiende a cada cosa. |

## Bloques disponibles

Están en `sesiones/tema.css`; la estética ya está resuelta, no la cambies aquí.

| Bloque | HTML dentro de `mo.md` |
| --- | --- |
| Portada | `<div class="portada"><span class="numero">Sesión N</span><span class="titulo">...</span><span class="bajada">...</span></div>` |
| Idea central | `<div class="idea">...</div>` |
| Tarjetas | `<div class="tarjetas"><div class="tarjeta"><b>Nombre</b> frase</div>...</div>` |
| Tarjeta con veredicto | clase extra `ok`, `aviso` o `error`, solo cuando el color significa algo |
| Nota | `<div class="nota">Demo: ...</div>` |
| Anatomía | `<div class="anatomia"><code>parte</code><span>su porqué</span>...</div>` |
| Texto tecleado | `class="escribir"`; los títulos y la portada ya lo traen |

Imágenes: SVG en `sesiones/img/` con la paleta del tema (fondo `#121212`, acento
`#a3e635`, neutro `#404040`, texto `#fafafa`, tenue `#737373`, fuente monoespaciada),
insertadas con `mo.image(mo.notebook_dir() / "img" / "<nombre>.svg", width="100%")`.

## Pasos

1. Lee la sesión actual y lista sus temas. Para cada uno, escribe la pregunta y la idea
   central antes de tocar el archivo. Muéstralas al dueño si cambian el contenido.
2. Reescribe `sesiones/<sesion>.py`: una celda por diapositiva, con
   `css_file="tema.css"` y `layout_file="layouts/<sesion>.slides.json"` en `marimo.App`.
3. Crea `sesiones/layouts/<sesion>.slides.json` con `{"type": "slides", "data": {}}`.
4. Revisa: `uv run ruff check sesiones` y `uv run marimo check sesiones/<sesion>.py`.
5. Míralo de verdad: sirve la sesión con
   `uv run marimo run sesiones/<sesion>.py --headless --port 2719 --no-token` y captura
   cada diapositiva con `scripts/presentaciones/capturas.py`. Revisa cada captura:
   título completo, nada cortado, nada que se superponga.
6. Registra el cambio en el CHANGELOG.

## Lista de control por diapositiva

- [ ] El título es una pregunta de hasta 48 caracteres.
- [ ] La idea central responde la pregunta en una frase.
- [ ] Ninguna tarjeta describe un paso, un comando o una opción.
- [ ] Si quito la diapositiva, se pierde una razón, no una instrucción.
- [ ] Se lee en menos de 15 segundos.

## Antipatrones

- Listas de viñetas con comandos: eso es un manual, no una presentación.
- Definir en vez de justificar: "Commit: una foto del cambio" sin decir para qué sirve.
- Meter todo el detalle "por si acaso": el detalle lo pone quien presenta.
- Colores de veredicto como decoración.
- Títulos largos: se cortan y rompen la animación.

## Historial de reglas

| Regla | Fallo que la motivó |
| --- | --- |
| Diapositivas con el porqué, no el cómo | La primera versión de s08 explicaba pasos que el instructor ya cuenta. |
| Anatomía con el porqué de cada parte | Al quitar el YAML se perdió la referencia; volvió, pero explicando para qué sirve cada campo. |
| Una idea central por diapositiva | Las listas de viñetas no dejaban ninguna frase para recordar. |
| Revisar con capturas | Detalles como un YAML ilegible o un cursor mal ubicado solo se vieron en pantalla. |
