import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
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
    mo.md(r"""
    ## ¿Por qué no sabe lo último?

    <div class="idea">Su conocimiento tiene fecha de corte: lo nuevo hay que traérselo.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>Escribe con lo que aprendió</b>
        Puede usar una versión vieja con total seguridad.</div>
      <div class="tarjeta ok"><b>La fuente gana</b>
        Documentación actual en el contexto pesa más que su memoria.</div>
      <div class="tarjeta"><b>Se le da, no se le pide</b>
        Docs, MCP o web: traer el dato es tarea nuestra.</div>
    </div>
    """)
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
    mo.md(r"""
    ## ¿Por qué una memoria como Engram?

    <div class="idea">Las decisiones y su porqué sobreviven al chat que las tomó.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Guarda el porqué</b>
        Decisiones y hallazgos, no el chat entero.</div>
      <div class="tarjeta"><b>Se consulta al retomar</b>
        El agente busca lo que necesita, cuando lo necesita.</div>
      <div class="tarjeta aviso"><b>No reemplaza los docs</b>
        Explica decisiones; la verdad del proyecto sigue en el repo.</div>
    </div>

    <div class="nota">Demo: guardar una decisión y recuperarla en un chat nuevo.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué instrucciones claras?

    <div class="idea">Un modelo potente avanza rápido, también en la dirección equivocada.</div>

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
