from src.grid import create_grid
from src.graph import compute_edges
from src.visualize import plot_graph
from src.pde import solve_laplace
from src.pyg import to_pyg_data
from src.gnn import SimpleGNN

import matplotlib.pyplot as plt


def main():
    # Step 1: Create grid + graph
    points = create_grid(20)
    edges = compute_edges(points, k=4)

    # Step 2: Visualize graph
    plot_graph(points, edges)

    # Step 3: Solve PDE
    u = solve_laplace(20)
    values = u.flatten()

    plt.imshow(u, origin='lower')
    plt.colorbar()
    plt.title("Laplace Equation Solution")
    plt.show()

    # Step 4: Convert to PyG
    data = to_pyg_data(points, edges, values)
    print(data)

    # Step 5: Run GNN
    model = SimpleGNN()
    out = model(data)

    print("GNN output shape:", out.shape)


if __name__ == "__main__":
    main()
from src.grid import create_grid
from src.graph import compute_edges
from src.visualize import plot_graph
import numpy as np
import matplotlib.pyplot as plt
def main():
    points = create_grid(20)
    edges = compute_edges(points, k=4)
    plot_graph(points, edges)
    values = np.sin(points[:,0]*np.pi) * np.sin(points[:,1]*np.pi)
    print(values)
    # You can also visualize the values on the grid
    plt.imshow(values.reshape(20, 20), extent=(0, 1, 0, 1), origin='lower')
    plt.colorbar()
    plt.title("Function Values on Grid")
    plt.show()
    plt.scatter(points[:,0], points[:,1], c=values, cmap='viridis')
    plt.colorbar()
    plt.title("Function Values on Scatter")
    plt.show()
if __name__ == "__main__":
    main()