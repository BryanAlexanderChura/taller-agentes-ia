import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    html_head_file="lapiz.html",
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
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué orquestar?

    <div class="idea">Cada agente carga solo su tarea; al orquestador solo le sube el resumen.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta ok"><b>Contexto limpio</b>
        El subagente explora mucho y devuelve poco.</div>
      <div class="tarjeta ok"><b>En paralelo</b>
        Dos tareas que no se tocan no esperan turno.</div>
      <div class="tarjeta aviso"><b>No siempre conviene</b>
        Tareas acopladas se pisan; lo pequeño, inline.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "orquestar.svg", width="92%"),
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
    ## ¿Por qué un worktree por agente?

    <div class="idea">Dos agentes en la misma carpeta se pisan: cada uno necesita su copia.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>Su propia rama</b>
        Cada cambio se revisa e integra por separado.</div>
      <div class="tarjeta"><b>Barato y desechable</b>
        Mismo repo, sin clonar; si sale mal, se descarta.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "worktrees.svg", width="92%"),
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
    ## ¿Por qué separar los roles?

    <div class="idea">Quien decide, quien escribe y quien revisa no son el mismo.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "roles.svg", width="80%"),
            mo.md(r"""
    <div class="nota">Demo: en ia-postuler, orquestador en Codex, dos workers en sus worktrees y un reviewer pi.</div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Cómo entra y sale el trabajo?

    <div class="idea">Entra un brief: el worker no vio la conversación. Sale solo lo que da PASS.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "brief_flujo.svg", width="84%"),
            mo.md(r"""
    <div class="nota">El orquestador no relee todo: confía en la evidencia.</div>
    """),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
