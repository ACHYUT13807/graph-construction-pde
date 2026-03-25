import numpy as np

def compute_edges(points, k=4):
    edges = []
    for i in range(len(points)):
        distances = np.linalg.norm(points - points[i], axis=1)
        neighbors = np.argsort(distances)[1:k+1]
        for j in neighbors:
            edges.append((i, j))
    return edges