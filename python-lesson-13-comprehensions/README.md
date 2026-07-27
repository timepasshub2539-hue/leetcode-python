# Python Comprehensions — Turn 4 Lines Into 1

Lesson 13 of the **Fun with Learning Technology** Python series.

## Problem

You have a collection and want to build a **new** collection where each item is
transformed — and optionally where some items are filtered out. The classic loop
works, but costs three lines of ceremony (empty container, `for`, `append`) to
express one simple idea.

## Intuition

A comprehension is a factory conveyor belt: raw items roll in, each gets a quick
stamp, finished items pile up. In order, it answers three questions:

1. **What** do I want each output item to be? → the expression (up front)
2. **Where** do items come from? → the loop (at the back)
3. **Which** items qualify? → the filter (optional)

Start from the loop you know, then move the appended expression to the front and
the loop header to the back. The empty list and `.append` disappear.

## Approach

| Pattern | Syntax |
|---|---|
| Transform | `[n * n for n in nums]` |
| Filter (keep/drop, no else) | `[n for n in nums if n % 2 == 0]` |
| Choose (value per item, needs else) | `["even" if n % 2 == 0 else "odd" for n in nums]` |
| Set (auto-dedupe) | `{ch for ch in "banana"}` |
| Dict (key: value) | `{n: n * n for n in nums}` |
| Nested (outer first, inner fastest) | `[(x, y) for x in range(3) for y in range(3)]` |

**Rule of thumb:** one clean step → comprehension. Branching logic or side
effects → plain loop.

## Python Solution

```python
def squares(numbers):
    return [n * n for n in numbers]

def evens(numbers):
    return [n for n in numbers if n % 2 == 0]

def parity_labels(numbers):
    return ["even" if n % 2 == 0 else "odd" for n in numbers]

def unique_chars(text):
    return {ch for ch in text}

def square_map(numbers):
    return {n: n * n for n in numbers}

def coordinate_grid(size):
    return [(x, y) for x in range(size) for y in range(size)]
```

## Complexity

- **Time:** O(n) — each item visited once (nested: O(m²) for two size-m loops).
- **Space:** O(n) — a new collection is built. Use a generator expression
  `(n * n for n in nums)` for O(1) space when you consume results once.

## Video

▶️ Watch the full walkthrough: (video link coming soon)

## Article

Full written deep-dive with dry runs, edge cases, and common mistakes:
(video link coming soon)
