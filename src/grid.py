import numpy as np

def create_grid(n):
    x = np.linspace(0, 1, n)
    y = np.linspace(0, 1, n)
    xv, yv = np.meshgrid(x, y)
    return np.vstack([xv.ravel(), yv.ravel()]).T