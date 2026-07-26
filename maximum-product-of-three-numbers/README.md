# Maximum Product of Three Numbers (LeetCode 628)

Find three numbers in a list whose product is the largest possible, and return that product. A beginner-friendly problem that teaches a surprisingly deep lesson about negative numbers.

## Problem

Given an integer array `nums`, choose exactly three numbers whose product is
maximized, and return that maximum product. The array may contain positive
numbers, negative numbers, and zeros, and is guaranteed to have at least
three elements.

**Examples**

| Input | Output | Why |
|-------|--------|-----|
| `[1, 2, 3, 4]` | `24` | 2 × 3 × 4 |
| `[-9, -8, 1, 2, 3]` | `216` | (-9) × (-8) × 3 — two negatives flip positive |
| `[-1, -2, -3]` | `-6` | Three values closest to zero |

## Intuition

The tempting answer is "take the three biggest numbers." That works for
all-positive lists, but breaks the moment large negatives appear, because
**two negatives multiply into a positive**.

After sorting, every candidate for the answer lives at the two ends of the
list ("Two Corners"):

1. The **three largest** numbers, or
2. The **two smallest** numbers (possibly big negatives) times the **largest**.

Nothing in the middle can ever win — the extremes control both magnitude and
sign. So we only ever compare two products.

## Approach

1. Sort the array.
2. Compute Candidate A: `nums[-1] * nums[-2] * nums[-3]`.
3. Compute Candidate B: `nums[0] * nums[1] * nums[-1]`.
4. Return `max(A, B)`.

This handles negatives, zeros, and all-negative lists with no special cases.

## Python Solution

```python
def maximum_product(nums: list[int]) -> int:
    """Return the largest product obtainable from any three numbers in nums."""
    nums.sort()
    top_three = nums[-1] * nums[-2] * nums[-3]          # three largest
    two_smallest_and_largest = nums[0] * nums[1] * nums[-1]  # negative pair play
    return max(top_three, two_smallest_and_largest)
```

### Optional: O(n) one-pass (no sort)

```python
def maximum_product_no_sort(nums: list[int]) -> int:
    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")
    for n in nums:
        if n >= max1:   max1, max2, max3 = n, max1, max2
        elif n >= max2: max2, max3 = n, max2
        elif n >= max3: max3 = n
        if n <= min1:   min1, min2 = n, min1
        elif n <= min2: min2 = n
    return max(max1 * max2 * max3, min1 * min2 * max1)
```

## Complexity

| Solution | Time | Space |
|----------|------|-------|
| Sort-based | `O(n log n)` | `O(1)` extra |
| One-pass scan | `O(n)` | `O(1)` |
| Brute force | `O(n³)` | `O(1)` |

## Video

▶️ Watch the full walkthrough: (video link coming soon)

## Article

Full write-up with dry runs, edge cases, and common mistakes is available in
the accompanying article. Part of the **Fun with Learning Technology** series.
