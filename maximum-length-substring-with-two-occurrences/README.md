# Maximum Length Substring With Two Occurrences

## Problem

Given a string, return the length of the longest substring in which no
character appears more than twice.

## Intuition

Checking every substring from scratch re-does the same character counting
over and over. A sliding window avoids this: grow the window from the right,
and when a character's count exceeds two, shrink from the left only until
that one violation is resolved. No restarting, no re-scanning.

## Approach

1. Maintain a `count` dict, a `left` pointer, and a `best` length.
2. Walk a `right` pointer across the string, incrementing the count of each
   new character.
3. While the newly added character's count exceeds 2, remove characters from
   the left edge and advance `left`.
4. After each addition, the window `[left, right]` is guaranteed valid —
   update `best` with its size.

Every character enters the window once and leaves at most once, bounding
total work to O(n).

## Python Solution

\`\`\`python
def max_substring_two_occurrences(s: str) -> int:
    counts = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        counts[char] = counts.get(char, 0) + 1

        while counts[char] > 2:
            left_char = s[left]
            counts[left_char] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best
\`\`\`

## Complexity

- **Time:** O(n) — `left` and `right` each move forward at most n times.
- **Space:** O(1) — bounded by alphabet size (26 for lowercase letters).

## Video

Full walkthrough with a step-by-step trace, quiz rounds, and a no-dictionary
variant: (video link coming soon)

## Article

Full write-up with brute force comparison, dry run, and common mistakes:
part of the Fun with Learning Technology series.
