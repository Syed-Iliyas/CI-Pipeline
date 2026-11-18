# Screen Recording Script — CI Pipeline Basics

Target length: **3–4 minutes** (safe range 2–5). Record at 1080p, browser/terminal zoom 125%.

Repository: https://github.com/Syed-Iliyas/CI-Pipeline

---

## Before you record (2-minute setup)

- [ ] Close chat apps, email, and anything with personal notifications.
- [ ] Turn on **Do Not Disturb** (Windows: `Win + N` → Focus assist).
- [ ] Open these tabs in your browser, in this order:
  1. GitHub repo: https://github.com/Syed-Iliyas/CI-Pipeline
  2. Actions page: https://github.com/Syed-Iliyas/CI-Pipeline/actions
- [ ] Open VS Code (or File Explorer) on the project folder:
      `C:\Users\Ilyas\Desktop\CI-Pipeline-Basics`
- [ ] Open **two PowerShell windows** (or use VS Code terminal). Keep them clean.
- [ ] Test your mic and do a 10-second test recording; delete it.
- [ ] Recording shortcut: **Windows Game Bar = `Win + Alt + R`**, or press **Record** in OBS.
      OBS is recommended if you have it (cleaner, easy stop/export).

Tip: If you mess up a section, **pause recording**, redo the section, then resume — or just record the whole thing twice. Talk slowly and use short sentences.

---

## 0:00 – 0:20 — Intro (show the repo page)

**On screen:** GitHub repo homepage.

**Say:**
> "Hi, this is my CI Pipeline Basics project. It's a small Python calculator with automated tests, and a GitHub Actions pipeline that runs those tests on every push. Here's the repository, and in this video I'll show the app, the tests, the workflow file, and a real green CI run."

---

## 0:20 – 0:55 — Project structure

**On screen:** VS Code / File Explorer showing the folder tree. Expand `.github/workflows`.

**Say:**
> "The project has a calculator package with five operations, a pytest test file, a requirements file, pytest config, a README that documents everything, and a Windows launcher called run.bat. The CI workflow lives in `.github/workflows/ci.yml`."

 Briefly point at:
- `calculator/calculator.py`
- `tests/test_calculator.py`
- `requirements.txt`
- `.github/workflows/ci.yml`
- `README.md`, `run.bat`

---

## 0:55 – 1:45 — Run the app locally (interactive + arguments)

**Terminal 1 — type exactly:**

```powershell
cd C:\Users\Ilyas\Desktop\CI-Pipeline-Basics
python -m calculator.calculator
```

Then enter this input slowly so viewers can follow:

```
add
2
3
multiply
6
7
divide
10
0
quit
```

**Say:**
> "Running with no arguments starts interactive mode. It asks which operation, then two numbers. Here 2 plus 3 is 5, 6 times 7 is 42. Dividing by zero is handled with a clear error instead of crashing, and typing quit exits cleanly."

**Then in Terminal 2 (or same terminal after quit):**

```powershell
python -m calculator.calculator power 2 10
python -m calculator.calculator add 5 4
```

**Say:**
> "I can also pass the operation and numbers as command-line arguments. Two to the power of ten is 1024, and 5 plus 4 is 9. So the input is fully dynamic — nothing is hard-coded."

---

## 1:45 – 2:15 — Run the tests locally

**On screen:** terminal.

```powershell
python -m pytest -q
```

**Say:**
> "Now I run the test suite. There are 21 tests covering the math functions, edge cases like division by zero, argument parsing, and the interactive loop. All 21 pass locally."

 Point at the `21 passed` line.

 Optional: mention `run.bat` — "On Windows you can also just double-click run.bat; no virtual environment needed."

---

## 2:15 – 2:55 — The CI configuration

**On screen:** open `.github/workflows/ci.yml` in VS Code, then in GitHub ("Code" → `.github` → `workflows` → `ci.yml`).

**Say:**
> "Here is the CI configuration. The `on` block triggers the workflow on every push and pull request to main. The job runs on Ubuntu, and the matrix runs it on Python 3.10, 3.11, and 3.12. The steps check out the code, set up Python with pip caching, install requirements, and run the tests. If any step fails, the whole check is red."

 Note: "Earlier, a bare `pytest` command failed because the package wasn't on the import path. We fixed it with `python -m pytest` plus `pythonpath = .` in pytest.ini — that's why it's green now."

---

## 2:55 – 3:35 — The green pipeline run

**On screen:** switch to the GitHub **Actions** tab.

 Show run **#2** with the green check, then click into it and show the three jobs all green:
- Test on Python 3.10 ✅
- Test on Python 3.11 ✅
- Test on Python 3.12 ✅

 Expand the **Run tests** step if you want to show the pytest output.

**Say:**
> "This is the real run recorded by GitHub. My push triggered CI automatically. All three Python versions passed. Run number 1 failed earlier — that actually proves the pipeline is doing real work — and after the fix, run 2 is fully green."

---

## 3:35 – 3:55 — Wrap up

**On screen:** repo page again.

**Say:**
> "To summarize: a small calculator app with dynamic input, 21 automated tests, and a GitHub Actions pipeline that runs them on every push across three Python versions. The repository link is https://github.com/Syed-Iliyas/CI-Pipeline. The full configuration is documented in the README. Thanks for watching."

---

## After recording

- Stop recording (`Win + Alt + R` or OBS **Stop**).
- Watch it once; trim dead air at the start/end.
- Export as **MP4, 1080p**.
- Check that the file length is between 2 and 5 minutes.
- If submitting, attach the MP4 along with the repository link and the short explanation from the README.
