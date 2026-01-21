# Task 05: Basic Numerics

**Goal:** Learn to solve mathematical problems with numerical methods in Python

## Overview

In this task, you'll learn:

- How to solve quadratic equations programmatically
- How to calculate mathematical constants using series
- How to handle special cases and edge conditions
- How to work with tuples for multiple return values

Open `task05_basic.py` and edit the file to do the following tasks.

## Task 05a (Required)

A function `solve_equation(a, b, c)` should solve the equation $ax^2+bx+c=0$. Fix the code.

### Specifications

- **Input**: three `int` numbers. From -1000000 to +1000000. All can be zero.
- **Output**: a `tuple` of two numbers.
  - If a = b = 0, you need to `raise ValueError`.
  - If the equation has only one real solution, the second element should be `None`. For example, `(1, None)` for $x^2-2x+1=0$.
  - If the equation has no real solution, both elements should be `None`. For example, `(None, None)` for $x^2+1=0$.
  - Otherwise, the first element should be the smaller solution and the second element should be the larger solution.

### Important Notes

Notice the difference between **tuples** and **lists**:

- Tuples use parentheses: `(1, 2)` and are immutable
- Lists use brackets: `[1, 2]` and are mutable

<details>
<summary>Click to see hint 1</summary>

For a quadratic equation $ax^2+bx+c=0$:

- If $a = 0$, it's a linear equation: $bx + c = 0$
- If $a \neq 0$, use the quadratic formula: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$

</details>

<details>
<summary>Click to see hint 2</summary>

The discriminant $\Delta = b^2 - 4ac$ tells you:

- $\Delta > 0$: Two real solutions
- $\Delta = 0$: One real solution
- $\Delta < 0$: No real solutions

</details>

<details>
<summary>Click to see hint 3</summary>

Use Python's `math.sqrt()` for square roots:

```python
import math
result = math.sqrt(value)
```

</details>

## Task 05b (Required)

The Euler's number [can be obtained by](https://en.wikipedia.org/wiki/E_(mathematical_constant)) the following series:

$$ e = \sum_{n=0}^{\infty} \frac{1}{n!}$$

Namely, `1 + 1 + 1/2 + 1/6 + 1/24 + 1/120 + ....`.

Make a function `calc_e()` to calculate `e` by this method, at least up to 9-th digit `2.718281828`.

### Specifications

- **Input**: None
- **Output**: a float representing the value of $e$, accurate to at least 9 decimal places

<details>
<summary>Click to see hint 1</summary>

You'll need to:

1. Calculate factorials: $n! = 1 \times 2 \times 3 \times ... \times n$
2. Sum up the series: $\frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + ...$

</details>

<details>
<summary>Click to see hint 2</summary>

You can calculate factorial and the sum in the same loop:

```python
factorial = 1
e = 1.0  # Start with 1/0! = 1
for n in range(1, some_number):
    factorial *= n  # Update factorial
    e += 1.0 / factorial  # Add 1/n!
```

</details>

<details>
<summary>Click to see hint 3</summary>

How many terms do you need? Try different values and check the result:

- For 9 decimal places, you'll need around 15-20 terms

</details>

## Task 05c (Optional)

Rewrite `solve_equation(a, b, c)` (Task 05a) with taking care of the **cancellation problem**. Now the input values can be float.

### What is the Cancellation Problem?

When subtracting two nearly equal numbers in floating-point arithmetic, you lose precision. For example, if $b$ is large and $\sqrt{b^2-4ac} \approx |b|$, then $-b + \sqrt{b^2-4ac}$ suffers from cancellation.

<details>
<summary>Click to see hint</summary>

Use the formula:

$$x_1 = \frac{-b - \text{sign}(b)\sqrt{b^2-4ac}}{2a}, \quad x_2 = \frac{c}{ax_1}$$

This avoids catastrophic cancellation.

</details>

## Task 05d (Optional)

Rewrite `calc_e()` (Task 05b) to calculate `e` as precise as possible.

<details>
<summary>Click to see hint</summary>

Think about:

- How many terms should you sum to get the maximum precision?
- What limits the precision in floating-point arithmetic?

</details>

## Task 05e (Optional, Advanced)

This is not a coding problem. Explain how many terms you should sum up to get `e` up to `p`-th digit. Explain what is the optimal choice of `n` for Task 05d under the assumption we use IEEE754 64bit (double precision) floating point numbers.

---

## Common Mistakes

1. **Returning a list instead of a tuple**
   - ❌ `return [x1, x2]`
   - ✅ `return (x1, x2)`

2. **Not handling special cases**
   - ❌ Forgetting to check if $a = 0$ (linear equation)
   - ✅ Check all edge cases: $a=0$, $\Delta < 0$, etc.

3. **Wrong order of solutions**
   - ❌ Returning larger solution first
   - ✅ Return smaller solution first: `(min(x1, x2), max(x1, x2))`

4. **Incorrect factorial calculation**
   - ❌ Recalculating factorial from scratch each time
   - ✅ Update factorial in the loop: `factorial *= n`

---

## Need Help?

- Review Python's `math` module documentation
- Understand the quadratic formula and discriminant
- Test with simple examples first (e.g., $x^2 - 1 = 0$)
- See the [python-starter-1](https://github.com/nsysu-iwamoto/python-starter-1) for setup and testing help
