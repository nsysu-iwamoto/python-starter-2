# Contributing to Python Starter 2

Thank you for working through these exercises!

## How to Submit Your Solutions

### Option 1: Fork and Pull Request (Recommended)

1. **Fork this repository** to your GitHub account
2. **Clone your fork** to your computer:
   ```bash
   git clone https://github.com/YOUR-USERNAME/python-starter-2.git
   cd python-starter-2
   ```
3. **Install dependencies**:
   ```bash
   pip install numpy scipy pytest pytest-timeout
   ```
4. **Work on the tasks** - edit the `task*.py` files
5. **Test your solutions**:
   ```bash
   python -m pytest tests/
   ```
6. **Commit your changes**:
   ```bash
   git add task*.py
   git commit -m "Complete Task 05: Basic Numerics"
   git push
   ```
7. **Create a Pull Request** from your fork to submit your work

### Option 2: Direct Submission

If you're not comfortable with Git yet:
1. Complete the exercises locally
2. Run the tests to verify your solutions
3. Email your completed `task*.py` files to your instructor

## Testing Your Code

### Run all tests:
```bash
python -m pytest tests/
```

### Run tests for a specific task:
```bash
python -m pytest tests/test_05_basic.py -v
```

### Run only required tests (skip optional):
```bash
python -m pytest tests/ -m "not optional"
```

## Code Style

We use `ruff` for code quality. Check your code with:
```bash
ruff check .
```

Don't worry too much about style at first - focus on making the tests pass!

## Getting Help

- **Read the task descriptions** in the `task*.md` files carefully
- **Check the hints** in the markdown files (click "Show Hint")
- **Look at the tests** in `tests/` to understand what's expected
- **Ask your instructor** if you're stuck

## What to Expect

- ✅ All required tests should pass before submission
- ✅ Optional tests are for extra learning (not required)
- ✅ Your code should follow the function signatures in the task files
- ⚠️ Don't modify the test files
- ⚠️ Don't modify the markdown documentation

## Learning Tips

1. **Start with Task 05** and work sequentially
2. **Run tests frequently** to get immediate feedback
3. **Read error messages carefully** - they tell you what's wrong
4. **Try the examples** in the Python interactive shell first
5. **Ask questions** when concepts are unclear

Happy coding! 🎉
