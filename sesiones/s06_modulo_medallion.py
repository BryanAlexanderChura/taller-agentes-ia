import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 6: Arquitectura medallion y módulos

    Una estructura predecible para que humanos y agentes se ubiquen.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Medallion

    | Capa | Contenido | Etapa del módulo |
    |---|---|---|
    | Bronze | dato crudo, tal como llega | `a` extraer |
    | Silver | limpio, validado | `b` procesar |
    | Gold | listo para consumo | `c` reporte |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. `/new-module`

    - `pipeline/a01_extraer.py`, `b01_procesar.py`, `c01_reporte.py`.
    - `schemas/`: contratos de entrada y salida.
    - `docs/`: README, arquitectura, CHANGELOG, `RESUME.yaml`.

    *Demo: crear un módulo y recorrer su árbol.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Por qué importa al agente

    - Sabe dónde va cada cosa sin explorar todo el repo: menos contexto.
    - Los contratos le dicen qué debe cumplir: verificable.
    """)
    return


if __name__ == "__main__":
    app.run()
