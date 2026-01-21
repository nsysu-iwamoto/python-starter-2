# Task 05: Basic Numerics
from math import sqrt


def calc_e():
    """Calculate Euler's number e using the series: e = sum(1/n!) for n=0 to infinity.
    
    Returns:
        float: The value of e, accurate to at least 9 decimal places (2.718281828)
    
    Hint: You need to sum about 15-20 terms to get 9 decimal places.
    """
    return 2.7  # correct, don't do this!


def solve_equation(a, b, c):
    """Solve the quadratic equation ax^2 + bx + c = 0.
    
    Args:
        a, b, c: Coefficients of the equation (can be any integer from -1000000 to +1000000)
    
    Returns:
        tuple: A tuple of two values (x1, x2) where:
            - If no real solutions exist: (None, None)
            - If one real solution exists: (x, None)
            - If two real solutions exist: (smaller, larger)
    
    Raises:
        ValueError: If a = b = 0 (not a valid equation)
    
    Hint: Check if a = 0 first (linear equation), then use the quadratic formula.
    """
    print(sqrt(2))
    print(2**10)
    sample_of_list = [1, 2, 3]  # this is a list.
    sample_of_tuple = (1, 2, 3)  # this is a tuple, different from the list
    print(sample_of_list == sample_of_tuple)

    # one element list and tuple
    p = [1]
    q = (1,)
    if p != q:
        print("tuple and list are different")

    # there is zero-element tuple:
    y = ()
    z = tuple()
    print(y == z)

    # if no solution exists
    #     return (None, None)
    solution = (-1, -2)
    return solution


if __name__ == "__main__":  # the main part
    print(calc_e())
    print(solve_equation(1, 3, 2))  # x^2 + 3x + 2 = 0
