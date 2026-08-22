# LeetCode 3622 — Check Divisibility by Digit Sum and Product

## Problem

Given a positive integer `n`, compute the sum of its digits (digit sum) and the
product of its digits (digit product). Add the two together. Return `true` if
`n` is divisible by that combined total, otherwise `false`.

**Constraints:** `1 <= n <= 10^6`

## Intuition

This is a single pass over the digits of `n`: accumulate a running sum and a
running product together, then perform one combined divisibility check at the
end. No special-casing is needed for a zero digit — the digit sum of any
positive number is always at least 1, so `sum + product` can never be zero.

## Approach

1. Copy `n` into a working variable `temp` (since `n` is needed intact later).
2. While `temp > 0`: extract the last digit with `temp % 10`, fold it into
   `digit_sum` and `digit_product`, then shrink `temp` with `temp // 10`.
3. Add `digit_sum + digit_product` into `total`.
4. Return `n % total == 0`.

## Python Solution

```python
def check_divisibility(n: int) -> bool:
    digit_sum = 0
    digit_product = 1
    temp = n

    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        digit_product *= digit
        temp //= 10

    total = digit_sum + digit_product
    return n % total == 0
```

## Complexity

- **Time:** O(log n) — at most 7 iterations for `n <= 1,000,000`.
- **Space:** O(1) — a fixed number of integer counters.

## Video

Full walkthrough with a hand-traced example, code build, and quizzes: (video link coming soon)

## Article

Complete write-up with dry run, edge cases, and interview follow-ups:
see the accompanying blog post in this repo / linked from the video description.
