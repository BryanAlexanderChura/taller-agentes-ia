"""Captura cada diapositiva de una sesión para revisarla sin abrir el navegador.

Requiere la sesión servida en modo presentación:
    uv run marimo run sesiones/<sesion>.py --headless --port 2719 --no-token

Uso:
    uv run --with playwright python scripts/presentaciones/capturas.py <url> <salida> <n> [chromium]

- <n>: cuántas diapositivas capturar.
- [chromium]: ruta a un Chromium del sistema si Playwright no tiene el suyo
  (por ejemplo /usr/bin/chromium-browser).
Las capturas se toman con el título ya escrito (espera la animación).
"""

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

CARGA_MS = 7000
ESCRITURA_MS = 2600


def main(argv: list[str]) -> int:
    if len(argv) not in (4, 5):
        print(__doc__)
        return 2
    url, salida, n = argv[1], Path(argv[2]), int(argv[3])
    chromium = argv[4] if len(argv) == 5 else None
    salida.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        navegador = p.chromium.launch(executable_path=chromium)
        pagina = navegador.new_page(viewport={"width": 1600, "height": 900})
        pagina.goto(url)
        pagina.wait_for_timeout(CARGA_MS)
        pagina.mouse.click(800, 450)
        for i in range(n):
            if i:
                pagina.keyboard.press("ArrowRight")
            pagina.wait_for_timeout(ESCRITURA_MS)
            pagina.screenshot(path=str(salida / f"{i:02d}.png"))
        navegador.close()
    print(f"{n} capturas en {salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
