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

    Instrucciones piden; skills enseñan; MCP conecta; hooks obligan; subagentes aíslan.
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
    ## 2. MCP

    - Protocolo estándar para dar al agente tools y datos externos.
    - Un servidor MCP sirve a cualquier herramienta compatible.
    - Ejemplos: Engram (memoria), CodeGraph (índice del código), docs actuales, GitHub.
    - Cada tool ocupa contexto: pocos servidores, bien elegidos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Hooks: por qué

    - Las instrucciones son sugerencias: el modelo puede olvidarlas.
    - Un hook es código que corre siempre, fuera del modelo: determinista.
    - Lo crítico (seguridad, formato, verificación) va en hooks, no en prompts.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Hooks: eventos

    | Cuándo | Claude Code / Codex | opencode (plugin) | Uso típico |
    |---|---|---|---|
    | al abrir sesión | `SessionStart` | evento de sesión | inyectar memoria (Engram) |
    | antes de una tool | `PreToolUse` | `tool.execute.before` | **bloquear**: `.env`, `/tmp`, `--no-verify` |
    | después de una tool | `PostToolUse` | `tool.execute.after` | formatear, lint, tests |
    | al terminar el turno | `Stop` | `session.idle` | exigir verificación |

    Codex: `.codex/hooks.json`; revisar soporte en Windows. pi: extensiones.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Seguridad: bloquear lo destructivo

    - La seguridad no se pide en el prompt: se impone con un hook bloqueante.
    - Antes de cada comando (`PreToolUse`), el hook lo compara con una lista y lo rechaza.
    - El agente recibe el motivo y busca otro camino.

    | Bloquear | Por qué |
    |---|---|
    | `rm -rf`, borrar archivos | irreversible; mover a `legacy/` |
    | `git push --force`, `git reset --hard` | destruye historial |
    | leer o nombrar `.env` | secretos |
    | `--no-verify` | salta los controles |
    | `DROP`, `DELETE`, `UPDATE` en producción | datos reales |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Subagentes

    - Otro agente con su propio contexto; devuelve solo un resumen.
    - Útil para explorar mucho o revisar con ojos frescos.
    - Costo: más tokens y pierde detalle en el traspaso. Lo pequeño, inline.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 7. El harness empaqueta todo esto

    - Instrucciones + skills + MCP + hooks + roles de subagentes, versionados en el repo.
    - Se instala una vez y habilita `/new-module`, `/yaml-resume`, `/retomar-proyecto`.
    """)
    return


if __name__ == "__main__":
    app.run()
