# src/utils.py
import numpy as np

def pairwise_distance(points):
    diff = points[:, None, :] - points[None, :, :]
    return np.linalg.norm(diff, axis=-1)

def normalize(values):
    return (values - np.min(values)) / (np.max(values) - np.min(values))

def to_grid(values, n):
    return values.reshape(n, n)