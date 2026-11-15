import polars as pl
from scripts.a01_extraer import ensuciar, simular_panel


def test_crudo_trae_los_defectos_de_una_descarga():
    crudo = ensuciar(simular_panel(42))
    costaluna_2020 = crudo.filter((pl.col("pais") == "Costaluna") & (pl.col("anio") == 2020))
    assert costaluna_2020["inflacion"].to_list() == [None]
    assert "Del norte" in crudo["pais"].to_list()
    assert crudo.height == 8 * 25
