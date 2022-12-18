from copy import deepcopy
from itertools import chain


class Matrix:
    def __init__(self, arr):
        """
        Class for 2D matrices
        """
        self.matrix = arr
        self.shape = len(arr), len(arr[0])

    def __add__(self, other):
        if self.shape != other.shape:
            if __debug__: print("Размеры суммируемых матриц не равны")
            return

        new_matrix = deepcopy(self.matrix)

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_matrix[i][j] += other.matrix[i][j]

        return Matrix(new_matrix)

    def __str__(self) -> str:
        return str(self.matrix)

    def __mul__(self, other):
        if self.shape[1] != other.shape[0]:
            if __debug__: print(f"Размеры умножаемых матриц не верные: {self.shape[0]} != {other.shape[1]}")
            return

        new_matrix = [[0] * other.shape[1] for _ in range(self.shape[0])]

        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                new_matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.shape[1]))

        return Matrix(new_matrix)

    def __rmul__(self, other):
        new_matrix = deepcopy(self.matrix)

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_matrix[i][j] *= other

        return Matrix(new_matrix)

    def getT(self):
        new_matrix = []

        for i in range(self.shape[1]):
            row = []
            for j in range(self.shape[0]):
                row.append(self.matrix[j][i])
            new_matrix.append(row)

        return Matrix(new_matrix)

    def flatten(self):
        return tuple(chain.from_iterable(self.matrix))

    @staticmethod
    def from_what(flat_matrix, rows, columns):
        new_matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(flat_matrix[columns * i + j])
            new_matrix.append(row)

        return Matrix(new_matrix)


with open("input.txt", encoding='utf8') as f:
    alpha, beta = map(int, next(f).split())

    matrices = []
    for _ in range(5):
        n, m = map(int, next(f).split())
        a = tuple(map(float, next(f).split()))

        matrices.append(Matrix.from_what(a, n, m))

    a, b, c, d, f = matrices

try:
    x = c * (alpha * a + beta * b.getT()).getT() * d + (-1) * f

    with open("output.txt", "w") as f:
        f.write("1\n")
        f.write(f"{x.shape[0]} {x.shape[1]}\n")

        flat_x = x.flatten()
        for e in flat_x[:-1]:
            f.write(f"{e} ")
        f.write(str(flat_x[-1]))

except AttributeError:
    with open("output.txt", "w") as f:
        f.write("0")
