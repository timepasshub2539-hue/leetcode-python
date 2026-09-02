# LeetCode 3875 — Construct Uniform Parity Array I

## Problem

Given an array of distinct integers, construct a new array of the same
length where every element has the same parity (all even or all odd).
For each position, you may either:

1. Keep the original value as-is, or
2. Replace it with the difference between it and another value from the
   original array.

Return `True` if a uniform-parity array can always be constructed,
`False` otherwise.

**Constraints:**
- `1 <= nums1.length <= 100`
- `1 <= nums1[i] <= 100`
- All values in `nums1` are distinct.

## Intuition

Two cases cover every input:

- **Already uniform** (all-even or all-odd): keep every value as-is.
- **Mixed parity:** subtraction mod 2 behaves like addition mod 2, so
  `even - odd` is always odd. Every even element can subtract any odd
  element and become odd; existing odd elements stay odd. The whole
  array can always be pushed to all-odd.

Since both cases succeed, the answer is always `True` — no array under
these constraints can fail.

## Approach

No traversal is needed. The array's contents never change the outcome,
so the function returns a constant value.

## Python Solution

```python
class Solution:
    def canConstruct(self, nums1: list[int]) -> bool:
        # Uniform arrays need no change; mixed arrays can always be
        # driven to all-odd since even - odd is always odd (mod 2).
        return True
```

## Complexity

- **Time:** O(1) — no loop over the input.
- **Space:** O(1) — no auxiliary storage.

Correctness follows directly from modular arithmetic: every possible
input configuration under the stated constraints resolves to `True`.

## Video

Full walkthrough with a traced example and quiz checkpoints: (video link coming soon)

## Article

Complete write-up with intuition, dry run, and complexity analysis:
see the accompanying article in this repository / linked in the video
description.
