from copy import deepcopy


class Matrix:
    def __init__(self, arr):
        """
        Class for 2x2 matrices
        """
        self.matrix = arr
        self.shape = len(arr), len(arr[0])

    def replace_column(self, col, vec):
        new_matrix = deepcopy(self.matrix)

        new_matrix[0][col] = vec[0]
        new_matrix[1][col] = vec[1]

        return Matrix(new_matrix)

    def getD(self):
        return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]

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
    slae = tuple(map(float, next(f).split()))
    a, b, c, d, p, q = slae

array, bias = slae[:4], slae[4:]
m0 = Matrix.from_what(array, 2, 2)

m1 = m0.replace_column(0, bias)
m2 = m0.replace_column(1, bias)

d0 = m0.getD()
d1 = m1.getD()
d2 = m2.getD()

with open("output.txt", "w") as f:
    if d0 != 0:
        f.write(f"2 {d1/d0} {d2/d0}")

    elif not any(slae):
        f.write("5")

    elif d == 0 and c != 0:
        x = q / c
        f.write(f"3 {x}")

    elif a != 0 and b == 0:
        x = p / a
        f.write(f"3 {x}")

    elif c == 0 and d != 0:
        y = q / d
        f.write(f"4 {y}")

    elif a == 0 and b != 0:
        y = p / b
        f.write(f"4 {y}")

    elif a / c == b / d == p / q:
        f.write(f"1 {-a / b} {p / b}")

    else:
        f.write("0")

