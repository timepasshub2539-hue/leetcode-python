# Maximum Subarray Sum With Length Divisible by K

## Problem

Given an array of integers `nums` and an integer `k`, find the maximum sum of
a contiguous subarray whose **length** is a multiple of `k` (i.e. length is
`k`, `2k`, `3k`, ...). Array size can be up to 200,000, so an `O(n)` or
`O(n log n)` solution is required.

## Intuition

Kadane's algorithm maximizes subarray sum with no regard for length, so it
can return a subarray whose length isn't a valid multiple of `k`.

Any subarray sum can be written as `prefix[j] - prefix[i]`. The length
`j - i` divides `k` exactly when `i` and `j` share the same remainder mod
`k`. So indices split naturally into `k` "lanes" by `index % k`, and within
each lane the problem reduces to "maximize `prefix[j]` minus the smallest
prior `prefix[i]`."

## Approach

1. Build a prefix sum as you scan the array.
2. Maintain one running minimum prefix value per remainder lane
   (`index % k`).
3. At each index, compute the candidate answer using that index's lane
   minimum, then update the lane minimum.

Single forward pass, no nested loops.

## Python Solution

```python
def max_subarray_sum_div_by_k(nums: list[int], k: int) -> int | None:
    n = len(nums)
    if k <= 0 or n < k:
        return None

    lane_min = [None] * k
    lane_min[0] = 0

    prefix = 0
    best = float("-inf")

    for j in range(1, n + 1):
        prefix += nums[j - 1]
        lane = j % k

        if lane_min[lane] is not None:
            best = max(best, prefix - lane_min[lane])

        if lane_min[lane] is None or prefix < lane_min[lane]:
            lane_min[lane] = prefix

    return best if best != float("-inf") else None
```

## Complexity

- **Time:** `O(n)` — one pass, constant work per index.
- **Space:** `O(k)` — one minimum tracked per remainder lane.

Brute force checking every window of every valid length is `O(n²)` in the
worst case — on 200,000 elements, the difference between this and the
optimal solution is the difference between instant and a timeout.

## Video

Full walkthrough with a live trace, edge cases, and a real timing
comparison: (video link coming soon)

## Article

Complete write-up with dry run, complexity analysis, and common mistakes:
see the accompanying blog post.
