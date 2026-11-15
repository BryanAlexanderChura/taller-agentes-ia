# GOAL.md

**Approved:** 2026-11-14 (dueño)

## Objetivo

Tabla de shocks para el anexo del paper: inflación y desempleo medios por país, antes y
después de los shocks de 2009, 2020 y 2022, a partir del panel del EDA
(`sesiones/demos/eda_economia.py`), reproducible con un comando por etapa.

## Alcance

- Entra: `scripts/a01_extraer.py`, `scripts/b01_procesar.py`, `scripts/c01_reporte.py`,
  sus tests en `tests/` y `config/config.yaml`.
- Queda fuera: gráficos, inferencia o regresiones, datos reales del Banco Mundial y
  cambios al notebook del EDA.

## Criterios

- C1: la tabla tiene 24 filas (3 shocks x 8 países) y, donde no falta ningún año, sus
  números son idénticos a los calculados sobre el panel del EDA con semilla 42.
- C2: un año sin dato no se imputa como 0: con inflación 4.0, 5.0, sin dato y 3.6 la
  media es 4.2, no 3.15.
- C3: "Del norte" y "Del Norte" quedan como un solo país: 8 países tras limpiar.
- C4: un valor fuera de rango (inflación fuera de [-10, 50] o desempleo fuera de
  [0, 40]) detiene la limpieza con un error que nombra la columna.
- C5: `uv run python .agents/skills/verificar/scripts/check.py ejemplos/panel_macro`
  imprime `VERIFY PASS`.

## Límites

- L1: no rellenar faltantes con 0 ni con ningún otro valor.
- L2: no tocar `sesiones/demos/eda_economia.py`.
- L3: `data/` no entra a git; rutas, shocks, ventana y rangos viven en
  `config/config.yaml`, no en el código.
