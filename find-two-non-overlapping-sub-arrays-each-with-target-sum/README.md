# LeetCode 1477 — Find Two Non-overlapping Sub-arrays Each With Target Sum

## Problem

Given an array of positive integers and a target value, find two non-overlapping
subarrays that each sum exactly to the target, minimizing their combined length.
Return -1 if no such pair exists.

## Intuition

The sum of any subarray equals one running prefix sum minus an earlier one.
Track cumulative sums in a hash map, and detecting a qualifying subarray
becomes an O(1) lookup. To find the optimal pair without comparing every
combination, carry forward the shortest valid subarray found so far and check
each new candidate against that single running value.

## Approach

1. Seed a `seen` dict with `{0: -1}` (running sum → index).
2. Walk the array once, maintaining a running `total`.
3. At each index, check if `total - target` is in `seen`. If so, a valid
   subarray ends here.
4. Look up the shortest valid subarray that already finished before this one
   started (`min_len[start]`), and combine lengths if one exists.
5. Update the running best single-subarray length and store it in `min_len`.
6. Record the current `total` in `seen`.
7. Return the best combined length found, or -1.

## Python Solution

```python
def min_sum_of_lengths(arr, target):
    n = len(arr)
    INF = float('inf')
    min_len = [INF] * n
    seen = {0: -1}

    total = 0
    best_so_far = INF
    best_combined = INF

    for i, num in enumerate(arr):
        total += num
        needed = total - target

        if needed in seen:
            start = seen[needed]
            current_len = i - start

            if start != -1 and min_len[start] != INF:
                best_combined = min(best_combined, min_len[start] + current_len)

            best_so_far = min(best_so_far, current_len)

        min_len[i] = best_so_far
        seen[total] = i

    return best_combined if best_combined != INF else -1
```

## Complexity

- **Time:** O(N) — single pass, O(1) hash map operations.
- **Space:** O(N) — the `seen` dict and `min_len` array.

## Video

Full walkthrough with dry run and diagrams: (video link coming soon)

## Article

Complete writeup with brute force comparison, edge cases, and interview
follow-ups: see the accompanying article in this repo / linked in the video
description.
