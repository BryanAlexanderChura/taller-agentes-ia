"""Levanta todas las sesiones en un solo servidor y abre el índice del curso.

Uso: uv run python scripts/presentaciones/presentar.py [puerto]

Cada sesión queda en http://localhost:<puerto>/?file=<sesion>.py; el índice enlaza a todas.
Ctrl+C detiene el servidor.
"""

import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SESIONES = RAIZ / "sesiones"
INDICE = "indice.py"


def abrir_cuando_responda(url: str) -> None:
    for _ in range(60):
        try:
            urllib.request.urlopen(url, timeout=1)
        except OSError:
            time.sleep(0.5)
            continue
        webbrowser.open(url)
        return


def main(argv: list[str]) -> int:
    puerto = argv[1] if len(argv) > 1 else "2718"
    url = f"http://localhost:{puerto}/?file={INDICE}"
    print(f"índice del curso: {url}", flush=True)
    threading.Thread(target=abrir_cuando_responda, args=(url,), daemon=True).start()
    comando = [sys.executable, "-m", "marimo", "run", str(SESIONES), "--headless"]
    comando += ["--port", puerto, "--no-token"]
    try:
        return subprocess.call(comando)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
