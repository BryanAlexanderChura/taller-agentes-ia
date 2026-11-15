import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    html_head_file="lapiz.html",
    layout_file="layouts/s09_herdr.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 9 · parte avanzada</span>
      <span class="titulo">Herdr</span>
      <span class="bajada">El entorno completo: varios agentes, un solo lugar.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué no bastan varias terminales?

    <div class="idea">Con varios agentes, el cuello de botella pasa a ser tu atención.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta ok"><b>Un contexto por tarea</b>
        Varios agentes enfocados rinden más que uno lleno de todo.</div>
      <div class="tarjeta aviso"><b>Nadie avisa</b>
        Hay que revisar cada ventana para saber quién espera.</div>
      <div class="tarjeta error"><b>Cerrar lo mata</b>
        Una terminal cerrada se lleva al agente y su trabajo.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "terminales_caos.svg", width="92%"),
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
    ## ¿Por qué un multiplexor para agentes?

    <div class="idea">Herdr no solo ve terminales: sabe qué agente corre en cada una.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "herdr_pantalla.svg", width="70%"),
            mo.md(r"""
    <div class="nota">La sesión vive aparte de la ventana: cerrarla no detiene a nadie.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué un estado por agente?

    <div class="idea">Un vistazo dice a quién atender primero.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta aviso"><b>blocked primero</b>
        Un agente esperando aprobación no avanza.</div>
      <div class="tarjeta ok"><b>done, después</b>
        Revisar lo terminado antes de darle otra tarea.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "estados_agentes.svg", width="92%"),
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
    ## ¿Por qué Herdr tiene una CLI?

    <div class="idea">Lo que tú haces con el teclado, un agente lo hace con comandos.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "herdr_cli.svg", width="86%"),
            mo.md(r"""
    <div class="nota">Demo en ia-postuler: Codex en un panel, pi en otro, tests en un tercero. Es la base de la sesión 10.</div>
    """),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
