import numpy as np

def laplace_step(u, dx, dy):
    u_new = u.copy()
    u_new[1:-1, 1:-1] = (
        (u[2:, 1:-1] + u[:-2, 1:-1]) * dy**2 +
        (u[1:-1, 2:] + u[1:-1, :-2]) * dx**2
    ) / (2 * (dx**2 + dy**2))
    return u_new

def solve_laplace(n=20, iterations=100):
    u = np.zeros((n, n))
    u[0, :] = 1  # boundary condition

    dx = dy = 1.0 / n

    for _ in range(iterations):
        u = laplace_step(u, dx, dy)

    return u