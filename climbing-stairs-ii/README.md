# LeetCode 3693 — Climbing Stairs II (Python)

## Problem

You start at step `0` of a staircase numbered `0` to `n`. From any step `i`
you may jump to `i + 1`, `i + 2`, or `i + 3`. Landing on step `j` costs
`cost[j] + (jump distance)^2`. Find the minimum total cost to reach step `n`.

## Intuition

The farthest jump covers the most ground but pays the steepest squared
penalty (a 3-step jump costs 9 before the landing step's own price even
counts). Always jumping as far as possible is **not** guaranteed to be
cheapest — a sequence of smaller jumps can beat it.

Since the only way to land on step `j` is from `j-1`, `j-2`, or `j-3`, the
cheapest cost to reach `j` is:

```
dp[j] = min(dp[j-k] + cost[j] + k**2  for k in (1, 2, 3) if j - k >= 0)
```

## Approach

Bottom-up DP, one pass left to right:

1. `dp[0] = 0`, everything else starts at infinity.
2. For each step `j` from `1` to `n`, check the three valid predecessors and
   keep the cheapest resulting cost.
3. Return `dp[n]`.

## Python Solution

```python
from typing import List


def min_cost_climbing_stairs(n: int, cost: List[int]) -> int:
    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for j in range(1, n + 1):
        for k in (1, 2, 3):
            prev = j - k
            if prev >= 0:
                dp[j] = min(dp[j], dp[prev] + cost[j] + k * k)

    return dp[n]
```

## Complexity

- **Time:** `O(n)` — each step checks exactly 3 fixed neighbors.
- **Space:** `O(n)` for the DP table (reducible to `O(1)` with a rolling
  window of the last three values).

## Video

Full walkthrough with a dry run, timed brute-force comparison, and quiz
rounds: (video link coming soon)

## Article

Full written breakdown: see the accompanying blog post for intuition,
brute force comparison, edge cases, and common mistakes.
