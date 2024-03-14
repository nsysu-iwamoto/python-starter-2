# Task 07: Newton Method


def fixed_point_iteration(g, x0, n):
    # Example 1 in Section 19.2
    print("g(0) is...", g(0))  # these lines are just for fun.
    print("g(1) is...", g(1))  # remove these
    print("g(2) is...", g(2))  # lines.
    result = [0]
    for i in range(n):
        result.append(i)
    return result


def newton(f, fp, x0, eps=1e-7, n=100000):
    # for n = 0, ..., n-1, do
    #     compute fp(xn)
    #     if it is zero, then
    #         return None
    #     compute ...
    #     if good convergence,
    #          return x_(n+1)
    #     otherwise repeat.
    #
    # if no convergence after n steps
    return None


if __name__ == "__main__":

    def g(x):
        return (x * x + 1) / 3

    print(fixed_point_iteration(g, 1.0, 2))  # should print out a sequence [1, 0.6, 0.5]

    def f0(x):
        return x * x - 5

    def f1(x):
        return 2 * x

    x0 = 2.0
    solution = newton(f0, f1, x0)
    print(solution)  # should print out sqrt(5)
