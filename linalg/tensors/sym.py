import math

from itertools import product
from itertools import permutations

import numpy as np


# Получаем строку столбиков тензора
text = "2 5 −3 0 4 −5 −5 −4 3 5 −3 4 5 −5 −5 −2 −6 0 −2 1 1 5 0 3 −6 4 0 −3 4 −3 3 −4"
columns = tuple(map(int, text.replace("−", "-").split()))

tensor = np.zeros((2, 2, 2, 2, 2), dtype=float)

# Формируем тензор
for i in range(len(columns)):
    tensor[i % 2, i // 4 % 2, i // 2 % 2, i // 8 % 2, i // 16] = float(columns[i])

# Выводим тензор для проверки
for i in range(tensor.shape[2]):
    for j in range(tensor.shape[0]):
        for k in range(tensor.shape[4]):
            for l in range(tensor.shape[3]):
                for m in range(tensor.shape[1]):
                    print(tensor[j, m, i, l, k], end="\t")
        print()

# Симметризуем
# new_tensor = tensor.copy()
# for el in product([0, 1], repeat=5):
#     r = 4  # Число симметризуемых индексов
#     index_perms = tuple(permutations([el[0], el[1], el[3], el[4]], r=r))
#     comb = np.array([
#         tensor[x[0], x[1], el[2], x[2], x[3]]
#         for x in index_perms])
#     new_tensor[el] = comb.sum() / math.factorial(r)

new_tensor = tensor.copy()
for el in product([0, 1], repeat=5):
    r = 2  # Число симметризуемых индексов
    index_perms = tuple(permutations([el[0], el[3]], r=r))
    comb = np.array([
        tensor[x[0], el[1], el[2], x[1], el[4]]
        for x in index_perms])
    new_tensor[el] = comb.sum() / math.factorial(r)

print()

# Формируем список из тензора по строкам
fineout = []
for i in range(tensor.shape[2]):
    for j in range(tensor.shape[0]):
        for k in range(tensor.shape[4]):
            fineline = []
            for l in range(tensor.shape[3]):
                for m in range(tensor.shape[1]):
                    fineline.append(round(new_tensor[j, m, i, l, k], 2))
                    print(new_tensor[j, m, i, l, k], end="\t")
            fineout.append(fineline)
        print()

print(fineout)





















