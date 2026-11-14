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
    ## 1. La carpeta `.agents` de este repo

    ```text
    AGENTS.md              reglas del proyecto
    .agents/
      skills/              verificar, tdd, new-module, yaml-resume,
                           retomar-proyecto, revisar-con-pi,
                           grill-me, root-cause, write-goal,
                           presentar-porque
      plantillas/SKILL.md  punto de partida para una skill nueva
      hooks/              bloquear.py + bloqueados.txt (una sola lista)
      sync_claude.py       copia skills a .claude/skills
    .codex/hooks.json      hook para Codex
    .claude/               settings.json (hook) + copia de skills
    .opencode/plugins/     plugin con la misma lista
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Una fuente, varias herramientas

    | Herramienta | Reglas | Skills | Hook |
    |---|---|---|---|
    | Codex | `AGENTS.md` | `.agents/skills` (nativo) | `.codex/hooks.json` |
    | opencode | `AGENTS.md` | `.agents/skills` (nativo) | `.opencode/plugins/` |
    | Claude Code | `AGENTS.md` | `.claude/skills` (copia) | `.claude/settings.json` |
    | pi | `AGENTS.md` | se le pasa el prompt | no aplica |

    Se edita en `.agents`; sin symlinks, para que funcione en Windows.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Próximos pasos

    1. Copiar `AGENTS.md`, `.agents/`, `.codex/`, `.claude/` y `.opencode/` a un proyecto propio.
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


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Por qué un framework y no solo prompts

    - Un proyecto largo no cabe en un chat: vive en docs, tests y memoria.
    - El framework convierte cada sesión en un paso verificable y retomable.

    | Sin framework | Con framework |
    |---|---|
    | cada chat reexplica todo | `/retomar-proyecto` |
    | "ya está" sin pruebas | TDD y checker |
    | reglas olvidadas | hooks que las imponen |
    | estructura improvisada | `/new-module` |
    """)
    return


if __name__ == "__main__":
    app.run()
