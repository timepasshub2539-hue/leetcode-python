# LeetCode 3364 — Minimum Positive Sum Subarray

## Problem

Given an array `nums` and two integers `l` and `r`, find a contiguous subarray
with length between `l` and `r` (inclusive) whose sum is the smallest
positive value possible. If no such subarray exists, return `-1`.

## Intuition

Sliding window seems tempting but fails: with negative numbers, growing a
window can shrink the sum instead of growing it, breaking the monotonicity
sliding window relies on.

Prefix sums fix this. Any subarray sum is `prefix[j] - prefix[i]`. The task
becomes: for each `j`, find the closest smaller `prefix[i]` seen so far,
among the ones that satisfy the length constraint — a sorted-lookup problem,
not a window problem.

## Approach

1. Build prefix sums.
2. Maintain a sorted window of prefixes whose corresponding start index keeps
   the subarray length between `l` and `r`.
3. For each step, binary search (`bisect_left`) the window for the closest
   smaller prefix, and track the smallest positive gap found.

## Python Solution

```python
from bisect import bisect_left, insort


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + num

        window = []
        best = -1

        for end in range(l, n + 1):
            insort(window, prefix[end - l])
            if end - r - 1 >= 0:
                window.remove(prefix[end - r - 1])

            pos = bisect_left(window, prefix[end])
            if pos > 0:
                candidate = prefix[end] - window[pos - 1]
                if best == -1 or candidate < best:
                    best = candidate

        return best
```

## Complexity

- Binary search lookup: `O(log n)` per step.
- Insertion/removal in a plain list: `O(n)` per step, giving `O(n²)` worst
  case overall — acceptable at `n ≤ 100`, but not the full `O(n log n)` the
  pattern allows. Swap the list for a Fenwick tree or a balanced sorted
  structure to close that gap.
- Space: `O(n)` for the prefix array and window.

## Video

Full walkthrough with timing comparisons and quizzes: (video link coming soon)

## Article

Full write-up with intuition, dry run, and interview follow-ups: see the
linked article above.
