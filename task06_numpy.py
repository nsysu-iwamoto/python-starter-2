# Task 06: NumPy

import math

import numpy as np


def rotation_matrix_2d(theta):
    """Create a 2D rotation matrix for rotating by theta radians.
    
    Args:
        theta: Rotation angle in radians
    
    Returns:
        2x2 NumPy array representing the rotation matrix
    
    Hint: Use np.cos(theta), np.sin(theta), and np.array([[a, b], [c, d]])
    """
    return np.array([[1, 0], [0, 1]])


def rotation_matrix_2d_degree(deg):
    """Create a 2D rotation matrix for rotating by deg degrees.
    
    Args:
        deg: Rotation angle in degrees
    
    Returns:
        2x2 NumPy array representing the rotation matrix
    
    Hint: Convert degrees to radians using np.radians(deg), then use rotation_matrix_2d
    """
    return rotation_matrix_2d(0)


def distance(p1, p2):
    """Calculate the Euclidean distance between two points.
    
    Args:
        p1: A tuple (x1, y1) representing the first point
        p2: A tuple (x2, y2) representing the second point
    
    Returns:
        float: The distance between p1 and p2
    
    Hint: Use math.sqrt() and the distance formula, or np.linalg.norm()
    """
    return 0


def rotate(p, theta):
    """Rotate a point p around the origin by theta radians.
    
    Args:
        p: A tuple (x, y) representing the point to rotate
        theta: Rotation angle in radians
    
    Returns:
        tuple: The rotated point as (x', y')
    
    Hint: 
        1. Convert p to a NumPy array: np.array(p)
        2. Get rotation matrix: rotation_matrix_2d(theta)
        3. Multiply: matrix @ point_array
        4. Convert back to tuple: tuple(result)
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
