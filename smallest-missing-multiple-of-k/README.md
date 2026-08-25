# LeetCode 3718 — Smallest Missing Multiple of K (Python)

## Problem

Given an array `nums` and a positive integer `k`, return the smallest
positive multiple of `k` that does not appear in `nums`.

## Intuition

The search space isn't "every integer" — it's only multiples of `k`
(`k, 2k, 3k, ...`). Since each value in `nums` can block at most one
multiple of `k`, the answer is guaranteed to appear within the first
`n + 1` multiples, where `n = len(nums)`.

The remaining question is how to check membership cheaply. Rescanning
the array for every candidate multiple is wasteful since the array
never changes — a hash set turns each check into O(1).

## Approach

1. Convert `nums` into a hash set, `claimed`.
2. Walk `multiple = k, 2k, 3k, ...`, checking `multiple in claimed`.
3. Return the first `multiple` not found in the set.

## Python Solution

```python
def smallest_missing_multiple(nums: list[int], k: int) -> int:
    """Return the smallest positive multiple of k not present in nums."""
    claimed = set(nums)

    multiple = k
    while multiple in claimed:
        multiple += k

    return multiple
```

## Complexity

- **Time:** O(n) — O(n) to build the set, O(n) worst-case walk (bounded
  by the pigeonhole argument above).
- **Space:** O(n) for the hash set.

## Video

Full walkthrough with a live test run and quizzes: (video link coming soon)

## Article

Full write-up with dry run, alternative approaches, and interview
follow-ups: see the linked article in this repo/description.
