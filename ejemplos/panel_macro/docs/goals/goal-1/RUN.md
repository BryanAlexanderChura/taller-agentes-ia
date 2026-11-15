# RUN.md

**State:** done

## Tareas

### T01 Panel crudo en bronze

- Status: done
- Files: `scripts/a01_extraer.py`, `tests/test_a01_extraer.py`
- Test: `test_crudo_trae_los_defectos_de_una_descarga`
- Validation: `uv run pytest -q ejemplos/panel_macro/tests/test_a01_extraer.py` (base de C1:
  200 filas, con Costaluna 2020 sin inflación y "Del norte")

### T02 Panel limpio en silver

- Status: done
- Files: `scripts/b01_procesar.py`, `tests/test_b01_procesar.py`
- Test: `test_anio_faltante_queda_nulo_no_cero`
- Validation: `uv run pytest -q ejemplos/panel_macro/tests/test_b01_procesar.py` (C2, C3,
  C4)

### T03 Tabla de shocks en gold

- Status: done
- Files: `scripts/c01_reporte.py`, `tests/test_c01_reporte.py`
- Test: `test_anio_faltante_no_cuenta_como_cero`
- Validation: `uv run python .agents/skills/verificar/scripts/check.py ejemplos/panel_macro`
  imprime `VERIFY PASS` (C1, C2, C5)

## Decisiones

| ID | Decisión | Fuente |
|----|----------|--------|
| D1 | Antes = los 3 años previos al shock; después = el año del shock y los 2 siguientes. | Elegida al implementar; por confirmar con el dueño |
| D2 | Un año sin dato queda nulo y la media usa solo los años con dato. | Encargo del dueño, 2026-11-14 |
| D3 | El panel es sintético (semilla 42, misma simulación que el EDA); se trata como si viniera del Banco Mundial. | `sesiones/demos/eda_economia.py` |
