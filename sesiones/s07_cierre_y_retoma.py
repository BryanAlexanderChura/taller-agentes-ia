import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s07_cierre_y_retoma.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 7</span>
      <span class="titulo">Cerrar y retomar</span>
      <span class="bajada">El agente no recuerda. El proyecto sí.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué cerrar una sesión?

    <div class="idea">Lo que no quedó escrito, para el siguiente chat no existió.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>El contexto es temporal</b>
        Al cerrar el chat, todo lo que el agente entendió se pierde.</div>
      <div class="tarjeta"><b>Lo escrito sobrevive</b>
        Un archivo en el repo dura más que cualquier conversación.</div>
      <div class="tarjeta"><b>Cualquiera puede seguir</b>
        Otro agente, otra herramienta o tú mismo dentro de un mes.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un marcador y no un diario?

    <div class="idea">Un diario crece hasta que nadie lo lee. Un marcador dice dónde seguir.</div>

    <div class="tarjetas">
      <div class="tarjeta error"><b>Diario</b>
        Cuenta todo lo que pasó. Hay que leerlo entero para saber dónde estamos.</div>
      <div class="tarjeta ok"><b>Marcador</b>
        Cabe en una pantalla. Se lee en segundos y apunta a la siguiente acción.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía del marcador"),
            mo.hstack(
                [
                    mo.md(r"""
    ```yaml
    current_focus: Etapa silver de ventas a medias.
    goal: docs/goals/goal-1
    updated: 2026-11-14
    head: 60a432c
    next: [Validar montos negativos.]
    open: ["2026-11-10: confirmar fuente de clientes"]
    blockers: []
    last_session: 1042
    engram:
      decision_fuente_clientes: 1038
      bug_montos_negativos: 1017
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>current_focus</code><span>Una sola línea obliga a saber en qué estamos.</span>
      <code>goal</code><span>Conecta la sesión con un objetivo mayor.</span>
      <code>updated · head</code><span>El punto de cierre: lo posterior se verifica.</span>
      <code>next</code><span>La primera acción concreta: retomar sin pensar.</span>
      <code>open</code><span>Con fecha, para ver cuánto lleva pendiente.</span>
      <code>blockers</code><span>Lo que impide avanzar queda a la vista.</span>
      <code>last_session</code><span>Dónde quedó la conversación, sin copiarla aquí.</span>
      <code>engram</code><span>El historial que importa: qué responde cada memoria y su ID para abrirla.</span>
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
    ## ¿Por qué reglas tan estrictas?

    <div class="idea">Un estado que miente es peor que no tener estado.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Las fechas no se tocan</b>
        Ver cuánto lleva abierto algo revela lo que se está evitando.</div>
      <div class="tarjeta"><b>Se marca el punto de cierre</b>
        Lo que pasó después no está registrado: no se da por sabido.</div>
      <div class="tarjeta"><b>"Hecho" lo dice el checker</b>
        Escribir que algo está terminado no lo hace verdad.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué retomar sin tocar nada?

    <div class="idea">Antes de actuar, confirmar que el mapa coincide con el terreno.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Coincide</b>
        Se sigue con confianza.</div>
      <div class="tarjeta aviso"><b>Hay algo sin registrar</b>
        Se verifica antes de construir encima.</div>
      <div class="tarjeta error"><b>Se contradice</b>
        Se corrige el estado antes de trabajar.</div>
    </div>

    <div class="nota">Desconfiar cinco minutos es más barato que rehacer una tarde.</div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## El ciclo"),
            mo.image(mo.notebook_dir() / "img" / "ciclo.svg", width="100%"),
            mo.md(
                '<div class="idea">Cada sesión empieza donde terminó la anterior, '
                "no desde cero.</div>"
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
