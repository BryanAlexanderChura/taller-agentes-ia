import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s04_herramientas.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 4</span>
      <span class="titulo">Herramientas</span>
      <span class="bajada">Cambia la herramienta; el bucle y las reglas del proyecto se quedan.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué cuatro herramientas y no una?

    <div class="idea">Todas son el mismo bucle: cambia la interfaz, no el método.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Mismo bucle</b>
        Contexto, modelo y tool: lo de la sesión 1 vale en todas.</div>
      <div class="tarjeta"><b>Ninguna gana siempre</b>
        Como los modelos, la mejor para tu tarea cambia con el tiempo.</div>
      <div class="tarjeta ok"><b>Sin quedar atado</b>
        Si el método vive en el repo, cambiar de herramienta no cuesta.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué cada una tiene su lugar?

    <div class="idea">Se elige por lo que necesitas controlar, no por moda.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Codex</b>
        Lee <code>AGENTS.md</code> de forma nativa, con hooks y subagentes.</div>
      <div class="tarjeta"><b>opencode</b>
        Cambiar de proveedor sin cambiar de herramienta.</div>
      <div class="tarjeta"><b>Claude Code</b>
        Skills, hooks y subagentes integrados desde el inicio.</div>
      <div class="tarjeta"><b>pi</b>
        Mínimo: solo tiene lo que tú le agregas.</div>
    </div>

    <div class="nota">Demo: el mismo pedido en dos herramientas.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un archivo de instrucciones?

    <div class="idea">Lo que el agente no puede deducir, lo lee al empezar cada vez.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Cada chat empieza de cero</b>
        El archivo es lo primero que lee, sin que nadie lo repita.</div>
      <div class="tarjeta"><b>Reglas del proyecto</b>
        Viven en el repo, no en la memoria de quien escribe el prompt.</div>
      <div class="tarjeta"><b>Iguales para todos</b>
        Cada persona y cada agente parten de las mismas reglas.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un AGENTS.md corto?

    <div class="idea">Se carga en cada turno: cada línea compite por atención, siempre.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Solo lo no obvio</b>
        Lo que el agente deduce del código no necesita escribirse.</div>
      <div class="tarjeta"><b>Una regla, un lugar</b>
        Dos versiones de la misma regla terminan contradiciéndose.</div>
      <div class="tarjeta"><b>Lo largo, aparte</b>
        Un procedimiento va a una skill o a los docs.</div>
      <div class="tarjeta ok"><b>Inicio estable</b>
        Va al principio del contexto: si no cambia, se cachea.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía de AGENTS.md"),
            mo.hstack(
                [
                    mo.md(r"""
    ```text
    # Reglas del proyecto
    ## Trabajo
      Test primero, verlo fallar.
      Sin VERIFY PASS no está terminado.
      Python solo con uv run.
      No borres: mueve a legacy/.
      Si algo es ambiguo, pregunta.
    ## Sesión
      Al abrir: /retomar-proyecto.
      Al cerrar: /yaml-resume.
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>Test primero</code><span>Un test que falla antes prueba que el cambio importa.</span>
      <code>VERIFY PASS</code><span>"Terminado" no se afirma: se demuestra.</span>
      <code>uv run</code><span>Si el entorno no se reproduce, el error tampoco.</span>
      <code>legacy/</code><span>Lo que se mueve se recupera; lo borrado, no.</span>
      <code>pregunta</code><span>Ante la duda, frena en vez de inventar.</span>
      <code>Sesión</code><span>Retomar y cerrar igual en cada chat.</span>
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
    mo.vstack(
        [
            mo.md("## ¿Por qué AGENTS.md y no uno por herramienta?"),
            mo.image(mo.notebook_dir() / "img" / "agents_md.svg", width="100%"),
            mo.md(
                '<div class="idea">Un solo archivo que todas leen: '
                "las reglas no se duplican ni divergen.</div>"
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué no darle permiso total?

    <div class="idea">La confianza se da por grados, según lo que cuesta deshacer.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Lo reversible fluye</b>
        Con git como punto de retorno, editar es barato.</div>
      <div class="tarjeta aviso"><b>Lo irreversible pregunta</b>
        Lo que no se deshace pasa primero por ti.</div>
      <div class="tarjeta"><b>El diff cierra</b>
        Lo que aprobaste se confirma viendo qué cambió de verdad.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué planear antes de editar?

    <div class="idea">Corregir un plan cuesta una frase; corregir código, una tarde.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Se ve la intención</b>
        Sabes qué va a hacer antes de que toque nada.</div>
      <div class="tarjeta"><b>El error sale temprano</b>
        Un malentendido se nota en el plan, no en el diff.</div>
      <div class="tarjeta"><b>Alcance acordado</b>
        Lo que entra y lo que no queda dicho antes de empezar.</div>
    </div>

    <div class="nota">Demo: el mismo pedido en modo plan y directo.</div>
    """)
    return


if __name__ == "__main__":
    app.run()
