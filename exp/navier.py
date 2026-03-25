from src.pde import solve_laplace
import matplotlib.pyplot as plt

u = solve_laplace(30)

plt.imshow(u, cmap="viridis")
plt.title("PDE Simulation Demo")
plt.colorbar()
plt.show()