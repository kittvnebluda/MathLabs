import numpy as np
from matplotlib import pyplot as plt

space = np.linspace(-1, 1, num=50)
smol_space = np.linspace(-1, 1, num=4)


def f(x):
    return np.cos(x) * np.sin(x)


def omega(x: float, k: int = None):
    par = x - smol_space
    res = 1
    for i, j in enumerate(par):
        if k != i:
            res *= j
    return res


def Q(x, m):
    assert m <= len(smol_space)
    res = 0
    for i in range(m + 1):
        o = omega(x, i)
        res += o / (omega(smol_space[i], i) if o != 0 else 1) * f(smol_space[i])
    return res


# print(Q(smol_space[2], 2))
plt.plot(space, f(space))
y = [Q(x, 2) for x in smol_space]
plt.plot(smol_space, y)
plt.show()
