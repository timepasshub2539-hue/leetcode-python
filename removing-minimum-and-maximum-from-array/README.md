# LeetCode 2091 — Removing Minimum and Maximum From Array

## Problem

Given a 0-indexed array of **distinct** integers, in one operation you may
delete either the leftmost or the rightmost element of the array. Return the
minimum number of deletions needed so that both the minimum and maximum
values have been removed from the array.

Constraints:
- `3 <= nums.length <= 10^5`
- All values in `nums` are distinct.

## Intuition

Simulating the deletions works but is unnecessary. Only two positions in the
array matter: the index of the minimum value and the index of the maximum
value. Every other element is deleted incidentally, regardless of which
strategy you pick. Once you have those two indices, the answer is the
minimum of three fixed-cost strategies.

## Approach

1. Find `i`, the index of the minimum value, and `j`, the index of the
   maximum value.
2. Normalize so `i < j` (swap if necessary).
3. Compute three costs:
   - `front_only = j + 1`
   - `back_only = n - i`
   - `both_ends = (i + 1) + (n - j)`
4. Return the smallest of the three.

## Python Solution

```python
def minimum_deletions(nums: list[int]) -> int:
    n = len(nums)

    i = nums.index(min(nums))
    j = nums.index(max(nums))

    if i > j:
        i, j = j, i

    front_only = j + 1
    back_only = n - i
    both_ends = (i + 1) + (n - j)

    return min(front_only, back_only, both_ends)
```

## Complexity

- **Time:** O(n) — one linear scan to find the min, one to find the max.
- **Space:** O(1) — only a fixed number of scalar variables.

## Video

Full derivation, dry run, and quiz breaks: (video link coming soon)

## Article

Complete write-up with intuition, brute force comparison, and edge cases:
see the accompanying blog post for this problem.
