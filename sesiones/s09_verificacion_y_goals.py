import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 9: Verificación y goals

    Que el agente demuestre su trabajo, y que pueda avanzar solo por horas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. TDD

    1. **RED**: escribir el test; llama a la función real; verlo fallar.
    2. **GREEN**: el código mínimo que lo hace pasar.
    3. **REFACTOR**: limpiar con los tests en verde.

    - El test fija el objetivo antes de que el agente interprete.
    - Ver el RED prueba que el test mide algo.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. El checker

    Un script que decide si el trabajo está listo, no el agente.

    | Salida | Estado | Significa |
    |---|---|---|
    | 0 | PASS | docs, lint y tests en orden |
    | 1 | FAIL | algo falla |
    | 2 | INCOMPLETE | falta evidencia: docs o tests |

    Sin evidencia no hay PASS.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Demo del checker

    ```text
    > uv run python .agents/skills/verificar/scripts/check.py ejemplos/modulo_demo
    VERIFY PASS

    > uv run python .agents/skills/new-module/scripts/new_module.py ventas "Ventas"
    > uv run python .agents/skills/verificar/scripts/check.py ventas
    INCOMPLETE tests: no hay tests
    VERIFY INCOMPLETE
    ```

    Skill `verificar`: 60 líneas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. El checker como regla

    - En `AGENTS.md`: "no declares terminado sin `VERIFY PASS`".
    - Mejor aún, en un hook al terminar el turno (`Stop`, `session.idle`):
      si no hay PASS, el agente sigue trabajando.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. Revisión con otra IA

    - Hoy la IA revisa bien: encuentra defectos reales en un diff.
    - El autor no ve sus propios errores; un modelo distinto tiene otros puntos ciegos.
    - Siempre un reviewer de otro proveedor: por ejemplo, un worker pi con otro modelo.

    | Capa | Revisa | Ejemplo |
    |---|---|---|
    | Checker | lo mecánico | docs, lint, tests |
    | Reviewer de otra IA | lo semántico | lógica, casos borde, alcance |
    | Tú | la decisión | aceptar o pedir cambios |
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Goal

    - `GOAL.md`: qué se quiere y criterios de aceptación verificables.
    - `RUN.md`: tareas ejecutables, cada una con su test.
    - El checker comprueba los criterios; el goal no se cierra por opinión.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 7. Ejecución larga

    ```text
    goal -> tarea -> test RED -> código GREEN -> checker -> commit -> siguiente tarea
    ```

    - El bucle corre solo mientras el checker diga PASS en cada paso.
    - Al cortarse la sesión: `/yaml-resume`, y luego se retoma donde quedó.
    """)
    return


if __name__ == "__main__":
    app.run()
