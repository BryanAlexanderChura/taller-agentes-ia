from pathlib import Path

SESIONES = Path(__file__).resolve().parent.parent / "sesiones"


def test_cada_sesion_carga_el_lapiz():
    archivos = sorted(SESIONES.glob("s[0-9][0-9]_*.py"))
    assert archivos
    sin_lapiz = [
        a.name
        for a in archivos
        if 'html_head_file="lapiz.html"' not in a.read_text(encoding="utf-8")
    ]
    assert sin_lapiz == []
    assert (SESIONES / "lapiz.html").is_file()
