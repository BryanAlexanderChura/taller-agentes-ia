from ventas import limpiar, total_por_cliente

FILAS = [
    {"cliente": "ana", "monto": 100.5},
    {"cliente": "ana", "monto": 20},
    {"cliente": "luis", "monto": 50},
    {"cliente": "", "monto": 10},
    {"cliente": "luis", "monto": -5},
]


def test_limpiar_descarta_sin_cliente_y_monto_no_positivo():
    assert len(limpiar(FILAS)) == 3


def test_total_por_cliente_suma_solo_filas_limpias():
    assert total_por_cliente(FILAS) == {"ana": 120.5, "luis": 50}
