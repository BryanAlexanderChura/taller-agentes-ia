import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/indice.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Taller de IA</span>
      <span class="titulo">De usuario a operador</span>
      <span class="bajada">Agentes de código con método: Claude Code, Codex, opencode y pi.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué este taller?

    <div class="idea">Un agente sin método es rápido. Con método, además, es confiable.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Entender cómo piensa</b>
        Sus límites explican cada regla que vamos a usar.</div>
      <div class="tarjeta"><b>Darle buenas herramientas</b>
        Un entorno que perdona y extensiones que obligan.</div>
      <div class="tarjeta"><b>Trabajar con método</b>
        Verificar, cerrar y retomar sin depender de la memoria del chat.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Entender

    <div class="idea">Antes de pedirle algo, saber cómo piensa y qué no puede hacer solo.</div>

    <div class="tarjetas">
      <a class="tarjeta" href="?file=s01_fundamentos.py"><span class="num">SESIÓN 01</span>
        <b>Fundamentos</b>Cómo piensa el agente decide cómo trabajamos con él.</a>
      <a class="tarjeta" href="?file=s02_entorno.py"><span class="num">SESIÓN 02</span>
        <b>Entorno</b>Un agente rápido necesita un entorno que perdone errores.</a>
      <a class="tarjeta" href="?file=s03_limites_y_memoria.py"><span class="num">SESIÓN 03</span>
        <b>Límites y memoria</b>Lo que el modelo no puede solo, se lo damos nosotros.</a>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Equipar

    <div class="idea">Las instrucciones piden; las herramientas hacen que se cumpla.</div>

    <div class="tarjetas">
      <a class="tarjeta" href="?file=s04_herramientas.py"><span class="num">SESIÓN 04</span>
        <b>Herramientas</b>Cambia la herramienta; el bucle y las reglas del proyecto se quedan.</a>
      <a class="tarjeta" href="?file=s05_extender_el_agente.py"><span class="num">SESIÓN 05</span>
        <b>Extender el agente</b>Cada pieza resuelve lo que las instrucciones solas no alcanzan.</a>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Organizar

    <div class="idea">Cada cosa en su lugar y un estado que no miente.</div>

    <div class="tarjetas">
      <a class="tarjeta" href="?file=s06_herdr.py"><span class="num">SESIÓN 06</span>
        <b>Herdr</b>Varios agentes ayudan solo si ves quién te necesita.</a>
      <a class="tarjeta" href="?file=s07_modulo_medallion.py"><span class="num">SESIÓN 07</span>
        <b>Medallion y módulos</b>Si cada cosa tiene su lugar, nadie gasta tiempo buscándola.</a>
      <a class="tarjeta" href="?file=s08_cierre_y_retoma.py"><span class="num">SESIÓN 08</span>
        <b>Cerrar y retomar</b>El agente no recuerda. El proyecto sí.</a>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Confiar

    <div class="idea">"Terminado" se demuestra, también cuando trabajan varios agentes.</div>

    <div class="tarjetas">
      <a class="tarjeta" href="?file=s09_verificacion_y_goals.py"><span class="num">SESIÓN 09</span>
        <b>Verificación y goals</b>Terminado lo decide una prueba, no el agente.</a>
      <a class="tarjeta" href="?file=s10_multiagente.py"><span class="num">SESIÓN 10</span>
        <b>Orquestación multiagente</b>Repartir el trabajo para que cada agente atienda una sola cosa.</a>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Tu proyecto

    <div class="idea">El método solo sirve si se usa en algo real.</div>

    <div class="tarjetas">
      <a class="tarjeta" href="?file=s11_como_continuar.py"><span class="num">SESIÓN 11</span>
        <b>Cómo continuar</b>El método vive en el proyecto, no en el chat ni en la herramienta.</a>
    </div>

    <div class="nota">Cada tarjeta abre su sesión. Para volver aquí: atrás en el navegador.</div>
    """)
    return


if __name__ == "__main__":
    app.run()
