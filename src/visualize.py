import matplotlib.pyplot as plt

def plot_graph(points, edges):
    plt.scatter(points[:, 0], points[:, 1], s=10)

    for i, j in edges:
        plt.plot(
            [points[i][0], points[j][0]],
            [points[i][1], points[j][1]],
            linewidth=0.3
        )

    plt.title("Graph Representation of Grid")
    plt.show()