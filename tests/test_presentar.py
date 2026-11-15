import importlib.util
import socket
import subprocess
import sys
import time
from pathlib import Path

RUTA = Path(__file__).resolve().parents[1] / "scripts/presentaciones/presentar.py"
spec = importlib.util.spec_from_file_location("presentar", RUTA)
presentar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(presentar)


def puerto_libre() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def test_liberar_puerto_detiene_al_proceso_que_lo_ocupa():
    puerto = puerto_libre()
    ocupante = subprocess.Popen(
        [
            sys.executable,
            "-c",
            (
                f"import socket,time; s=socket.socket(); s.bind(('127.0.0.1',{puerto})); "
                "s.listen(); time.sleep(60)"
            ),
        ]
    )
    try:
        for _ in range(50):
            with socket.socket() as s:
                if s.connect_ex(("127.0.0.1", puerto)) == 0:
                    break
            time.sleep(0.1)

        presentar.liberar_puerto(puerto)

        assert ocupante.wait(timeout=5) is not None
    finally:
        ocupante.kill()


def test_liberar_puerto_libre_no_falla():
    presentar.liberar_puerto(puerto_libre())


def test_comandos_lanza_sesiones_en_run_y_demo_en_edit():
    sesiones, demo = presentar.comandos("2718")

    assert sesiones[3:5] == ["run", str(presentar.SESIONES)]
    assert "2718" in sesiones
    assert demo[3:5] == ["edit", str(presentar.DEMO)]
    assert str(presentar.PUERTO_DEMO) in demo
    assert presentar.DEMO.is_file()
