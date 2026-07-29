# Smallest Palindromic Rearrangement II

## Problem

Given a palindrome string `s` and an integer `k`, find the k-th smallest
rearrangement of `s` (alphabetical order) that is also a palindrome. If
fewer than `k` such palindromes exist, return an empty string.

## Intuition

A palindrome is fully determined by its left half — the right half is
always the left half reversed. If a letter has an odd count, it becomes
the single middle character; every other letter splits evenly between
the two halves. This means the entire problem reduces to: rank
arrangements of the left half, then mirror.

## Approach

1. Count letter frequencies. Identify the (at most one) odd-count letter
   as the middle character; halve the rest to get the left-half counts.
2. Use the multinomial coefficient `L! / (c1! · c2! · ...)` to compute
   the total number of valid arrangements. If `k` exceeds this, return `""`.
3. Greedily build the left half one position at a time: for each
   candidate letter (alphabetical order), compute how many arrangements
   remain if that letter is placed next. If `k` fits within that count,
   commit; otherwise subtract the count from `k` and try the next letter.
4. Mirror the completed left half around the middle character to produce
   the final palindrome.

## Python Solution

```python
from collections import Counter
from math import factorial


def kth_palindrome_rearrangement(s: str, k: int) -> str:
    counts = Counter(s)

    middle = ""
    half_counts = {}
    for letter, count in counts.items():
        if count % 2 == 1:
            middle = letter
            count -= 1
        if count:
            half_counts[letter] = count // 2

    half_length = sum(half_counts.values())

    def arrangements(remaining_counts, remaining_length):
        total = factorial(remaining_length)
        for count in remaining_counts.values():
            total //= factorial(count)
        return total

    total_arrangements = arrangements(half_counts, half_length)
    if k > total_arrangements:
        return ""

    left_half = []
    remaining = dict(half_counts)
    remaining_length = half_length

    for _ in range(half_length):
        for letter in sorted(remaining):
            if remaining[letter] == 0:
                continue

            remaining[letter] -= 1
            remaining_length -= 1
            count = arrangements(remaining, remaining_length)

            if k <= count:
                left_half.append(letter)
                if remaining[letter] == 0:
                    del remaining[letter]
                break
            else:
                k -= count
                remaining[letter] += 1
                remaining_length += 1

    left_str = "".join(left_half)
    return left_str + middle + left_str[::-1]
```

## Complexity

- **Time:** O(n²) roughly — n/2 positions, each trying up to 26 letters
  with O(n) work per arrangement count.
- **Space:** O(n) for counters and the result string.

## Video

Full walkthrough: (video link coming soon)

## Article

Written breakdown with dry run and complexity analysis: see the linked
article on the blog.
