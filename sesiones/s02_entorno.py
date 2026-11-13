import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 2: Entorno

    Las herramientas que hacen seguro y reproducible el trabajo del agente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. uv

    - Un entorno reproducible: `pyproject.toml` + `uv.lock`.
    - `uv sync`, `uv add`, `uv run`: el agente no rompe el Python del sistema.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. git

    - Punto de retorno barato: deshacer lo que hizo el agente.
    - `status`, `diff`, `add`, `commit`, `restore`.
    - Revisar el diff antes de aceptar.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. gh (GitHub CLI)

    - `gh auth login`: una vez por máquina.
    - `gh repo clone`, `gh pr create`, `gh pr view`, `gh issue list`.
    - El agente lo usa para PRs e issues sin salir de la terminal.
    """)
    return


if __name__ == "__main__":
    app.run()
