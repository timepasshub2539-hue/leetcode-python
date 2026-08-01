# Predict the Winner — Python Minimax / DP Solution

## Problem

Two players alternate turns taking a number from either end of an array
(Player 1 goes first). Both play optimally. Can Player 1 guarantee a final
score greater than or equal to Player 2's? A tie counts as a win for
Player 1.

## Intuition

Track a single value — my score minus the opponent's — instead of two
separate scores. Because the game is fixed-sum, anything one player gains
is exactly what the other didn't get. This collapses the two-player
problem into a single-number recursive question.

Define `dp(i, j)` as the best score-difference the player whose turn it is
can force, given only the sub-array `nums[i..j]`.

```
dp(i, j) = max(nums[i] - dp(i+1, j), nums[j] - dp(i, j-1))
dp(i, i) = nums[i]
```

We subtract because `dp(i+1, j)` / `dp(i, j-1)` represents the *opponent's*
best forced outcome — their advantage is our disadvantage.

## Approach

1. Recursively define `dp(i, j)` as above.
2. Memoize with `functools.lru_cache` so each `(i, j)` pair is computed once.
3. Player 1 wins if `dp(0, n-1) >= 0`.

## Python Solution

```python
from functools import lru_cache
from typing import List


def predict_winner(nums: List[int]) -> bool:
    @lru_cache(None)
    def dp(i: int, j: int) -> int:
        if i == j:
            return nums[i]

        pick_left = nums[i] - dp(i + 1, j)
        pick_right = nums[j] - dp(i, j - 1)
        return max(pick_left, pick_right)

    return dp(0, len(nums) - 1) >= 0


if __name__ == "__main__":
    assert predict_winner([1, 5, 233, 7]) is True
    assert predict_winner([2, 2]) is True   # tie counts as a win
    assert predict_winner([1, 5, 2]) is False
    print("all checks passed")
```

## Complexity

- **Time:** O(n²) — one computation per distinct `(i, j)` pair, memoized.
- **Space:** O(n²) for the cache, O(n) for the recursion stack.

## Video

Full walkthrough with a cell-by-cell dry run: (video link coming soon)

## Article

Full written breakdown with intuition, dry run, and common mistakes:
see the accompanying article.
