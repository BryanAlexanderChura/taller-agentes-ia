import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

RAIZ = Path(__file__).resolve().parent.parent


def cargar(ruta: str):
    spec = importlib.util.spec_from_file_location(Path(ruta).stem, RAIZ / ruta)
    assert spec and spec.loader
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


bloquear = cargar(".agents/hooks/bloquear.py")
new_module = cargar(".agents/skills/new-module/scripts/new_module.py")
check = cargar(".agents/skills/verificar/scripts/check.py")


@pytest.mark.parametrize(
    "tool_input",
    [
        {"command": "rm -rf build"},
        {"command": "git push --force origin main"},
        {"command": "git push -f"},
        {"command": "git reset --hard HEAD~1"},
        {"command": "git commit --no-verify -m x"},
        {"command": "cat .env"},
        {"file_path": "C:\\repo\\.env"},
        {"command": "psql -c 'drop table ventas'"},
        {"command": "Remove-Item carpeta -Recurse -Force"},
    ],
)
def test_bloquea_destructivos(tool_input):
    assert bloquear.motivo({"tool_input": tool_input}) is not None


@pytest.mark.parametrize(
    "tool_input",
    [
        {"command": "git push origin main"},
        {"command": "git status"},
        {"command": "uv run pytest -q"},
        {"file_path": "docs/.envrc.md"},
        {"command": "ls -la"},
    ],
)
def test_permite_legitimos(tool_input):
    assert bloquear.motivo({"tool_input": tool_input}) is None


@pytest.mark.parametrize(("comando", "salida"), [("rm -rf build", 2), ("git status", 0)])
def test_hook_por_stdin_sale_2_al_bloquear(comando, salida):
    evento = json.dumps({"tool_name": "Bash", "tool_input": {"command": comando}})
    r = subprocess.run(
        [sys.executable, str(RAIZ / ".agents/hooks/bloquear.py")],
        input=evento,
        capture_output=True,
        text=True,
        check=False,
    )
    assert r.returncode == salida


def test_new_module_crea_etapas_y_queda_incompleto_sin_tests(tmp_path, capsys):
    ruta = tmp_path / "ventas"
    new_module.crear(ruta, "Ventas por cliente")

    for archivo in (
        "a01_extraer.py",
        "b01_procesar.py",
        "c01_reporte.py",
        "docs/RESUME.yaml",
        "docs/CHANGELOG.md",
    ):
        assert (ruta / archivo).is_file()
    assert check.main(["check.py", str(ruta)]) == 2
    assert "tests: no hay tests" in capsys.readouterr().out


def test_new_module_no_sobrescribe(tmp_path):
    with pytest.raises(SystemExit):
        new_module.crear(tmp_path, "x")
