# python-starter-2

An Introductory exercise for numerical analysis (Step 2), prepared for Sho's lecture course "[Math and Coding in Physics](https://www2.nsysu.edu.tw/iwamoto/physmath2.html)".

**Prerequisites:** Complete [python-starter-1](https://github.com/nsysu-iwamoto/python-starter-1) first for setup instructions, Git basics, and testing fundamentals.

## Requirements

You need to install [`NumPy`](https://numpy.org/) and [`SciPy`](https://scipy.org/). If you want to run tests on your laptop, you will also need [`PyTest`](https://pytest.org/) and `PyTest-Timeout`.

```bash
# commands may be python3 and pip3 on your system
python --version  # Check version >= 3.8
pip --version     # Check your pip is for correct Python version

pip install numpy scipy pytest pytest-timeout
```

## Tasks

- [ ] 5. [Basic Numerics](task05_basic.md) - Equations and series
- [ ] 6. [NumPy](task06_numpy.md) - Arrays and vector operations
- [ ] 7. [Matrix](task07_matrix.md) - Matrix operations and properties
- [ ] 8. [Newton Method](task08_newton.md) - Numerical methods

Each task includes basic problems (required) and optional problems (advanced).

## How to Work on Tasks

Open each `.md` file and follow the instructions to edit `.py` files.

You can edit `.py` files on GitHub, but it is recommended to code on your computer. Following Git/GitHub starter from python-starter-1, you are asked to:

- **clone** this repository to your computer,
- edit your files,
- **commit** your changes, and
- **push** to GitHub.

## Testing Your Code

Test system is provided on GitHub, but you can run tests on your computer if you install the tools above.

```bash
# Run all tests
python -m pytest

# Run tests for a specific task
python -m pytest tests/test_05_basic.py -v

# Include optional problems
python -m pytest --optional
```

**Note:** Test codes may have bugs - you are the first testers! Please report any issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
