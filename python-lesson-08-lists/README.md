# Python Lists — Indexing, Slicing & Methods (Lesson 8)

Part of the **Daily Python & LeetCode** series. A from-scratch guide to Python's
most-used data structure, with the intuition behind every operation.

## Problem

You have many related pieces of data and need one structure that keeps them in
order, lets you read any item instantly, and lets you change the collection as
your program runs.

## Intuition

Picture a list as an **egg carton**: one container, many numbered slots, each
holding one item in a fixed order.

- An **index** is an offset — "how far from the start" — which is why counting
  begins at `0`. `-1` counts back from the end.
- A **slice** `start:stop` is half-open: it includes `start` and stops just
  before `stop`, so the item count is always `stop - start`.
- A **variable name is a label, not a box**: `b = a` binds a second name to the
  same list. Use `.copy()` for a true clone.

## Approach

| Task | Tool |
|------|------|
| Read one item | `list[i]` / `list[-1]` |
| Read a range | `list[start:stop]` |
| Change an item | `list[i] = value` |
| Grow | `append`, `insert`, `extend` |
| Shrink | `remove` (by value), `pop` (by index, returns item) |
| Reorder / search | `sort`, `reverse`, `index`, `len` |
| Clone | `list.copy()` or `list[:]` |

## Python Solution

```python
fruits = ["apple", "banana", "plum"]

# Reading
fruits[0]        # "apple"
fruits[-1]       # "plum"
fruits[1:4]      # slice: up to but not including index 4

# Mutating in place
fruits[1] = "kiwi"

# Growing
fruits.append("mango")
fruits.insert(0, "pear")
fruits.extend(["fig", "date"])

# Shrinking
fruits.remove("kiwi")   # deletes first match
last = fruits.pop()     # removes + returns last item

# Copying safely
clone = fruits.copy()   # a real, separate list
```

## Complexity

| Operation | Time |
|-----------|------|
| Index | O(1) |
| Slice / copy | O(k) |
| `append` / `pop()` end | O(1) amortized |
| `insert` / `remove` / `pop(i)` middle | O(n) |
| `sort` | O(n log n) |

Most in-place methods use O(1) extra space; slicing and `copy()` use O(n).

## Common Pitfalls

- `b = a` shares a reference — use `.copy()` to clone.
- Slice stop is **exclusive**: `nums[1:4]` returns 3 items.
- Last valid index is `len(list) - 1`; going past it raises `IndexError`.
- `sort()` returns `None` and mutates in place; use `sorted()` for a new list.

## Video

📺 Watch the full lesson: (video link coming soon)

## Article

📖 Full written breakdown available on the Daily Python Substack.
