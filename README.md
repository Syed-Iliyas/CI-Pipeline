# CI Pipeline Basics

A tiny Python project that demonstrates a basic Continuous Integration (CI)
pipeline using **GitHub Actions**. Every push and pull request to `main`
automatically runs the test suite.

## Project contents

- `calculator/calculator.py` — a calculator module (`add`, `subtract`,
  `multiply`, `divide`, `power`) with a dynamic CLI: command-line arguments
  or an interactive prompt.
- `tests/test_calculator.py` — pytest unit tests covering normal cases, edge
  cases, error handling, the CLI, and interactive mode.
- `.github/workflows/ci.yml` — the GitHub Actions workflow that runs the tests.
- `requirements.txt` — Python dependencies (`pytest`).
- `pytest.ini` — pytest configuration.

## Run locally

A virtual environment is **optional** — if `pytest` is already installed in
your Python, you can skip straight to running the app/tests.

**Easiest on Windows:** double-click `run.bat` in this folder. It starts the
interactive calculator using your normal Python (no activation needed). You can
also pass arguments: `run.bat add 2 3`.

**Using a terminal** (from this folder):

```bash
# 1. Install dependencies once (skip if pytest is already installed)
python -m pip install -r requirements.txt

# 2. Run the tests
python -m pytest

# 3. Run the calculator (see "Using the calculator" below)
python -m calculator.calculator
```

If you do want an isolated environment, these optional steps work too:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Using the calculator

The calculator takes input dynamically — you don't hard-code anything.

### Option A: Interactive mode (run with no arguments)

```bash
python -m calculator.calculator
```

It prompts you in a loop until you type `quit`:

```
Interactive calculator. Available operations: add, subtract, multiply, divide, power.
Type 'quit' (or 'q' / 'exit') to stop.

Operation [add, subtract, multiply, divide, power]: add
First number:  2
Second number: 3
Result: 5

Operation [add, subtract, multiply, divide, power]: quit
Goodbye!
```

Invalid numbers and unknown operations are handled gracefully, so you can
keep trying without the program crashing.

### Option B: Command-line arguments

```bash
python -m calculator.calculator add 2 3        # Result: 5
python -m calculator.calculator multiply 4 7   # Result: 28
python -m calculator.calculator power 2 8      # Result: 256
```

Operation names are case-insensitive (`ADD`, `Add`, and `add` all work).
Errors are reported clearly, e.g. dividing by zero:

```
python -m calculator.calculator divide 10 0
# error: argument: Cannot divide by zero
```

### Option C: Import it in your own Python code

```python
from calculator import add, divide

print(add(2, 3))      # 5
print(divide(10, 2))  # 5.0
```

## CI pipeline configuration explained

The workflow file is `.github/workflows/ci.yml`. Here is what each part does:

```yaml
name: CI

on:
  push:
    branches: [main]        # trigger on pushes to main
  pull_request:
    branches: [main]        # trigger on PRs targeting main

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4          # fetch the repository code
      - uses: actions/setup-python@v5      # install the chosen Python version
        with:
          python-version: ${{ matrix.python-version }}
          cache: pip                       # cache downloaded packages
      - run: python -m pip install -r requirements.txt
      - run: python -m pytest -q           # run the test suite
```

Key ideas:

1. **Triggers (`on`)** — the workflow runs on every `push` and `pull_request`
   to `main`, so broken code is caught as soon as it is proposed or merged.
2. **Job** — a single job named `test` runs on a fresh Ubuntu runner provided
   by GitHub.
3. **Matrix strategy** — the same job runs three times, once per Python
   version in the matrix. `fail-fast: false` lets all versions finish so you
   see the full result.
4. **Steps** — check out the code, set up Python (with pip caching for speed),
   install dependencies, and run `pytest`.
5. **Result** — if any test fails in any matrix job, the overall CI check is
   red and the pull request is blocked from merging (if branch protection is
   enabled).

The `tests` now also cover the dynamic CLI (argument parsing, error handling,
and the interactive loop), so CI verifies both the math and the input flow.

## How to publish this project

```bash
# From this folder:
git init
git add .
git commit -m "Initial commit: calculator app with CI pipeline"

# Create an empty repository on GitHub, then:
git remote add origin https://github.com/<your-username>/ci-pipeline-basics.git
git branch -M main
git push -u origin main
```

After pushing, open the repo on GitHub and click the **Actions** tab to see
the workflow run. The repository URL is the link you submit.
