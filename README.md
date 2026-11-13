# Taller de agentes de IA

Claude Code, Codex, opencode y pi: del modelo mental al flujo de trabajo con harness.

## Preparación (Windows)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\windows\instalar.ps1
```

Verifica git, gh, lazygit, uv, node, claude, codex, opencode, pi, engram y herdr (preview en Windows);
instala solo lo que falta, conecta Engram a cada agente y deja el entorno Python listo (`uv sync`).

## Harness del taller

Al clonar el repo ya está configurado: `AGENTS.md` con las reglas y `.agents/` con skills y hook.

| Pieza | Qué hace |
|---|---|
| `verificar` | checker: 0 PASS, 1 FAIL, 2 INCOMPLETE |
| `tdd` | test primero, verlo fallar |
| `new-module` | crea un módulo con etapas a/b/c y docs |
| `yaml-resume` / `retomar-proyecto` | cerrar y retomar sesión |
| `revisar-con-pi` | revisión del diff con otro modelo |
| `.agents/hooks/` | bloquea comandos destructivos (Codex, Claude Code, opencode) |

Codex pide confiar en los hooks del proyecto la primera vez (`/hooks`).

## Sesiones

| # | Archivo | Tema |
|---|---------|------|
| 1 | `sesiones/s01_fundamentos.py` | Tokens, embeddings, atención, contexto, bucle del harness, cache |
| 2 | `sesiones/s02_entorno.py` | uv, git, GitHub, gh, por qué marimo |
| 3 | `sesiones/s03_limites_y_memoria.py` | Límites del LLM, memoria (Engram), instrucciones, verificación |
| 4 | `sesiones/s04_herramientas.py` | Las cuatro herramientas, archivo de instrucciones, controles |
| 5 | `sesiones/s05_extender_el_agente.py` | Skills, MCP, CLI y TUI, hooks, seguridad, subagentes |
| 6 | `sesiones/s06_herdr.py` | Herdr: varios agentes, sidebar de estados, CLI |
| 7 | `sesiones/s07_modulo_medallion.py` | Arquitectura medallion y `/new-module` |
| 8 | `sesiones/s08_cierre_y_retoma.py` | `/yaml-resume` y `/retomar-proyecto` |
| 9 | `sesiones/s09_verificacion_y_goals.py` | TDD, checker, goals y ejecución larga |
| 10 | `sesiones/s10_multiagente.py` | Worktrees, roles y orquestación |
| 11 | `sesiones/s11_como_continuar.py` | Carpeta `.agents`, próximos pasos, práctica, por qué un framework |

## Ejemplos

- `ejemplos/modulo_demo/`: módulo de juguete con docs y tests para la demo.

```powershell
uv run python .agents/skills/verificar/scripts/check.py ejemplos/modulo_demo
```

Abrir una sesión:

```powershell
uv run marimo edit sesiones\s01_fundamentos.py
```

En marimo, la vista de diapositivas se elige en el menú de layout (app view: slides).
