# LeetCode 3414 — Maximum Score of Non-overlapping Intervals

## Problem

Given a list of intervals, each defined by `[start, end, weight]`, select up to 4
intervals such that no two selected intervals overlap (touching endpoints count
as overlapping) and the total weight is maximized. Among all subsets achieving
the maximum score, return the one with the lexicographically smallest list of
original indices.

## Intuition

Picking the single highest-weight interval is a trap — it may overlap with two
or more lower-weight intervals that together score higher. The right question
isn't "which interval is heaviest," it's "which chain of compatible intervals
scores highest." That reframes the problem as weighted interval scheduling,
with an added cap on the number of picks.

## Approach

1. Sort interval indices by start time; extract parallel `start`, `end`,
   `weight` arrays.
2. For each interval, binary search for the next interval whose start is
   strictly after this one's end (`nxt[i]`).
3. Build a DP table `dp[i][k]`: best score using intervals from position `i`
   onward, picking at most `k` (0–4) of them.
   - `dp[i][k] = max(dp[i+1][k], weight[i] + dp[nxt[i]][k-1])`
4. `dp[0][4]` is the maximum score.
5. Reconstruct the chosen intervals by retracing the same take/skip decision
   forward, skipping on exact ties to keep indices minimal, then sort the
   result.

## Python Solution

```python
from bisect import bisect_right
from typing import List


def maximum_weight(intervals: List[List[int]]) -> List[int]:
    n = len(intervals)
    order = sorted(range(n), key=lambda i: intervals[i][0])
    start = [intervals[i][0] for i in order]
    end = [intervals[i][1] for i in order]
    weight = [intervals[i][2] for i in order]

    nxt = [bisect_right(start, end[i]) for i in range(n)]

    dp = [[0] * 5 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for k in range(1, 5):
            dp[i][k] = max(dp[i + 1][k], weight[i] + dp[nxt[i]][k - 1])

    chosen = []
    i, k = 0, 4
    while i < n and k > 0:
        if weight[i] + dp[nxt[i]][k - 1] > dp[i + 1][k]:
            chosen.append(order[i])
            i = nxt[i]
            k -= 1
        else:
            i += 1

    return sorted(chosen)
```

## Complexity

- **Time:** O(n log n) — sorting plus binary search dominate; the DP itself
  is O(n) with a constant factor of 5.
- **Space:** O(n) for the sorted arrays and the DP table.

## Video

Full walkthrough with diagrams and a live dry run: (video link coming soon)

## Article

Complete write-up with dry run, edge cases, and interview follow-ups:
see the accompanying article in this series.
