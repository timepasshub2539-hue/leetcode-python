# Smallest Divisible Digit Product II (LeetCode 3348)

## Problem

Given a number `num` (as a string, up to 200,000 digits) and an integer `t`,
find the smallest integer greater than or equal to `num` such that:

- it contains no digit `0`, and
- the product of its digits is divisible by `t`.

Return `-1` if no such number exists.

## Intuition

Every digit is between 1 and 9, so a number of fixed length has a hard
ceiling on the digit product it can produce. No digit ever contributes a
prime factor larger than 7 — this is the **Nine Cap**. Two consequences:

1. If `t`, after removing all factors of 2, 3, 5, and 7, has anything left
   over, no number of any length can ever satisfy it. Return `-1`.
2. Otherwise, you don't need to search for the answer — you can build it,
   left to right, keeping as much of `num` as possible.

## Approach

1. Factor `t` into counts of 2, 3, 5, 7. Any leftover prime factor → `-1`.
2. If `num` already satisfies the requirement, return it as-is.
3. Walk `num` left to right, keeping each digit as long as the remaining
   suffix can still cover the outstanding requirement (checked via a small
   cached subproblem: minimum digits needed for N more 2s and M more 3s,
   accounting for digit 6 supplying one of each at once).
4. At the first digit that can't be kept, bump it to the smallest value that
   keeps the suffix feasible, then greedily fill every digit after it.
5. If no digit works at the current length, grow the length by one and
   retry.

## Python Solution

See [`solution.py`](./solution.py) for the full implementation, including:

- `factor_requirement` — strips 2/3/5/7 out of `t`.
- `min_digits_needed` — cached minimum-digit subproblem for 2s/3s.
- `feasible_suffix` — checks whether N remaining slots can cover a
  requirement.
- `smallest_valid_at_length` — the greedy left-to-right construction.
- `smallest_divisible_digit_product` — orchestrates the full solution.

## Complexity

- **Time:** O(L), where L is the length of `num` — each position is
  resolved in O(1) amortized time against a small, cached lookup table.
- **Space:** O(L) for the digit array, plus a bounded-size cache.

This replaces the brute-force approach's effectively exponential candidate
count (up to 9^L in the worst case) with a single linear pass.

## Video

Full walkthrough, including a live trace to `1488` and a two-round quiz:
(video link coming soon)

## Article

Full write-up with dry run, complexity proof, and common mistakes:
(video link coming soon)
