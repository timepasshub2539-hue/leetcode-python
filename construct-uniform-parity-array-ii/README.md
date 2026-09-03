# LeetCode 3876 — Construct Uniform Parity Array II

## Problem

Given an array `nums1` of `n` distinct integers, build a second array of the
same length where each position either:

- keeps the original value, or
- is replaced by the difference between it and some other, smaller value in
  the array (difference must be >= 1)

Every value in the resulting array must share one parity — all odd or all
even. Return whether such an array can be constructed.

## Intuition

Subtracting two same-parity numbers always yields an even result.
Subtracting two different-parity numbers always yields an odd result. That's
the entire mechanism.

Consequences:
- An even number can only become odd by subtracting a smaller odd number.
- If any odd number exists, the smallest odd number can never itself become
  even (nothing smaller and odd exists to subtract from it), so targeting
  "all-even" is dead the moment one odd number is present.
- The only viable target is "all-odd," and every even number's eligibility
  depends only on whether it's larger than the single smallest odd number in
  the array.

## Approach

1. Collect all odd numbers from `nums1`.
2. If there are none, the array is already all even — return `True`.
3. Find the smallest odd number.
4. Check every even number in `nums1` — if any is smaller than the smallest
   odd number, return `False`.
5. Otherwise, return `True`.

## Python Solution

```python
def canConstruct(nums1: list[int]) -> bool:
    odds = [x for x in nums1 if x % 2 == 1]

    if not odds:
        return True

    smallest_odd = min(odds)

    for x in nums1:
        if x % 2 == 0 and x < smallest_odd:
            return False

    return True
```

## Complexity

- **Time:** O(n) — two linear passes over the array (build odds list, verify
  evens), plus O(n) for `min()`.
- **Space:** O(n) for the odds list (O(1) extra with a single-pass generator
  variant).

## Video

Full walkthrough, timing comparison, and quiz: (video link coming soon)

## Article

Complete write-up with dry run, complexity proof, and alternative
approaches: see the accompanying article in this repo / linked from the
video description.
