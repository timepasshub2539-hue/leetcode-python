# LeetCode 115 — Distinct Subsequences (Python)

## Problem

Given two strings `s` and `t`, return the number of distinct subsequences of
`s` that equal `t`. A subsequence is formed by deleting some (or no)
characters from `s` without changing the relative order of the remaining
characters.

**Constraints:** `1 <= s.length, t.length <= 1000`. The answer fits in a
32-bit signed integer.

**Example**

```
Input:  s = "rabbbit", t = "rabbit"
Output: 3
```

`rabbbit` has three b's; `rabbit` only needs two, so any pair of the three
b's produces a valid match — three distinct deletions in total.

## Intuition

Walk through `s` one character at a time. At each position, ask whether it
matches the next character still needed from `t`:

- No match → forced skip.
- Match → choice: use it, or skip it and hope a later occurrence works.

Recursing on this directly re-solves the same `(i, j)` position pairs
repeatedly. Caching those results — either top-down or as a bottom-up table —
removes the redundant work.

## Approach

Build a grid `dp[i][j]` = number of ways to form `t[:j]` from `s[:i]`.

- `dp[i][0] = 1` for all `i` — an empty target has exactly one way to form
  (delete everything).
- `dp[0][j] = 0` for `j > 0` — an empty source can't produce a non-empty
  target.
- `dp[i][j] = dp[i-1][j]`, plus `dp[i-1][j-1]` if `s[i-1] == t[j-1]`.

The final answer is `dp[len(s)][len(t)]`. Since each row only depends on the
row above it, the table rolls down to a single array of length `len(t) + 1`,
updated right to left.

## Python Solution

```python
def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]

    return dp[m][n]


def num_distinct_optimized(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]

    return dp[n]
```

## Complexity

| | Time | Space |
|---|---|---|
| Brute force (recursion) | O(2^m) | O(m) |
| 2D DP | O(m · n) | O(m · n) |
| Rolled-down DP | O(m · n) | O(n) |

`m = len(s)`, `n = len(t)`. Every `(i, j)` pair is computed exactly once, so
the polynomial bound is tight.

## Video

Full video walkthrough, including the recursive call tree and a timed
brute-force-vs-optimal comparison: (video link coming soon)

## Article

Full writeup with dry run, edge cases, and interview follow-ups: see the
accompanying article in this repo / linked from the video description.
