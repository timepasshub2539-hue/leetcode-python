# Python Modules & Imports: greetings.py Example

A minimal, working example demonstrating Python modules, all three import
styles, the `if __name__ == "__main__":` guard, and packages via `__init__.py`.

## Problem

Copy-pasting the same function into multiple files means every bug fix has
to be applied everywhere the function was pasted — and nothing enforces that
you remember to do it. This project shows the alternative: write it once,
import it everywhere.

## Intuition

Think of a `.py` file as a toolbox in a shared garage. A module is just that
file — its functions and variables are tools you can borrow without copying
them. `import` doesn't paste code in; it runs the file once and hands back a
*reference* to everything inside it. One function, one source of truth.

## Approach

1. Write a normal Python file (`greetings.py`) — it's automatically a module
   the moment something imports it.
2. Guard any code that shouldn't run on import with
   `if __name__ == "__main__":`.
3. Group related modules into a folder with an `__init__.py` to make a
   package.
4. Import via `import x`, `from x import y`, or `import x as z`, depending on
   what's clearest at the call site.

## Project Structure

\`\`\`
project/
├── app.py
└── toolkit/
    ├── __init__.py
    └── greetings.py
\`\`\`

## Python Solution

\`\`\`python
# toolkit/greetings.py

def hello(name: str) -> None:
    """Print a friendly greeting."""
    print(f"Hello {name}")


def goodbye(name: str) -> None:
    """Print a friendly farewell."""
    print(f"Goodbye {name}")


if __name__ == "__main__":
    hello("test run")
\`\`\`

\`\`\`python
# app.py

from toolkit import greetings

greetings.hello("Ada")
\`\`\`

Run it:

\`\`\`bash
python app.py
# Hello Ada

python toolkit/greetings.py
# Hello test run
\`\`\`

## Complexity

- **Time:** A module executes once per process regardless of how many files
  import it — Python caches it in `sys.modules`, so repeat imports are O(1).
- **Space:** One in-memory copy of each function, referenced by every
  importer, versus O(n) duplicated code with copy-paste.

## Video

Full walkthrough: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview questions:
`python-name-main-modules-imports-packages`
