# Task 06: Matrices

import math

import numpy as np


def rotation_matrix_2d(theta):
    return np.array([[1, 0], [0, 1]])


def rotation_matrix_2d_degree(deg):
    return rotation_matrix_2d(0)


def distance(p1, p2):
    return 0


def rotate(p, theta):
    return (0, 0)


if __name__ == "__main__":  # the main part
    print(rotation_matrix_2d(math.pi))
    print(rotation_matrix_2d_degree(180))
    p1 = (7, 3)
    p2 = (3, 0)
    d = distance(p1, p2)
    print(d)  # should give 5
    p2_new = rotate(p2, math.pi / 2)  # should give (0, 3)
    print(p2_new)
