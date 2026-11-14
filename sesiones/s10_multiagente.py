import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s10_multiagente.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 10</span>
      <span class="titulo">Orquestación multiagente</span>
      <span class="bajada">Repartir el trabajo para que cada agente atienda una sola cosa.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué orquestar y no solo abrir varios?

    <div class="idea">En Herdr cada agente hacía lo suyo; aquí trabajan juntos hacia un mismo objetivo.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Contexto chico y enfocado</b>
        Cada agente carga solo su tarea: menos ruido, más atención.</div>
      <div class="tarjeta ok"><b>En paralelo</b>
        Dos tareas que no se tocan no tienen por qué esperar turno.</div>
      <div class="tarjeta ok"><b>Ojos que no escribieron</b>
        Un revisor aparte ve lo que el autor no ve.</div>
      <div class="tarjeta aviso"><b>No siempre conviene</b>
        Tareas acopladas se pisan: dividirlas cuesta más de lo que ahorra.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué subagentes?

    <div class="idea">Un contexto limpio para el trabajo que ensuciaría el tuyo.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Contexto propio</b>
        Explora mucho y devuelve solo un resumen.</div>
      <div class="tarjeta ok"><b>Ojos frescos</b>
        Revisa sin el sesgo de quien escribió el código.</div>
      <div class="tarjeta aviso"><b>Tiene costo</b>
        Más tokens y detalle perdido en el traspaso: lo pequeño, inline.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un worktree por agente?

    <div class="idea">Dos agentes en la misma carpeta se pisan: cada uno necesita su copia.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Nadie pisa a nadie</b>
        Cada agente edita sus archivos sin cambiarle el suelo al otro.</div>
      <div class="tarjeta"><b>Su propia rama</b>
        Cada cambio se revisa e integra por separado.</div>
      <div class="tarjeta"><b>Barato y desechable</b>
        Mismo repo, sin clonar; si sale mal, se descarta sin tocar lo bueno.</div>
    </div>

    <div class="nota">Demo: dos worktrees del mismo repo, un agente trabajando en cada uno.</div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué separar los roles?

    <div class="idea">Quien decide, quien escribe y quien revisa no son el mismo.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "orquestacion.svg", width="100%"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Anatomía de los roles

    <div class="anatomia">
      <code>orquestador</code><span>Divide, asigna e integra. Si implementa, pierde la vista de conjunto.</span>
      <code>worker</code><span>Una tarea en su worktree. Si sale de sus archivos, choca con otro.</span>
      <code>reviewer</code><span>Busca defectos sin editar. Si corrige, deja de ser independiente; mejor otro modelo.</span>
      <code>tú</code><span>Fijas el objetivo y aceptas el resultado: el orquestador no reemplaza al dueño.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un brief y no un "hazlo"?

    <div class="idea">El worker empieza de cero: solo sabe lo que dice el brief.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>No vio la conversación</b>
        Lo que el orquestador sabe no le llega si no se escribe.</div>
      <div class="tarjeta"><b>Archivos propios</b>
        Decir qué puede tocar evita que dos workers editen lo mismo.</div>
      <div class="tarjeta"><b>Criterio de entrega</b>
        Con <code>VERIFY PASS</code> como meta, sabe cuándo terminó.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué integrar solo lo que da PASS?

    <div class="idea">El orquestador no relee todo: confía en la evidencia.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>La revisión escala</b>
        Con cinco workers, leerlo todo a mano es imposible.</div>
      <div class="tarjeta"><b>El mismo listón</b>
        Da igual qué herramienta hizo el trabajo: entrega igual.</div>
      <div class="tarjeta"><b>Un fallo no contamina</b>
        Lo que no pasa se queda en su rama, lejos de lo integrado.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué mezclar herramientas?

    <div class="idea">Cada agente es un proceso: da igual cuál, si sigue las mismas reglas.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Mismas reglas</b>
        Codex, opencode, Claude Code y pi leen el mismo <code>AGENTS.md</code>.</div>
      <div class="tarjeta"><b>Todos a la vista</b>
        Herdr muestra quién trabaja, quién espera y quién terminó.</div>
      <div class="tarjeta"><b>Otro proveedor revisa</b>
        Un reviewer pi con otro modelo no comparte los puntos ciegos.</div>
    </div>

    <div class="nota">Demo: en ia-postuler, orquestador en Codex, dos workers en sus worktrees y un reviewer pi.</div>
    """)
    return


if __name__ == "__main__":
    app.run()
