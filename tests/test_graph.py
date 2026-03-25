from src.grid import create_grid
from src.graph import compute_edges

def test_graph():
    points = create_grid(10)
    edges = compute_edges(points, k=3)
    
    assert len(points) == 100
    assert len(edges) > 0