# Maximum Product of Two Digits

## Problem

Given a positive integer, find the two digits inside it that produce the
largest possible product when multiplied together. If a digit appears more
than once in the number, it may be used twice.

**Example**
```
Input:  124
Digits: 1, 2, 4
Output: 8   (2 * 4)
```

## Intuition

Maximizing the product of two non-negative digits only requires maximizing
each digit independently — you don't need to check every pair, just find
the largest and second-largest digit values.

## Approach

1. Convert the number to its digits.
2. Track two running values, `max1` and `max2`, both starting at 0.
3. For each digit:
   - If it's greater than `max1`, promote it to `max1` and demote the old
     `max1` into `max2`.
   - Otherwise, if it's greater than `max2`, it becomes the new `max2`.
4. Return `max1 * max2`.

This finds the top two digits in a single pass, without comparing every
possible pair.

## Python Solution

```python
def max_product_of_two_digits(number: int) -> int:
    max1 = max2 = 0
    for char in str(number):
        digit = int(char)
        if digit > max1:
            max1, max2 = digit, max1
        elif digit > max2:
            max2 = digit
    return max1 * max2
```

## Complexity

| Approach     | Time  | Space |
|--------------|-------|-------|
| Brute force  | O(n²) | O(n)  |
| Optimal      | O(n)  | O(1)  |

n = number of digits (at most ~10 for typical inputs).

## Video

Full walkthrough with a leaderboard analogy and step-by-step trace: (video link coming soon)

## Article

Full write-up including brute force, optimal solution, dry run, edge cases,
and common mistakes: see the linked blog post / Substack article.
