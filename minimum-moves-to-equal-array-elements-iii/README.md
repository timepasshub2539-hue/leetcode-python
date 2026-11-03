# LeetCode 3736 — Minimum Moves to Equal Array Elements III

## Problem

Given an array of integers, you may repeatedly pick any single element and
increase it by 1. Decreasing is not allowed. Find the minimum total number
of moves needed to make every element in the array equal.

## Intuition

This problem is easy to mis-solve by pattern-matching it to its sibling,
*Minimum Moves to Equal Array Elements II*, where moves go in both
directions and the median minimizes total distance. Here, moves are
one-directional (increase only), so the median is often unreachable — it
can require the current maximum to decrease, which isn't a legal move.

Since nothing can decrease, the only value every element can legally reach
is the array's current maximum. It costs zero moves for itself and is the
lowest common target reachable by every other element.

## Approach

1. Find `mx = max(nums)` — one linear pass.
2. Sum `mx - x` for every `x` in `nums` — a second linear pass.
3. Return the total.

No sorting, no median, no search over candidate targets.

## Python Solution

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mx = max(nums)
        return sum(mx - x for x in nums)
```

## Complexity

- **Time:** O(n) — two linear passes over the array.
- **Space:** O(1) — only a running max and running sum are kept.

## Video

Full derivation, including why the median trick fails here and a couple of
quiz checks along the way: (video link coming soon)

## Article

Full write-up with brute force comparison, dry run, and interview
follow-ups: see the linked article in this repo / channel.
