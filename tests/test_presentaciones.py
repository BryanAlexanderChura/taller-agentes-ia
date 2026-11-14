import importlib.util
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location("tema", RAIZ / "scripts/presentaciones/tema.py")
assert spec and spec.loader
tema = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tema)


def test_reemplazar_bloque_cambia_solo_lo_marcado():
    css = "a {}\n/* generado:lluvia:inicio */\nviejo\n/* generado:lluvia:fin */\nb {}\n"
    nuevo = tema.reemplazar_bloque(css, "lluvia", "nuevo")

    assert nuevo == ("a {}\n/* generado:lluvia:inicio */\nnuevo\n/* generado:lluvia:fin */\nb {}\n")
    assert tema.reemplazar_bloque(nuevo, "lluvia", "nuevo") == nuevo


def test_reemplazar_bloque_sin_marcas_falla():
    with pytest.raises(SystemExit):
        tema.reemplazar_bloque("a {}\n", "lluvia", "x")


def test_lluvia_es_determinista_y_trae_comandos():
    css = tema.lluvia_css()

    assert css == tema.lluvia_css()
    assert "@keyframes lluvia" in css
    assert "data:image/svg+xml," in css
    assert '"' not in css.split('url("', 1)[1].split('")', 1)[0]


def test_tema_tiene_los_bloques_generados_y_no_depende_de_internet():
    css = (RAIZ / "sesiones/tema.css").read_text(encoding="utf-8")

    for nombre in ("fuentes", "lluvia"):
        assert f"/* generado:{nombre}:inicio */" in css
        assert f"/* generado:{nombre}:fin */" in css
    assert "@import" not in css
    assert "fonts.googleapis.com" not in css
    assert "font/woff2;base64," in css
