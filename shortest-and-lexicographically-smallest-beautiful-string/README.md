# LeetCode 2904 — Shortest and Lexicographically Smallest Beautiful Substring

## Problem

Given a binary string `s` and an integer `k`, a substring is *beautiful* if it
contains exactly `k` ones. Find the shortest beautiful substring; if multiple
substrings share that minimum length, return the lexicographically smallest
one. If no beautiful substring exists, return an empty string.

## Intuition

For any fixed starting index, the first position where the running count of
ones reaches `k` is guaranteed to produce the shortest beautiful substring
starting there — the count only increases as the window grows, so continuing
past that point can never shorten the window. Checking every starting index
and comparing candidates (length first, then lexicographic order) covers all
cases without needing a shrinking two-pointer mechanism, which cannot
correctly track lexicographic ties across different starting points.

## Approach

1. For each starting index `i`, grow a window rightward, counting ones.
2. Stop as soon as the count hits `k` — record the candidate substring.
3. Compare against the best candidate seen so far: shorter length wins
   outright; equal lengths fall back to lexicographic comparison.
4. Return the best candidate found (empty string if none exists).

## Python Solution

\`\`\`python
def shortest_beautiful_substring(s: str, k: int) -> str:
    best = ""
    n = len(s)

    for i in range(n):
        ones_count = 0
        for j in range(i, n):
            if s[j] == '1':
                ones_count += 1
            if ones_count == k:
                candidate = s[i:j + 1]
                if not best or len(candidate) < len(best) or (
                    len(candidate) == len(best) and candidate < best
                ):
                    best = candidate
                break

    return best
\`\`\`

## Complexity

- **Time:** O(n²) — n starting indices, each scanning up to n characters.
- **Space:** O(n) — for the current best substring.

Given the constraint `n ≤ 100`, this runs effectively instantly.

## Video

Full walkthrough with example trace, proof of correctness, and quiz rounds: (video link coming soon)

## Article

Full write-up with dry run, complexity analysis, and common mistakes: (video link coming soon)
