import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 11: Cómo continuar

    Una sola fuente de reglas para todas las herramientas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. La carpeta `.agents`

    ```text
    AGENTS.md            reglas del proyecto
    .agents/
      skills/            procedimientos (/new-module, /yaml-resume...)
      subagents/         roles: worker, reviewer, explorer...
      guards/            hooks que imponen las reglas
      references/        formatos de docs, goals y changelog
      project/           configuración propia del proyecto
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Una fuente, varias herramientas

    | Herramienta | Lee | Enlace a `.agents` |
    |---|---|---|
    | Codex | `AGENTS.md` | `.codex/agents`, `.codex/hooks.json` |
    | opencode, pi | `AGENTS.md` | según su configuración de skills |
    | Claude Code | `AGENTS.md` | `.claude/skills`, `.claude/agents` |

    Se edita en `.agents`; cada herramienta lo ve por su enlace.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Próximos pasos

    1. Instalar el harness en un proyecto propio.
    2. Crear un módulo con `/new-module` y llevarlo con TDD y el checker.
    3. Cerrar cada sesión con `/yaml-resume`; abrir con `/retomar-proyecto`.
    4. Cuando haya tareas independientes: worktrees y varios agentes.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Para practicar

    - Agregar una etapa bronze a `ejemplos/modulo_demo` que lea un CSV.
    - Empezar por el test (RED), terminar con `VERIFY PASS`.
    """)
    return


if __name__ == "__main__":
    app.run()
