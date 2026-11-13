import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 5: Extender el agente

    Instrucciones piden; skills enseñan; hooks obligan; subagentes aíslan.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Skills

    - Una carpeta con `SKILL.md`: nombre, descripción y procedimiento.
    - En contexto solo va la descripción; el cuerpo se carga al usarla.
    - Procedimientos largos sin pagar contexto en cada turno.

    ```text
    skills/retomar-proyecto/
      SKILL.md
      scripts/retomar.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Hooks: por qué

    - Las instrucciones son sugerencias: el modelo puede olvidarlas.
    - Un hook es código que corre siempre, fuera del modelo: determinista.
    - Lo crítico (seguridad, formato, verificación) va en hooks, no en prompts.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Hooks: eventos

    | Evento | Cuándo | Uso típico |
    |---|---|---|
    | `SessionStart` | al abrir sesión | inyectar memoria (Engram) |
    | `UserPromptSubmit` | al enviar un mensaje | agregar contexto |
    | `PreToolUse` | antes de una tool | **bloquear**: `.env`, `/tmp`, `--no-verify` |
    | `PostToolUse` | después de una tool | formatear, lint, tests |
    | `Stop` | al terminar el turno | exigir verificación |

    Nombres de Claude Code; otras herramientas tienen equivalentes (plugins, extensiones).
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Subagentes

    - Otro agente con su propio contexto; devuelve solo un resumen.
    - Útil para explorar mucho o revisar con ojos frescos.
    - Costo: más tokens y pierde detalle en el traspaso. Lo pequeño, inline.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. El harness empaqueta todo esto

    - Instrucciones + skills + hooks + roles de subagentes, versionados en el repo.
    - Se instala una vez y habilita `/new-module`, `/yaml-resume`, `/retomar-proyecto`.
    """)
    return


if __name__ == "__main__":
    app.run()
