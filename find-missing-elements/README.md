# Find Missing Elements

Given an array of unique integers that originally covered every value in a
contiguous range (smallest to largest, no gaps), some numbers from the
middle have been removed. Return the missing numbers, sorted ascending. If
nothing is missing, return an empty list.

## Problem

- Input: `nums`, a list of unique integers.
- The range is `[min(nums), max(nums)]`; both endpoints are always present.
- Output: a sorted list of integers within that range that are absent from `nums`.

**Example**
```
Input:  nums = [1, 4, 2, 5]
Output: [3]
```

## Intuition

Checking "is this number in my array?" against a plain list is slow (it
rescans every time). A set fixes the speed problem but costs extra memory.
The in-place trick avoids both: treat one array's *indices* as a lookup
table, and the *sign* of each value as a "have I seen this" marker.

## Approach

1. Find `lo = min(nums)` and `hi = max(nums)`.
2. Build `tracker = list(range(lo, hi + 1))`.
3. For every `num` in `nums`, flip `tracker[num - lo]` negative.
4. Whatever remains positive was never marked — those are the missing values,
   already sorted since `tracker` was built in order.

## Python Solution

```python
def find_missing_elements(nums: list[int]) -> list[int]:
    lo, hi = min(nums), max(nums)
    tracker = list(range(lo, hi + 1))

    for num in nums:
        idx = num - lo
        tracker[idx] = -abs(tracker[idx])

    return [val for val in tracker if val > 0]
```

## Complexity

- **Time:** O(n) — one pass to mark, one pass to collect.
- **Space:** O(1) extra — `tracker` doubles as the output; no second hash
  structure is allocated.

## Video

Full walkthrough with dry run and edge cases: (video link coming soon)

## Article

Full written breakdown: (video link coming soon)
