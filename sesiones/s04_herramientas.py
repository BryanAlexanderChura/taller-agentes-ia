import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 4: Herramientas

    Mismo bucle, distintas interfaces.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Las cuatro herramientas

    | Herramienta | Instrucciones | Nota |
    |---|---|---|
    | Codex | `AGENTS.md` | hooks, subagentes |
    | opencode | `AGENTS.md` | varios proveedores, plugins |
    | Claude Code | `CLAUDE.md` o `AGENTS.md` | skills, hooks, subagentes |
    | pi | `AGENTS.md` | mínimo, extensible |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. El archivo de instrucciones

    - Se carga en cada turno: es el prefijo que más pesa y más se cachea.
    - Corto y decisivo: reglas que el agente no deduciría solo.
    - Una regla, un lugar; lo largo va a una skill o a docs.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Controles comunes

    - Permisos: qué puede ejecutar sin preguntar.
    - Modo plan: proponer antes de editar.
    - Revisar el diff de cada cambio.
    """)
    return


if __name__ == "__main__":
    app.run()
