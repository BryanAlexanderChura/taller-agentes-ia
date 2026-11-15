import polars as pl
import pytest
from scripts.b01_procesar import limpiar

NOMBRES = {"Del norte": "Del Norte"}
RANGOS = {"inflacion": [-10, 50], "desempleo": [0, 40]}


def crudo(inflacion: list) -> pl.DataFrame:
    return pl.DataFrame(
        {
            "pais": ["Del norte", "Del Norte", "Costaluna"],
            "anio": [2008, 2010, 2020],
            "inflacion": inflacion,
            "desempleo": [4.5, 4.8, 9.1],
        }
    )


def test_armoniza_nombres_de_pais():
    limpio = limpiar(crudo([2.0, 2.5, None]), NOMBRES, RANGOS)
    assert limpio["pais"].unique().sort().to_list() == ["Costaluna", "Del Norte"]


def test_anio_faltante_queda_nulo_no_cero():
    limpio = limpiar(crudo([2.0, 2.5, None]), NOMBRES, RANGOS)
    assert limpio["inflacion"].to_list() == [2.0, 2.5, None]


def test_valor_fuera_de_rango_falla():
    with pytest.raises(ValueError, match="inflacion"):
        limpiar(crudo([2.0, 250.0, None]), NOMBRES, RANGOS)
