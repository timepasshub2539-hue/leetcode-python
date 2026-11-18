# LeetCode 2914 — Minimum Number of Changes to Make Binary String Beautiful

## Problem

Given a binary string `s` of even length, you may flip any characters.
The string is "beautiful" if it can be split into blocks where each block
has even length and contains only one repeated character (`0` or `1`).
Return the minimum number of flips required to make `s` beautiful.

## Intuition

The even-length guarantee means the string can always be walked in fixed
pairs: `(0,1)`, `(2,3)`, `(4,5)`, ... Each pair only depends on its own two
characters — fixing one pair never changes what another pair needs. That
independence means no dynamic programming is required: just score each
pair and sum.

## Approach

- Stride through the string two characters at a time.
- A pair that already matches (`00` or `11`) costs 0 flips.
- A mismatched pair (`01` or `10`) costs exactly 1 flip.
- Sum the costs across all pairs — that sum is the answer.

## Python Solution

\`\`\`python
def min_changes(s: str) -> int:
    changes = 0
    for i in range(0, len(s), 2):
        if s[i] != s[i + 1]:
            changes += 1
    return changes
\`\`\`

## Complexity

- **Time:** O(n) — single linear pass over the string.
- **Space:** O(1) — one counter, no auxiliary structures.

## Video

Full walkthrough with dry run, quizzes, and common mistakes: (video link coming soon)

## Article

Written breakdown covering intuition, brute force vs. optimal approach,
edge cases, and interview follow-ups: see the linked article above.
