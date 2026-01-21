# python-starter-2

An Introductory exercise for numerical analysis (Step 2), prepared for Sho's lecture course "[Math and Coding in Physics](https://www2.nsysu.edu.tw/iwamoto/physmath2.html)".

Prerequisites: Complete **Python Starter 1** first for setup instructions, Git basics, and Python fundamentals.

## Requirements

You need to install [`NumPy`](https://numpy.org/) and [`SciPy`](https://scipy.org/).

```bash
# commands may be python3 and pip3 on your system
python --version  # Check version >= 3.11
pip --version     # Check your pip is for correct Python version

pip install numpy scipy
```

Motivated student who uses [`uv`](https://docs.astral.sh/uv/) can install all the required packages by one command:

```bash
uv sync
```

See Documents in Python Starter 1 for further information.

## Tasks

- [ ] 5. [Basic Numerics](task05_basic.md) - Equations and series
- [ ] 6. [NumPy](task06_numpy.md) - Arrays and vector operations
- [ ] 7. [Matrix](task07_matrix.md) - Matrix operations and properties
- [ ] 8. [Newton Method](task08_newton.md) - Your first numerical method

Each task includes:

- Basic problems (required)
- Optional problems (advanced, for extra learning)

## Getting Started

1. **Check Prerequisites**: You should have completed Python Starter 1 first
2. **Install dependencies**: See Requirements section above
3. **Start with Task 05**: Work through tasks in order
4. **Test your code**: Run `python -m pytest tests/` to check your solutions
5. **Submit your work**: See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions

## Troubleshooting

### Common Issues

**Import Error: No module named 'numpy'**
```bash
# Make sure you installed the packages:
pip install numpy scipy pytest pytest-timeout
```

**Tests fail with floating-point differences**
- This is normal! Small differences like `2.99999999` vs `3.0` happen in numerical computing
- Our tests use `pytest.approx()` to handle this automatically
- Read the error message to see if the difference is acceptable

**Function not found errors**
- Make sure your function name exactly matches what's in the instructions
- Check spelling and capitalization (Python is case-sensitive)

**Getting stuck on a task?**
1. Read the task markdown file (`task*.md`) completely
2. Check the hints (expand the "Show Hint" sections)
3. Look at the test file to see what's expected
4. Try breaking the problem into smaller steps
5. Ask your instructor for help

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
