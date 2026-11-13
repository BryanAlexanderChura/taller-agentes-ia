import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 3: Límites del LLM y memoria

    Qué no puede hacer el modelo solo, y qué le damos para compensarlo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Corte de conocimiento

    - Entrenado hasta una fecha: no conoce versiones nuevas.
    - Solución: documentación actual en el contexto (docs, MCP, web), no memoria.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Cada chat empieza de cero

    - Sin memoria entre sesiones: lo decidido ayer se pierde.
    - Necesitamos memoria explícita y persistente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Engram

    - Memoria persistente vía MCP: guarda decisiones y hallazgos.
    - Se consulta al retomar; no reemplaza la documentación del proyecto.

    *Demo: guardar una decisión y recuperarla en un chat nuevo.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Instrucciones claras

    - Un modelo potente avanza rápido, también en la dirección equivocada.
    - Interpreta lo ambiguo sin avisar: alcance, criterio de éxito y límites explícitos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Verificar su trabajo

    - "Terminado" se demuestra: tests, diff, ejecución real.
    - Reglas escritas (`AGENTS.md`) para que verifique antes de afirmar.
    """)
    return


if __name__ == "__main__":
    app.run()
