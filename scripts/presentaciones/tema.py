"""Regenera los bloques generados de sesiones/tema.css.

- fuentes: Inter y JetBrains Mono embebidas en base64 (solo alfabeto latino), para
  presentar sin internet. Descarga una vez desde Google Fonts (licencia OFL).
- lluvia: fondo de caracteres que caen (SVG embebido) con números, katakana y
  comandos de Linux en vertical.

Uso: uv run python scripts/presentaciones/tema.py [fuentes|lluvia|todo]
"""

import base64
import random
import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import quote

RAIZ = Path(__file__).resolve().parents[2]
TEMA = RAIZ / "sesiones" / "tema.css"

FUENTES = {"Inter": (400, 600), "JetBrains Mono": (400, 700)}
# Google Fonts entrega woff2 solo a navegadores modernos.
AGENTE = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"

ANCHO, ALTO, PASO, FILA = 720, 960, 20, 22
CARACTERES = "0123456789012345アイウエオカキクケコサシスセソ<>/{}[]=+*#$%&@"
COMANDOS = [
    "sudo apt update", "ls -la", "git log", "grep -rn", "chmod +x", "uv run",
    "ssh", "cat .bashrc", "ps aux", "tail -f", "echo $PATH", "mkdir -p", "curl -sL",
    "sudo systemctl", "kill -9", "cd ~", "pwd", "top", "df -h", "whoami",
]  # fmt: skip


def reemplazar_bloque(css: str, nombre: str, contenido: str) -> str:
    inicio = f"/* generado:{nombre}:inicio */\n"
    fin = f"/* generado:{nombre}:fin */"
    if inicio not in css or fin not in css:
        raise SystemExit(f"faltan las marcas del bloque '{nombre}' en {TEMA.name}")
    antes, resto = css.split(inicio, 1)
    _, despues = resto.split(fin, 1)
    return f"{antes}{inicio}{contenido.strip()}\n{fin}{despues}"


def lluvia_css(semilla: int = 7) -> str:
    azar = random.Random(semilla)
    partes = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO}" height="{ALTO}" '
            'font-family="monospace" font-size="16">'
        )
    ]
    filas = ALTO // FILA
    for x in range(PASO // 2, ANCHO, PASO):
        if azar.random() < 0.1:
            continue
        comando = azar.choice(COMANDOS) if azar.random() < 0.3 else None
        largo = len(comando) if comando else azar.randint(6, 26)
        inicio = azar.randint(0, filas)
        for k in range(largo):
            c = comando[k] if comando else azar.choice(CARACTERES)
            if c == " ":
                continue
            y = ((inicio + k) % filas) * FILA + FILA
            opacidad = round(0.15 + 0.85 * (k + 1) / largo, 2)
            color = "#d9f99d" if k == largo - 1 else "#a3e635"
            c = c.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            partes.append(
                f'<text x="{x}" y="{y}" fill="{color}" fill-opacity="{opacidad}">{c}</text>'
            )
    partes.append("</svg>")
    uri = "data:image/svg+xml," + quote("".join(partes), safe=":/=,;' ")
    return f"""
/* Fondo: lluvia de caracteres, tenue y lenta */
.reveal::before {{
  content: "";
  position: absolute;
  inset: 0;
  background-image: url("{uri}");
  background-size: {ANCHO}px {ALTO}px;
  opacity: 0.45;
  animation: lluvia 90s linear infinite;
  pointer-events: none;
  z-index: 0;
}}

@keyframes lluvia {{
  from {{ background-position: 0 0; }}
  to {{ background-position: 0 {ALTO}px; }}
}}
"""


def descargar(url: str) -> bytes:
    pedido = urllib.request.Request(url, headers={"User-Agent": AGENTE})
    with urllib.request.urlopen(pedido, timeout=30) as respuesta:
        return respuesta.read()


def fuentes_css() -> str:
    bloques = []
    for familia, pesos in FUENTES.items():
        url = (
            "https://fonts.googleapis.com/css2?family="
            + familia.replace(" ", "+")
            + ":wght@"
            + ";".join(map(str, pesos))
            + "&display=swap"
        )
        hoja = descargar(url).decode("utf-8")
        for peso, fuente in re.findall(
            r"/\* latin \*/\s*@font-face \{[^}]*?font-weight: (\d+);[^}]*?src: url\(([^)]+)\)",
            hoja,
        ):
            datos = base64.b64encode(descargar(fuente)).decode("ascii")
            bloques.append(
                f'@font-face {{ font-family: "{familia}"; font-weight: {peso}; '
                f"font-style: normal; font-display: swap; "
                f'src: url("data:font/woff2;base64,{datos}") format("woff2"); }}'
            )
    if len(bloques) != sum(len(p) for p in FUENTES.values()):
        raise SystemExit(
            f"se esperaban {sum(map(len, FUENTES.values()))} fuentes, hay {len(bloques)}"
        )
    return "/* Inter y JetBrains Mono (OFL 1.1), alfabeto latino, embebidas */\n" + "\n".join(
        bloques
    )


def main(argv: list[str]) -> int:
    que = argv[1] if len(argv) > 1 else "todo"
    if que not in ("fuentes", "lluvia", "todo"):
        print(__doc__)
        return 2
    css = TEMA.read_text(encoding="utf-8")
    if que in ("lluvia", "todo"):
        css = reemplazar_bloque(css, "lluvia", lluvia_css())
    if que in ("fuentes", "todo"):
        css = reemplazar_bloque(css, "fuentes", fuentes_css())
    TEMA.write_text(css, encoding="utf-8")
    print(f"actualizado: {TEMA.relative_to(RAIZ)} ({que})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
