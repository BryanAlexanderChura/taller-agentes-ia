"""Grafico de prueba: seno y coseno guardados en PNG."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

x = np.linspace(0, 2 * np.pi, 200)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, np.sin(x), label="seno")
ax.plot(x, np.cos(x), label="coseno")
ax.set_title("Grafico de prueba")
ax.legend()
salida = Path(__file__).with_name("grafico.png")
fig.savefig(salida, dpi=120)
print(f"Guardado en {salida}")
