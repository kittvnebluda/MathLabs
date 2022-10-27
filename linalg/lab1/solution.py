with open("input.txt") as f:
    n = int(next(f))
    odds = [int(x) for x in next(f).split()]
    x = int(next(f))

curr = odds[0]
for i in range(n):
    curr = x * curr + odds[i + 1]

with open("output.txt", "w") as f:
    f.write(f"{curr}\n")
    f.write(str(curr))
