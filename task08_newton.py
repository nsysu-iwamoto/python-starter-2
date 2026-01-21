# Task 08: Newton Method


def fixed_point_iteration(g, x0, n):
    """Perform fixed-point iteration.
    
    Args:
        g (callable): Function to iterate
        x0 (float): Initial value
        n (int): Number of iterations
        
    Returns:
        list: Sequence [x0, x1, x2, ..., xn] of length n+1
    """
    # Example 1 in Section 19.2
    result = [x0]
    for i in range(n):
        # TODO: compute next value using g() and append to result
        result.append(i)
    return result


def newton(f, fp, x0, eps=1e-7, n=100000):
    """Find a root of f using Newton's method.
    
    Args:
        f (callable): Function to find root of
        fp (callable): Derivative of f
        x0 (float): Initial guess
        eps (float): Convergence tolerance (default: 1e-7)
        n (int): Maximum iterations (default: 100000)
        
    Returns:
        float: Approximate root, or None if no convergence
    """
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
