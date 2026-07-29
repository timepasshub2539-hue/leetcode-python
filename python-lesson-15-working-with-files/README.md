# Python File Handling: `with`, Modes, and `pathlib`

## Problem

Opening a file manually with `open()` requires you to remember to call
`.close()` yourself. If an exception occurs between opening and closing,
the close call never runs — leaking the file handle and, in write scenarios,
risking unflushed or corrupted data.

## Intuition

A context manager (`with`) ties resource cleanup to block scope instead of
to a human remembering a line of code. It behaves like a librarian who
automatically checks a book back in the moment you leave, regardless of
whether you left calmly or got yanked out by a fire alarm (an exception).

## Approach

1. Always open files using `with open(path, mode) as f:` — never manual
   `open()`/`close()` pairs.
2. Choose the mode deliberately: `"r"` read, `"w"` overwrite (destructive),
   `"a"` append.
3. Stream large files line by line (`for line in f`) instead of `.read()`-ing
   everything into memory.
4. Build paths with `pathlib.Path` and the `/` join operator instead of
   string concatenation, for cross-platform correctness.

## Python Solution

```python
from pathlib import Path


def write_note(folder: str, filename: str, text: str) -> Path:
    """Append a line of text to a note file, creating the folder if needed."""
    dir_path = Path(folder)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / filename

    with open(file_path, "a") as f:
        f.write(text + "\n")

    return file_path


def read_notes(file_path: Path) -> list[str]:
    """Read all lines from a note file, stripped of trailing newlines."""
    if not file_path.exists():
        return []

    with open(file_path, "r") as f:
        return [line.strip() for line in f]
```

## Complexity

- **Time:** O(n) in the size of data written or read.
- **Space:** O(1) for streaming writes; O(n) for `read_notes`, since it
  materializes every line into a list.

## Video

Full walkthrough with live coding: (video link coming soon)

## Article

Full write-up with intuition, dry runs, and common mistakes: see the
accompanying article in this repo / linked in the video description.
