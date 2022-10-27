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
            return

        new_matrix = deepcopy(self.matrix)

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_matrix[i][j] += other.matrix[i][j]

        return Matrix(new_matrix)

    def __str__(self) -> str:
        return str(self.matrix)

    def __mul__(self, other):
        if type(other) == Matrix and self.shape[0] != other.shape[1]:
            return

        new_matrix = deepcopy(self.matrix)

        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if isinstance(other, Matrix):
                    new_matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.shape[1]))

                elif isinstance(other, int) or isinstance(other, float):
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


with open("input.txt") as f:
    n1, m1 = map(int, next(f).split())
    a = tuple(map(float, next(f).split()))

    n2, m2 = map(int, next(f).split())
    b = tuple(map(float, next(f).split()))

    n3, m3 = map(int, next(f).split())
    c = tuple(map(float, next(f).split()))

    k = float(next(f))

a = Matrix.from_what(a, n1, m1)
b = Matrix.from_what(b, n2, m2)
c = Matrix.from_what(c, n3, m3)

try:
    x = a * (b * k + c.getT())

    with open("output.txt", "w") as f:
        f.write(f"{1}\n")
        f.write(f"{x.shape[0]} {x.shape[1]}\n")

        flat_x = x.flatten()
        for e in flat_x[:-1]:
            f.write(f"{e} ")
        f.write(str(flat_x[-1]))

except AttributeError:
    with open("output.txt", "w") as f:
        f.write(str(0))

# print(str(a).replace("[", "{").replace("]", "}").replace(".0", ""))
# print(str(b).replace("[", "{").replace("]", "}").replace(".0", ""))
# print(str(c).replace("[", "{").replace("]", "}"))
# print(str(c.getT()).replace("[", "{").replace("]", "}"))
# print(str(a * b).replace("[", "{").replace("]", "}").replace(".0", ""))
# print(str(b * a).replace("[", "{").replace("]", "}").replace(".0", ""))

print(Matrix.from_what([1, 2, 3, 4, 5, 6], 2, 3))
print(Matrix.from_what([1, 2, 3, 4, 5, 6], 2, 3).getT())
