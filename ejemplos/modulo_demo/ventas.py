"""Módulo de juguete con etapas medallion: silver (limpiar) y gold (agregar)."""


def limpiar(filas: list[dict]) -> list[dict]:
    """Silver: descarta filas sin cliente o con monto no positivo."""
    return [f for f in filas if f.get("cliente") and f.get("monto", 0) > 0]


def total_por_cliente(filas: list[dict]) -> dict[str, float]:
    """Gold: suma de montos por cliente."""
    totales: dict[str, float] = {}
    for f in limpiar(filas):
        totales[f["cliente"]] = totales.get(f["cliente"], 0) + f["monto"]
    return totales
