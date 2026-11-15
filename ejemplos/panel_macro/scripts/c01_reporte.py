"""Gold: tabla de shocks para el anexo del paper.

Inflación y desempleo medios por país, antes y después de cada shock.
"""

from pathlib import Path

import polars as pl
import yaml

RAIZ = Path(__file__).resolve().parents[1]
COLUMNAS = ["inflacion", "desempleo"]


def promedios(df: pl.DataFrame) -> pl.DataFrame:
    """Media por país. Un año sin dato no cuenta: no es 0."""
    return df.group_by("pais").agg(pl.col(COLUMNAS).mean()).sort("pais")


def inflacion_media(df: pl.DataFrame, pais: str) -> float:
    return promedios(df.filter(pl.col("pais") == pais))["inflacion"].item()


def media_en(df: pl.DataFrame, desde: int, hasta: int, sufijo: str) -> pl.DataFrame:
    """Promedios entre dos años (inclusive), con sufijo en las columnas."""
    medias = promedios(df.filter(pl.col("anio").is_between(desde, hasta)))
    return medias.rename({c: f"{c}_{sufijo}" for c in COLUMNAS})


def tabla_shocks(df: pl.DataFrame, shocks: list, ventana: int) -> pl.DataFrame:
    """Antes: los `ventana` años previos. Después: el año del shock y los siguientes."""
    filas = []
    for shock in shocks:
        antes = media_en(df, shock - ventana, shock - 1, "antes")
        despues = media_en(df, shock, shock + ventana - 1, "despues")
        filas.append(antes.join(despues, on="pais").with_columns(shock=pl.lit(shock)))
    return pl.concat(filas).select(
        "shock", "pais", *[f"{c}_{s}" for c in COLUMNAS for s in ("antes", "despues")]
    )


def run() -> None:
    config = yaml.safe_load((RAIZ / "config" / "config.yaml").read_text(encoding="utf-8"))
    panel = pl.read_parquet(RAIZ / config["rutas"]["silver"] / "panel.parquet")
    destino = RAIZ / config["rutas"]["gold"] / "tabla_shocks.csv"
    destino.parent.mkdir(parents=True, exist_ok=True)
    tabla_shocks(panel, config["shocks"], config["ventana"]).write_csv(destino)
    print(f"escrito: {destino}")


if __name__ == "__main__":
    run()
