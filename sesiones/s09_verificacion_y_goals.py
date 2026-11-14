import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s09_verificacion_y_goals.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 9</span>
      <span class="titulo">Verificación y goals</span>
      <span class="bajada">Terminado lo decide una prueba, no el agente.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué el test va antes que el código?

    <div class="idea">El test dice qué es correcto antes de que el agente lo interprete.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>El objetivo no se mueve</b>
        Escrito después, el test se acomoda al código que ya existe.</div>
      <div class="tarjeta"><b>Sabe cuándo parar</b>
        Verde es la señal de terminado, no su impresión.</div>
      <div class="tarjeta"><b>Lo que funciona queda</b>
        La próxima sesión no rompe en silencio lo que ya andaba.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué verlo fallar primero?

    <div class="idea">Un test que nunca falló no demuestra nada.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "tdd.svg", width="100%"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un checker y no su palabra?

    <div class="idea">Quien hizo el trabajo no es quien debe juzgarlo.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Siempre el mismo criterio</b>
        Mide igual en cada sesión y con cada herramienta.</div>
      <div class="tarjeta"><b>No se deja convencer</b>
        Da igual lo seguro que suene el agente.</div>
      <div class="tarjeta"><b>Cuesta casi nada</b>
        Se corre cien veces sin gastar contexto ni atención.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué tres resultados y no dos?

    <div class="idea">Sin evidencia no hay PASS: que falten pruebas no es pasar.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>PASS</b>
        Docs, lint y tests existen y están en orden.</div>
      <div class="tarjeta error"><b>FAIL</b>
        Algo se rompió: hay que arreglarlo.</div>
      <div class="tarjeta aviso"><b>INCOMPLETE</b>
        Falta evidencia: no se sabe si funciona, y eso no cuenta como bien.</div>
    </div>

    <div class="nota">Demo: el módulo de ejemplo da PASS; uno recién creado, sin tests, da INCOMPLETE.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué un hook y no solo una regla?

    <div class="idea">Una regla escrita se puede olvidar; un hook no deja cerrar sin PASS.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>AGENTS.md pide</b>
        Con el contexto lleno, una instrucción leída al inicio pierde peso.</div>
      <div class="tarjeta ok"><b>El hook impone</b>
        Si al terminar el turno no hay PASS, el agente sigue trabajando.</div>
      <div class="tarjeta"><b>No depende de su memoria</b>
        Lo importante queda en el harness, no en que el modelo se acuerde.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué otra IA revisa el diff?

    <div class="idea">El autor no ve sus errores; otro modelo tiene otros puntos ciegos.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Hoy revisa bien</b>
        Encuentra defectos reales en un diff, no solo estilo.</div>
      <div class="tarjeta"><b>Otro proveedor</b>
        Un modelo distinto no comparte los sesgos del que escribió.</div>
      <div class="tarjeta"><b>Sin el contexto del autor</b>
        Lee el cambio como lo leerá el próximo, sin justificaciones.</div>
    </div>

    <div class="nota">Demo: <code>/revisar-con-pi</code> sobre el diff actual.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué tres capas de revisión?

    <div class="idea">Cada capa revisa lo que las otras no pueden.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Checker: lo mecánico</b>
        Docs, lint y tests: rápido, repetible y sin opinión.</div>
      <div class="tarjeta"><b>Otra IA: lo semántico</b>
        Lógica, casos borde y alcance: lo que un script no entiende.</div>
      <div class="tarjeta"><b>Tú: la decisión</b>
        Aceptar o pedir cambios sigue siendo responsabilidad del dueño.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué escribir un goal?

    <div class="idea">El trabajo largo necesita un objetivo que sobreviva a cada chat.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Vive en el repo</b>
        El marcador apunta al goal: cualquier sesión sabe hacia dónde va.</div>
      <div class="tarjeta"><b>Criterios antes del código</b>
        Se acuerda qué es terminado antes de que haya algo que defender.</div>
      <div class="tarjeta aviso"><b>Solo para lo largo</b>
        Para una tarea corta, un goal es burocracia.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## Anatomía de un goal"),
            mo.hstack(
                [
                    mo.md(r"""
    ```markdown
    # GOAL.md
    **Approved:** pending
    ## Objetivo
    ## Alcance    (entra / queda fuera)
    ## Criterios  C1, C2...
    ## Límites    L1, L2...

    # RUN.md
    **State:** open
    ### T01 <resultado>
      Status / Files / Test / Validation
    ## Decisiones
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>Approved</code><span>El dueño lo aprueba: el agente no se fija sus propias metas.</span>
      <code>Alcance</code><span>Lo que queda fuera también se escribe, o se cuela.</span>
      <code>Criterios</code><span>Observables y con umbral: el goal se cierra con pruebas, no por opinión.</span>
      <code>Límites</code><span>Lo que no debe tocar, dicho antes de que lo toque.</span>
      <code>Tareas</code><span>Pequeñas y con su test: cada una deja algo comprobado.</span>
      <code>Files</code><span>Dos tareas independientes no tocan lo mismo: se pueden repartir.</span>
      <code>Decisiones</code><span>Con su fuente: la próxima sesión no las vuelve a discutir.</span>
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
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué puede avanzar solo por horas?

    <div class="idea">Porque ningún paso empieza sin que el anterior esté comprobado.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "ejecucion.svg", width="100%"),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué cortarse no hace perder nada?

    <div class="idea">Cada tarea cerrada es un commit y el marcador dice cuál sigue.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Commit por tarea</b>
        Siempre hay un punto de retorno que pasó el checker.</div>
      <div class="tarjeta"><b>El marcador apunta</b>
        Al cerrar, el RESUME dice qué goal y qué tarea siguen.</div>
      <div class="tarjeta"><b>Se retoma verificando</b>
        Antes de seguir, el checker confirma que el estado es cierto.</div>
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
