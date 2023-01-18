import numpy as np


class Line:
    def __init__(self, pt: np.ndarray, vec: np.ndarray):
        self.pt = pt
        self.vec = vec

    def solve(self, t: float | int) -> np.ndarray:
        """
        Принимает параметр.
        Возвращает решение векторно-параметрического уравнения.
        """
        return self.pt + t * self.vec


class Plane:
    def __init__(self, pts):
        p1, p2, p3 = pts
        # Находим A, B, C и D общего уравнения плоскости: Ax + Bx + Cz = D
        a = (p2[1] - p1[1]) * (p3[2] - p1[2]) - (p3[1] - p1[1]) * (p2[2] - p1[2])
        b = (p3[0] - p1[0]) * (p2[2] - p1[2]) - (p2[0] - p1[0]) * (p3[2] - p1[2])
        c = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

        self.norm = np.array([a, b, c])
        self.D = a * p1[0] + b * p1[1] + c * p1[2]


class CuboidWithMirrors:
    def __init__(self, task_data):
        self.intersection = None  # (id, pt)

        cuboid_pts, ray_vec, ray_pt, ray_energy, mirrors_pts = task_data

        a, b, c, d = cuboid_pts
        e = d - c
        f = a - b
        g = b - c

        self.cuboid = [Plane([a, c, b]),
                       Plane([b, c, d]),
                       Plane([c, d, c + f]),
                       Plane([a, b, d + g]),
                       Plane([a, d + f, c + f]),
                       Plane([d, a + e, b + e])]

        self.mirrors = [Plane(pts) for pts in mirrors_pts]

        self.planes = self.cuboid + self.mirrors  # 0 - 5 - грани параллелепипеда, 6 ... - зеркала

        self.ray = Line(ray_pt, ray_vec)
        self.ray_energy = ray_energy

        # for plane in self.planes[6:]:
        #     print(plane.norm, plane.D)

    def find_interception(self):
        r0 = self.ray.pt
        a = self.ray.vec

        intersections = []
        for i, plane in enumerate(self.planes):
            n = plane.norm
            d = plane.D
            # Находим параметр пересечения прямой и плоскости
            t = (d - np.dot(n, r0)) / np.dot(n, a)
            # Не будем учитывать текущую точку луча света и точки вне параллелепипеда
            if t > 0:
                intersections.append((i, self.ray.solve(t)))

        self.intersection = min(intersections, key=lambda x: np.linalg.norm(x[1] - r0))

    def reflect(self):
        if self.intersection:
            # Если луч отразился от зеркала
            if self.intersection[0] > 5:
                r0 = self.intersection[1]
                r1 = self.ray.vec
                a = self.planes[self.intersection[0]].norm
                # Строим новый отраженный луч света, путем нахождения симметричной точки относительно нормали плоскости
                self.ray.pt = r0
                self.ray.vec = 2 * r0 - r1 - 2 * np.dot(r1 - r0, a) / np.dot(a, a) * a

                return self.reduce_ray_energy()
            return 1  # Луч вылетел из параллелепипеда
        else:
            raise RuntimeWarning("Не найдено отражение")

    def reduce_ray_energy(self):
        self.ray_energy -= 1
        if self.ray_energy:
            return 2  # Все хорошо, продолжаем
        else:
            return 0  # У луча закончилась энергия

    def raytracing(self):
        while 1:
            self.find_interception()
            reflection_res = self.reflect()

            if reflection_res < 2:
                s = reflection_res
                if s:
                    return s, self.ray_energy, self.ray.pt, self.ray.vec
                return s, self.ray.pt


def read_input(fn="input.txt"):
    with open(fn, "r") as f:
        # 4 точки параллелограмма
        cuboid = [np.array(list(map(float, f.readline().split()))) for _ in range(4)]

        ray_vec = np.array(list(map(float, f.readline().split())))
        ray_pt = np.array(list(map(float, f.readline().split())))
        ray_energy = int(f.readline())
        mirrors_cnt = int(f.readline())

        # n зеркал по 3 точки на каждое
        mirrors = []
        for _ in range(mirrors_cnt):
            mirrors.append([np.array(list(map(float, f.readline().split()))) for _ in range(3)])

        return cuboid, ray_vec, ray_pt, ray_energy, mirrors


def write_output(s: int, *args, fn="output.txt"):
    with open(fn, "w") as f:
        # Луч вылетел из параллелепипеда
        if s:
            ray_energy = str(args[0]) + "\n"
            ray_pt = " ".join(map(str, args[1])) + "\n"
            ray_vec = " ".join(map(str, args[2]))
            f.writelines([str(s) + "\n", ray_energy, ray_pt, ray_vec])
        # Луч потратил всю энергию
        else:
            ray_pt = " ".join(map(str, args[0]))
            f.writelines([str(s) + "\n", ray_pt])


def main():
    input_data = read_input()
    cuboid = CuboidWithMirrors(input_data)
    output_data = cuboid.raytracing()
    write_output(*output_data)


if __name__ == "__main__":
    main()
