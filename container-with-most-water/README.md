# Container With Most Water — Python Solution

LeetCode 11 | Two Pointers | O(n) Time, O(1) Space

## Problem

Given an array of non-negative integers representing wall heights, pick two
walls that, together with the ground between them, form a container. Return
the maximum amount of water that container can hold. The container's sides
must stay upright — you cannot tilt them.

Water height is capped by the shorter of the two chosen walls.

## Intuition

Start with the widest possible container: the two outer walls. If you move
the **taller** wall inward, the width shrinks while the height cap (bounded
by the shorter wall) stays the same or gets worse — so the area can never
improve. Moving the taller wall is therefore always a wasted move.

That leaves exactly one useful move at each step: shrink the container from
the **shorter** side. This single observation is what turns an O(n²) brute
force into an O(n) two-pointer solution.

## Approach

1. Place `left` at index 0 and `right` at the last index.
2. Compute the area for the current pair: `min(height[left], height[right]) * (right - left)`.
3. Update the running maximum.
4. Move whichever pointer points at the shorter wall, one step inward.
5. Repeat until `left == right`.

## Python Solution

```python
def max_area(height: list[int]) -> int:
    """Return the maximum water a container formed by two walls can hold."""
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        max_area = max(max_area, width * current_height)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

## Complexity

| Metric | Complexity | Why |
|--------|------------|-----|
| Time   | O(n)       | Each pointer moves inward at most once per position; together they traverse the array a single time. |
| Space  | O(1)       | Only a fixed set of scalar variables is used, regardless of input size. |

## Video

Full walkthrough with a step-by-step trace on a 9-wall example: (video link coming soon)

## Article

Complete write-up including brute force, dry run, edge cases, and common
mistakes: (video link coming soon)
