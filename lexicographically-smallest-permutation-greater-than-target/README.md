# LeetCode 3720 — Lexicographically Smallest Permutation Greater Than Target

## Problem

Given two lowercase strings `s` and `target` of equal length, rearrange the
letters of `s` into the lexicographically smallest string that is strictly
greater than `target`. If no such rearrangement exists, return an empty string.

`s` can be rearranged freely. `target` is fixed and is not necessarily a
permutation of `s` — it may use different letters or different letter counts.

## Intuition

This is a variant of the classic "next permutation" problem. For a plain
digit sequence, the pattern is:

1. Scan right to left for the last position where a bigger arrangement is
   still possible (the **pivot**).
2. Swap the pivot with the smallest value to its right that's still bigger
   than it.
3. Reverse everything after the pivot to get the smallest possible tail.

Here, since `target` may not share `s`'s letter frequencies, we replace the
pivot scan with a **letter-count** check: at each prefix length, track
whether `s` actually has enough letters to build that prefix of `target`.

## Approach

1. Count every letter in `s` with `Counter`.
2. Tentatively consume `target`'s letters for every position except the
   last, tracking how many letters go into shortfall (`neg`).
3. Walk backward from the end. At each position where `neg == 0` (the
   prefix is buildable), search upward from `target[i]` for the smallest
   available letter that's bigger. If found, swap it in and append all
   remaining letters in ascending order — that's the answer.
4. If no position works, return `""`.

## Python Solution

```python
from collections import Counter


def smallest_string_greater_than_target(s: str, target: str) -> str:
    n = len(s)
    counts = Counter(s)
    neg = 0

    for i in range(n - 1):
        counts[target[i]] -= 1
        if counts[target[i]] < 0:
            neg += 1

    for i in range(n - 1, -1, -1):
        if neg == 0:
            for c in range(ord(target[i]) + 1, ord('z') + 1):
                letter = chr(c)
                if counts[letter] > 0:
                    counts[letter] -= 1
                    remaining = sorted(counts.elements())
                    return "".join(target[:i]) + letter + "".join(remaining)

        if i > 0:
            counts[target[i - 1]] += 1
            if counts[target[i - 1]] > 0:
                neg -= 1

    return ""
```

## Complexity

- **Time:** O(n log n) — a fixed 26-letter check per position, dominated by
  a single final sort of the remaining letters.
- **Space:** O(n) for the letter counts and output string.

## Video

Full walkthrough with a brute-force vs. optimal timing comparison and a
quiz: (video link coming soon)

## Article

Full write-up with dry run, complexity analysis, and interview follow-ups:
see the accompanying article.
