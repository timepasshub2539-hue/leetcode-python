# Stone Game V — LeetCode 1563 (Python)

## Problem

Given a row of stone values, repeatedly split the row into two non-empty
groups. Score increases by the sum of the *smaller* group, which is then
discarded; the larger group survives as the new row. If the groups are
equal, either may be discarded. Continue until one stone remains. Return
the maximum total score achievable.

## Intuition

Splitting the row as evenly as possible every round looks safe, but it's
provably not optimal — a 3-stone counterexample shows a lopsided split
outscoring an even one. Every split creates two smaller instances of the
same problem, which is the signal to solve it with interval DP:
`dp[i][j]` = best score obtainable from stones `i` through `j`.

## Approach

1. Build a prefix-sum array for O(1) range sums.
2. For every segment `[i, j]`, try every split point `k`.
3. Score the smaller side plus its own DP value; on ties, keep the side
   with the larger DP value.
4. Memoize on `(i, j)` only — the accumulated score does not belong in
   the cache key.
5. Answer is `dp(0, n - 1)`.

## Python Solution

```python
from functools import lru_cache
from itertools import accumulate


def stone_game_v(stone_values: list[int]) -> int:
    n = len(stone_values)
    prefix = [0] + list(accumulate(stone_values))

    def range_sum(i: int, j: int) -> int:
        return prefix[j + 1] - prefix[i]

    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> int:
        if i == j:
            return 0
        best = 0
        for k in range(i, j):
            left_sum = range_sum(i, k)
            right_sum = range_sum(k + 1, j)
            if left_sum < right_sum:
                best = max(best, left_sum + dp(i, k))
            elif right_sum < left_sum:
                best = max(best, right_sum + dp(k + 1, j))
            else:
                best = max(best, left_sum + max(dp(i, k), dp(k + 1, j)))
        return best

    return dp(0, n - 1)
```

## Complexity

- **Time:** O(n³) — O(n²) segments, O(n) split points each.
- **Space:** O(n²) for memoization, O(n) for prefix sums.

## Video

Full walkthrough with the DP table filled in by hand and a brute-force
timing comparison: (video link coming soon)

## Article

Complete write-up with dry run, edge cases, and interview follow-ups:
see the accompanying article in this repo/series.
