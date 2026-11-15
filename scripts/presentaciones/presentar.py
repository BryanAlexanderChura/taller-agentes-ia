"""Levanta todas las sesiones en un solo servidor y abre el índice del curso.

Uso: uv run python scripts/presentaciones/presentar.py [puerto]

Cada sesión queda en http://localhost:<puerto>/?file=<sesion>.py; el índice enlaza a todas.
La demo EDA corre aparte en modo edición (http://localhost:2719), para mostrar el notebook
tal como se trabaja.
Si el puerto está ocupado (un servidor anterior), lo libera antes de lanzar.
Ctrl+C detiene el servidor.
"""

import os
import re
import signal
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
DEMO = SESIONES / "demos" / "eda_economia.py"
PUERTO_DEMO = 2719


def pids_en_puerto(puerto: int) -> set[int]:
    if sys.platform == "win32":
        salida = subprocess.run(
            ["netstat", "-ano", "-p", "tcp"], check=False, capture_output=True, text=True
        )
        patron = rf":{puerto}\s+\S+\s+LISTENING\s+(\d+)"
        return {int(pid) for pid in re.findall(patron, salida.stdout)}
    salida = subprocess.run(
        ["lsof", "-ti", f"tcp:{puerto}", "-sTCP:LISTEN"],
        check=False,
        capture_output=True,
        text=True,
    )
    return {int(pid) for pid in salida.stdout.split()}


def liberar_puerto(puerto: int) -> None:
    for pid in pids_en_puerto(puerto):
        print(f"puerto {puerto} ocupado por el proceso {pid}: se detiene", flush=True)
        if sys.platform == "win32":
            subprocess.run(
                ["taskkill", "/PID", str(pid), "/T", "/F"], check=False, capture_output=True
            )
        else:
            os.kill(pid, signal.SIGTERM)
    for _ in range(20):
        if not pids_en_puerto(puerto):
            return
        time.sleep(0.25)


def abrir_cuando_responda(url: str) -> None:
    for _ in range(60):
        try:
            urllib.request.urlopen(url, timeout=1)
        except OSError:
            time.sleep(0.5)
            continue
        webbrowser.open(url)
        return


def comandos(puerto: str) -> list[list[str]]:
    marimo = [sys.executable, "-m", "marimo"]
    sesiones = [*marimo, "run", str(SESIONES), "--headless", "--port", puerto, "--no-token"]
    demo = [*marimo, "edit", str(DEMO), "--headless", "--port", str(PUERTO_DEMO), "--no-token"]
    return [sesiones, demo]


def main(argv: list[str]) -> int:
    puerto = argv[1] if len(argv) > 1 else "2718"
    url = f"http://localhost:{puerto}/?file={INDICE}"
    liberar_puerto(int(puerto))
    liberar_puerto(PUERTO_DEMO)
    print(f"índice del curso: {url}", flush=True)
    print(f"demo EDA en modo edición: http://localhost:{PUERTO_DEMO}", flush=True)
    threading.Thread(target=abrir_cuando_responda, args=(url,), daemon=True).start()
    sesiones, demo = comandos(puerto)
    editor = subprocess.Popen(demo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        return subprocess.call(sesiones)
    except KeyboardInterrupt:
        return 0
    finally:
        editor.terminate()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
