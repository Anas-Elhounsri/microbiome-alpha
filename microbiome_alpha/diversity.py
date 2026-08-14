import numpy as np


def shannon(counts):
    counts = np.asarray(counts, dtype=float)
    p = counts[counts > 0] / counts.sum()
    return float(-(p * np.log(p)).sum())
