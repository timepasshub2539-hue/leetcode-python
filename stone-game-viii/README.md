# LeetCode 1872 — Stone Game VIII (Python, O(n))

## Problem

Alice and Bob take turns removing a prefix (at least two stones) from the
front of a row of stones, scoring the sum of the removed stones, and
replacing them with one new stone holding that sum. Alice maximizes the
final (Alice score − Bob score) gap; Bob minimizes it. Both play optimally.
Return the final gap.

## Intuition

At any point, the only state that matters is a single index — everything
before it is sunk cost. Since every move removes a prefix, every possible
score is a prefix sum, so those can be precomputed once. The DP recurrence
only ever needs the value one index ahead of it, so a single backward pass
replaces both recursion and branching over every cut point.

## Approach

1. Build prefix sums in one forward pass (`itertools.accumulate`).
2. Seed `best` with the last prefix sum (the final move is forced).
3. Scan backward from the second-to-last index to index 1:
   `best = max(best, prefix[i] - best)`
4. Return `best`.

## Python Solution

```python
from itertools import accumulate
from typing import List


def stoneGameVIII(stones: List[int]) -> int:
    prefix = list(accumulate(stones))
    n = len(prefix)
    best = prefix[-1]
    for i in range(n - 2, 0, -1):
        best = max(best, prefix[i] - best)
    return best
```

## Complexity

- Time: **O(n)** — one pass to build prefix sums, one backward pass for the DP.
- Space: **O(n)** — the prefix sum array.

## Video

Full walkthrough, derivation, and a timed brute-force vs. optimal benchmark: (video link coming soon)

## Article

Complete write-up with dry run, complexity proof, and common mistakes: (video link coming soon)
