import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s06_modulo_medallion.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 6</span>
      <span class="titulo">Medallion y módulos</span>
      <span class="bajada">Si cada cosa tiene su lugar, nadie gasta tiempo buscándola.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué una estructura predecible?

    <div class="idea">Si sabe dónde va cada cosa, el agente no gasta contexto buscándola.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta ok"><b>Menos exploración</b>
        Lee solo lo que toca y el contexto queda corto.</div>
      <div class="tarjeta"><b>Uno enseña todos</b>
        Si los módulos se parecen, entender uno es entenderlos todos.</div>
      <div class="tarjeta"><b>Sirve a ambos</b>
        Lo que orienta al agente también te orienta a ti.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "predecible.svg", width="92%"),
                ],
                widths=[1, 1.1],
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
    ## ¿Por qué separar el dato en capas?

    <div class="idea">Un script que hace todo se rehace entero ante cualquier cambio.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "medallion.svg", width="74%"),
            mo.md(r"""
    <div class="tarjetas">
      <div class="tarjeta"><b>Bronze: el crudo</b>
        Tal como llega: se reprocesa sin volver a pedirlo.</div>
      <div class="tarjeta"><b>Silver: lo validado</b>
        Los errores del dato se atrapan una vez.</div>
      <div class="tarjeta ok"><b>Gold: lo consumible</b>
        Quien lo usa no necesita saber cómo se limpió.</div>
    </div>
    """),
        ]
    )
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    ## ¿Por qué letras y números en los nombres?

    <div class="idea">El nombre dice la etapa y el orden sin abrir el archivo.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>La etapa a la vista</b>
        <code>a</code>, <code>b</code> y <code>c</code> son bronze, silver y gold.</div>
      <div class="tarjeta"><b>El orden es el de ejecución</b>
        Al listar la carpeta, los pasos salen en el orden en que corren.</div>
      <div class="tarjeta ok"><b>Crece sin renombrar</b>
        Un paso nuevo toma el siguiente número y nada se mueve.</div>
    </div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "nombres.svg", width="92%"),
                ],
                widths=[1, 1.1],
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
            mo.md("## Anatomía de un módulo"),
            mo.hstack(
                [
                    mo.md(r"""
    ```text
    ventas/
      .gitignore
      data/
      scripts/
        a01_extraer.py
        b01_procesar.py
        c01_reporte.py
      tests/
        test_b01_procesar.py
      docs/
        RESUME.yaml
        CHANGELOG.md
      config/
        config.yaml
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>data/</code><span>Los datos no van a git: pesan, cambian y pueden ser sensibles.</span>
      <code>scripts/</code><span>Las etapas en orden: a, b y c son bronze, silver y gold.</span>
      <code>tests/</code><span>Un test por etapa, con su mismo nombre.</span>
      <code>docs/</code><span>RESUME dice dónde seguir; CHANGELOG, qué cambió y por qué.</span>
      <code>config/</code><span>Reglas y rutas fuera del código: cambiarlas no toca un script.</span>
      <code>.gitignore</code><span>Deja fuera data/ desde el primer commit, no cuando ya es tarde.</span>
    </div>
    """),
                ],
                widths=[1, 1.4],
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
    ## ¿Por qué un comando para crear módulos?

    <div class="idea">Lo que se crea igual cada vez no se deja a la memoria de nadie.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>Siempre el mismo esqueleto</b>
        Ni tú ni el agente olvidan una carpeta o un documento.</div>
      <div class="tarjeta ok"><b>No pisa nada</b>
        Si la ruta ya existe, no la toca: crear nunca destruye.</div>
      <div class="tarjeta aviso"><b>Nace INCOMPLETE</b>
        <code>tests/</code> vacía: el checker pide el primer test.</div>
    </div>

    <div class="nota">Demo: crear un módulo con <code>/new-module</code> y recorrer su árbol.</div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "scaffold.svg", width="92%"),
                ],
                widths=[1, 1.1],
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
    ## ¿Dónde va el test?

    <div class="idea">Cada etapa tiene su prueba al lado, con el mismo nombre.</div>
    """),
            mo.hstack(
                [
                    mo.md(r"""
    <div class="tarjetas columna">
      <div class="tarjeta"><b>En tests/, no mezclado</b>
        El código de producción y sus pruebas no se confunden.</div>
      <div class="tarjeta"><b>Un nombre, una pareja</b>
        <code>b01_procesar</code> se prueba en <code>test_b01_procesar</code>.</div>
      <div class="tarjeta ok"><b>El test va primero</b>
        Dice qué debe cumplir la etapa antes de escribirla.</div>
    </div>

    <div class="nota">El ciclo completo de TDD, en la sesión 8.</div>
    """),
                    mo.image(mo.notebook_dir() / "img" / "test_lugar.svg", width="92%"),
                ],
                widths=[1, 1.1],
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
    ## ¿Por qué esta estructura y no otra?

    <div class="idea">Es una sugerencia: la estructura depende de lo que vas a construir.</div>
    """),
            mo.image(mo.notebook_dir() / "img" / "estructuras.svg", width="62%"),
            mo.md(r"""
    <div class="tarjetas">
      <div class="tarjeta"><b>Hay estándares</b>
        Cada tipo de proyecto tiene una forma conocida de ordenarse.</div>
      <div class="tarjeta"><b>Se elige por el trabajo</b>
        Un pipeline, una librería y un análisis no se ordenan igual.</div>
      <div class="tarjeta ok"><b>Lo que importa</b>
        Que sea predecible y esté escrita, para ti y para el agente.</div>
    </div>
    """),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
