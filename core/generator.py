import numpy as np
from typing import Tuple

def get_lorenz_coords(n_points: int = 2000, dt: float = 0.01) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Computes Lorenz Attractor coordinates using vectorized NumPy arrays.
    Type hinting and docstrings are mandatory for senior-level readability.
    """
    x, y, z = np.empty(n_points), np.empty(n_points), np.empty(n_points)
    x[0], y[0], z[0] = (0., 1., 1.05)

    for i in range(n_points - 1):
        dx = 10 * (y[i] - x[i])
        dy = x[i] * (28 - z[i]) - y[i]
        dz = x[i] * y[i] - (8/3) * z[i]
        
        x[i+1] = x[i] + (dx * dt)
        y[i+1] = y[i] + (dy * dt)
        z[i+1] = z[i] + (dz * dt)
        
    return x, y, z