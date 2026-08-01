# Why pip install Breaks Your Other Project (And How venv Fixes It)

## Problem

Two Python projects on the same machine, sharing one global package
installation. Each needs a different version of the same package.
Installing one silently breaks the other, with no clear error pointing
at the real cause.

## Intuition

Your shell resolves `python` and `pip` by searching folders listed in
`PATH`, in order, and running the first match. A virtual environment
is a folder containing its own interpreter and package directory;
activating it puts that folder first in `PATH`. Same commands,
different program running underneath — full isolation with zero
changes to your code.

## Approach

1. Create an isolated environment per project: `python -m venv .venv`
2. Activate it so `python`/`pip` resolve to the private copy:
   - macOS/Linux: `source .venv/bin/activate`
   - Windows: `.venv\Scripts\activate`
3. Install packages — they land inside `.venv` only:
   `pip install <package>`
4. Freeze exact versions for reproducibility:
   `pip freeze > requirements.txt`
5. Teammates rebuild the exact same environment:
   `pip install -r requirements.txt`
6. `.gitignore` the `.venv` folder. Commit only `requirements.txt`.

## Python Solution

```python
"""setup_env.py — bootstrap an isolated environment for this project."""

import subprocess
import sys
from pathlib import Path

VENV_DIR = Path(".venv")
REQUIREMENTS_FILE = Path("requirements.txt")


def create_virtualenv() -> None:
    if VENV_DIR.exists():
        print(f"{VENV_DIR} already exists, skipping creation.")
        return
    subprocess.run([sys.executable, "-m", "venv", str(VENV_DIR)], check=True)
    print(f"Created virtual environment at {VENV_DIR}")


def venv_pip_path() -> Path:
    if sys.platform.startswith("win"):
        return VENV_DIR / "Scripts" / "pip.exe"
    return VENV_DIR / "bin" / "pip"


def install_requirements() -> None:
    if not REQUIREMENTS_FILE.exists():
        print("No requirements.txt found, nothing to install.")
        return
    subprocess.run(
        [str(venv_pip_path()), "install", "-r", str(REQUIREMENTS_FILE)],
        check=True,
    )
    print("Installed dependencies from requirements.txt")


if __name__ == "__main__":
    create_virtualenv()
    install_requirements()
```

## Complexity

- **Time:** O(n) in number of packages installed — each is downloaded
  and unpacked independently.
- **Space:** O(p × v) across v venvs with p average packages each —
  the deliberate cost of true isolation versus one shared install.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with diagrams, dry run, and common mistakes:
see the companion article in this repo / linked from the video
description.
