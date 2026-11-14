import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s11_como_continuar.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 11</span>
      <span class="titulo">Cómo continuar</span>
      <span class="bajada">El método vive en el proyecto, no en el chat ni en la herramienta.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué el curso siguió este orden?

    <div class="idea">Cada sesión resolvió un problema que la anterior dejó a la vista.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "arco.svg", width="100%"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un framework y no solo prompts?

    <div class="idea">Un proyecto largo no cabe en un chat: vive en docs, tests y memoria.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Retomar sin reexplicar</b>
        El estado está en el repo, no en la cabeza de nadie.</div>
      <div class="tarjeta"><b>Terminado con pruebas</b>
        TDD y checker en lugar de "ya está".</div>
      <div class="tarjeta"><b>Reglas que se cumplen</b>
        Un prompt pide; un hook impone.</div>
      <div class="tarjeta"><b>Estructura repetible</b>
        Cada módulo nace igual: cualquier agente lo entiende.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué una sola fuente de reglas?

    <div class="idea">Si cada herramienta tiene sus reglas, tarde o temprano se contradicen.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Se edita en un lugar</b>
        <code>.agents</code> es la verdad; lo demás son copias o adaptadores.</div>
      <div class="tarjeta"><b>Cambiar de herramienta es barato</b>
        Codex, opencode, Claude Code y pi trabajan con las mismas reglas.</div>
      <div class="tarjeta"><b>Sin symlinks</b>
        Copias simples: funciona igual en Windows.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía de <code>.agents</code>"),
            mo.hstack(
                [
                    mo.md(r"""
    ```text
    AGENTS.md
    .agents/
      skills/
        verificar  tdd  new-module
        cerrar-sesion  retomar-sesion
        revisar-con-pi  grill-me
        root-cause  write-goal
        presentar-porque
      plantillas/SKILL.md
      hooks/
      sync_claude.py
    .codex/  .claude/  .opencode/
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>AGENTS.md</code><span>Las reglas del proyecto, en el único archivo que todas leen.</span>
      <code>skills/</code><span>El cómo se escribe una vez y cualquier agente lo repite igual.</span>
      <code>plantillas/</code><span>Una skill nueva nace con la forma de las demás.</span>
      <code>hooks/</code><span>Una sola lista de bloqueos: lo prohibido no depende de la herramienta.</span>
      <code>sync_claude.py</code><span>Claude Code lee otra carpeta: se le copia, no se mantiene a mano.</span>
      <code>.&lt;herramienta&gt;/</code><span>Adaptadores finos: enganchan el mismo hook en cada herramienta.</span>
    </div>
    """),
                ],
                widths=[1, 1],
                gap=2.5,
                align="center",
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué llevarlo a tu propio proyecto?

    <div class="idea">Lo que no se usa en un proyecto real se olvida en una semana.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Empieza chico</b>
        Un módulo con TDD y checker enseña más que repasar el curso.</div>
      <div class="tarjeta"><b>El hábito es cerrar y abrir</b>
        Es lo que convierte cada sesión en un paso retomable.</div>
      <div class="tarjeta"><b>Paralelo cuando haya con qué</b>
        Worktrees y varios agentes solo con tareas independientes.</div>
    </div>

    <div class="nota">Por eso: copia <code>AGENTS.md</code> y <code>.agents/</code> a un proyecto tuyo y crea un módulo.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un ejercicio tan pequeño?

    <div class="idea">Recorre el ciclo completo en algo que cabe en una sesión.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Empieza en RED</b>
        El test define qué debe leer antes de escribir una línea.</div>
      <div class="tarjeta"><b>Termina en PASS</b>
        No se da por hecho hasta que el checker lo diga.</div>
      <div class="tarjeta"><b>Sin distracciones</b>
        Un CSV y una etapa: toda la atención va al método.</div>
    </div>

    <div class="nota">Ejercicio: agregar a <code>ejemplos/modulo_demo</code> una etapa bronze que lea un CSV.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué esto no caduca?

    <div class="idea">Los modelos cambian cada mes; sus límites y el método, no.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Las herramientas rotan</b>
        Hoy son cuatro; mañana habrá otras que leen las mismas reglas.</div>
      <div class="tarjeta"><b>Los límites siguen</b>
        Contexto finito, sin memoria, sin juicio propio sobre su trabajo.</div>
      <div class="tarjeta"><b>El proyecto es tuyo</b>
        Reglas, tests y estado viven en tu repo, no en un proveedor.</div>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
