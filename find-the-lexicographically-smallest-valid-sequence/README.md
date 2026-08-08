# Lexicographically Smallest Valid Sequence (LeetCode 3302)

## Problem

Given two strings `word1` and `word2`, find the lexicographically smallest
list of increasing indices into `word1` such that the characters at those
indices spell `word2` exactly, or differ from `word2` in at most one
position. Return `[]` if no such sequence exists.

## Intuition

Walk both strings forward with two pointers. Take every free match
immediately — it never costs anything. On a mismatch, you may spend your
one allowed "swap," but only if the rest of `word1` can still complete the
rest of `word2` afterward. That feasibility check, done naively, requires
rescanning ahead each time — expensive. Precomputing it once from the back
turns it into an O(1) lookup.

## Approach

1. **Backward pass:** build `suffix[i]`, the count of trailing characters
   of `word2` that can still be matched using `word1[i:]`.
2. **Forward pass:** walk `word1`. Take free matches immediately. On a
   mismatch, spend the one allowed swap only if `suffix[i + 1]` covers
   everything still needed of `word2`.

## Python Solution

\`\`\`python
def valid_sequence(word1: str, word2: str) -> list[int]:
    n, m = len(word1), len(word2)

    suffix = [0] * (n + 1)
    j = m - 1
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1]
        if j >= 0 and word1[i] == word2[j]:
            suffix[i] += 1
            j -= 1

    result = []
    j = 0
    swapped = False

    for i in range(n):
        if j == m:
            break
        if word1[i] == word2[j]:
            result.append(i)
            j += 1
        elif not swapped and suffix[i + 1] >= m - j - 1:
            result.append(i)
            j += 1
            swapped = True

    return result if j == m else []
\`\`\`

## Complexity

- **Time:** O(n + m) — one backward pass, one forward pass.
- **Space:** O(n) for the suffix array.

## Video

Full walkthrough with a hand-traced dry run and complexity comparison
against brute force: (video link coming soon)

## Article

Full write-up with intuition, dry run, and edge cases:
see the accompanying article in this repository / linked post.
