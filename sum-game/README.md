# LeetCode 2029 — Sum Game (Python)

## Problem

Given a string `num` of even length containing digits and `?` characters,
Alice and Bob alternately replace each `?` with a digit `0-9`, Alice first,
until the string is complete. Split the finished string in half. Bob wins if
the two halves have equal digit sums; Alice wins if they don't. Both play
optimally. Determine the winner.

## Intuition

Track a single value: `diff = left_sum - right_sum`. Because digits are
bounded to 0-9, any move one player makes can always be exactly cancelled by
the other player choosing the complementary digit. That guarantee converts
the problem from game-tree search into pure counting: only the existing sum
difference and the gap in blank counts between the two halves matter.

## Approach

1. Split the string at the midpoint.
2. Count blanks (`?`) in each half; sum the fixed digits in each half.
3. If total blanks is odd, Alice wins outright (an unpaired move always
   exists).
4. Otherwise, Bob wins only if `diff == 9 * (leftBlanks - rightBlanks) / 2`.

## Python Solution

```python
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left, right = num[:half], num[half:]

        left_blanks = left.count('?')
        right_blanks = right.count('?')
        left_sum = sum(int(c) for c in left if c != '?')
        right_sum = sum(int(c) for c in right if c != '?')

        total_blanks = left_blanks + right_blanks
        if total_blanks % 2 == 1:
            return True

        diff = left_sum - right_sum
        blank_gap = left_blanks - right_blanks

        return diff != 9 * blank_gap // 2
```

## Complexity

- **Time:** O(n) — one linear scan of the string.
- **Space:** O(n) from slicing (reducible to O(1) with an index-based single pass).

## Video

Full derivation, proof, and dry run: (video link coming soon)

## Article

Full write-up with intuition, brute force comparison, and edge cases:
see the accompanying article in this repo / linked from the video description.
