# Python Iterators & Generators: Zero-Memory Sequences

## Problem
Why does `range(1_000_000_000)` run instantly while `list(range(1_000_000_000))`
can exhaust memory on a typical machine, even though both "represent" the same
billion numbers?

## Intuition
A `for` loop isn't a primitive — it's shorthand for calling `iter()` once and
`next()` repeatedly until `StopIteration` is raised. An iterable (like a list)
knows how to produce an iterator; the iterator is the separate object that
actually tracks position and produces values one at a time. Since producing
"the next value" doesn't require already having every value, you never need to
store them all — that's the entire basis for `range()`, generators, and
`yield`.

## Approach
1. Confirm the iterator protocol manually: call `iter()` on a list, then call
   `next()` repeatedly to see values and the eventual `StopIteration`.
2. Implement a hand-built iterator class with `__iter__` and `__next__`.
3. Replace it with a generator function using `yield` — same behavior, far
   less code, because Python builds the state machine for you.
4. Compare a list comprehension (`[...]`, eager) against a generator
   expression (`(...)`, lazy) for the same computation.

## Python Solution
\`\`\`python
def count_up(start: int, end: int):
    """Yield integers from start up to (but not including) end, one at a time."""
    current = start
    while current < end:
        yield current
        current += 1


def evens_generator_expression(limit: int):
    return (n for n in range(limit) if n % 2 == 0)
\`\`\`

## Complexity
| Approach | Time | Space |
|---|---|---|
| `list(range(n))` | O(n) | O(n) |
| `range(n)` / generator | O(n) total, spread over consumption | O(1) |

`range` objects store only `start`, `stop`, `step` — never the full sequence.
Generators hold only their current local state between `yield` calls.

## Video
Full walkthrough with live tracing of a generator pausing and resuming:
(video link coming soon)

## Article
Complete write-up with dry runs, edge cases, and interview questions:
(video link coming soon)
