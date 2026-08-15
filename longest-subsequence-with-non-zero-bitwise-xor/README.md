# Longest Subsequence With Non-Zero XOR (LeetCode 3702)

## Problem

Given an array of integers, find the length of the longest subsequence
(elements in original order, any subset) whose XOR is nonzero. Return 0
if no such subsequence exists.

## Intuition

Don't reason about subsequences directly — reason about the XOR of the
whole array.

- If the total XOR of the array is nonzero, the entire array is already
  a valid answer.
- If the total XOR is zero, removing any single nonzero element flips
  the total away from zero (since `x XOR x = 0`), giving length `n - 1`.
- If every element is zero, no subsequence can ever produce a nonzero
  XOR, so the answer is 0.

## Approach

1. XOR every element together in one pass.
2. If the total is nonzero, return `n`.
3. If the total is zero and at least one element is nonzero, return `n - 1`.
4. If every element is zero, return `0`.

## Python Solution

\`\`\`python
from functools import reduce
from operator import xor


def longest_subsequence(nums: list[int]) -> int:
    total = reduce(xor, nums, 0)

    if total != 0:
        return len(nums)

    if any(nums):
        return len(nums) - 1

    return 0
\`\`\`

## Complexity

- **Time:** O(n) — one pass to compute the total XOR.
- **Space:** O(1) — a single running variable.

## Video

Full walkthrough with dry run and quiz: (video link coming soon)

## Article

Full written breakdown: see the linked article on the Fun with Learning
Technology Substack.
