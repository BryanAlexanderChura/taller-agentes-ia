# Changelog

## 2026-11-14

- Clonados `config-linux` y `bot_bcrp` (cuenta BryanAlexanderChura) en `prueba/` con `gh repo clone`.
  - Verificado: ambos clones completos (listado de archivos).
  - Sin verificar: `prueba/` no está en `.gitignore`; aparece como untracked.
- Creados `docs/CHANGELOG.md` y `docs/RESUME.yaml`; el borrador `RESUME.md` se movió a `legacy/`.
  - Checker sobre `.`: VERIFY FAIL por lint y tests de `prueba/bot_bcrp` (código externo; faltan fastapi y requests).
- Creado `prueba/grafico/grafico.py` (19 líneas): seno y coseno con matplotlib, guarda `grafico.png`.
  - Verificado: corre con `uv run` y genera el PNG.
  - Checker sobre `.` al cierre: VERIFY FAIL (sigue fallando por tests de `prueba/bot_bcrp`, falta fastapi).
