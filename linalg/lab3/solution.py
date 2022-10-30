with open("input.txt") as f:
    a, b, c, d, p, q = map(float, next(f).split())

with open("output.txt", "w") as f:
    try:
        if d == 0 and c == 0 or a == 0 and b == 0:
            f.write(f"5")

        elif d == 0:
            x = q / c
            f.write(f"3 {x}")

        elif b == 0:
            x = p / a
            f.write(f"3 {x}")

        elif c == 0:
            y = q / d
            f.write(f"4 {y}")

        elif a == 0:
            y = p / b
            f.write(f"4 {y}")

        elif a / c == b / d == p / q:
            f.write(f"1 {-a / b} {p / b}")

        else:
            y = (c * p - a * q) / (c * b - a * d)
            x = (q - d * y) / c

            f.write(f"2 {x} {y}")

    except Exception as e:
        print(e)
        f.write("0")



