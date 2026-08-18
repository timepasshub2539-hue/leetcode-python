# LeetCode 3471 — Find the Largest Almost Missing Integer (Python)

## Problem
Given an array `nums` and window size `k`, consider every contiguous window of
`k` elements. A value is "almost missing" if it appears in exactly one window.
Return the largest almost missing value, or -1 if none exists.

## Intuition
Split the array into three zones: left edge, middle, right edge (each edge is
`k - 1` elements wide). Every window covers the middle the same number of
times — always `k` — so middle elements can only be almost missing when
`k == 1`. That means only edge positions are ever candidates, shrinking the
search space from `n` elements to roughly `2k`.

## Approach
1. If `k >= n`, every value qualifies — return `max(nums)`.
2. Compute `window_coverage(i) = min(i, k-1, n-k, n-1-i) + 1` for any index.
3. Collect candidate values from the first and last `k - 1` indices.
4. For each candidate value, sum `window_coverage` across **every** index
   where it occurs (handles duplicates correctly).
5. Return the largest value whose total coverage equals exactly 1.

## Python Solution
```python
from typing import List


def largest_almost_missing_integer(nums: List[int], k: int) -> int:
    n = len(nums)
    if k >= n:
        return max(nums)

    def window_coverage(index: int) -> int:
        return min(index, k - 1, n - k, n - 1 - index) + 1

    edge_indices = set(range(k - 1)) | set(range(n - k + 1, n))

    value_to_indices = {}
    for i, val in enumerate(nums):
        value_to_indices.setdefault(val, []).append(i)

    best = -1
    seen_values = {nums[i] for i in edge_indices}

    for val in seen_values:
        total_coverage = sum(window_coverage(i) for i in value_to_indices[val])
        if total_coverage == 1:
            best = max(best, val)

    return best
```

## Complexity
- **Time:** O(n) — candidate set is bounded by ~2k, and total coverage
  summation touches each index a bounded number of times.
- **Space:** O(n) — for the value-to-indices map.

## Video
Full walkthrough with brute force comparison and dry run: (video link coming soon)

## Article
Complete write-up with diagrams, complexity analysis, and interview
follow-ups: (video link coming soon)
