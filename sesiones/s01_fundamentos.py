import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s01_fundamentos.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 1</span>
      <span class="titulo">Fundamentos</span>
      <span class="bajada">Cómo piensa el agente decide cómo trabajamos con él.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué hablar de tokens?

    <div class="idea">El modelo no lee palabras: lee tokens. Y todo se paga en tokens.</div>

    <div class="tokens">
      <span><i>casa</i><small>1</small></span>
      <span><i>des</i><i>arroll</i><i>ador</i><small>3</small></span>
      <span><i>config</i><i>ur</i><i>ación</i><small>3</small></span>
      <span><i>AG</i><i>ENTS</i><i>.md</i><small>3</small></span>
    </div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Se cobra por token</b>
        Lo que entra y lo que sale tiene precio.</div>
      <div class="tarjeta"><b>El contexto tiene tope</b>
        Se mide en tokens, no en páginas ni en archivos.</div>
      <div class="tarjeta"><b>Ser conciso es ahorrar</b>
        Menos ruido deja más espacio para lo que importa.</div>
    </div>

    <div class="nota">Demo: tokenizador en vivo; cada modelo corta distinto.</div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué importan los embeddings?

    <div class="idea">El modelo entiende por cercanía de significado, no por palabras exactas.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "embeddings.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>Lo parecido se encuentra</b>
        Dos formas de decir lo mismo quedan cerca.</div>
      <div class="tarjeta"><b>Los nombres guían</b>
        Un buen nombre acerca al agente al concepto correcto.</div>
      <div class="tarjeta"><b>Base de la búsqueda</b>
        Así se encuentra lo relevante sin coincidencia literal.</div>
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
    ## ¿Por qué la atención importa?

    <div class="idea">Cada palabra mira a todas las demás para saber a qué se refiere.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "atencion.svg", width="100%"),
            mo.md(r"""
    <div class="nota">Por eso entiende "estaba" como el servidor. Y por eso cada token de más compite por esa atención.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué se degrada el contexto?

    <div class="idea">La atención es finita: cuanto más le das, menos atiende a cada cosa.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "curva_u.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta aviso"><b>Más es peor</b>
        Al crecer el contexto, el rendimiento baja.</div>
      <div class="tarjeta aviso"><b>El centro se pierde</b>
        Lo que queda en medio se atiende peor.</div>
      <div class="tarjeta error"><b>Un error se queda</b>
        Lo equivocado sigue en el contexto y se reutiliza.</div>
    </div>

    <div class="nota">Por eso: lo importante al inicio y un chat por tarea.</div>
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
    ## ¿Por qué el agente es un bucle?

    <div class="idea">No recuerda: cada salida va al final y en cada vuelta relee todo.</div>
    """),
            # En línea y no como imagen: así la animación corre dentro de la diapositiva.
            mo.Html(
                '<div class="animada" style="width: 88%">'
                + (mo.notebook_dir() / "img" / "bucle_animado.svg").read_text(encoding="utf-8")
                + "</div>"
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué cuidar el cache?

    <div class="idea">Lo que no cambia al inicio se reutiliza; cambiarlo invalida todo lo que sigue.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "cache.svg", width="100%"),
            mo.md(r"""
    <div class="nota">Demo: calculadora de tokens por turno, con y sin cache.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué comparar modelos?

    <div class="idea">Ninguno gana en todo, y el mejor para tu tarea cambia cada pocos meses.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b><a href="https://openrouter.ai">OpenRouter</a></b>
        Una sola API para muchos modelos: precios y uso real.</div>
      <div class="tarjeta"><b><a href="https://artificialanalysis.ai">Artificial Analysis</a></b>
        Calidad, velocidad y precio medidos con el mismo criterio.</div>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
