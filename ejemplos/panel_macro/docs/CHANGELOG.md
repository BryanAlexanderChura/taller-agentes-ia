# Changelog

## 0.1.0 - 2026-11-14

### Added

- Módulo creado: Tabla de shocks para el anexo del paper
- Etapas `a01_extraer` (panel sintético del EDA, semilla 42, con años sin dato y
  "Del norte"), `b01_procesar` (nombres armonizados, faltantes nulos, rangos validados) y
  `c01_reporte` (inflación y desempleo medios antes y después de 2009, 2020 y 2022).
- Tests de las tres etapas; `test_anio_faltante_no_cuenta_como_cero` cubre el error de
  contar un año sin dato como 0.
- Goal `docs/goals/goal-1` (GOAL.md y RUN.md).
