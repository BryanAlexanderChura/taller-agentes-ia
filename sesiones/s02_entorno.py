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
    - Visual: el panel de git de VS Code, o `lazygit` en un pane junto al agente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. GitHub: conceptos

    | Concepto | Qué es |
    |---|---|
    | Repo | el proyecto con todo su historial |
    | Remoto | la copia en GitHub (`origin`) |
    | Commit | una foto del cambio, con mensaje |
    | Rama | una línea de trabajo aislada |
    | Pull request | propuesta para unir una rama, con revisión |
    | Issue | una tarea o bug registrado |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. gh (GitHub CLI)

    - `gh auth login`: una vez por máquina.
    - `gh repo clone`, `gh pr create`, `gh pr view`, `gh issue list`.
    - El agente lo usa para PRs e issues sin salir de la terminal.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Por qué marimo

    - El notebook es un `.py` normal: diffs limpios en git, el agente lo lee y edita.
    - Reactivo: al cambiar una celda se recalcula lo que depende de ella; sin estado oculto.
    - Un mismo archivo es notebook, script, app o presentación.
    - Corre con `uv run`: mismo entorno para todos.
    """)
    return


if __name__ == "__main__":
    app.run()
