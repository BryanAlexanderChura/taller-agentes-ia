import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Sesión 1: Fundamentos

    Cómo "piensa" un agente, y por qué eso dicta cómo trabajamos con él.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Modelos: dónde compararlos

    - [OpenRouter](https://openrouter.ai): una API para muchos modelos; precios y ranking de uso.
    - [Artificial Analysis](https://artificialanalysis.ai): benchmarks de calidad, velocidad y precio.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 1. Tokens

    - El modelo no lee palabras: lee tokens.
    - Todo se mide y se cobra en tokens: entrada, salida, contexto.

    *Demo: tokenizador en vivo.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 2. Embeddings

    - Cada token es un vector; significado parecido, vectores cercanos.

    *Demo: mapa 2D de palabras.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 3. Atención

    - Cada token "mira" a todos los demás para decidir qué importa.
    - La atención es finita: más contexto, menos foco por pieza.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4. Degradación del contexto

    - *Context rot*: el rendimiento baja al crecer el contexto.
    - *Lost in the middle*: lo del centro se atiende peor.
    - *Context poisoning*: un error queda en el contexto y se reutiliza.

    **Regla:** contexto corto y limpio; `/clear` entre tareas.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 5. El harness es un bucle

    - Cada turno reenvía todo: system + tools + historial + nuevo mensaje.
    - El modelo responde o pide una tool; el resultado se agrega y se repite.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 6. Cache

    - Se reutiliza el prefijo idéntico: system, luego tools, luego mensajes.
    - El bucle solo agrega al final, por eso cachea bien.
    - Cambiar el inicio invalida todo lo que sigue.

    **Regla:** no tocar instrucciones ni tools a mitad de sesión.

    *Demo: calculadora de tokens por turno, con y sin cache.*
    """)
    return


if __name__ == "__main__":
    app.run()
