# Stone Game — LeetCode Solution (Python)

## Problem

Alice and Bob take turns picking up whole piles of stones from either end of
a row (never the middle). There's an even number of piles, and the total is
guaranteed odd, so no ties are possible. Both play optimally. Does Alice end
up with more stones than Bob?

## Intuition

The total number of stones never changes no matter who takes what — so
instead of tracking each player's raw score, track the *gap* between them.
This turns the problem into a clean interval DP: `dp[i][j]` is the best gap
a player can guarantee on the range of piles `[i, j]`.

## Approach

- Base case: a single pile — take it, gap equals its value.
- Recurrence: `dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])`
- Fill the table by increasing slice length, since larger ranges depend on
  smaller ones.
- Answer: `dp[0][n-1] > 0`

## Python Solution

```python
def stoneGame(piles: list[int]) -> bool:
    n = len(piles)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = piles[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

    return dp[0][n - 1] > 0
```

## Complexity

- Time: O(n²) — one computation per range `(i, j)`
- Space: O(n²) — the full table is needed since ranges are reused

## Video

Full walkthrough with a hand-traced dry run: (video link coming soon)

## Article

Written breakdown with intuition, brute force comparison, and the O(1)
parity shortcut: see the linked article.
