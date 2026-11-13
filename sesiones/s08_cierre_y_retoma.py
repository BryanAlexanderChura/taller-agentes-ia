import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 8: Cerrar y retomar

    Cerrar bien una sesión es lo que permite retomarla.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. `/yaml-resume`

    - Al cerrar: sincroniza `RESUME.yaml` con lo hecho.
    - Foco actual, siguiente paso, pendientes y bloqueantes.
    - Guarda el resumen de sesión en Engram.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. `/retomar-proyecto`

    - Al abrir: lee RESUME, CHANGELOG, git y Engram.
    - Responde estado, siguiente acción y bloqueantes, sin tocar nada.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. El ciclo

    `/new-module` -> trabajo -> `/yaml-resume` -> chat nuevo -> `/retomar-proyecto`

    *Demo en ia-postuler: cerrar, abrir un chat nuevo y retomar.*
    """)
    return


if __name__ == "__main__":
    app.run()
