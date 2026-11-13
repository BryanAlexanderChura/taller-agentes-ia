# Taller de agentes de IA

Claude Code, Codex, opencode y pi: del modelo mental al flujo de trabajo con harness.

## Preparación (Windows)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\windows\instalar.ps1
```

Verifica git, gh, uv, node, claude, codex, opencode, pi y engram; instala solo lo que falta y
deja el entorno Python listo (`uv sync`).

## Sesiones

| # | Archivo | Tema |
|---|---------|------|
| 1 | `sesiones/s01_fundamentos.py` | Tokens, embeddings, atención, contexto, bucle del harness, cache |
| 2 | `sesiones/s02_entorno.py` | uv, git, gh, por qué marimo |
| 3 | `sesiones/s03_limites_y_memoria.py` | Límites del LLM, memoria (Engram), instrucciones, verificación |
| 4 | `sesiones/s04_herramientas.py` | Las cuatro herramientas, archivo de instrucciones, controles |
| 5 | `sesiones/s05_extender_el_agente.py` | Skills, hooks, subagentes y el harness |
| 6 | `sesiones/s06_modulo_medallion.py` | Arquitectura medallion y `/new-module` |
| 7 | `sesiones/s07_cierre_y_retoma.py` | `/yaml-resume`, `/retomar-proyecto` y por qué un framework |

Abrir una sesión:

```powershell
uv run marimo edit sesiones\s01_fundamentos.py
```

En marimo, la vista de diapositivas se elige en el menú de layout (app view: slides).
