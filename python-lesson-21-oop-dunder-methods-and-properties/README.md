# Python Dunder Methods: Fixing print(), ==, and len() on Custom Objects

## Problem

By default, Python's built-in operations don't know how to handle custom
objects meaningfully:

- `print(obj)` shows a memory address instead of your data.
- `obj1 == obj2` checks identity, not whether the data matches.
- `len(obj)` raises a `TypeError`.

This isn't a bug — Python refuses to guess, and instead exposes hook methods
(dunder methods) that let you define the behavior yourself.

## Intuition

Every built-in operation against a custom object is routed through a matching
dunder method:

| Syntax | Method called |
|---|---|
| `print(obj)` / `repr(obj)` | `__repr__` |
| `str(obj)` | `__str__` (falls back to `__repr__`) |
| `obj1 == obj2` | `__eq__` |
| `len(obj)` | `__len__` |
| `obj1 + obj2` | `__add__` |

Define the method, and the built-in syntax does what you want.

## Approach

1. Implement `__repr__` for a meaningful `print()` output — define this even
   if you skip `__str__`, since it's the universal fallback.
2. Implement `__eq__` to compare actual field values, returning
   `NotImplemented` for incompatible types.
3. Implement `__len__`, returning a non-negative `int`.
4. Use `@property` for values that should be computed on access but read like
   plain attributes.
5. Use `classmethod` for alternate constructors, `staticmethod` for related
   functions that don't need instance or class state.

## Python Solution

\`\`\`python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def area(self):
        return abs(self.x * self.y)

    @classmethod
    def from_tuple(cls, coords):
        return cls(coords[0], coords[1])

    @staticmethod
    def distance(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
\`\`\`

## Complexity

- Time: O(1) for every dunder method shown — each does a fixed number of
  attribute lookups and arithmetic operations.
- Space: O(1) — no additional data structures are allocated.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview questions:
(video link coming soon)
