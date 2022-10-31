def det(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def trans(mat):
    mat_tr = []
    for i in range(len(mat[0])):
        mat_tr.append([])
        for j in range(len(mat)):
            mat_tr[i].append(mat[j][i])
    return mat_tr


def solve(mat, ans):
    detA = det(mat)
    mat = trans(mat)
    det1 = det([ans, mat[1]])
    det2 = det([mat[0], ans])
    return [det1 / detA, det2 / detA]


def check_mn(f, s):
    return "0" if s == 0 else f / s


def is_line(a, b):
    mn = a[0][0] / a[1][0] \
        if check_mn(a[0][0], a[1][0]) != "0" else a[0][1] / a[1][1] \
        if check_mn(a[0][1], a[1][1]) != "0" else b[0] / b[1] \
        if check_mn(b[0], b[1]) != "0" else 0

    return (a[0][0] * mn == a[1][0] and a[0][1] * mn == a[1][1] and b[0] * mn == b[1]) or \
           (a[0][0] == a[1][0] * mn and a[0][1] == a[1][1] * mn and b[0] == b[1] * mn)


with open("input.txt", "r") as inp:
    arr = list(map(float, inp.readline().split()))

a = [arr[:2], arr[2:4]]
b = arr[4:]


def task():
    if det(a) != 0:
        return 2, solve(a, b)

    if not any(arr):
        return 5, []

    if is_line(a, b) and not any([a[1][0], a[1][1], b[1]]):
        if a[0][0] == 0 and a[0][1] != 0:
            return 4, [b[0] / a[0][1]]
        if a[0][1] == 0 and a[0][0] != 0:
            return 3, [b[0] / a[0][0]]

    if is_line(a, b):
        if a[1][0] == 0 and a[1][1] != 0:
            return 4, [b[1] / a[1][1]]
        if a[1][1] == 0 and a[1][0] != 0:
            return 3, [b[1] / a[1][0]]

    if is_line(a, b):
        if a[0][1] != 0:
            return 1, [-1 * a[0][0] / a[0][1], b[0] / a[0][1]]
        elif a[1][1] != 0:
            return 1, [-1 * a[1][0] / a[1][1], b[1] / a[1][1]]

    return 0, []


ans = task()

with open("output.txt", "w") as out:
    out.write(str(ans[0]) + " " + str(ans[1]).replace('[', '').replace(']', '').replace(',', ''))
