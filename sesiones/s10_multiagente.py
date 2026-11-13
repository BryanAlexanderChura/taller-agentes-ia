import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 10: Orquestación multiagente

    Varios agentes en paralelo sin pisarse.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Por qué varios agentes

    - Tareas independientes avanzan a la vez.
    - Cada agente con contexto chico y enfocado.
    - Un revisor que no escribió el código ve lo que el autor no ve.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Worktrees

    - Una copia de trabajo extra del mismo repo, en su propia rama.
    - Cada agente escribe en su worktree: nadie pisa a nadie.

    ```text
    git worktree add ../repo-tarea-1 -b tarea-1
    git worktree list
    git worktree remove ../repo-tarea-1
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Roles

    | Rol | Hace | No hace |
    |---|---|---|
    | Orquestador | divide, asigna, integra, decide | implementar todo él mismo |
    | Worker | implementa una tarea en su worktree | salirse de sus archivos |
    | Reviewer | busca defectos; mejor otro modelo (pi con otro proveedor) | editar |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Reglas que lo hacen funcionar

    - Brief claro: objetivo, archivos propios, criterio de aceptación.
    - Cada worker entrega con `VERIFY PASS`; el orquestador integra solo eso.
    - Herdr muestra el estado de todos; Codex, opencode y pi pueden ser workers.

    *Demo: orquestador en Codex, dos workers en sus worktrees, un reviewer.*
    """)
    return


if __name__ == "__main__":
    app.run()
