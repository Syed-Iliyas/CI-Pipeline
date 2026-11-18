# CI Pipeline Basics

A tiny Python project that demonstrates a basic Continuous Integration (CI)
pipeline using **GitHub Actions**. Every push and pull request to `main`
automatically runs the test suite.

## Project contents

- `calculator/calculator.py` — a small calculator module (`add`, `subtract`,
  `multiply`, `divide`, `power`).
- `tests/test_calculator.py` — pytest unit tests covering normal cases, edge
  cases, and error handling (division by zero).
- `.github/workflows/ci.yml` — the GitHub Actions workflow that runs the tests.
- `requirements.txt` — Python dependencies (`pytest`).
- `pytest.ini` — pytest configuration.

## Run locally

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Run the tests
pytest

# 4. (Optional) run the demo app
python -m calculator.calculator
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
      - run: pytest -q                     # run the test suite
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
