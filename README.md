# python-starter-2

An Introductory exercise for numerical analysis (Step 2), prepared for Sho's lecture course "[Math and Coding in Physics](https://www2.nsysu.edu.tw/iwamoto/physmath2.html)".

## 🚀 Quick Start

**New to this course? Start here!**

👉 **[Getting Started Guide](docs/getting_started.md)** - Complete setup instructions

**Already completed python-starter-1?** Great! This is the next step. If not, please complete python-starter-1 first.

### Essential Guides

- 📚 [Getting Started Guide](docs/getting_started.md) - Setup and how to complete tasks
- 🔧 [Git Introduction](docs/git_intro.md) - Learn Git basics

## Tasks

- [ ] 5. [Basic Numerics](task05_basic.md) - Equations and series
- [ ] 6. [NumPy](task06_numpy.md) - Arrays and vector operations
- [ ] 7. [Matrix](task07_matrix.md) - Matrix operations and properties
- [ ] 8. [Newton Method](task08_newton.md) - Numerical methods

Each task includes:

- Basic problems (required)
- Optional problems (advanced, for extra learning)

## How to Work on Tasks

### Method 1: Edit on GitHub (Simplest)

You can edit `.py` files directly on GitHub through your web browser.

### Method 2: Work on Your Computer (Recommended)

**This is the recommended approach for learning Git and proper development workflow.**

1. **Clone** this repository to your computer
2. **Edit** files on your computer
3. **Test** your code locally
4. **Commit** your changes
5. **Push** to GitHub

See the [Getting Started Guide](docs/getting_started.md) for detailed instructions.

## Requirements

You need to install [`NumPy`](https://numpy.org/) and [`SciPy`](https://scipy.org/). Furthermore, if you want to run "test codes" on your laptop, you will need [`PyTest`](https://pytest.org/) and `PyTest-Timeout`. They can be installed using `pip`:

```bash
# commands may be python3 and pip3 on your system,
python --version  # Check version >= 3.8
pip --version     # Check your pip is for correct Python version

pip install numpy scipy pytest pytest-timeout
```

Detailed setup instructions are provided in [Getting Started Guide](docs/getting_started.md).

## Testing Your Code

You may "test" your code automatically. Test system is provided on the GitHub, but you can run the tests on your computer if you install some tools.

### What are Tests?

**Tests** are automated programs that check if your code works correctly. Think of them as a teacher checking your homework automatically! See the [Getting Started Guide](docs/getting_started.md) for more details on how tests work.

### Running Tests

```bash
# Run all tests
python -m pytest

# Run tests for a specific task
python -m pytest tests/test_05_basic.py -v

# Include optional problems
python -m pytest --optional
```

**Note:** Test codes may have bugs - you are the first testers! Please report any issues.

## Getting Help

1. Read the documentation in the [`docs/`](docs/) folder
2. Check error messages carefully
3. Ask your instructor or classmates
4. Search online for Python/NumPy concepts

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
