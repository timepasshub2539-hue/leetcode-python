# Python Functional Toolkit: The Loop Bug It Prevents

## Problem
Sort a list of student dictionaries by score, descending, without hand-writing
comparison/swap logic that can silently break if one operator gets flipped.

## Intuition
Describe *what* to sort by (the score) instead of *how* to compare items.
`sorted(key=...)` removes the possibility of a backwards-comparison bug because
there's no comparison code left for you to get wrong. The same idea applies to
`filter`/`map` (separate "which items" from "what happens to them") and
`reduce` (fold a sequence to one value without a hand-managed accumulator).

## Approach
1. `sorted(students, key=lambda s: s["score"], reverse=True)` — declarative sort.
2. `filter` then `map` — narrow the list, then transform only what survives.
3. `functools.reduce` — fold to a single running value.
4. `functools.partial` / `lru_cache` — pre-fill arguments / memoize results.
5. `itertools.groupby` — cluster consecutive matches (sort first, always).

## Python Solution

\`\`\`python
from functools import reduce, partial, lru_cache
from itertools import groupby


def sort_students_by_score(students, descending=True):
    return sorted(students, key=lambda s: s["score"], reverse=descending)


def passing_students_scaled(students, passing_score=60, curve=1.05):
    passed = filter(lambda s: s["score"] >= passing_score, students)
    curved = map(lambda s: {**s, "score": round(s["score"] * curve, 1)}, passed)
    return list(curved)


def class_average(students):
    total = reduce(lambda acc, s: acc + s["score"], students, 0)
    return total / len(students) if students else 0


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def group_by_grade_letter(students, grade_fn):
    ordered = sorted(students, key=grade_fn)
    return {k: list(v) for k, v in groupby(ordered, key=grade_fn)}


round_to_one_decimal = partial(round, ndigits=1)
\`\`\`

## Complexity
| Operation | Time | Space |
|---|---|---|
| `sorted(key=...)` | O(n log n) | O(n) |
| `filter` + `map` | O(n) | O(1) extra (lazy) |
| `reduce` | O(n) | O(1) |
| `lru_cache` (fib) | O(n) | O(n) |

## Video
(video link coming soon)

## Article
Full article with dry runs, edge cases, and interview questions: see the
companion write-up in this repo / linked blog post.
