import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    html_head_file="lapiz.html",
    layout_file="layouts/s08_verificacion_y_goals.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 8</span>
      <span class="titulo">Verificación y goals</span>
      <span class="bajada">Terminado lo decide una prueba, no el agente.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## El caso: de la EDA al anexo del paper

    <div class="idea">La exploración de la sesión 2 ahora alimenta una tabla que irá al paper.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>panel_macro</b>
        El mismo panel, en un módulo: extraer, limpiar, tabla de shocks.</div>
      <div class="tarjeta error"><b>El error clásico</b>
        Un año sin dato se cuenta como 0 y baja el promedio.</div>
      <div class="tarjeta ok"><b>La pregunta de la sesión</b>
        ¿Cómo sabemos que la tabla está bien, sin creerle al agente?</div>
    </div>

    <div class="nota">Demo: <code>ejemplos/panel_macro</code>, con su goal en <code>docs/goals/goal-1</code>.</div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué el test va antes que el código?

    <div class="idea">El test fija el número correcto antes de que el agente lo interprete.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "test_primero.svg", width="70%"),
            mo.md(r"""
    <div class="nota">Un test que nunca falló no demuestra nada: primero rojo, después verde.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué un checker y no su palabra?

    <div class="idea">Quien hizo el trabajo no es quien debe juzgarlo.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "checker_estados.svg", width="88%"),
            mo.md(r"""
    <div class="tarjetas">
      <div class="tarjeta aviso"><b>INCOMPLETE</b>
        Faltan pruebas: no es pasar.</div>
      <div class="tarjeta error"><b>FAIL</b>
        Algo comprobado no se cumple.</div>
      <div class="tarjeta ok"><b>PASS</b>
        Docs, lint y tests en orden.</div>
    </div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué un hook y no solo una regla?

    <div class="idea">Una regla escrita se puede olvidar; un hook no deja cerrar sin PASS.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta aviso"><b>AGENTS.md pide</b>
        Con el contexto largo, puede olvidarlo.</div>
      <div class="tarjeta ok"><b>El hook impone</b>
        Corre el checker cada vez que intenta cerrar.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "hook_cierre.svg", width="92%"),
                ],
                widths=[1, 1.1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué otra IA revisa el diff?

    <div class="idea">El test ve números; la pregunta metodológica la ve otro par de ojos.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "revision.svg", width="72%"),
            mo.md(r"""
    <div class="nota">Demo: <code>/revisar-con-pi</code> sobre el diff actual.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## Anatomía de un goal

    <div class="idea">El trabajo largo necesita un objetivo que sobreviva a cada chat.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    ```markdown
    # GOAL.md
    **Approved:** 2026-11-14 (dueño)
    ## Objetivo
      Tabla de shocks para el anexo del paper
    ## Criterios
      C1 24 filas, iguales a la EDA
      C2 año sin dato no cuenta como 0
      C3 "Del norte" = "Del Norte"
    ## Límites
      L1 no rellenar faltantes
    # RUN.md
    ### T03 Tabla de shocks en gold
      Test: test_anio_faltante_no_cuenta_como_cero
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>Approved</code><span>Lo aprueba el dueño, no el agente.</span>
      <code>Criterios</code><span>Con número: 4.2, no 3.15.</span>
      <code>Límites</code><span>Lo que no debe hacer, dicho antes.</span>
      <code>Tareas</code><span>Cada una con el test que la cierra.</span>
    </div>
    """),
                ],
                widths=[1.2, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué puede avanzar solo por horas?

    <div class="idea">Porque ningún paso empieza sin que el anterior esté comprobado.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "ejecucion.svg", width="100%"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué cortarse no hace perder nada?

    <div class="idea">Cada tarea cerrada es un commit y el marcador dice cuál sigue.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "commits.svg", width="84%"),
            mo.md(r"""
    <div class="nota">Demo: <code>/retomar-sesion ejemplos/panel_macro</code> en un chat nuevo.</div>
    """),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
