# Length of Longest Subarray With at Most K Frequency (LeetCode 2958)

## Problem

Given an integer array `nums` and an integer `k`, return the length of the
longest subarray such that the frequency of each distinct value in that
subarray is at most `k`.

## Intuition

Sliding the window forward by one element barely changes its contents, yet
brute force recounts everything from scratch on every step. Track frequency
counts incrementally instead, and the problem collapses to a linear pass.

## Approach

- Maintain a `counts` dictionary and two pointers, `left` and `right`.
- Expand the window by moving `right` forward, incrementing the count of the
  newly added value.
- While the added value's count exceeds `k`, shrink from `left`, decrementing
  counts, until the window is legal again. Use a `while` loop, not an `if` —
  a single removal isn't always enough.
- After each shrink, update the best window size seen so far.

## Python Solution

```python
from collections import defaultdict


def max_subarray_length(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    left = 0
    best = 0

    for right, value in enumerate(nums):
        counts[value] += 1

        while counts[value] > k:
            counts[nums[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
```

## Complexity

- **Time:** O(n) — each element is added and removed from the window at most once.
- **Space:** O(n) — worst case, every element is a distinct key in `counts`.

## Video

Full walkthrough with diagrams and dry runs: (video link coming soon)

## Article

Full written breakdown: (video link coming soon)
