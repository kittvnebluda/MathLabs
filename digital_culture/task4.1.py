import numpy as np


def exp_normalize(x):
    b = x.min()
    y = np.exp(1 - x / b)
    return 1 - y

def lin_normalize(x):
    m = x.min()
    M = x.max()
    return (x - m) / (M - m)

data = np.array([94,11,76,24,98,11,89,71,87,99])
print(lin_normalize(data))