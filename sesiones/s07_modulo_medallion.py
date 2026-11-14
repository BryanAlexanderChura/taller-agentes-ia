import marimo

app = marimo.App(
    width="medium",
    css_file="tema.css",
    layout_file="layouts/s07_modulo_medallion.slides.json",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    <div class="portada">
      <span class="numero">Sesión 7</span>
      <span class="titulo">Medallion y módulos</span>
      <span class="bajada">Si cada cosa tiene su lugar, nadie gasta tiempo buscándola.</span>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué una estructura predecible?

    <div class="idea">Si sabe dónde va cada cosa, el agente no gasta contexto buscándola.</div>

    <div class="tarjetas">
      <div class="tarjeta ok"><b>Menos exploración</b>
        No recorre todo el repo: lee solo lo que toca y el contexto queda corto.</div>
      <div class="tarjeta"><b>Uno enseña todos</b>
        Si todos los módulos se parecen, entender uno es entenderlos todos.</div>
      <div class="tarjeta"><b>Sirve a ambos</b>
        Lo que orienta al agente también te orienta a ti y a tu equipo.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md("## ¿Por qué separar el dato en capas?"),
            mo.image(mo.notebook_dir() / "img" / "medallion.svg", width="100%"),
            mo.md(
                '<div class="idea">Cada capa hace una sola cosa: '
                "si algo falla, se sabe dónde.</div>"
            ),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué tres capas y no un solo script?

    <div class="idea">Un script que hace todo se rehace entero ante cualquier cambio.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Bronze: el crudo</b>
        Tal como llega: siempre se puede reprocesar sin volver a pedirlo.</div>
      <div class="tarjeta"><b>Silver: lo validado</b>
        Los errores del dato se atrapan una vez, no en cada reporte.</div>
      <div class="tarjeta"><b>Gold: lo consumible</b>
        Quien lo usa no necesita saber cómo se limpió.</div>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué letras y números en los nombres?

    <div class="idea">El nombre dice la etapa y el orden sin abrir el archivo.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>La etapa a la vista</b>
        <code>a</code>, <code>b</code> y <code>c</code> son bronze, silver y gold.</div>
      <div class="tarjeta"><b>El orden es el de ejecución</b>
        Al listar la carpeta, los pasos aparecen en el orden en que corren.</div>
      <div class="tarjeta"><b>Crece sin renombrar</b>
        Un paso nuevo toma el siguiente número y nada se mueve.</div>
    </div>
    """)
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
      a01_extraer.py
      b01_procesar.py
      c01_reporte.py
      docs/
        RESUME.yaml
        CHANGELOG.md
    ```
    """),
                    mo.md(r"""
    <div class="anatomia">
      <code>a01_extraer</code><span>Lee sin transformar: el origen se puede repetir.</span>
      <code>b01_procesar</code><span>Limpia y valida en un solo lugar.</span>
      <code>c01_reporte</code><span>Entrega listo para usar, sin lógica escondida.</span>
      <code>RESUME.yaml</code><span>Dice dónde seguir: el chat siguiente no empieza de cero.</span>
      <code>CHANGELOG.md</code><span>Qué cambió y por qué, para quien llegue después.</span>
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
    mo.md(r"""
    ## ¿Por qué un comando para crear módulos?

    <div class="idea">Lo que se crea igual cada vez no se deja a la memoria de nadie.</div>

    <div class="tarjetas">
      <div class="tarjeta"><b>Siempre el mismo esqueleto</b>
        Ni tú ni el agente olvidan una carpeta o un documento.</div>
      <div class="tarjeta ok"><b>No pisa nada</b>
        Si la ruta ya existe, no la toca: crear nunca destruye.</div>
      <div class="tarjeta"><b>Nace con su estado</b>
        Desde el primer minuto tiene dónde anotar cómo va.</div>
    </div>

    <div class="nota">Demo: crear un módulo con <code>/new-module</code> y recorrer su árbol; luego un módulo real en ia-postuler.</div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## ¿Por qué el módulo nace sin tests?

    <div class="idea">Un módulo que nada verifica no está terminado, y el checker lo dice.</div>

    <div class="tarjetas">
      <div class="tarjeta aviso"><b>INCOMPLETE a propósito</b>
        El checker no deja pasar un módulo sin al menos un test.</div>
      <div class="tarjeta"><b>El test es el objetivo</b>
        Escribirlo primero obliga a decir qué debe cumplir.</div>
      <div class="tarjeta ok"><b>El agente sabe a qué apuntar</b>
        Con un test que pasar, "terminado" se demuestra.</div>
    </div>

    <div class="nota">Por eso: el módulo es el punto de partida del ciclo de cerrar y retomar.</div>
    """)
    return


if __name__ == "__main__":
    app.run()
