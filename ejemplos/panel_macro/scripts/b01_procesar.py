"""Silver: limpiar y validar el panel crudo.

Un año sin dato queda nulo: nunca se rellena con 0.
"""

from pathlib import Path

import polars as pl
import yaml

RAIZ = Path(__file__).resolve().parents[1]


def armonizar_nombres(df: pl.DataFrame, nombres: dict) -> pl.DataFrame:
    """Lleva cada variante ("Del norte") a su nombre oficial ("Del Norte")."""
    return df.with_columns(pl.col("pais").replace(nombres))


def validar_rangos(df: pl.DataFrame, rangos: dict) -> pl.DataFrame:
    """Falla si un valor sale del rango plausible. Los nulos no se juzgan: faltan."""
    for columna, (minimo, maximo) in rangos.items():
        fuera = df.filter(~pl.col(columna).is_between(minimo, maximo))
        if fuera.height:
            raise ValueError(f"{columna} fuera de [{minimo}, {maximo}] en {fuera.height} filas")
    return df


def limpiar(df: pl.DataFrame, nombres: dict, rangos: dict) -> pl.DataFrame:
    return validar_rangos(armonizar_nombres(df, nombres), rangos)


def run() -> None:
    config = yaml.safe_load((RAIZ / "config" / "config.yaml").read_text(encoding="utf-8"))
    crudo = pl.read_csv(RAIZ / config["rutas"]["bronze"] / "panel_crudo.csv")  # vacío -> nulo
    destino = RAIZ / config["rutas"]["silver"] / "panel.parquet"
    destino.parent.mkdir(parents=True, exist_ok=True)
    limpiar(crudo, config["nombres"], config["rangos"]).write_parquet(destino)
    print(f"escrito: {destino}")


if __name__ == "__main__":
    run()
