# LeetCode 3116 — Kth Smallest Amount With Single Denomination Combination

## Problem

Given an array of distinct coin denominations and an integer `k`, you may
build a payment using unlimited coins of a single denomination at a time
(no mixing denominations within one payment). Across every denomination,
combine all payable amounts, sort them, and return the k-th smallest.

Constraints:
- 1 <= coins.length <= 15
- 1 <= coins[i] <= 25
- 1 <= k <= 2 * 10^9

## Intuition

Brute force (generate every multiple, dedupe, sort, index k) breaks
because k can reach 2 billion — you cannot materialize that list.

Instead: binary search on the answer value `x`, using a predicate
"how many valid amounts are <= x?" That count is monotonic in `x`,
which is exactly what binary search needs.

## Approach

1. **Count function** — for every non-empty subset of coins, compute the
   LCM of the subset and count its multiples up to `x` (`x // lcm`).
   Add the count for odd-sized subsets, subtract for even-sized subsets
   (inclusion-exclusion). This gives an exact count with no double-counting
   of shared multiples.
2. **Binary search** — search `x` in `[1, min(coins) * k]` for the smallest
   value where `count_at_most(x) >= k`.

## Python Solution

\`\`\`python
from itertools import combinations
from math import lcm
from typing import List


def findKthSmallest(coins: List[int], k: int) -> int:
    n = len(coins)

    def count_at_most(x: int) -> int:
        total = 0
        for size in range(1, n + 1):
            sign = 1 if size % 2 == 1 else -1
            for combo in combinations(coins, size):
                total += sign * (x // lcm(*combo))
        return total

    lo, hi = 1, min(coins) * k
    while lo < hi:
        mid = (lo + hi) // 2
        if count_at_most(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo
\`\`\`

## Complexity

- **Time:** O(2^n * log(range)) — 2^n - 1 subsets per count check,
  ~40 binary search steps for the given constraints.
- **Space:** O(n) — no list of amounts is ever built.

## Video

Full walkthrough, including a brute-force vs. optimal timing comparison:
(video link coming soon)

## Article

Full write-up with dry run, complexity analysis, and common mistakes:
See the accompanying article in this repository / linked post.
