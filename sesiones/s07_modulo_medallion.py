import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 7: Arquitectura medallion y módulos

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

    ```text
    ventas/
      a01_extraer.py     bronze
      b01_procesar.py    silver
      c01_reporte.py     gold
      docs/RESUME.yaml   estado
      docs/CHANGELOG.md  historial
    ```

    Sin tests: el checker da INCOMPLETE hasta escribir el primero.

    *Demo: crear un módulo y recorrer su árbol; luego un módulo real en ia-postuler.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Por qué importa al agente

    - Sabe dónde va cada cosa sin explorar todo el repo: menos contexto.
    - Los tests le dicen qué debe cumplir: verificable.
    """)
    return


if __name__ == "__main__":
    app.run()
