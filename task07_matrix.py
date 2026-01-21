# Task 07: Matrix

import numpy as np


def is_square(m):
    """Check if a matrix is square (same number of rows and columns).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is square, False otherwise
    
    Hint: Use m.shape to get (rows, cols), then check if rows == cols
    """
    # hint: use m.shape
    if 1 + 2 == 3:
        return True
    else:
        return False


def is_symmetric(m):
    """Check if a matrix is symmetric (equals its transpose).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is symmetric, False otherwise
    
    Hint: First check if square, then use np.array_equal(m, m.T)
    """
    # hint: first, use your codes above.
    return False


def is_skew_symmetric(m):
    """Check if a matrix is skew-symmetric (equals negative of its transpose).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is skew-symmetric, False otherwise
    
    Hint: Check if m == -m.T (use np.array_equal)
    """
    return False


def is_upper_triangular(m):
    """Check if a matrix is upper triangular (all elements below diagonal are zero).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is upper triangular, False otherwise
    
    Hint: Use np.triu(m) to get upper triangular part, compare with m
    """
    return False


def is_lower_triangular(m):
    """Check if a matrix is lower triangular (all elements above diagonal are zero).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is lower triangular, False otherwise
    
    Hint: NumPy can transpose a matrix. Use m.T or np.transpose(m). Or use np.tril(m).
    """
    return False


def is_diagonal(m):
    """Check if a matrix is diagonal (all non-diagonal elements are zero).
    
    Args:
        m: A NumPy 2D array
    
    Returns:
        bool: True if the matrix is diagonal, False otherwise
    
    Hint: A diagonal matrix is both upper and lower triangular
    """
    # hint: you can use your codes above
    return False


def classify_linear_system(aug):
    """Classify a linear system as having unique, many, or no solutions.
    
    Args:
        aug: Augmented matrix [A|b] as a NumPy 2D array
    
    Returns:
        str: "unique", "many", or "none"
    
    Hint: 
        1. Extract A (all columns except last): aug[:, :-1]
        2. Calculate rank of A: np.linalg.matrix_rank(A)
        3. Calculate rank of aug: np.linalg.matrix_rank(aug)
        4. Compare ranks with number of unknowns (n = A.shape[1])
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
