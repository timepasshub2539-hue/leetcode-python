# Python Decorators, Closures, and functools.wraps

## Problem

How do you add behavior (timing, logging, caching) to a function without
modifying its code — and without losing information about what that
function actually is?

## Intuition

Two facts make decorators possible:

1. Functions are first-class values in Python — they can be assigned,
   passed as arguments, and returned from other functions.
2. A closure is a function bundled with variables captured from its
   enclosing scope. Those variables stay alive as long as the closure
   needs them, even after the enclosing function has returned.

A decorator is the closure pattern applied on purpose: a function that
takes another function, defines a new function around it, and returns
the new function. The `@decorator` syntax is sugar for:

```python
func = decorator(func)
```

## Approach

1. Build a closure (`make_counter`) to prove variables survive scope exit.
2. Build a decorator (`timer`) that wraps any function with timing logic.
3. Observe that the wrapped function loses `__name__` and `__doc__`.
4. Fix it with `functools.wraps`.

## Python Solution

```python
import functools
import time


def timer(func):
    """Decorator that prints how long `func` took to run."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result

    return wrapper


@timer
def slow_task(n: int) -> int:
    """Sum of squares from 0 to n-1."""
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    slow_task(1_000_000)
    print(slow_task.__name__)  # "slow_task"
    print(slow_task.__doc__)   # original docstring
```

## Complexity

- **Time:** O(1) overhead from the wrapper itself, on top of the wrapped
  function's own cost.
- **Space:** O(1) extra — one closure reference plus copied metadata.

## Video

Full walkthrough, built live: (video link coming soon)

## Article

Full written breakdown: (video link coming soon)
