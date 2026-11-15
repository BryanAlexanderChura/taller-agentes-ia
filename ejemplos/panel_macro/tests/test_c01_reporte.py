import polars as pl
import pytest
from scripts.a01_extraer import ensuciar, simular_panel
from scripts.b01_procesar import limpiar
from scripts.c01_reporte import inflacion_media, tabla_shocks

SHOCKS = [2009, 2020, 2022]
NOMBRES = {"Del norte": "Del Norte"}
RANGOS = {"inflacion": [-10, 50], "desempleo": [0, 40]}


def test_anio_faltante_no_cuenta_como_cero():
    df = pl.DataFrame(
        {
            "pais": ["Costaluna"] * 4,
            "anio": [2018, 2019, 2020, 2021],
            "inflacion": [4.0, 5.0, None, 3.6],
            "desempleo": [9.0, 9.2, 9.8, 9.5],
        }
    )
    # (4.0 + 5.0 + 3.6) / 3 = 4.2; si el faltante contara como 0, daría 3.15
    assert inflacion_media(df, "Costaluna") == pytest.approx(4.2)


def test_tabla_tiene_antes_y_despues_de_cada_shock():
    df = pl.DataFrame(
        {
            "pais": ["Andoria"] * 4,
            "anio": [2007, 2008, 2009, 2010],
            "inflacion": [3.0, 5.0, 1.0, 2.0],
            "desempleo": [5.0, 5.0, 7.0, 8.0],
        }
    )
    fila = tabla_shocks(df, shocks=[2009], ventana=2).row(0, named=True)
    assert fila == {
        "shock": 2009,
        "pais": "Andoria",
        "inflacion_antes": 4.0,
        "inflacion_despues": 1.5,
        "desempleo_antes": 5.0,
        "desempleo_despues": 7.5,
    }


def test_tabla_coincide_con_el_eda():
    # Mismos números que el EDA salvo las celdas donde falta un año
    eda = tabla_shocks(simular_panel(42), SHOCKS, ventana=3)
    limpio = limpiar(ensuciar(simular_panel(42)), NOMBRES, RANGOS)
    nuestra = tabla_shocks(limpio, SHOCKS, ventana=3)
    afectadas = pl.col("pais").is_in(["Costaluna", "Galicea"]) & (pl.col("shock") >= 2020)
    assert nuestra.filter(~afectadas).equals(eda.filter(~afectadas))
    assert nuestra.height == eda.height == 24
