from typing import List

inp = open("input.txt", "r")
out = open("output.txt", "w")

def sum_matr(f:List[List[float]], s:List[List[float]]) -> List[List[float]]:
    for i in range(len(f)):
        for j in range(len(f[0])):
            f[i][j] += s[i][j]
    return f

def mul(f:List[List[float]], el:float) -> List[List[float]]:
    for i in range(len(f)):
        for j in range(len(f[0])):
            f[i][j] *= el
    return f

def mul_matr(f:List[List[float]], s:List[List[float]]) -> List[List[float]]:
    m = [[0] * len(s[0]) for _ in f]
    for i in range(len(f)):
        for j in range(len(s[0])):
            m[i][j] = sum([f[i][x] * s[x][j] for x in range(len(s))])
    return m

def trans(f:List[List[float]]) -> List[List[float]]:
    tr = []
    for i in range(len(f[0])):
        tr.append([])
        for j in range(len(f)):
            tr[i].append(f[j][i])
    return tr

r1, c1 = list(map(int, inp.readline().split()))

inp_l = list(map(float, inp.readline().split()))
a = [[0] * c1 for _ in range(r1)]
for i in range(r1 * c1):
        a[i // c1][i % c1] = inp_l[i]

r2, c2 = list(map(int, inp.readline().split()))

inp_l = list(map(float, inp.readline().split()))
b = [[0] * c2 for _ in range(r2)]
for i in range(r2 * c2):
    b[i // c2][i % c2] = inp_l[i]

r3, c3 = list(map(int, inp.readline().split()))

inp_l = list(map(float, inp.readline().split()))
c = [[0] * c3 for _ in range(r3)]
for i in range(r3 * c3):
    c[i // c3][i % c3] = inp_l[i]

al = float(inp.readline())

x = [[0.0] * len(b[0]) for _ in a]

def task():
    if len(c[0]) != len(b) or len(c) != len(b[0]):
        return 0
    if len(a[0]) != len(b):
        return 0

    global x
    x = [el.copy() for el in mul_matr(a, sum_matr(mul(b, al), trans(c)))]

    return 1
if task():
    out.write('1\n')
    out.write(str(len(x)) + " " + str(len(x[0])) + "\n")
    [out.write(str(el).replace('[', '').replace(']', '').replace(',','') + " ") for el in x]
    out.seek(out.tell()-1)
    out.truncate()
else:
    out.write('0')