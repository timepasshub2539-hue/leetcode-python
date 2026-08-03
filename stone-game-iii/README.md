# Stone Game III

## Problem

Alice and Bob take turns removing 1, 2, or 3 stones from the front of a row
of stones, where each stone has an integer value (possibly negative). Alice
moves first. Both players play optimally. Given the stone values, determine
whether "Alice", "Bob", or "Tie" is the result.

- Row length up to 50,000.
- Stones can only be taken from the front — never the middle or back.

## Intuition

Greedy ("take as many stones as possible") fails. Example: `[1, 2, 3, 7]` —
grabbing the first three piles banks 6 points but leaves the opponent the
lone 7, and they win. What matters isn't how many stones you take, it's what
you leave behind.

Rather than tracking two separate scores, track a single number: the gap
between the current player's best outcome and the opponent's, from a given
position onward. This works identically regardless of whose turn it is,
since the DP never names Alice or Bob — only "current player" vs. "the
other player."

## Approach

Define `dp[i]` = best score gap achievable by whoever moves first starting
at stone `i`, with `dp[n] = 0` (empty row).

Fill `dp` backward, from `i = n - 1` down to `0`. At each `i`, try taking
1, 2, or 3 stones:

```
candidate = sum(stones taken) - dp[i + stones_taken]
dp[i] = max over all candidates
```

The subtraction reflects that after this move, the remaining row becomes
the opponent's problem, and their best gap counts against you.

Answer: sign of `dp[0]`. Positive → Alice, negative → Bob, zero → Tie.

## Python Solution

```python
from typing import List


def stone_game_iii(stone_value: List[int]) -> str:
    n = len(stone_value)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        best = float("-inf")
        take = 0
        for k in range(3):
            if i + k >= n:
                break
            take += stone_value[i + k]
            best = max(best, take - dp[i + k + 1])
        dp[i] = best

    if dp[0] > 0:
        return "Alice"
    if dp[0] < 0:
        return "Bob"
    return "Tie"
```

## Complexity

- **Time:** O(n) — constant work per position.
- **Space:** O(n) for the DP array (reducible to O(1), since `dp[i]` only
  depends on the next three slots).

## Video

Full walkthrough with a hand-traced dry run and the three most common
beginner mistakes: (video link coming soon)

## Article

Full write-up with intuition, brute force comparison, and edge cases: see
the accompanying blog post linked in the video description.
