"""Checker mínimo: decide si un módulo está listo.

Uso:    uv run python ejemplos/checker/check.py <modulo>
Salida: 0 PASS, 1 FAIL, 2 INCOMPLETE.

Regla clave: sin evidencia no hay PASS. Docs faltantes o tests ausentes
dan INCOMPLETE, nunca PASS.
"""

import subprocess
import sys
from pathlib import Path

DOCS_REQUERIDOS = ("docs/RESUME.yaml", "docs/CHANGELOG.md")
PYTEST_SIN_TESTS = 5


def correr(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", *args], check=False, capture_output=True, text=True
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("uso: check.py <modulo>")
        return 2
    modulo = Path(argv[1])

    fallas, incompletos = [], []

    for doc in DOCS_REQUERIDOS:
        if not (modulo / doc).is_file():
            incompletos.append(f"docs: falta {doc}")

    lint = correr("ruff", "check", str(modulo))
    if lint.returncode != 0:
        fallas.append("lint:\n" + lint.stdout)

    tests = correr("pytest", "-q", str(modulo))
    if tests.returncode == PYTEST_SIN_TESTS:
        incompletos.append("tests: no hay tests")
    elif tests.returncode != 0:
        fallas.append("tests:\n" + tests.stdout)

    for linea in fallas:
        print("FAIL", linea)
    for linea in incompletos:
        print("INCOMPLETE", linea)

    if fallas:
        print("VERIFY FAIL")
        return 1
    if incompletos:
        print("VERIFY INCOMPLETE")
        return 2
    print("VERIFY PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
