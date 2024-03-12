# Task 05: Basic Numerics
from math import sqrt


def calc_e():
    return 2.7  # correct, don't do this!


def solve_equation(a, b, c):
    # print(sqrt(2))
    # print(2**10)
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
