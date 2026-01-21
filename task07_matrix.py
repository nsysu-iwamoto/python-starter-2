# Task 07: Matrix

import numpy as np


def is_square(m):
    """Check if a matrix is square (rows = columns).

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if square, False otherwise
    """
    # hint: use m.shape
    if 1 + 2 == 3:
        return True
    else:
        return False


def is_symmetric(m):
    """Check if a matrix is symmetric (A = A^T).

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if symmetric, False otherwise
    """
    # hint: first, use your codes above.
    return False


def is_skew_symmetric(m):
    """Check if a matrix is skew-symmetric (A = -A^T).

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if skew-symmetric, False otherwise
    """
    return False


def is_upper_triangular(m):
    """Check if a matrix is upper triangular.

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if upper triangular, False otherwise
    """
    return False


def is_lower_triangular(m):
    """Check if a matrix is lower triangular.

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if lower triangular, False otherwise
    """
    # Hint: NumPy can transpose a matrix. Read the manual.
    return False


def is_diagonal(m):
    """Check if a matrix is diagonal.

    Args:
        m (np.ndarray): A 2D NumPy array

    Returns:
        bool: True if diagonal, False otherwise
    """
    # hint: you can use your codes above
    return False


def classify_linear_system(aug):
    """Classify a linear system as unique, many, or no solutions.

    Args:
        aug (np.ndarray): Augmented matrix [A|b]

    Returns:
        str: "unique", "many", or "none"
    """
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
