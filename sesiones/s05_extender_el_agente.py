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

    Instrucciones piden; skills enseñan; CLI y MCP conectan; hooks obligan; subagentes aíslan.
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
    skills/verificar/
      SKILL.md
      scripts/check.py
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Cómo crece una skill

    - Versión 1: los pasos mínimos. Se usa en un caso real.
    - Cada fallo observado del agente se convierte en una regla, y se anota cuál fue.
    - Una regla que no evitó ningún fallo real sobra.

    | Regla de `retomar-proyecto` | Fallo que la motivó |
    |---|---|
    | Mirar `git log <head>..HEAD` | Tomó `next` como pendiente cuando ya estaba hecho. |
    | Veredicto COHERENTE / CONTRADICCIÓN | Mezcló fuentes que no coincidían sin avisar. |
    | Edad en días de cada pendiente | Un bloqueante de un mes parecía de ayer. |
    | Solo lectura | Empezó a programar dentro de la retoma. |

    Plantilla: `.agents/plantillas/SKILL.md`.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. MCP

    - Protocolo estándar para dar al agente tools y datos externos.
    - Un servidor MCP sirve a cualquier herramienta compatible.
    - Ejemplos: Engram (memoria), CodeGraph (índice del código), docs actuales, GitHub.
    - Cada tool ocupa contexto: pocos servidores, bien elegidos.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. CLI: el idioma nativo del agente

    - El agente vive en la terminal: una CLI es su forma más directa de actuar.
    - No ocupa contexto hasta que la usa; `--help` le enseña lo que necesita.
    - Salida en texto o JSON: la lee, la filtra y la encadena.
    - Ejemplos: `git`, `gh`, `uv`, `herdr`, `engram`.

    | Interfaz | Para quién | Ejemplo |
    |---|---|---|
    | CLI | el agente | `gh pr create`, `herdr agent list` |
    | TUI | la persona | `lazygit`, herdr |
    | MCP | el agente, cuando no hay CLI | Engram, docs |

    Las mejores herramientas traen ambas: TUI para ti, CLI para el agente.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Hooks: por qué

    - Las instrucciones son sugerencias: el modelo puede olvidarlas.
    - Un hook es código que corre siempre, fuera del modelo: determinista.
    - Lo crítico (seguridad, formato, verificación) va en hooks, no en prompts.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Hooks: eventos

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
    ## 7. Seguridad: bloquear lo destructivo

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
    ## 8. Subagentes

    - Otro agente con su propio contexto; devuelve solo un resumen.
    - Útil para explorar mucho o revisar con ojos frescos.
    - Costo: más tokens y pierde detalle en el traspaso. Lo pequeño, inline.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 9. El harness empaqueta todo esto

    - Instrucciones + skills + MCP + hooks + roles de subagentes, versionados en el repo.
    - Este repo trae uno en `.agents/`: al clonarlo ya está configurado.
    - Hook de seguridad listo para Codex, Claude Code y opencode, con una sola lista.
    """)
    return


if __name__ == "__main__":
    app.run()
