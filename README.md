# python-starter-2

Introduction to Numerical Analysis

## Requirements

You need to install [`NumPy`](https://numpy.org/) and [`SciPy`](https://scipy.org/). Furthermore, if you want to run "test codes" on your laptop, you will need [`PyTest`](https://pytest.org/) and `PyTest-Timeout`. They can be installed using `pip` (using a virtual environment is recommended but optional):

```bash
# commands may be python3 and pip3 on your system,
python --version  # Check version >= 3.8
pip --version     # Check your pip is for correct Python version

pip install numpy scipy
pip install pytest pytest-timeout
```

## How to run test codes

Try `python -m pytest` on the root directory of this repository (i.e., where this file is).

If you want to run a specific test file, you can use `python -m pytest -k tests/test_file_name.py`.
