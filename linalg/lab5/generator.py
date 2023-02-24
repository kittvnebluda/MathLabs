import random

import numpy as np

print(random.randint(0, 10))
N = random.randint(2, 4)
print(N)

for _ in range(N):
    print(*np.random.rand(3).round(2))
    print(*np.random.rand(3).round(2))
    print(*np.random.rand(3).round(2))
