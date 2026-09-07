# LeetCode 940 — Distinct Subsequences II

## Problem

Given a string `s` of lowercase English letters, count the number of
**distinct** non-empty subsequences of `s`. Return the answer modulo
`1_000_000_007`.

A subsequence is any sequence obtainable by deleting zero or more
characters from `s` without reordering the remaining characters.

## Intuition

Track a running total `dp` of distinct subsequences seen so far. Each new
character can either be skipped (keep existing subsequences) or appended to
every existing subsequence (doubles the count), plus stand alone as a new
one-character subsequence:

```
dp = 2 * dp + 1
```

This is exact only if the character has never appeared before. If it has,
doubling regenerates subsequences that already existed as of that letter's
previous appearance. Subtract exactly that prior count to correct for it.

## Approach

Maintain:
- `dp`: running count of distinct subsequences.
- `last[26]`: the value `dp` was updated to right after each letter's most
  recent occurrence.

For each character:
1. Compute `new_dp = 2 * dp + 1 - last[idx]` (mod arithmetic throughout).
2. Update `last[idx] = new_dp`.
3. Set `dp = new_dp`.

Return `dp % MOD` after the loop.

## Python Solution

```python
MOD = 10**9 + 7


def distinct_subseq_ii(s: str) -> int:
    dp = 0
    last = [0] * 26

    for ch in s:
        idx = ord(ch) - ord('a')
        new_dp = (2 * dp + 1 - last[idx]) % MOD
        last[idx] = new_dp
        dp = new_dp

    return dp % MOD
```

## Complexity

- **Time:** O(n) — single pass over the string.
- **Space:** O(1) — fixed 26-element array regardless of input size.

## Video

Full walkthrough with a live brute-force timing comparison:
(video link coming soon)

## Article

Complete write-up with dry run, complexity proof, and common mistakes:
(video link coming soon)
