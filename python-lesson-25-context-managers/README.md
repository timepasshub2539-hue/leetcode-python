# Python Context Managers: Enter, Exit, and contextlib.contextmanager

## Problem
Cleanup code (closing a file, releasing a lock, closing a connection) that's
just the last line of a function only runs if execution actually reaches it.
An exception raised earlier in the function skips it entirely, leaking the
resource. `try/finally` fixes this per-call, but doesn't give you a reusable,
named unit of "how to set up and tear down this resource."

## Intuition
Python's `with` statement guarantees teardown runs no matter how a block
exits — like a hotel key card cutting the lights the instant it's pulled,
regardless of how you left the room. That guarantee is implemented through
two dunder methods: `__enter__` (setup) and `__exit__` (teardown, always
called, receives exception info if one occurred).

## Approach
1. Build a context manager as a class with `__enter__` / `__exit__`.
2. Understand that `__exit__` returning `True` suppresses the exception —
   returning `False`/`None` lets it propagate normally.
3. Rewrite the same behavior with `contextlib.contextmanager`: everything
   before `yield` is enter, everything after is exit.

## Python Solution

### Class-based

\`\`\`python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {elapsed:.4f}s")
        return False
\`\`\`

### Generator-based (recommended for simple cases)

\`\`\`python
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.4f}s")
\`\`\`

## Complexity
- **Time:** O(1) protocol overhead; actual cost is whatever your
  setup/teardown code does.
- **Space:** O(1) — only the state you explicitly store.

## Video
Full walkthrough, including tracing an exception through a `with` block
step by step: (video link coming soon)

## Article
Full write-up with dry runs, edge cases, and interview questions: (video link coming soon)
