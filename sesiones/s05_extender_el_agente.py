import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s05_extender_el_agente.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 5</span>
      <span class="titulo">Extender el agente</span>
      <span class="bajada">Cada pieza resuelve lo que las instrucciones solas no alcanzan.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué skills?

    <div class="idea">Un procedimiento largo solo ocupa contexto cuando se usa.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Solo la descripción</b>
        Es lo único que paga en cada turno; con eso decide si la usa.</div>
      <div class="tarjeta"><b>El cuerpo, a demanda</b>
        Los pasos entran al contexto recién cuando hacen falta.</div>
      <div class="tarjeta ok"><b>Siempre igual</b>
        El método no depende de cómo lo pidas ese día.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía de una skill"),
            mo.hstack(
                [
                    mo.md(r"""
    ```markdown
    ---
    name: verificar
    description: Verifica un módulo antes
      de declarar terminado.
    ---
    ## Reglas
    ## Pasos
    ## Antipatrones
    ## Historial de reglas

    scripts/check.py
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>description</code><span>Lo único que el agente ve siempre: decide con eso si la carga.</span>
      <code>Reglas</code><span>Lo que nunca debe hacer, antes que cualquier paso.</span>
      <code>Pasos</code><span>El método, para no improvisarlo cada vez.</span>
      <code>Antipatrones</code><span>El error típico, nombrado para reconocerlo.</span>
      <code>Historial</code><span>Cada regla con el fallo que la justificó.</span>
      <code>scripts/</code><span>Lo mecánico lo hace código, no el modelo.</span>
    </div>
    """),
                ],
                widths=[1, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué una skill crece con fallos?

    <div class="idea">Cada regla nace de un fallo real; la que no evitó ninguno, sobra.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Mirar git tras el cierre</b>
        Tomó como pendiente algo que ya estaba hecho.</div>
      <div class="tarjeta"><b>Veredicto explícito</b>
        Mezcló fuentes que no coincidían sin avisar.</div>
      <div class="tarjeta"><b>Edad de cada pendiente</b>
        Un bloqueante de un mes parecía de ayer.</div>
      <div class="tarjeta"><b>Solo lectura</b>
        Empezó a programar dentro de la retoma.</div>
    </div>

    <div class="nota">Reglas de <code>retomar-proyecto</code>. Plantilla: <code>.agents/plantillas/SKILL.md</code>.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué la CLI es su idioma nativo?

    <div class="idea">El agente vive en la terminal: una CLI no ocupa contexto hasta que la usa.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Gratis en reposo</b>
        Su ayuda se lee solo cuando hace falta.</div>
      <div class="tarjeta"><b>Texto que se encadena</b>
        La salida se lee, se filtra y se combina con otra.</div>
      <div class="tarjeta"><b>Ya está instalada</b>
        git, gh, uv: lo que usas tú, lo usa él.</div>
      <div class="tarjeta"><b>TUI para ti, CLI para él</b>
        Las mejores herramientas traen las dos.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué MCP?

    <div class="idea">Un estándar para conectar al agente con lo que no tiene CLI.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Uno sirve a todas</b>
        El mismo servidor funciona en cualquier herramienta compatible.</div>
      <div class="tarjeta"><b>Trae lo que no sabe</b>
        Memoria, índice del código, docs actuales.</div>
      <div class="tarjeta aviso"><b>Cada tool pesa</b>
        Sus descripciones viven en el contexto: pocos y bien elegidos.</div>
    </div>

    <div class="nota">Demo: Engram y CodeGraph respondiendo desde el agente.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué hooks?

    <div class="idea">Las instrucciones son sugerencias; un hook es código que corre siempre.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>El modelo olvida</b>
        Con el contexto largo, una regla de AGENTS.md puede perderse.</div>
      <div class="tarjeta ok"><b>Determinista</b>
        Corre fuera del modelo: no interpreta, no se distrae.</div>
      <div class="tarjeta"><b>Lo crítico va aquí</b>
        Seguridad, formato y verificación no se dejan a la memoria.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## ¿Por qué un hook en cada momento?"),
            mo.image(mo.notebook_dir() / "img" / "hooks.svg", width="88%"),
            mo.md(
                '<div class="idea">Cada paso del bucle es un punto donde imponer una regla.</div>'
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué bloquear en vez de pedir?

    <div class="idea">La seguridad no se pide en el prompt: se impone antes de cada comando.</div>

    <div class="tarjetas">
      <div class="tarjeta error"><b>Antes, no después</b>
        Lo irreversible no se arregla con una disculpa.</div>
      <div class="tarjeta"><b>Explica el motivo</b>
        El agente sabe por qué se rechazó y busca otro camino.</div>
      <div class="tarjeta ok"><b>Una lista para todas</b>
        Codex, Claude Code y opencode bloquean lo mismo.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    # Los patrones van con entidades HTML: escritos tal cual, el hook de
    # seguridad del repo bloquea la edición de este archivo.
    mo.md(r"""
    ## Anatomía de la lista de bloqueo

    <div class="idea">Cada patrón bloqueado protege algo que no se recupera.</div>

    <div class="anatomia">
      <code>rm&#32;-rf</code><span>Borrar es irreversible: lo que sobra se mueve a <code>legacy/</code>.</span>
      <code>push --force · reset --hard</code><span>Destruyen historia que otros ya tienen.</span>
      <code>&#46;env</code><span>Los secretos no deben entrar al contexto.</span>
      <code>&#45;&#45;no-verify</code><span>Saltar los controles anula todos los demás.</span>
      <code>DROP · DELETE</code><span>En producción, los datos son reales.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué subagentes?

    <div class="idea">Un contexto limpio para el trabajo que ensuciaría el tuyo.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Contexto propio</b>
        Explora mucho y devuelve solo un resumen.</div>
      <div class="tarjeta ok"><b>Ojos frescos</b>
        Revisa sin el sesgo de quien escribió el código.</div>
      <div class="tarjeta aviso"><b>Tiene costo</b>
        Más tokens y detalle perdido en el traspaso: lo pequeño, inline.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué empaquetarlo en un harness?

    <div class="idea">Clonar el repo es configurar el agente.</div>

    <div class="anatomia">
      <code>AGENTS.md</code><span>Pide: las reglas que debe tener presentes.</span>
      <code>skills</code><span>Enseñan: el método, solo cuando hace falta.</span>
      <code>CLI · MCP</code><span>Conectan: lo que no sabe o no alcanza solo.</span>
      <code>hooks</code><span>Obligan: lo que no puede quedar a su criterio.</span>
      <code>subagentes</code><span>Aíslan: el trabajo que ensuciaría el contexto.</span>
      <code>.agents/</code><span>Versiona todo: viaja con el repo y mejora con cada fallo.</span>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
