import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 8: Cerrar y retomar

    Cerrar bien una sesión es lo que permite retomarla.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. `/yaml-resume`

    - Al cerrar: sincroniza `RESUME.yaml` y CHANGELOG con lo hecho.
    - RESUME es un marcador, no un diario: una frase por entrada.
    - Guarda el resumen de sesión en Engram.

    ```yaml
    current_focus: Etapa silver de ventas a medias.
    goal: docs/goals/goal-1      # solo con un goal activo
    updated: 2026-11-14
    head: 60a432c                # commit al cerrar
    next:
      - Validar montos negativos en b01_procesar.
    open:
      - "2026-11-10: confirmar la fuente de clientes"
    blockers: []
    ```
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Las reglas que lo mantienen honesto

    - Un pendiente resuelto sale de RESUME solo después de quedar en el CHANGELOG.
    - Un pendiente que sigue conserva su fecha: así se ve cuánto lleva abierto.
    - `head` marca el cierre: todo commit posterior es trabajo sin registrar.
    - Actualizar el marcador no prueba nada: el checker sí.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. `/retomar-proyecto`

    - Al abrir: lee RESUME, git desde `head`, la última entrada del CHANGELOG, el goal y Engram.
    - Responde estado, siguiente acción y bloqueantes, sin tocar nada.

    | Veredicto | Significa |
    |---|---|
    | COHERENTE | todas las fuentes cuentan la misma historia |
    | REQUIERE VERIFICACIÓN | hay trabajo después de `head` sin registrar |
    | CONTRADICCIÓN | dos fuentes afirman cosas incompatibles |

    Ante las dos últimas: `/yaml-resume` antes de seguir.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. El ciclo

    `/new-module` -> trabajo -> `/yaml-resume` -> chat nuevo -> `/retomar-proyecto`

    *Demo en ia-postuler: cerrar, abrir un chat nuevo y retomar.*
    """)
    return


if __name__ == "__main__":
    app.run()
