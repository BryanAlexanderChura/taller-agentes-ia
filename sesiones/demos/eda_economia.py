import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", css_file="demo.css", app_title="EDA economía (demo)")


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import numpy as np
    import polars as pl

    return alt, mo, np, pl


@app.cell
def _(mo):
    mo.md(r"""
    # EDA: inflación y desempleo ante shocks

    <span class="aviso-datos">datos ficticios</span>

    **Pregunta de investigación:** ¿cómo respondieron la inflación y el desempleo a la crisis
    de 2009, la pandemia de 2020 y el choque de oferta de 2022?

    Panel de 8 países inventados, 2000-2024. Mueve los filtros: cada tabla, gráfico y la
    conclusión final se recalculan solos, porque marimo sabe qué celdas dependen de cuáles.
    """)
    return


@app.cell
def _(alt):
    # Tema oscuro de los gráficos, con la paleta del taller
    PALETA = [
        "#a3e635",
        "#67e8f9",
        "#facc15",
        "#f87171",
        "#c084fc",
        "#fb923c",
        "#f472b6",
        "#94a3b8",
    ]

    MONO = "JetBrains Mono, ui-monospace, monospace"
    TEXTO = "Inter, system-ui, sans-serif"

    @alt.theme.register("terminal", enable=True)
    def _tema():
        ejes = {
            "domainColor": "#262626",
            "gridColor": "#1f1f1f",
            "tickColor": "#262626",
            "labelColor": "#a3a3a3",
            "titleColor": "#d4d4d4",
            "labelFont": MONO,
            "titleFont": TEXTO,
        }
        return {
            "config": {
                "background": "#121212",
                "font": TEXTO,
                "view": {"stroke": "#262626"},
                "axis": ejes,
                "legend": {
                    "labelColor": "#d4d4d4",
                    "titleColor": "#d4d4d4",
                    "labelFont": TEXTO,
                    "titleFont": TEXTO,
                },
                "title": {"color": "#fafafa", "font": MONO, "anchor": "start"},
                "range": {"category": PALETA},
            }
        }

    return


@app.cell
def _(np, pl):
    # nombre: (PIB per cápita 2000 en USD, crecimiento tendencial, desempleo natural, apertura)
    PAISES = {
        "Andoria": (18000, 0.022, 5.5, 0.45),
        "Borelia": (9000, 0.035, 7.5, 0.30),
        "Costaluna": (4500, 0.045, 9.0, 0.25),
        "Del Norte": (32000, 0.015, 4.5, 0.55),
        "Esmeralda": (6500, 0.040, 8.0, 0.40),
        "Ferrania": (14000, 0.025, 6.5, 0.35),
        "Galicea": (2500, 0.050, 11.0, 0.20),
        "Hesperia": (24000, 0.018, 5.0, 0.60),
    }
    # Shocks comunes por año: (efecto en crecimiento, efecto en inflación en puntos)
    SHOCKS = {
        2009: (-0.06, -2.0),
        2020: (-0.09, -1.0),
        2021: (0.04, 1.5),
        2022: (0.0, 5.0),
        2023: (0.0, 2.0),
    }
    META_INFLACION = 3.0

    def simular_panel(semilla=42):
        rng = np.random.default_rng(semilla)
        filas = []
        for pais, (pib, g, u_nat, apertura) in PAISES.items():
            u, infl = u_nat, 4.0 + rng.normal(0, 1)
            sensibilidad = 0.5 + apertura  # más abierto, más golpe del shock externo
            for anio in range(2000, 2025):
                shock_g, shock_pi = SHOCKS.get(anio, (0.0, 0.0))
                crec = g + sensibilidad * shock_g + rng.normal(0, 0.012)
                pib *= 1 + crec
                brecha = 100 * (crec - g)
                u = u + 0.3 * (u_nat - u) - 0.4 * brecha + rng.normal(0, 0.3)  # Okun
                infl = (  # Phillips con expectativas adaptativas
                    0.6 * infl
                    + 0.4 * META_INFLACION
                    - 0.35 * (u - u_nat)
                    + shock_pi
                    + rng.normal(0, 0.6)
                )
                tasa = max(0.25, 2 + infl + 0.5 * (infl - META_INFLACION) + 0.5 * brecha)  # Taylor
                export = 100 * apertura * (1 + 2 * sensibilidad * shock_g)
                export *= 1 + 0.005 * (anio - 2000)
                filas.append(
                    {
                        "pais": pais,
                        "anio": anio,
                        "pib_pc": pib,
                        "crec_pib": 100 * crec,
                        "inflacion": infl,
                        "desempleo": max(u, 1.0),
                        "tasa_interes": tasa,
                        "exportaciones": export + rng.normal(0, 1.5),
                    }
                )
        return pl.DataFrame(filas)

    datos = simular_panel()
    return PAISES, datos


@app.cell
def _(PAISES, mo):
    VARIABLES = {
        "Inflación (%)": "inflacion",
        "Desempleo (%)": "desempleo",
        "Crecimiento del PIB (%)": "crec_pib",
        "PIB per cápita (USD)": "pib_pc",
        "Tasa de interés (%)": "tasa_interes",
        "Exportaciones (% del PIB)": "exportaciones",
    }
    paises = mo.ui.multiselect(
        options=list(PAISES), value=["Andoria", "Costaluna", "Del Norte", "Galicea"], label="Países"
    )
    anios = mo.ui.range_slider(
        start=2000, stop=2024, step=1, value=[2000, 2024], label="Años", debounce=True
    )
    variable = mo.ui.dropdown(options=VARIABLES, value="Inflación (%)", label="Variable")
    mo.hstack([paises, anios, variable], justify="start", gap=2, wrap=True)
    return VARIABLES, anios, paises, variable


@app.cell
def _(anios, datos, mo, paises, pl):
    mo.stop(not paises.value, mo.md("**Elige al menos un país.**"))
    filtrado = datos.filter(
        pl.col("pais").is_in(paises.value) & pl.col("anio").is_between(*anios.value)
    )
    return (filtrado,)


@app.cell
def _(anios, filtrado, mo, pl, variable):
    _col = variable.value
    resumen = (
        filtrado.group_by("pais")
        .agg(
            media=pl.col(_col).mean(),
            desv=pl.col(_col).std(),
            minimo=pl.col(_col).min(),
            anio_min=pl.col("anio").get(pl.col(_col).arg_min()),
            maximo=pl.col(_col).max(),
            anio_max=pl.col("anio").get(pl.col(_col).arg_max()),
        )
        .sort("pais")
        .with_columns(pl.col("anio_min", "anio_max").cast(pl.String))  # años sin separador de miles
    )
    _fmt = {c: "{:,.2f}" for c in ["media", "desv", "minimo", "maximo"]}
    _desde, _hasta = anios.value
    mo.vstack(
        [
            mo.md(f"### Descriptivos por país: {variable.selected_key}, {_desde}-{_hasta}"),
            mo.ui.table(resumen, format_mapping=_fmt, selection=None, show_download=True),
        ]
    )
    return


@app.cell
def _(alt, anios, filtrado, pl, variable):
    _bandas = pl.DataFrame({"anio": [2009, 2020, 2022], "shock": ["crisis", "pandemia", "oferta"]})
    _bandas = _bandas.filter(pl.col("anio").is_between(*anios.value))
    _desde, _hasta = anios.value
    _paso = 1 if _hasta - _desde <= 12 else 2
    _x = alt.X(
        "anio:Q",
        title="Año",
        axis=alt.Axis(format="d", values=list(range(_desde, _hasta + 1, _paso))),
        scale=alt.Scale(domain=[_desde, _hasta]),
    )
    _lineas = (
        alt.Chart(filtrado)
        .mark_line(point=True, strokeWidth=2)
        .encode(
            x=_x,
            y=alt.Y(f"{variable.value}:Q", title=variable.selected_key),
            color=alt.Color("pais:N", title="País"),
            tooltip=["pais", "anio", alt.Tooltip(f"{variable.value}:Q", format=",.2f")],
        )
    )
    _shocks = (
        alt.Chart(_bandas)
        .mark_rule(color="#facc15", strokeDash=[4, 4], opacity=0.7)
        .encode(x=_x, tooltip=["shock", "anio"])
    )
    (_shocks + _lineas).properties(
        title=f"{variable.selected_key} en el tiempo (líneas amarillas: shocks)",
        width="container",
        height=320,
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Curva de Phillips

    Cada punto es un país-año. **Arrastra un rectángulo** sobre el gráfico: la tabla de abajo
    muestra solo los puntos seleccionados.
    """)
    return


@app.cell
def _(alt, filtrado, mo):
    _brocha = alt.selection_interval(name="brocha")
    phillips = mo.ui.altair_chart(
        alt.Chart(filtrado)
        .mark_circle(size=70, opacity=0.85)
        .encode(
            x=alt.X("desempleo:Q", title="Desempleo (%)", scale=alt.Scale(zero=False)),
            y=alt.Y("inflacion:Q", title="Inflación (%)"),
            color=alt.Color("pais:N", title="País"),
            tooltip=[
                "pais",
                "anio",
                alt.Tooltip("desempleo:Q", format=".2f"),
                alt.Tooltip("inflacion:Q", format=".2f"),
            ],
        )
        .add_params(_brocha)
        .properties(width="container", height=360)
    )
    phillips
    return (phillips,)


@app.cell
def _(mo, phillips, pl):
    _sel = phillips.value.with_columns(pl.col("anio").cast(pl.String))
    mo.vstack(
        [
            mo.md(f"**{len(_sel)} puntos seleccionados**"),
            mo.ui.table(
                _sel.select("pais", "anio", "desempleo", "inflacion", "tasa_interes"),
                format_mapping={c: "{:.2f}" for c in ["desempleo", "inflacion", "tasa_interes"]},
                selection=None,
                page_size=8,
            ),
        ]
    )
    return


@app.cell
def _(VARIABLES, alt, filtrado, pl):
    _cols = list(VARIABLES.values())
    _etiquetas = {v: k for k, v in VARIABLES.items()}
    correl = (
        filtrado.select(_cols)
        .corr()
        .with_columns(var1=pl.Series(_cols))
        .unpivot(index="var1", variable_name="var2", value_name="r")
        .with_columns(pl.col("var1", "var2").replace_strict(_etiquetas))
    )
    _orden = list(VARIABLES)
    _base = alt.Chart(correl).encode(
        x=alt.X("var2:N", sort=_orden, title=None, axis=alt.Axis(labelAngle=-30)),
        y=alt.Y("var1:N", sort=_orden, title=None),
    )
    _celdas = _base.mark_rect().encode(
        color=alt.Color(
            "r:Q",
            scale=alt.Scale(domain=[-1, 0, 1], range=["#f87171", "#121212", "#a3e635"]),
            title="r",
        ),
        tooltip=["var1", "var2", alt.Tooltip("r:Q", format=".2f")],
    )
    _texto = _base.mark_text(font="JetBrains Mono", fontSize=12).encode(
        text=alt.Text("r:Q", format=".2f"),
        # texto oscuro sobre celdas intensas, claro sobre las tenues
        color=alt.condition("abs(datum.r) > 0.6", alt.value("#0a0a0a"), alt.value("#fafafa")),
    )
    (_celdas + _texto).properties(
        title="Correlaciones (países y años filtrados)", width="container", height=340
    )
    return (correl,)


@app.cell
def _(anios, correl, filtrado, mo, pl):
    def _linea_2020():
        if not anios.value[0] <= 2020 <= anios.value[1]:
            return "2020 queda fuera del rango de años elegido."
        _peor = filtrado.filter(pl.col("anio") == 2020).sort("crec_pib").row(0, named=True)
        return (
            f"La mayor caída en 2020 fue de **{_peor['pais']}**: "
            f"el PIB creció {_peor['crec_pib']:.1f} % y el desempleo llegó a "
            f"{_peor['desempleo']:.1f} %."
        )

    _pico = filtrado.sort("inflacion", descending=True).row(0, named=True)
    _r = correl.filter(
        (pl.col("var1") == "Inflación (%)") & (pl.col("var2") == "Desempleo (%)")
    ).item(0, "r")
    _signo = "negativa (como predice Phillips)" if _r < 0 else "positiva (Phillips no se ve)"
    _puntos = mo.md(f"""
    - {_linea_2020()}
    - La inflación más alta fue **{_pico["inflacion"]:.1f} %** en **{_pico["pais"]}**
      ({_pico["anio"]}).
    - La correlación inflación-desempleo es **{_r:.2f}**: {_signo}.
    """)
    mo.vstack(
        [
            mo.md("### Conclusión preliminar"),
            mo.Html(f'<div class="conclusion">{_puntos.text}</div>'),
            mo.md(
                "<small>Datos ficticios. Esto es exploración, no inferencia: falta controlar"
                " por shocks y expectativas antes de afirmar nada.</small>"
            ),
        ]
    )
    return


if __name__ == "__main__":
    app.run()
