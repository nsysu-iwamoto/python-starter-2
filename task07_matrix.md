# Task 07: Matrix

**Goal:** Work with matrices and their properties using NumPy

## Overview

In this task, you'll learn:

- How to check matrix properties (square, symmetric, triangular, etc.)
- How to use NumPy functions for matrix operations
- How to classify linear systems of equations
- How to use matrix rank to determine solution existence

Open `task07_matrix.py` and edit the file to do the following tasks.

### Names for Matrices

- **Square matrix**: Number of rows equals number of columns
- **Symmetric matrix**: $A = A^T$ (matrix equals its transpose)
- **Skew-symmetric matrix**: $A = -A^T$ (matrix equals negative of its transpose)
- **Upper triangular matrix**: All elements below the main diagonal are zero
- **Lower triangular matrix**: All elements above the main diagonal are zero
- **Diagonal matrix**: All elements outside the main diagonal are zero
- **Scalar matrix**: Diagonal matrix where all diagonal elements are equal
- **Identity matrix**: Scalar matrix where all diagonal elements are 1
- **Zero matrix**: All elements are 0
- **Idempotent matrix**: $A^2 = A$
- **Nilpotent matrix**: There exists some positive integer $k$ such that $A^k = 0$

## Task 07a (Required)

Section 7.2 of Kreyszig defines several special matrices. We want to make functions to check if a matrix is one of these special matrices. So, complete the following functions:

- `is_square(m)` to check if `m` is square.
- `is_symmetric(m)` to check if `m` is (square and) symmetric.
- `is_skew_symmetric(m)` to check if `m` is (square and) skew-symmetric.
- `is_upper_triangular(m)` to check if `m` is (square and) upper-triangular.
- `is_lower_triangular(m)` to check if `m` is (square and) lower-triangular.
- `is_diagonal(m)` to check if `m` is (square and) diagonal.

All the functions have the same signature:

- **Input**: `m` is a NumPy 2-dimensional array. *(You can assume all elements are integer.)*
- **Output**: a bool (`True` or `False`)

You can assume `m` is a NumPy 2d array with at least one element; no need to check it.

**Examples:**
```python
identity = np.array([[1, 0], [0, 1]])
is_square(identity)        # True
is_symmetric(identity)     # True
is_diagonal(identity)      # True

matrix = np.array([[1, 2], [3, 4]])
is_square(matrix)          # True
is_symmetric(matrix)       # False

upper = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
is_upper_triangular(upper) # True
```

<details>
<summary>Click to see hint</summary>

Use the `shape` attribute to get matrix dimensions:

```python
rows, cols = m.shape
```

For a square matrix: `rows == cols`

Use NumPy's transpose:

```python
m.T  # or np.transpose(m)
```

To check if two arrays are equal:

```python
np.array_equal(m, m.T)  # Check if m equals its transpose
```

To check if a matrix is triangular or diagonal, use NumPy functions:

```python
np.triu(m)  # Upper triangular part
np.tril(m)  # Lower triangular part
```

For example, a matrix is upper triangular if it equals its upper triangular part:

```python
np.array_equal(m, np.triu(m))
```

</details>

## Task 07b (Required)

(This task will be a part of the "real" coding assignments after the midterm exam.)

In Kreyszig Section 7.5, we have learned how we can classify linear systems of equations (Theorem 1).
Let's make a code for this test.

As a linear system of equations is equivalent to an augmented matrix (See Section 7.3), we can use it as the input.
The output can just be a string: `"unique"`, `"many"`, or `"none"` to represent how many solutions we have.

Complete the function `classify_linear_system(aug)`.

- **Input**: `aug` is the augmented matrix of a linear system of equations. It is a 2d NumPy array.
- **Output**: a string: `"unique"`, `"many"`, or `"none"`.

For a system $Ax = b$ with augmented matrix $[A|b]$:

- **Unique solution**: $\text{rank}(A) = \text{rank}([A|b]) = n$ (number of unknowns)
- **Infinitely many solutions**: $\text{rank}(A) = \text{rank}([A|b]) < n$
- **No solution**: $\text{rank}(A) < \text{rank}([A|b])$

**Examples:**
```python
# System: x + 2y = 3, 4x + 5y = 6
aug1 = np.array([[1, 2, 3], [4, 5, 6]])
classify_linear_system(aug1)  # "unique"

# System: x + 2y = 3, 2x + 4y = 6 (same line, infinitely many solutions)
aug2 = np.array([[1, 2, 3], [2, 4, 6]])
classify_linear_system(aug2)  # "many"

# System: x + 2y = 3, 2x + 4y = 7 (parallel lines, no solution)
aug3 = np.array([[1, 2, 3], [2, 4, 7]])
classify_linear_system(aug3)  # "none"
```

<details>
<summary>Click to see hint</summary>

You don't have to implement rank calculation. Read [the manual of numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) very carefully.

Look for `numpy.linalg.matrix_rank()`.

The augmented matrix has the form $[A|b]$ where:

- $A$ is the coefficient matrix (all columns except the last)
- $b$ is the constant vector (the last column)

Extract them:

```python
A = aug[:, :-1]  # All rows, all columns except last
b = aug[:, -1]   # All rows, last column only
```

Calculate ranks and compare:

```python
import numpy as np

rank_A = np.linalg.matrix_rank(A)
rank_aug = np.linalg.matrix_rank(aug)
n = A.shape[1]  # Number of unknowns

# Then use if-elif-else to determine the case
```

</details>

## Task 07c (Optional)

As a continuation of Task 07a, implement the following functions:

- `is_scalar_matrix(m)` to check if `m` is a scalar matrix.
- `is_identity_matrix(m)` to check if `m` is an identity matrix.
- `is_zero_matrix(m)` to check if `m` is a zero matrix.
- `is_idempotent(m)` to check if `m` is idempotent (Problem 7.2.7).

<details>
<summary>Click to see hint</summary>

For idempotent, check if $A \times A = A$:

```python
np.array_equal(m @ m, m)
```

</details>

## Task 07d (Optional, Advanced)

You can further implement the following function, where you need to derive/find some mathematical theorems.

- `is_nilpotent(m)` to check if `m` is nilpotent (Problem 7.2.8).

## Task 07e (Optional, Advanced)

Task 07a has a remark *You can assume all elements are integer.* ...but why? Explain.

Furthermore, what happens if you run your code for non-integer matrices? Do they work? Or...?

(This is why, in **real projects**, we **need to** use pre-built codes and **should not** write our own codes. Meanwhile, in lecture courses, you are asked to write your own code so that you know how the pre-built codes are written and what kinds of caveats lie there.)

### Think About

- Floating-point precision and comparison
- Why `==` might not work reliably for floats
- How to properly compare floating-point numbers

## Common Mistakes

1. **Not checking if matrix is square first**
   - ❌ Checking symmetry without verifying the matrix is square
   - ✅ For symmetric/triangular matrices, first check if square

2. **Using `==` instead of `np.array_equal()`**
   - ❌ `m == m.T` (returns an array of booleans)
   - ✅ `np.array_equal(m, m.T)` (returns a single boolean)

3. **Confusing rank of A vs rank of [A|b]**
   - ❌ Only checking rank of coefficient matrix
   - ✅ Compare both ranks to classify the system

4. **Off-by-one errors when extracting submatrices**
   - ❌ `aug[:, -2]` for last column
   - ✅ `aug[:, -1]` for last column

## Understanding NumPy Indexing

### Slicing 2D Arrays

```python
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Get all rows, first two columns
A[:, :2]  # [[1, 2], [4, 5], [7, 8]]

# Get all rows, last column
A[:, -1]  # [3, 6, 9]

# Get first two rows, all columns
A[:2, :]  # [[1, 2, 3], [4, 5, 6]]
```

## Need Help?

- Review NumPy documentation on array operations and linear algebra
- Test with simple examples first (e.g., identity matrix, zero matrix)
