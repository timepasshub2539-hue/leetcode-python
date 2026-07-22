# Python Tuples & Sets — When to Use Each One

## Problem

Python offers three built-in collection types — `list`, `tuple`, and `set` —
each with different guarantees around order, mutability, and duplicates.
Choosing the wrong one can silently produce bugs or slow code as data grows.

## Intuition

Ask three questions about your data:
1. Does it need to change after creation? → No: tuple. Yes: list or set.
2. Does order matter, and are duplicates okay? → Yes: list. No: set.
3. Will you check membership repeatedly? → Set (O(1) average via hashing)
   beats list (O(n)) every time as data grows.

## Approach

- **Tuple**: ordered, immutable, created with `()`. Single-item tuples need
  a trailing comma: `(5,)`.
- **Set**: unordered, mutable, auto-deduplicates, created with `{}` or
  `set()` (note: `{}` alone makes a dict, not a set).
- Sets require **hashable** (immutable) elements — lists cannot go inside
  a set, but tuples can.
- Set operations: `|` union, `&` intersection, `-` difference.

## Python Solution

\`\`\`python
def unique_pairs(records: list[tuple[str, int]]) -> set[tuple[str, int]]:
    """Return unique (name, age) records using a set for dedup."""
    return set(records)


def shared_users(group_a: list[int], group_b: list[int]) -> set[int]:
    """Return user IDs present in both groups using set intersection."""
    return set(group_a) & set(group_b)


def fast_lookup_demo(candidates: list[int], target: int) -> bool:
    """Membership check backed by a set for O(1) average lookup."""
    seen = set(candidates)
    return target in seen
\`\`\`

## Complexity

| Operation | List | Set |
|---|---|---|
| Membership check | O(n) | O(1) average |
| Union/Intersection | O(n*m) manual | O(min(n, m)) |
| Space | O(n) | O(n) |

## Video

Full walkthrough with live coding: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and interview questions:
see the accompanying article in this repo / Substack.
