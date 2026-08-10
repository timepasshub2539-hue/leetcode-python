# How Python's Garbage Collector Actually Frees Memory

## Problem

When the last reference to a Python object disappears, when — and how —
does the memory actually get freed? Understand CPython's two-part memory
management system: reference counting and the generational cycle collector.

## Intuition

Reference counting is fast and immediate but has one structural blind spot:
reference cycles (A references B, B references A). Since neither object's
counter ever reaches zero on its own, a second mechanism is needed — one
based on *reachability* rather than reference counting.

## Approach

1. Every object carries a reference counter, incremented/decremented on
   assignment. Hits zero → freed immediately.
2. Objects are grouped into generations (0, 1, 2); younger objects are
   scanned more often.
3. A generational cycle collector periodically walks from live program
   roots and marks everything reachable. Anything left unmarked —
   including self-referencing cycles — is freed.

## Python Solution

```python
import gc
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.partner = None

    def __del__(self):
        print(f"Node({self.name}) is being freed")


def demonstrate_cycle():
    x, y = Node("X"), Node("Y")
    x.partner, y.partner = y, x  # cycle

    del x, y  # refcounts stay > 0, nothing freed yet

    print("Before collection:", gc.get_count())
    gc.collect()  # reachability scan frees the stuck pair


if __name__ == "__main__":
    demonstrate_cycle()
```

## Complexity

- Reference counting: O(1) per reference change, O(1) space per object.
- Cycle collection: O(k) per run, where k = objects in the scanned
  generation (not the full heap).

## Video

Full walkthrough with live `sys.getrefcount` / `gc` output: (video link coming soon)

## Article

Complete written breakdown, including brute-force vs. optimal comparison,
dry run, and interview questions: see the accompanying article.
