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
    """)
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


if __name__ == "__main__":
    app.run()
