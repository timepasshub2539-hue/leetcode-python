# LeetCode 1385 — Find the Distance Value Between Two Arrays

## Problem

Given two integer arrays `arr1` and `arr2`, and an integer `d`, return the
number of elements in `arr1` for which there is **no** element in `arr2`
such that `|arr1[i] - arr2[j]| <= d`.

## Intuition

Checking every pair is correct but wasteful. If `arr2` is sorted, the only
elements that could possibly be within `d` of a given value are its
immediate neighbors in sorted order — everything else is farther away by
definition. Binary search finds those neighbors in O(log m).

## Approach

1. Sort `arr2`.
2. For each value `x` in `arr1`, use `bisect_left` to find its insertion
   index `i` in the sorted array.
3. Check `arr2[i]` (smallest value ≥ x) and `arr2[i-1]` (largest value < x).
4. If both are farther than `d`, `x` is safe — count it.

## Python Solution

```python
from bisect import bisect_left
from typing import List


def find_the_distance_value(arr1: List[int], arr2: List[int], d: int) -> int:
    sorted_arr2 = sorted(arr2)
    m = len(sorted_arr2)
    count = 0

    for x in arr1:
        i = bisect_left(sorted_arr2, x)
        safe = True

        if i < m and abs(sorted_arr2[i] - x) <= d:
            safe = False
        if i > 0 and abs(sorted_arr2[i - 1] - x) <= d:
            safe = False

        if safe:
            count += 1

    return count
```

## Complexity

- **Time:** O((n + m) log m) — sorting `arr2` plus a binary search per
  element of `arr1`.
- **Space:** O(m) for the sorted copy of `arr2`.

## Video

Full walkthrough with a drones-and-beacons analogy, timed benchmark, and
quiz checkpoints: (video link coming soon)

## Article

Full write-up with brute force, optimal solution, dry run, and edge cases:
see the linked article in this repo's description.
