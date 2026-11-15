"""Bronze: el panel crudo, como si llegara del Banco Mundial.

Es sintético: la misma simulación y semilla que el EDA (sesiones/demos/eda_economia.py),
con los defectos típicos de una descarga real.
"""

from pathlib import Path

import numpy as np
import polars as pl
import yaml

RAIZ = Path(__file__).resolve().parents[1]

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

# Defectos de la descarga: años sin dato (país, año, columna)
FALTANTES = [("Costaluna", 2020, "inflacion"), ("Galicea", 2021, "desempleo")]


def simular_panel(semilla: int) -> pl.DataFrame:
    """Copia fiel de la simulación del EDA: mismos números con la misma semilla."""
    rng = np.random.default_rng(semilla)
    filas = []
    for pais, (pib, g, u_nat, apertura) in PAISES.items():
        u, infl = u_nat, 4.0 + rng.normal(0, 1)
        sensibilidad = 0.5 + apertura
        for anio in range(2000, 2025):
            shock_g, shock_pi = SHOCKS.get(anio, (0.0, 0.0))
            crec = g + sensibilidad * shock_g + rng.normal(0, 0.012)
            pib *= 1 + crec
            brecha = 100 * (crec - g)
            u = u + 0.3 * (u_nat - u) - 0.4 * brecha + rng.normal(0, 0.3)
            infl = (
                0.6 * infl
                + 0.4 * META_INFLACION
                - 0.35 * (u - u_nat)
                + shock_pi
                + rng.normal(0, 0.6)
            )
            tasa = max(0.25, 2 + infl + 0.5 * (infl - META_INFLACION) + 0.5 * brecha)
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


def ensuciar(df: pl.DataFrame) -> pl.DataFrame:
    """Lo que trae una descarga real: años sin dato y un nombre escrito distinto."""
    for pais, anio, columna in FALTANTES:
        es_celda = (pl.col("pais") == pais) & (pl.col("anio") == anio)
        df = df.with_columns(pl.when(es_celda).then(None).otherwise(pl.col(columna)).alias(columna))
    antiguo = (pl.col("pais") == "Del Norte") & (pl.col("anio") < 2010)
    return df.with_columns(
        pais=pl.when(antiguo).then(pl.lit("Del norte")).otherwise(pl.col("pais"))
    )


def run() -> None:
    config = yaml.safe_load((RAIZ / "config" / "config.yaml").read_text(encoding="utf-8"))
    destino = RAIZ / config["rutas"]["bronze"] / "panel_crudo.csv"
    destino.parent.mkdir(parents=True, exist_ok=True)
    ensuciar(simular_panel(config["semilla"])).write_csv(destino)  # un año sin dato queda vacío
    print(f"escrito: {destino}")


if __name__ == "__main__":
    run()
