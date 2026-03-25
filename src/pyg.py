import torch
from torch_geometric.data import Data

def to_pyg_data(points, edges, values=None):
    """
    Convert numpy graph → PyTorch Geometric Data
    """

    # Node features (positions)
    x = torch.tensor(points, dtype=torch.float)

    # Edge index (2, E)
    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()

    # Optional: add PDE values as features
    if values is not None:
        values = torch.tensor(values, dtype=torch.float).unsqueeze(1)
        x = torch.cat([x, values], dim=1)

    data = Data(x=x, edge_index=edge_index)

    return data