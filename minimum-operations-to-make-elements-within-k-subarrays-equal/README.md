# LeetCode 3505 — Minimum Operations to Make Elements Within K Subarrays Equal

## Problem

Given an integer array `nums` and integers `x`, `k`: you may increment or
decrement any element by 1 (each change = 1 operation). Find the minimum
operations needed so the array contains at least `k` non-overlapping
subarrays, each of length exactly `x`, where every element in a chosen
subarray is equal.

## Intuition

Two independent subproblems:

1. **Pricing a single window** — the cheapest value to equalize a fixed
   window to is its **median**, not its mean. Median minimizes the sum of
   absolute deviations; mean minimizes squared error. Our cost is per-unit
   absolute distance, so median wins.
2. **Selecting k windows** — with `k` capped at 15 (tiny) and `n` up to
   100,000 (large), the small bounded variable becomes a DP dimension
   instead of a brute-force multiplier.

## Approach

- Slide a sorted window across the array, maintaining a prefix sum so each
  window's median cost is computed in O(1) amortized (O(x) per shift for
  the sorted-list maintenance).
- Run a DP over `dp[i][j]` = minimum cost using `j` windows within the
  first `i` elements:
  - Skip: `dp[i][j] = dp[i-1][j]`
  - Close a window ending at `i`: `dp[i][j] = min(dp[i][j], dp[i-x][j-1] + cost[i-x])`
- Answer is `dp[n][k]`.

## Python Solution

```python
from bisect import insort
from itertools import accumulate


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        costs = self._window_costs(nums, x)

        INF = float("inf")
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j] = dp[i - 1][j]
                if i >= x and dp[i - x][j - 1] != INF:
                    candidate = dp[i - x][j - 1] + costs[i - x]
                    if candidate < dp[i][j]:
                        dp[i][j] = candidate

        return dp[n][k]

    def _window_costs(self, nums: list[int], x: int) -> list[int]:
        n = len(nums)
        window = sorted(nums[:x])
        costs = [self._median_cost(window)]
        for i in range(x, n):
            window.remove(nums[i - x])
            insort(window, nums[i])
            costs.append(self._median_cost(window))
        return costs

    def _median_cost(self, sorted_window: list[int]) -> int:
        mid = len(sorted_window) // 2
        target = sorted_window[mid]
        prefix = list(accumulate(sorted_window))
        total = prefix[-1]
        left_sum = prefix[mid] - sorted_window[mid]
        left_count = mid
        right_sum = total - prefix[mid]
        right_count = len(sorted_window) - mid - 1
        return (target * left_count - left_sum) + (right_sum - target * right_count)
```

## Complexity

- **Time:** O(n·x + n·k) — window pricing dominates when `x` is large;
  DP table fill is near-linear since `k ≤ 15`.
- **Space:** O(n·k) for the DP table, O(x) for the sliding window.

## Video

Full walkthrough with cell-by-cell DP trace and a live brute-force-vs-optimal
benchmark: (video link coming soon)

## Article

Complete write-up with intuition, dry run, edge cases, and interview
follow-ups: see the accompanying article.
