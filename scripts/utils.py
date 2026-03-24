"""
utils.py — Funciones reutilizables para Labo 6.

Importar en un notebook con:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.getcwd()), 'scripts'))
    from utils import ajuste_lineal, formato_resultado
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ──────────────────────────────────────────────────────────────
# Ajustes
# ──────────────────────────────────────────────────────────────

def ajuste_lineal(x, y, dy=None):
    """
    Ajuste lineal y = a*x + b usando scipy.stats.linregress o
    mínimos cuadrados ponderados si se proveen incertezas dy.

    Parámetros
    ----------
    x, y : array-like
        Datos experimentales.
    dy : array-like, opcional
        Incertezas en y para ajuste ponderado.

    Retorna
    -------
    dict con claves: pendiente, ordenada, err_pendiente, err_ordenada, r2
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if dy is None:
        resultado = stats.linregress(x, y)
        return {
            "pendiente":    resultado.slope,
            "ordenada":     resultado.intercept,
            "err_pendiente": resultado.stderr,
            "err_ordenada":  resultado.intercept_stderr,
            "r2":           resultado.rvalue ** 2,
        }
    else:
        w = 1.0 / np.asarray(dy, dtype=float) ** 2
        Sw  = w.sum()
        Sx  = (w * x).sum()
        Sy  = (w * y).sum()
        Sxx = (w * x * x).sum()
        Sxy = (w * x * y).sum()
        delta = Sw * Sxx - Sx ** 2
        a = (Sw * Sxy - Sx * Sy) / delta
        b = (Sxx * Sy - Sx * Sxy) / delta
        err_a = np.sqrt(Sw / delta)
        err_b = np.sqrt(Sxx / delta)
        return {
            "pendiente":    a,
            "ordenada":     b,
            "err_pendiente": err_a,
            "err_ordenada":  err_b,
            "r2":           None,   # no aplica para ajuste ponderado
        }


# ──────────────────────────────────────────────────────────────
# Formato de resultados
# ──────────────────────────────────────────────────────────────

def formato_resultado(valor, incerteza, unidad="", nombre=""):
    """
    Imprime un resultado con su incerteza correctamente redondeado.

    Parámetros
    ----------
    valor     : float
    incerteza : float
    unidad    : str, opcional
    nombre    : str, opcional  (nombre de la magnitud)
    """
    if incerteza <= 0:
        print(f"{nombre + ': ' if nombre else ''}{valor} {unidad}")
        return

    # Cifras significativas según la incerteza
    exp = int(np.floor(np.log10(abs(incerteza))))
    decimales = max(0, -exp + 1)
    fmt = f".{decimales}f"
    print(
        f"{nombre + ': ' if nombre else ''}"
        f"{valor:{fmt}} ± {incerteza:{fmt}} {unidad}"
    )


# ──────────────────────────────────────────────────────────────
# Visualización
# ──────────────────────────────────────────────────────────────

def configurar_estilo():
    """Aplica estilo minimalista y legible a matplotlib."""
    plt.rcParams.update({
        "figure.dpi":    120,
        "font.size":     12,
        "axes.grid":     True,
        "grid.alpha":    0.3,
        "lines.linewidth": 1.5,
        "axes.spines.top":   False,
        "axes.spines.right": False,
    })


def guardar_figura(fig, nombre, carpeta="figuras"):
    """
    Guarda una figura en PDF y PNG dentro de `carpeta`.

    Uso:
        guardar_figura(fig, "posicion_vs_tiempo")
    """
    import os
    os.makedirs(carpeta, exist_ok=True)
    ruta_pdf = os.path.join(carpeta, f"{nombre}.pdf")
    ruta_png = os.path.join(carpeta, f"{nombre}.png")
    fig.savefig(ruta_pdf, bbox_inches="tight")
    fig.savefig(ruta_png, bbox_inches="tight")
    print(f"Figura guardada: {ruta_pdf}  |  {ruta_png}")
