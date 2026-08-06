# LeetCode 3345 — Smallest Divisible Digit Product I

## Problem

Given two integers `n` and `t`, find the smallest integer greater than or
equal to `n` such that the product of its digits is divisible by `t`.

## Intuition

Brute force — scanning forward from `n` — looks risky at first glance because
it's not obviously bounded. It turns out to be provably fast: in any 10
consecutive integers, one always ends in `0`. A trailing zero makes the digit
product `0`, and `0` is divisible by every valid `t` in this problem's range.
That guarantees an answer within 9 steps past `n`, no matter what `t` is.

## Approach

1. Start at `candidate = n`.
2. Compute the digit product of `candidate`.
3. If `product % t == 0`, return `candidate`.
4. Otherwise increment `candidate` and repeat.

The loop is guaranteed to terminate within 10 iterations.

## Python Solution

\`\`\`python
def smallest_number(n: int, t: int) -> int:
    candidate = n
    while True:
        product = 1
        for digit_char in str(candidate):
            product *= int(digit_char)
        if product % t == 0:
            return candidate
        candidate += 1
\`\`\`

## Complexity

- **Time:** O(1) — bounded by the guaranteed trailing-zero within 10 numbers.
- **Space:** O(1) — no auxiliary storage.

## Video

Full walkthrough with dry run and quiz: (video link coming soon)

## Article

Full written breakdown with brute-force vs. optimal analysis, edge cases,
and common mistakes: see the accompanying article in this repo/blog.
