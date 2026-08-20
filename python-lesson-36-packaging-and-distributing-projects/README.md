# textutils

Small text formatting helpers, packaged the right way — installable with a
single `pip install`, no manual dependency chasing required.

## Problem

A folder of loose `.py` files works locally by accident: your imports resolve
because of your working directory, and your dependencies are already
installed because you installed them once and forgot. None of that travels
with the code, so anyone else who tries to run it hits `ModuleNotFoundError`
or broken imports.

## Intuition

Packaging just means writing down, in a format every tool can read, the two
things that were previously invisible: what this code is called and needs
(`pyproject.toml`), and where it actually lives relative to everything else
(a `src/` layout, so tests exercise the installed package instead of local
files by accident).

## Approach

1. Declare `name`, `version`, and `dependencies` in `pyproject.toml`.
2. Put importable code under `src/textutils/`, tests under `tests/`.
3. Build a wheel: `python -m build`.
4. Verify on TestPyPI before publishing for real — PyPI never allows
   overwriting a taken name or a published version.
5. Publish: `twine upload dist/*`.

## Python Solution

```python
# src/textutils/core.py
def title_case(text: str) -> str:
    """Return text with each word capitalized."""
    return " ".join(word.capitalize() for word in text.split())
```

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[project]
name = "textutils-yourname"
version = "0.1.0"
dependencies = ["python-dateutil>=2.8"]

[tool.setuptools.packages.find]
where = ["src"]
```

## Complexity

Not an algorithmic problem — the relevant cost is operational: build time
scales with project size (trivial for small packages), and the real
constraint is irreversibility, not runtime. Names and versions on PyPI can't
be undone once published, which is why TestPyPI exists in the workflow.

## Install

```bash
pip install textutils-yourname
```

## Video

Full walkthrough: (video link coming soon)

## Article

Written breakdown with the full build-and-publish flow: (video link coming soon)
