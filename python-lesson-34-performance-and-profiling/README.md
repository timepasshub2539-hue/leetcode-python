# Python Performance Debugging: timeit + cProfile

## Problem

A script processes a small test dataset instantly, then hangs for hours
against real production data — despite producing correct output the entire
time. The cause is a membership check (`item in some_list`) running inside a
loop, where the list grows with every iteration.

## Intuition

At small scale, an O(n) scan and an O(1) lookup both feel instant. As data
grows, they diverge sharply: O(n) work scales linearly, O(n^2) work scales
with the square of the input. A list's `in` check is O(n); a set's `in`
check is O(1) average, because it hashes directly to the answer instead of
scanning.

## Approach

1. Measure small snippets with `timeit` (averages repeated runs, avoids
   being misled by one fast/slow outlier).
2. Profile the full program with `cProfile` to find which function actually
   dominates runtime.
3. Sort profiler output by `tottime` (time inside the function itself), not
   `cumtime` (cumulative, including everything it calls) — cumtime commonly
   points at the wrong function.
4. Fix the bottleneck by swapping the data structure (list -> set), not by
   writing cleverer logic.
5. For memory-bound problems (large files), swap list comprehensions for
   generator expressions to avoid holding everything in memory at once.

## Python Solution

\`\`\`python
def dedupe_fast(ids):
    """O(n): set-based membership check."""
    seen = set()
    unique = []
    for uid in ids:
        if uid not in seen:
            unique.append(uid)
            seen.add(uid)
    return unique
\`\`\`

## Complexity

| Approach | Time | Space |
|---|---|---|
| List-based (brute force) | O(n^2) | O(n) |
| Set-based (optimal) | O(n) | O(n) |

## Video

Full walkthrough with live profiler output: (video link coming soon)

## Article

Full written breakdown with dry runs, edge cases, and interview questions
in the accompanying article.
