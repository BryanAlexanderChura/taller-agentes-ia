import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    html_head_file="lapiz.html",
    layout_file="layouts/s03_limites_y_memoria.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 3</span>
      <span class="titulo">Límites y memoria</span>
      <span class="bajada">Lo que el modelo no puede solo, se lo damos nosotros.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué no sabe lo último?

    <div class="idea">Su conocimiento tiene fecha de corte: lo nuevo hay que traérselo.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "corte.svg", width="100%"),
            mo.md(r"""
    <div class="tarjetas">
      <div class="tarjeta aviso"><b>Escribe con lo que aprendió</b>
        Puede usar una versión vieja con total seguridad.</div>
      <div class="tarjeta ok"><b>La fuente gana</b>
        Documentación actual en el contexto pesa más que su memoria.</div>
      <div class="tarjeta"><b>Se le da, no se le pide</b>
        Docs, MCP o web: traer el dato es tarea nuestra.</div>
    </div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué cada chat empieza de cero?

    <div class="idea">Lo que se decidió ayer no existe hoy si no quedó guardado.</div>

    <div class="tarjetas">
      <div class="tarjeta error"><b>Sin memoria propia</b>
        Cerrar el chat borra todo lo que el agente entendió.</div>
      <div class="tarjeta aviso"><b>Repetir cuesta</b>
        Volver a explicar gasta tiempo y tokens, y se olvidan detalles.</div>
      <div class="tarjeta ok"><b>La memoria se construye</b>
        Hay que decidir qué se guarda y dónde.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué una memoria como Engram?

    <div class="idea">Las decisiones y su porqué sobreviven al chat que las tomó.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "memoria.svg", width="78%"),
            mo.md(r"""
    <div class="tarjetas">
      <div class="tarjeta"><b>Guarda el porqué</b>
        Decisiones y hallazgos, no el chat entero.</div>
      <div class="tarjeta"><b>Se consulta al retomar</b>
        El agente busca lo que necesita, cuando lo necesita.</div>
      <div class="tarjeta aviso"><b>No reemplaza los docs</b>
        Explica decisiones; la verdad del proyecto sigue en el repo.</div>
    </div>

    <div class="nota">Demo: guardar una decisión y recuperarla en un chat nuevo.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué toma el camino promedio?

    <div class="idea">Es estadística: ante lo ambiguo elige el camino más probable, no el que necesitas.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "caminos.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta aviso"><b>Más potente, más interpreta</b>
        Llena los huecos del pedido sin preguntar.</div>
      <div class="tarjeta aviso"><b>Esperado no es requerido</b>
        Lo típico funciona, pero puede no ser lo que tu caso pide.</div>
      <div class="tarjeta error"><b>No usa lo que no nombras</b>
        Una herramienta que no mencionas, para él no existe.</div>
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
            mo.md(r"""
    ## ¿Por qué no sabemos lo que no sabemos?

    <div class="idea">La IA conoce el mapa, pero solo alumbra lo que le insinúas.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "bosque.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta error"><b>Amplifica lo que ignoramos</b>
        Si no sabes que algo existe, no lo pides y no aparece.</div>
      <div class="tarjeta error"><b>Reafirma nuestros sesgos</b>
        Sigue el enfoque que traes, aunque haya uno mejor.</div>
      <div class="tarjeta aviso"><b>Un bosque oscuro</b>
        Lo desconocido no se ve desde donde estás parado.</div>
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
            mo.md(r"""
    ## ¿Por qué atacar lo que no sabes que no sabes?

    <div class="idea">Con la IA, lo profundo es barato; lo caro es saber qué existe.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "zonas.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta ok"><b>No hace falta dominarlo</b>
        Saber que existe y qué resuelve ya permite pedirlo.</div>
      <div class="tarjeta ok"><b>La IA pone la profundidad</b>
        Tú pones la pregunta; ella, el detalle.</div>
      <div class="tarjeta ok"><b>Cada nombre es una pregunta</b>
        Lo que conoces de nombre sale del promedio.</div>
    </div>

    <div class="nota">Por eso el taller recorre tantas herramientas: para que sepas qué pedir.</div>
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
    ## ¿Por qué instrucciones claras?

    <div class="idea">Lo que no dices, lo decide el promedio.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Alcance</b>
        Qué entra y qué no: si no se dice, lo decide él.</div>
      <div class="tarjeta"><b>Criterio de éxito</b>
        Cómo se sabe que terminó: si no se dice, termina cuando cree.</div>
      <div class="tarjeta"><b>Límites</b>
        Qué no debe tocar: si no se dice, puede tocarlo.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué verificar su trabajo?

    <div class="idea">"Terminado" no se afirma: se demuestra.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Tests</b>
        Prueban que hace lo que debe, hoy y después.</div>
      <div class="tarjeta ok"><b>Diff</b>
        Muestra exactamente qué cambió.</div>
      <div class="tarjeta ok"><b>Ejecución real</b>
        Lo que corre en serio no se puede fingir.</div>
    </div>

    <div class="nota">Reglas escritas en <code>AGENTS.md</code>: verificar antes de afirmar.</div>
    """)
    return


if __name__ == "__main__":
    app.run()
