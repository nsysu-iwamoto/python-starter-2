# Task 08: Newton Method

**Goal:** Implement numerical methods for finding roots of equations

## Overview

In Section 19.2 of Kreyszig, methods for numerical calculations are introduced.
First, see (!= read) that section. You will find a few examples. It is important to implement them when you read the textbook.

In this task, you'll learn:

- How to implement iterative methods for solving equations
- How to implement the Newton method
- How to pass functions as arguments to other functions
- How to handle convergence and stopping criteria

Open `task08_newton.py` and edit the file to do the following tasks.

### Understanding Functions as Arguments

In Python, functions are "first-class objects", meaning you can:

- Assign functions to variables
- Pass functions as arguments to other functions
- Return functions from other functions

Example:

```python
def square(x):
    return x * x

def apply_twice(f, x):
    return f(f(x))

result = apply_twice(square, 3)  # Returns 81 (= (3²)²)
```

## Task 08a (Required)

Example 1 demonstrates an iterative method for calculating solutions of $x^2 - 3x + 1 = 0$.

The textbook says that this equation can be solved by Eq. (4a) and shows a sequence `1.0, 0.667, 0.481, 0.411, 0.390, ...`.
So, let us reproduce this sequence.

Complete the function `fixed_point_iteration(g, x0, n)` and reproduce the sequences in Example 1.

Namely, the following code should print-out `[1.0, 0.6666666666666666, 0.48148148148148145]`.

```python
def g(x):
    return (x * x + 1) / 3

print(fixed_point_iteration(g, 1.0, 2))
```

- **Input**:
  - `g` is a function that receives a float and returns a float. *Yes, we can assign not only a number but also a function to a variable!*
  - `x0` is the initial value (float).
  - `n` is the number of iterations (int).
- **Output**: a list of n+1 floats. The first element is x0. The last element is xn.

**Example:**
```python
def g(x):
    return (x * x + 1) / 3

result = fixed_point_iteration(g, 1.0, 5)
# Should return [1.0, 0.667..., 0.481..., 0.411..., 0.390..., 0.380...]
```

<details>
<summary>Click to see hint</summary>

The fixed-point iteration formula is:

$$x_{n+1} = g(x_n)$$

Starting from $x_0$, repeatedly apply $g$ to get the sequence.

Build the sequence iteratively:

```python
def fixed_point_iteration(g, x0, n):
    sequence = [x0]
    x = x0
    for i in range(n):
        x = g(x)  # Apply function g
        sequence.append(x)
    return sequence
```

</details>

## Task 08b (Required)

Table 19.1 summarizes the Newton method. According to the table, the method should receive the following inputs:

- a function `f`,
- its derivative `fp` (standing for f prime),
- the initial value `x0`,
- the error tolerance `eps`, and
- the maximum number of iterations `n`.

and return x_(n+1) if the method converges. If it does not converge, it should stop.

*(Notice again that we can assign a function to a variable `f` and pass it to another function `newton`.)*

Now, let us implement the Newton method, starting from the skeleton `newton(f, fp, x0, eps=1e-7, n=100000)` in the file.
Our function should return the solution (if converges) or `None` (if it stops).

Namely, according to Example 3, the following code should print out the square-root of 5.

```python
def f0(x):
    return x * x - 5

def f1(x):
    return 2 * x

x0 = 2.0
solution = newton(f0, f1, x0)
print(solution)
```

**Following the algorithm given in Table 19.1**, complete the function `newton(f, fp, x0, eps=1e-7, n=100000)`, where you need to follow the specification.

- **Input**: aforementioned `f`, `fp`, `x0` (int/float), `eps` (float), and `n` (int).
- **Output**: a floating-point number or `None`.

**Example:**
```python
def f(x):
    return x * x - 2

def fp(x):
    return 2 * x

result = newton(f, fp, 1.0)  # Find sqrt(2)
# Should return approximately 1.414213562373095
```

## Task 08c (Optional)

Calculate the solution of $x^3 + 2x + 2 = 0$ (we know it has only one solution) by using your `newton` function.

<details>
<summary>Click to see hint</summary>

Define the function and its derivative:

```python
def f(x):
    return x**3 + 2*x + 2

def fp(x):
    return 3*x**2 + 2

solution = newton(f, fp, x0=0.0)
```

Try different initial values to see if it converges.

</details>

## Task 08d (Optional, Advanced)

Calculate the solution of $x^3 - 2x + 2 = 0$ (we know it has only one solution) by using your `newton` function.

What happens if you use `x0 = 1.0` as the initial value? Describe what happens and explain why.

<details>
<summary>Click to see hint</summary>

Consider:

- What is $f'(1.0)$?
- What happens in the Newton iteration when $f'(x)$ is very small?
- Can the method get stuck in a cycle or diverge?

</details>

## Common Mistakes

1. **Not checking for division by zero**
   - ❌ `x_new = x - f(x) / fp(x)` without checking if `fp(x) == 0`
   - ✅ Check if `fp(x) == 0` and return `None` if true

2. **Wrong convergence check**
   - ❌ Checking if `abs(f(x)) < eps` (checking function value)
   - ✅ Checking if `abs(x_new - x) < eps` (checking change in x)

3. **Not handling non-convergence**
   - ❌ Infinite loop or error when method doesn't converge
   - ✅ Return `None` after max iterations

4. **Wrong sequence length**
   - ❌ For `fixed_point_iteration`, returning n elements instead of n+1
   - ✅ Include the initial value x0 in the sequence

## Need Help?

- Read Section 19.2 of Kreyszig textbook carefully
- Find some online resources on geometric interpretation of Newton's method
- Test with simple examples first (e.g., finding $\sqrt{2}$ by solving $x^2 - 2 = 0$)
