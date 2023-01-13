import numpy as np

CANNON_TURN_RANGE = 60  # Максимальный угол поворота пушек в градусах
ZEROS = np.zeros(3)


def length(v) -> np.float64:
    return np.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """ Returns the angle in degrees between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            90.0
            >>> angle_between((4, 8, 0), (4, 8, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            180.0
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)

    angle = np.degrees(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)))

    return angle if angle > .1 else 0.0


def ship_plane_vec(pt, n, vec):
    """
    Return vector in new plane made with point and normal
    It finds z, x and y are the same

            >>> ship_plane_vec((0, 0, 0), (0, 0, 1), (1, 1, 89))
            array([1, 1, 0])
    """
    z = (n[2] * pt[2] - n[0] * (vec[0] - pt[0]) - n[1] * (vec[1] - pt[1]))
    return np.array([vec[0], vec[1], z])


def main(*args):
    """
    Finds solution

            >>> main((0, 0, 0), (1, 0, 0), (0, 0, 1), (3, 4, 0))
            (1, 36.87, 0.0, 'Bye')
            >>> main((0, 0, 0), (1, 0, 0), (1, 0, 1), (-0.5, 1, 0))
            (1, -35.26, 45.0, 'Bye')
            >>> main((0, 0, 0), (1, 0, 0), (-1, 1, 1), (4, 4, 0))
            (1, 30.0, 54.74, 'Bye')
            >>> main((0, 0, 0), (1, 0, 0), (-1, 0, 1), (-3, -4, 0))
            (0, 0, 45.0, 'Bye')
    """
    def beautiful_output(angle, side):
        if -CANNON_TURN_RANGE <= angle <= CANNON_TURN_RANGE and enemy_vec[2] >= 0:
            return side, angle * sign, match_angle, "Bye"
        else:
            return 0, 0, match_angle, "Bye"

    if args:
        global fr_ship, keel_projection, mast, en_ship

        fr_ship = np.array(args[0])
        keel_projection = np.array(args[1])
        mast = np.array(args[2])
        en_ship = np.array(args[3])

    dist = en_ship - fr_ship

    keel = ship_plane_vec(ZEROS, mast, keel_projection)

    nl = np.cross(keel, mast)  # Нормаль левого борта
    nr = np.cross(mast, keel)  # Нормаль правого борта

    match_angle = round(angle_between(mast, np.array([0, 0, 1])), 2)

    enemy_vec = ship_plane_vec(ZEROS, mast, dist)

    angle_keel = angle_between(keel, enemy_vec)
    sign = -1 if angle_keel > 90 else 1

    left_cannon_turn = round(angle_between(nl, enemy_vec), 2)
    right_cannon_turn = round(angle_between(nr, enemy_vec), 2)

    if right_cannon_turn < left_cannon_turn:
        return beautiful_output(right_cannon_turn, 1)
    else:
        return beautiful_output(left_cannon_turn, -1)


if __name__ == "__main__":
    with open("input.txt") as f:
        fr_ship = np.array([*map(float, next(f).split()), 0])
        keel_projection = np.array([*map(float, next(f).split()), 0])
        mast = np.array([*map(float, next(f).split()), 1])
        en_ship = np.array([*map(float, next(f).split()), 0])

    s, beta, theta, w = main()

    with open("output.txt", "w") as f:
        f.writelines([str(s) + "\n", str(beta) + "\n", str(theta) + "\n", w])
