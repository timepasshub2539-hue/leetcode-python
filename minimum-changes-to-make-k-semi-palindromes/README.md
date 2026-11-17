# LeetCode 2911 — Minimum Changes to Make K Semi-Palindromes

## Problem

Given a string `s` and an integer `k`, split `s` into exactly `k` contiguous
pieces. Each piece may have characters changed so it becomes a
**semi-palindrome**: pick a divisor `d` (`1 <= d < length`, `d` evenly
divides `length`), group characters by index modulo `d`, and require each
group to read the same forwards and backwards. Return the minimum total
character changes across all `k` pieces.

## Intuition

`d` defines an **interleaved grouping**, not a contiguous chunk size — index
`0` groups with index `d`, which groups with `2d`, and so on. Once that's
clear, the problem splits into two independent layers:

1. **Local cost** — for any one substring, the minimum changes needed to
   become a semi-palindrome, found by trying every valid divisor.
2. **Global split** — a standard partition DP that picks cut points to
   minimize the sum of local costs.

## Approach

1. Build an `n x n` table `cost[i][j]`: minimum changes to make `s[i..j]`
   a semi-palindrome, by trying every valid divisor and counting mismatches
   in each interleaved group against its own reverse.
2. Run a partition DP: `dp[i][kk] = min(dp[j][kk-1] + cost[j][i-1])` over
   every earlier cut point `j`.
3. Answer is `dp[n][k]`.

## Python Solution

```python
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        def cost(i: int, j: int) -> int:
            m = j - i + 1
            if m == 1:
                return 0
            best = m
            for d in range(1, m):
                if m % d != 0:
                    continue
                total = 0
                for r in range(d):
                    group = s[i + r:j + 1:d]
                    half = len(group) // 2
                    for a in range(half):
                        if group[a] != group[-(a + 1)]:
                            total += 1
                best = min(best, total)
            return best

        cost_table = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                cost_table[i][j] = cost(i, j)

        INF = float("inf")
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for kk in range(1, k + 1):
                for j in range(kk - 1, i):
                    if dp[j][kk - 1] == INF:
                        continue
                    dp[i][kk] = min(dp[i][kk], dp[j][kk - 1] + cost_table[j][i - 1])

        return dp[n][k]
```

## Complexity

- **Time:** `O(n^3)` for building the cost table, `O(n^2 * k)` for the DP —
  dominated by the cost table, fast for `n <= 200`.
- **Space:** `O(n^2)` for the cost table and `O(n * k)` for the DP table.

## Video

Full walkthrough with a timed brute-force-vs-optimal comparison: (video link coming soon)

## Article

Written breakdown with examples, dry run, and edge cases: see the full article
linked in the video description.
