import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
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
      <span class="numero">Sesión 9</span>
      <span class="titulo">Herdr</span>
      <span class="bajada">Varios agentes ayudan solo si ves quién te necesita.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué varios agentes a la vez?

    <div class="idea">Un contexto limpio por tarea rinde más que uno lleno de todo.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Contexto enfocado</b>
        Cada agente atiende solo su tarea: la atención no se reparte.</div>
      <div class="tarjeta"><b>Avanzan en paralelo</b>
        Mientras uno explora, otro implementa y otro corre los tests.</div>
      <div class="tarjeta"><b>Errores aislados</b>
        Lo que confunde a un agente no contamina a los demás.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué no bastan varias terminales?

    <div class="idea">Con muchos agentes, el cuello de botella pasa a ser tu atención.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>¿Quién terminó?</b>
        Para saberlo hay que revisar ventana por ventana.</div>
      <div class="tarjeta aviso"><b>¿Quién te espera?</b>
        Un agente bloqueado pierde tiempo hasta que lo descubres.</div>
      <div class="tarjeta error"><b>Cerrar lo mata</b>
        Una terminal cerrada por error se lleva el trabajo a medias.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un multiplexor para agentes?

    <div class="idea">Herdr no solo ve terminales: sabe qué agente corre en cada una.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Reconoce al agente</b>
        Distingue Claude Code, Codex, opencode o pi y lee su estado.</div>
      <div class="tarjeta"><b>Todo en un lugar</b>
        Los agentes de un proyecto quedan juntos, a la vista.</div>
      <div class="tarjeta ok"><b>Sesión persistente</b>
        Cierras la ventana y, al volver, todo sigue trabajando.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Anatomía de Herdr

    <div class="anatomia">
      <code>workspace</code><span>Un proyecto por espacio: lo de uno no se mezcla con otro.</span>
      <code>tab</code><span>Una tarea por pestaña: se cambia de tema sin perder el hilo.</span>
      <code>pane</code><span>Un agente o comando por panel: cada uno con su propio contexto.</span>
      <code>sidebar</code><span>El estado de todos en una columna: no hay que ir a buscarlo.</span>
      <code>sesión</code><span>Vive aparte de la ventana: cerrarla no detiene a nadie.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un estado por agente?

    <div class="idea">Un vistazo dice a quién atender primero.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>working</b>
        Está avanzando: interrumpirlo solo rompe su ritmo.</div>
      <div class="tarjeta aviso"><b>blocked</b>
        Te espera: cada minuto sin verlo es tiempo perdido.</div>
      <div class="tarjeta ok"><b>done</b>
        Terminó: toca revisar lo que hizo, no darlo por bueno.</div>
      <div class="tarjeta"><b>idle</b>
        Está libre: puede tomar la siguiente tarea.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué Herdr tiene una CLI?

    <div class="idea">Lo que tú haces con el teclado, un agente lo hace con comandos.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>El idioma del agente</b>
        Vive en la terminal: una CLI es su forma más directa de actuar.</div>
      <div class="tarjeta"><b>Un agente coordina</b>
        Abre paneles, lanza a otro agente y espera su resultado.</div>
      <div class="tarjeta"><b>Base de la orquestación</b>
        Repartir trabajo entre agentes empieza aquí.</div>
    </div>

    <div class="nota">Demo en ia-postuler: Codex en un panel, pi en otro, tests en un tercero.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué Herdr no es obligatorio?

    <div class="idea">Herdr ordena el trabajo, pero el taller no depende de él.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>Windows en preview</b>
        La versión para Windows todavía es beta y puede fallar.</div>
      <div class="tarjeta ok"><b>Plan B: terminales</b>
        Sin Herdr, todo el taller funciona con terminales separadas.</div>
      <div class="tarjeta"><b>La idea se queda</b>
        Un contexto por tarea y el estado a la vista, con o sin herramienta.</div>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
