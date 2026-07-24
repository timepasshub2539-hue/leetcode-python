# Median of Two Sorted Arrays — Python Solution

## Problem

Given two sorted arrays `nums1` (size m) and `nums2` (size n), find the median
of the two arrays as if they were merged into a single sorted array.

Constraint: the algorithm must run in O(log(m+n)) time.

## Intuition

You don't need to merge the arrays. You only need to find a "partition" —
one imaginary cut through each array — such that every element left of both
cuts is smaller than every element right of both cuts. Once that partition
is found, the median is derived directly from the four values touching the
cuts.

## Approach

1. Always binary search the **shorter** array to keep the search range valid.
2. Fixing a cut `i` in the shorter array forces a cut `j` in the longer array,
   since the combined left side must always hold `(m+n+1)//2` elements.
3. Use `-inf` / `+inf` as border values when a cut sits at an array's edge —
   this removes the need for special-case branches.
4. The partition is valid when `Aleft <= Bright` and `Bleft <= Aright`.
   Otherwise, shift the binary search range based on which side failed.
5. Odd total length → median is `max(Aleft, Bleft)`.
   Even total length → median is the average of `max(Aleft, Bleft)` and
   `min(Aright, Bright)`.

## Python Solution

```python
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2

    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i

        a_left = nums1[i - 1] if i > 0 else float("-inf")
        a_right = nums1[i] if i < m else float("inf")
        b_left = nums2[j - 1] if j > 0 else float("-inf")
        b_right = nums2[j] if j < n else float("inf")

        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return max(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1

    raise ValueError("Input arrays must be sorted")
```

## Complexity

- **Time:** O(log(min(m, n))) — binary search runs only over the shorter
  array's index range.
- **Space:** O(1) — constant number of scalar variables.

## Video

Full walkthrough with diagrams, brute-force build-up, and live quizzes: (video link coming soon)

## Article

Full written breakdown: see the accompanying article for intuition, dry run,
alternative solutions, and common mistakes.
