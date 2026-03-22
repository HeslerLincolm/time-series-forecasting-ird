import os
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

def save_figure(fig, path: str, filename: str, dpi: int = 300):
    """
    Save a matplotlib figure to a specified path.

    Parameters:
    - fig: matplotlib figure object
    - path: directory where the image will be saved
    - filename: name of the file (e.g., "plot.png")
    - dpi: image resolution
    """

    # Crear carpeta si no existe
    os.makedirs(path, exist_ok=True)

    # Ruta completa
    full_path = os.path.join(path, filename)

    # Guardar figura
    fig.savefig(full_path, dpi=dpi, bbox_inches="tight")

    print(f"Figure saved at: {full_path}")

def adf_test(series):
    result = adfuller(series, autolag='AIC')

    return {
        "statistic": result[0],
        "p_value": result[1],
        "critical_values": result[4]
    }