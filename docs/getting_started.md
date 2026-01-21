# Getting Started Guide

Welcome to the Python Self-Study Course for Physics Students (Step 2)!

This guide will help you set up your environment and start working on numerical analysis tasks.

## Prerequisites

Before starting, you should have:

1. **Python 3.11 or higher** installed on your computer
   - Check: `python --version` or `python3 --version`
   - Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. **Git** installed on your computer
   - Check: `git --version`
   - Download from: [https://git-scm.com/downloads](https://git-scm.com/downloads)

3. A **GitHub account**
   - Sign up at: [https://github.com/](https://github.com/)

4. A **text editor** or IDE
   - Recommended: [Visual Studio Code](https://code.visualstudio.com/)
   - Alternatives: PyCharm, Sublime Text, etc.

5. **Completed python-starter-1**
   - This course assumes you've completed the basic setup and tasks from python-starter-1

## Setup Steps

### Step 1: Clone the Repository

First, you need to download this repository to your computer.

1. Open your terminal (Terminal on Mac/Linux, Command Prompt or PowerShell on Windows)
2. Navigate to where you want to save the project:

   ```bash
   cd ~/Documents  # Or any folder you prefer
   ```

3. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd python-starter-2
   ```

**New to Git?** Check out our [Git Introduction Guide](git_intro.md)!

### Step 2: Install Dependencies

You need to install NumPy, SciPy, and testing tools.

#### Standard Method: Using pip (Recommended)

Most students should use this method:

```bash
# First, check your Python and pip versions
python --version  # Should be >= 3.11
pip --version     # Check it's for the correct Python version

# Install required packages (Option 1: direct install)
pip install numpy scipy pytest pytest-timeout

# Or use the requirements file (Option 2: recommended)
pip install -r requirements.txt
```

Notice, however, that this operation installs packages globally, affecting all of your Python projects.

This is generally fine for beginners, but potentially causes version conflicts in your future work. The modern standard to avoid this issue is to use `uv`.

#### Advanced Alternative: Using uv (Optional - For Motivated Students)

*⚠️ This is optional and only for students who want to learn modern tools!*

If you're interested in learning cutting-edge Python development practices, you can use `uv` for better package management. See the python-starter-1 repository for the uv guide.

### Step 3: Verify Installation

Test that everything is working:

```bash
python -m pytest --version
python -c "import numpy; print(numpy.__version__)"
python -c "import scipy; print(scipy.__version__)"
```

You should see version information for pytest, NumPy, and SciPy.

## Understanding the Project Structure

```text
python-starter-2/
├── README.md              # Overview and task list
├── docs/                  # Documentation
│   ├── getting_started.md # This file
│   └── git_intro.md       # Git introduction
├── task05_basic.md        # Task 5 instructions
├── task05_basic.py        # Your code for task 5
├── task06_numpy.md        # Task 6 instructions
├── task06_numpy.py        # Your code for task 6
├── task07_matrix.md       # Task 7 instructions
├── task07_matrix.py       # Your code for task 7
├── task08_newton.md       # Task 8 instructions
├── task08_newton.py       # Your code for task 8
├── tests/                 # Test files
│   ├── test_05_basic.py   # Tests for task 5
│   ├── test_06_numpy.py
│   ├── test_07_matrix.py
│   └── test_08_newton.py
└── pyproject.toml         # Project configuration
```

## How to Complete Tasks

### Basic Workflow

For each task (e.g., Task 05):

1. **Read the instructions**

   ```bash
   # Open task05_basic.md in your text editor
   ```

2. **Edit the Python file**

   ```bash
   # Edit task05_basic.py
   # Complete the function according to the instructions
   ```

3. **Run your code**

   ```bash
   python task05_basic.py
   ```

4. **Test your code**

   ```bash
   # Run tests for this task
   python -m pytest tests/test_05_basic.py -v
   ```

5. **Commit your changes**

   ```bash
   git add task05_basic.py
   git commit -m "Complete task 05: basic numerics"
   ```

6. **Push to GitHub**

   ```bash
   git push
   ```

### Testing Your Work

#### What are Tests?

**Tests** are automated programs that check if your code works correctly. Think of them as:

- A teacher checking your homework automatically
- A way to verify your functions produce the expected output
- Instant feedback on whether your solution is correct

When you run tests, the testing system:

1. Calls your functions with specific inputs
2. Checks if the output matches what's expected
3. Reports whether each test passed or failed

#### Run all tests

```bash
python -m pytest
```

#### Run tests for a specific task

```bash
python -m pytest tests/test_05_basic.py -v
```

The `-v` flag means "verbose" and shows more details about each test.

#### Run tests including optional problems

```bash
python -m pytest --optional
```

By default, tests for optional problems are skipped. Use this flag to test them.

#### Understanding test output

- ✅ **PASSED**: Your code works correctly!
- ❌ **FAILED**: Something is wrong. Read the error message carefully.
- **⊘ SKIPPED**: Test was not run (e.g., optional problems without --optional flag)

Example output:

```text
tests/test_05_basic.py::test_solve_equation_basic PASSED     [ 25%]
tests/test_05_basic.py::test_solve_equation_one_root PASSED  [ 50%]
tests/test_05_basic.py::test_calc_e FAILED                   [ 75%]
```

This shows:
- 2 tests passed ✅
- 1 test failed ❌
- Your `calc_e()` function needs fixing

#### How to read test failures

When a test fails, you'll see helpful information:

```text
FAILED tests/test_05_basic.py::test_calc_e - AssertionError: ...
Expected: 2.718281828
Got:      2.718281
```

This tells you:
- Which test failed
- What was expected
- What your code actually returned

## Working on Tasks

### Task Order

We recommend completing tasks in order:

1. **Task 05: Basic Numerics** - Equations and series
2. **Task 06: NumPy** - Arrays and vector operations
3. **Task 07: Matrix** - Matrix operations and properties
4. **Task 08: Newton Method** - Numerical methods

### Optional Problems

Each task has optional (advanced) problems marked as "(optional)".

- These are **challenging** and not required
- Only attempt them if you have completed the basic task
- Great for learning more advanced concepts!

## Tips for Success

### 1. Don't Copy-Paste Solutions

Type every character by yourself, which makes your English typing faster!

(If you do copy-and-paste, you won't learn anything! Doing this task is just a waste of time!)

### 2. Read Error Messages Carefully

Error messages tell you what went wrong. Don't ignore them!

### 3. Test Frequently

Test your code often, not just at the end.

### 4. Use Print Statements for Debugging

```python
print(f"Debug: x = {x}")  # See what values variables have
```

### 5. Read Documentation

- NumPy docs: [https://numpy.org/doc/stable/](https://numpy.org/doc/stable/)
- SciPy docs: [https://scipy.org/](https://scipy.org/)
- Python tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)

## Common Issues and Solutions

### "ModuleNotFoundError: No module named 'numpy'"

**Solution**: Install dependencies (see Step 2 above)

### "ModuleNotFoundError: No module named 'pytest'"

**Solution**: Install pytest (see Step 2 above)

### "python: command not found"

**Solution**: Try `python3` instead, or install Python

### Tests are failing but my code looks correct

**Solution**:

- Read the test output carefully
- Check for typos in function names
- Make sure you're returning the expected format (tuple, list, etc.)
- Try running your code manually to see the output
- Check if your function handles edge cases correctly

### "Permission denied" when pushing to GitHub

**Solution**: Set up GitHub authentication

- Use HTTPS with a personal access token, or
- Use SSH keys
- See: [https://docs.github.com/en/authentication](https://docs.github.com/en/authentication)

## Getting Help

If you're stuck:

1. Read the error message carefully
2. Check the documentation in this folder
3. Ask your instructor or classmates
4. Search online for Python/NumPy concepts you don't understand

## Next Steps

Ready to start? Great!

1. ✅ Complete the setup steps above
2. ✅ Open `task05_basic.md`
3. ✅ Start coding!

**Good luck!** 🚀

---

## Additional Resources

- [Git Introduction](git_intro.md) - Learn Git basics
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [SciPy Documentation](https://scipy.org/)
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python - NumPy Tutorial](https://realpython.com/numpy-tutorial/)
