import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 4: Herramientas y harness

    Mismo bucle, distintas interfaces; un harness común las une.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Las cuatro herramientas

    | Herramienta | Instrucciones | Nota |
    |---|---|---|
    | Claude Code | `CLAUDE.md` | skills, hooks, subagentes |
    | Codex | `AGENTS.md` | |
    | opencode | `AGENTS.md` | varios proveedores |
    | pi | `AGENTS.md` | mínimo, extensible |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Controles comunes

    - Permisos: qué puede ejecutar sin preguntar.
    - Modo plan: proponer antes de editar.
    - Revisar el diff de cada cambio.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Instalar el harness

    - Reglas, skills y guards compartidos entre herramientas.
    - Se instala en el repo y habilita `/new-module`, `/yaml-resume`, `/retomar-proyecto`.
    """)
    return


if __name__ == "__main__":
    app.run()
