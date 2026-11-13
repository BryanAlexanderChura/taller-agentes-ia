import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 6: Herdr

    Varios agentes a la vez, sin perder de vista ninguno.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. El problema

    - Un agente explora, otro implementa, otro corre tests.
    - Muchas terminales: ¿quién terminó?, ¿quién espera tu aprobación?
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Qué es

    - Multiplexor de terminal pensado para agentes: workspaces, tabs y panes.
    - Reconoce el agente que corre en cada pane.
    - Sesión persistente: cierras la terminal y al volver todo sigue ahí.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. El sidebar

    | Estado | Significa |
    |---|---|
    | `working` | trabajando, no interrumpir |
    | `blocked` | espera aprobación o respuesta |
    | `done` | terminó, revisar |
    | `idle` | listo para otra tarea |

    Un vistazo dice a quién atender primero.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. CLI: un agente coordina a otros

    - `herdr agent list`, `herdr pane split`, `herdr agent prompt ... --wait`.
    - Un agente abre panes, lanza otro agente y espera su resultado.
    - Base de la orquestación con varios agentes.

    *Demo: Claude en un pane, pi en otro, tests en un tercero.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Windows

    - Versión preview (beta): la instala `scripts\windows\instalar.ps1`.
    - Si falla, el resto del taller funciona igual con terminales separadas.
    """)
    return


if __name__ == "__main__":
    app.run()
