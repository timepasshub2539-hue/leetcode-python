# LeetCode 1510 — Stone Game IV (Python Solution)

## Problem
Alice and Bob take turns removing a **perfect square** number of stones from
a pile of `n` stones. Alice moves first. If a player cannot make a legal
move (the pile is empty), they lose. Determine whether Alice wins, assuming
both players play optimally.

**Constraints:** `1 <= n <= 10^5`

## Intuition
A pile size is a **winning** state if there exists at least one perfect
square you can remove that leaves your opponent in a **losing** state. You
only need one such move — not all of them. This "loser flip" recurrence
means each pile size depends only on smaller pile sizes already solved,
which is the classic signal for dynamic programming.

## Approach
Build a boolean table `dp` where `dp[i]` is `True` if the player about to
move wins with `i` stones remaining.

1. `dp[0] = False` — no stones, no move, automatic loss.
2. For each `i` from `1` to `n`, try every square `j*j <= i`.
3. If `dp[i - j*j]` is `False`, set `dp[i] = True` and stop checking further
   squares for this `i`.
4. Return `dp[n]`.

Filling the table left to right guarantees every dependency is already
solved before it's needed — no repeated subproblems, no exponential tree.

## Python Solution

```python
def winner_square_game(n: int) -> bool:
    """Return True if the player who moves first wins with n stones."""
    dp = [False] * (n + 1)

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            if not dp[i - j * j]:
                dp[i] = True
                break
            j += 1

    return dp[n]
```

## Complexity
- **Time:** O(n√n) — each pile size `i` checks roughly `√i` perfect squares.
- **Space:** O(n) — one boolean table, no recursion stack.

## Video
Full derivation, hand-worked dry runs (n=7, n=5), and two live quiz rounds:
(video link coming soon)

## Article
Full write-up with brute force comparison, complexity analysis, common
mistakes, and related problems: see the linked blog post.
