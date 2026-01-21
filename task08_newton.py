# Task 08: Newton Method


def fixed_point_iteration(g, x0, n):
    """Perform fixed-point iteration: x_{i+1} = g(x_i)
    
    Args:
        g: A function that takes a float and returns a float
        x0: Initial value (float)
        n: Number of iterations (int)
    
    Returns:
        list: A list of (n+1) values [x0, x1, x2, ..., xn]
    
    Example:
        def g(x): return (x*x + 1) / 3
        fixed_point_iteration(g, 1.0, 2) returns [1.0, 0.666..., 0.481...]
    
    Hint: Start with [x0], then repeatedly apply g and append results
    """
    # Example 1 in Section 19.2
    print("g(0) is...", g(0))  # these lines are just for fun.
    print("g(1) is...", g(1))  # remove these
    print("g(2) is...", g(2))  # lines.
    result = [0]
    for i in range(n):
        result.append(i)
    return result


def newton(f, fp, x0, eps=1e-7, n=100000):
    """Implement Newton's method for finding roots of f(x) = 0.
    
    Args:
        f: The function f(x)
        fp: The derivative f'(x)
        x0: Initial guess (float)
        eps: Convergence tolerance (default 1e-7)
        n: Maximum number of iterations (default 100000)
    
    Returns:
        float: The root if found, or None if method fails to converge
    
    Algorithm (from Table 19.1):
        For i = 0, 1, ..., n-1:
            1. Compute f'(x_i)
            2. If f'(x_i) = 0, return None (division by zero)
            3. Compute x_{i+1} = x_i - f(x_i) / f'(x_i)
            4. If |x_{i+1} - x_i| < eps, return x_{i+1} (converged!)
            5. Otherwise, continue with x_{i+1}
        If no convergence after n iterations, return None
    
    Example:
        def f(x): return x*x - 2
        def fp(x): return 2*x
        newton(f, fp, 1.0) returns approximately 1.41421356... (sqrt(2))
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
