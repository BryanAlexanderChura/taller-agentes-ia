import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s02_entorno.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 2</span>
      <span class="titulo">Entorno</span>
      <span class="bajada">Un agente rápido necesita un entorno que perdone errores.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué uv?

    <div class="idea">Si el entorno no se puede reproducir, el error tampoco.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>El mismo para todos</b>
        Las versiones quedan fijadas: tu máquina, la mía, la del agente.</div>
      <div class="tarjeta"><b>El sistema intacto</b>
        El agente instala lo que quiera sin romper el Python de la máquina.</div>
      <div class="tarjeta"><b>Un comando, siempre igual</b>
        Correr algo no depende de qué está activado.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía de uv"),
            mo.hstack(
                [
                    mo.md(r"""
    ```bash
    uv init --python 3.14
    uv add polars
    uv sync
    uv run python main.py
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>uv init</code><span>Crea el proyecto y su pyproject.toml: las reglas quedan escritas desde el inicio.</span>
      <code>uv add</code><span>Declara la dependencia y fija el lock: nada se instala "de palabra".</span>
      <code>uv sync</code><span>Reproduce el entorno exacto en otra máquina.</span>
      <code>uv run</code><span>Corre dentro del entorno sin activarlo: no hay "en mi máquina sí funciona".</span>
    </div>
    """),
                ],
                widths=[1, 1.3],
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
            mo.md("## Anatomía de pyproject.toml"),
            mo.hstack(
                [
                    mo.md(r"""
    ```toml
    [project]
    name = "taller"
    version = "0.1.0"
    requires-python = ">=3.14"
    dependencies = [
        "polars>=1.0",
    ]
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>name</code><span>El proyecto tiene identidad, no es una carpeta suelta.</span>
      <code>requires-python</code><span>La versión de Python también es una dependencia.</span>
      <code>dependencies</code><span>Lo que el código necesita, escrito: el agente lo lee antes de instalar.</span>
      <code>uv.lock</code><span>Al lado: la versión exacta de todo, para que nada cambie solo.</span>
    </div>
    """),
                ],
                widths=[1, 1.3],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué git?

    <div class="idea">Dejar trabajar al agente es barato si deshacer es barato.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Punto de retorno</b>
        Cualquier cambio se puede deshacer en segundos.</div>
      <div class="tarjeta"><b>El diff es la verdad</b>
        Lo que el agente dice que hizo se confirma mirando el cambio.</div>
      <div class="tarjeta"><b>Historia que explica</b>
        Cada commit cuenta qué cambió y por qué.</div>
    </div>

    <div class="nota">Demo: <code>git init</code>. Desde ahí, cada cambio queda registrado.</div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué la historia es un árbol?

    <div class="idea">Probar en una rama no rompe lo que ya funciona.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "git_arbol.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta ok"><b>Volver es barato</b>
        Cada commit es un punto al que regresar.</div>
      <div class="tarjeta"><b>Probar sin miedo</b>
        La rama se tira si no sirve; main no se entera.</div>
      <div class="tarjeta"><b>Red del agente</b>
        Que se equivoque cuesta poco: se deshace.</div>
    </div>
    """),
                ],
                widths=[1.4, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## El vocabulario de GitHub

    <div class="idea">El trabajo del agente se revisa como el de cualquier persona.</div>

    <div class="anatomia">
      <code>repo</code><span>El proyecto y toda su historia en un lugar.</span>
      <code>remoto</code><span>Una copia fuera de tu máquina: nada se pierde.</span>
      <code>commit</code><span>Una foto del cambio, con su porqué.</span>
      <code>rama</code><span>Experimentar sin tocar lo que funciona.</span>
      <code>pull request</code><span>El cambio se revisa antes de entrar.</span>
      <code>issue</code><span>La tarea queda escrita, no en la cabeza de alguien.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué una CLI?

    <div class="idea">Una CLI se usa escribiendo: la persona y el agente, igual.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "cli_encuentro.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>La misma puerta</b>
        Lo que tú tecleas, el agente lo ejecuta tal cual.</div>
      <div class="tarjeta"><b>Texto para los dos</b>
        La salida se lee, se copia y se revisa.</div>
      <div class="tarjeta"><b>Sin clics</b>
        Una interfaz gráfica deja fuera al agente.</div>
    </div>
    """),
                ],
                widths=[1.4, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué gh?

    <div class="idea">Lo que se puede hacer desde la terminal, el agente lo hace sin pedirte clics.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Sin salir de la terminal</b>
        Pull requests e issues desde donde trabaja el agente.</div>
      <div class="tarjeta"><b>Salida que se lee</b>
        Texto que el agente entiende, filtra y encadena.</div>
      <div class="tarjeta"><b>El mismo flujo</b>
        Tú y el agente usan la misma herramienta.</div>
    </div>

    <div class="nota">Demo: <code>gh auth login</code> en vivo.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué marimo?

    <div class="idea">Un notebook que también es código: se versiona, se revisa y se reproduce.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Diffs limpios</b>
        Es un archivo Python normal: git y el agente lo leen sin ruido.</div>
      <div class="tarjeta"><b>Sin estado oculto</b>
        Al cambiar una celda se recalcula todo lo que depende de ella.</div>
      <div class="tarjeta"><b>Un archivo, muchos usos</b>
        Notebook, script, app o presentación, como esta.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué un notebook reactivo?

    <div class="idea">Lo que ves en pantalla siempre corresponde al código actual.</div>
    """),
            mo.hstack(
                [
                    mo.image(mo.notebook_dir() / "img" / "marimo_reactivo.svg", width="100%"),
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>Cambia y se propaga</b>
        Solo se recalcula lo que depende del cambio.</div>
      <div class="tarjeta"><b>Sin orden mágico</b>
        No importa en qué orden corriste las celdas.</div>
      <a class="tarjeta" href="?file=demos/eda_economia.py"><span class="num">DEMO</span><b>EDA de economía</b>
        Un notebook real para tocarlo.</a>
    </div>
    """),
                ],
                widths=[1.4, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
