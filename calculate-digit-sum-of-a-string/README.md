# LeetCode 2243 — Calculate Digit Sum of a String

## Problem

Given a string `s` of digits and an integer `k`:
1. Split `s` into groups of `k` consecutive characters (the last group may be shorter).
2. Replace each group with the sum of its digits.
3. Join the results into a new string.
4. Repeat while the string's length is greater than `k`.
5. Return the final string once its length is ≤ `k`.

## Intuition

The key realization: a group like `"346"` must be reduced to the **sum of its digits** (3+4+6=13), not interpreted as the number 346. Once that's clear, the solution splits into two independent pieces — a digit-sum helper for a single chunk, and an outer loop that keeps re-grouping and re-summing until the string is short enough. No need to precompute the number of rounds; a simple `while len(s) > k` loop converges on its own since the string shrinks every round.

## Approach

1. Write a helper that walks a chunk character by character, checks `isdigit()`, and sums the valid digits.
2. In a loop, slice the current string into chunks of size `k` using `range(0, len(s), k)`.
3. Reduce each chunk via the helper, collect the string results, and join them.
4. Repeat until `len(s) <= k`, then return.

## Python Solution

\`\`\`python
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def group_sum(chunk: str) -> int:
            total = 0
            for ch in chunk:
                if ch.isdigit():
                    total += int(ch)
            return total

        while len(s) > k:
            pieces = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                pieces.append(str(group_sum(chunk)))
            s = "".join(pieces)

        return s
\`\`\`

## Complexity

- **Time**: O(n) per round; the string shrinks every round and `s` is capped at 100 characters, so the total work stays effectively linear.
- **Space**: O(n) per round for the rebuilt string.

## Video

Full walkthrough with a live trace and quiz rounds: (video link coming soon)

## Article

Written breakdown with brute force vs optimal comparison, dry run, and interview follow-ups: (video link coming soon)
