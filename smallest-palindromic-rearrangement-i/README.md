# Smallest Palindromic Rearrangement I (LeetCode)

## Problem
Given a string that is already a palindrome, rearrange its letters to form the
**alphabetically smallest** palindrome possible using the same letters.

Example: `"babab"` → `"abbba"`

## Intuition
A palindrome is completely determined by its left half — the right half is
always just a mirrored copy. So instead of solving for the whole string, solve
for the smallest possible *left half*, then mirror it.

Since the input is guaranteed to be a palindrome, **at most one letter** can
have an odd count. That letter belongs in the exact center; every other
letter's count splits evenly across the two halves.

## Approach
1. Count each letter's frequency (`collections.Counter`).
2. Iterate letters alphabetically. The one odd-count letter becomes the
   middle character; every other letter contributes `count // 2` to the half.
3. Return `half + middle + reversed(half)`.

## Python Solution
```python
from collections import Counter


def smallest_palindrome(s: str) -> str:
    counts = Counter(s)
    half_chars = []
    middle_char = ""

    for letter in sorted(counts):
        count = counts[letter]
        if count % 2 == 1:
            middle_char = letter
        half_chars.append(letter * (count // 2))

    half = "".join(half_chars)
    return half + middle_char + half[::-1]
```

## Complexity
- **Time:** O(n) — counting and building are each a single linear pass.
- **Space:** O(n) — for the counter and the resulting string.

Brute force (generate all permutations, filter palindromes, sort) costs
O(n!) and is infeasible past small inputs.

## Video
Full walkthrough with a live dry run: (video link coming soon)

## Article
Complete write-up with brute force comparison, edge cases, and interview
follow-ups: see the linked article in this repo's description.
