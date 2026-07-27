# Python Scope, `*args`, and `**kwargs`

Lesson 12 of the **Fun with Learning Technology** Python series — understand
where your variables live and how to accept any number of function arguments.

## Problem

Two closely related beginner stumbling blocks:

1. **Scope** — Why does changing a variable inside a function sometimes get
   ignored, and why does Python raise `UnboundLocalError` on a variable you
   clearly defined?
2. **Flexible arguments** — How do you write one function that accepts any
   number of positional or keyword arguments?

## Intuition

Think of a house. Each function is a **room**; the whole program is the
**hallway** (global scope).

- A name created inside a function is **local** — it vanishes when the
  function returns.
- A name at the top level is **global** — any function can *read* it.
- **Key rule:** assigning to a name *anywhere* inside a function marks it
  **local for the entire function**, even if a global shares the name. That is
  the root cause of `UnboundLocalError`.

The stars follow the same "where does this live?" logic:

- `*args` **packs** loose positional values into a **tuple**.
- `**kwargs` **packs** labeled values into a **dictionary**.
- At a call site, the stars **spread** collections back into arguments.

## Approach

| Tool | Definition side | Call side |
|------|-----------------|-----------|
| `*`  | collect positional → tuple | spread a list/tuple |
| `**` | collect keyword → dict     | spread a dict |

Parameter order is strict: **plain → `*args` → `**kwargs`**. Use `global`
sparingly; prefer returning values.

## Python Solution

```python
def apply(func, *args, **kwargs):
    """Forward any number of arguments to func (the wrapper pattern)."""
    return func(*args, **kwargs)


def add(a, b, c):
    return a + b + c


counter = 0

def bump():
    global counter          # target the outer variable explicitly
    counter += 1
    return counter


if __name__ == "__main__":
    assert apply(add, 1, 2, 3) == 6
    assert add(*[10, 20, 30]) == 60
    assert add(**{"a": 1, "b": 2, "c": 3}) == 6
    assert bump() == 1 and bump() == 2 and counter == 2
    print("All checks passed.")
```

## Complexity

- **Time:** O(n) to pack or spread n arguments.
- **Space:** O(n) for the tuple (`*args`) or dict (`**kwargs`).

## Video

▶️ Watch Lesson 12: (video link coming soon)

## Article

Full written deep-dive — mental models, dry run, edge cases, and common
mistakes — available on the series Substack.

---
*Part of the **Fun with Learning Technology** Python series.*
