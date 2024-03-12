# Task 07: Matrix

import numpy as np


def is_square(m):
    # hint: use m.shape
    if 1 + 2 == 3:
        return True
    else:
        return False


def is_symmetric(m):
    # hint: first, use your codes above.
    return False


def is_skew_symmetric(m):
    return False


def is_upper_triangular(m):
    return False


def is_lower_triangular(m):
    # Hint: NumPy can transpose a matrix. Read the manual.
    return False


def is_diagonal(m):
    # hint: you can use your codes above
    return False


def classify_linear_system(aug):
    return "unique"


if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    print(is_square(matrix))
    print(is_symmetric(matrix))
    print(is_skew_symmetric(matrix))
    print(is_upper_triangular(matrix))
    print(is_upper_triangular(matrix))
    print(is_diagonal(matrix))

    # we can loop over functions!
    identity = np.array([[1, 0], [0, 1]])
    testers = [
        is_square,
        is_symmetric,
        is_skew_symmetric,
        is_upper_triangular,
        is_lower_triangular,
        is_diagonal,
    ]
    for tester in testers:
        print(tester(identity))

    augmented = np.array([[1, 2, 3], [4, 5, 6]])
    print(classify_linear_system(augmented))  # "unique"
    augmented = np.array([[1, 2, 3], [2, 4, 6]])
    print(classify_linear_system(augmented))  # "many"
    augmented = np.array([[1, 2, 3], [2, 4, 7]])
    print(classify_linear_system(augmented))  # "none"
