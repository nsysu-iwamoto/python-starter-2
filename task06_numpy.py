# Task 06: NumPy

import math

import numpy as np


def rotation_matrix_2d(theta):
    """Create a 2D rotation matrix for the given angle in radians.

    Args:
        theta (float): Rotation angle in radians

    Returns:
        np.ndarray: 2x2 rotation matrix
    """
    return np.array([[1, 0], [0, 1]])


def rotation_matrix_2d_degree(deg):
    """Create a 2D rotation matrix for the given angle in degrees.

    Args:
        deg (float): Rotation angle in degrees

    Returns:
        np.ndarray: 2x2 rotation matrix
    """
    return rotation_matrix_2d(0)


def distance(p1, p2):
    """Calculate the Euclidean distance between two 2D points.

    Args:
        p1, p2 (tuple): Points as (x, y) tuples

    Returns:
        float: Distance between the points
    """
    return 0


def rotate(p, theta):
    """Rotate a 2D point by the given angle.

    Args:
        p (tuple): Point as (x, y) tuple
        theta (float): Rotation angle in radians

    Returns:
        tuple: Rotated point as (x, y) tuple
    """
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
