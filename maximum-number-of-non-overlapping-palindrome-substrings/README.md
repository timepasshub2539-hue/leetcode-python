# LeetCode 2472 — Maximum Number of Non-overlapping Palindrome Substrings

## Problem

Given a string `s` and an integer `k`, find the maximum number of
non-overlapping substrings of `s` such that each substring is a
palindrome and has length at least `k`.

## Intuition

The naive instinct is to greedily take the *longest* palindrome
available at each step. This is wrong — it can consume characters that
would otherwise support multiple smaller valid palindromes.

The correct greedy: take the *shortest* valid palindrome as soon as one
is found, then jump past it. This works because:

1. Any palindrome's inner core (after peeling matching outer
   characters) is itself a shorter palindrome — so you never need to
   check lengths beyond `k` and `k + 1` at any starting position.
2. Using fewer characters per pick always leaves at least as much room
   for future picks, so the shortest valid choice is never worse.

## Approach

1. Scan the string left to right with pointer `i`.
2. At `i`, check if `s[i:i+k]` is a palindrome. If so, count it and
   jump `i` forward by `k`.
3. Otherwise check `s[i:i+k+1]`. If it's a palindrome, count it and
   jump `i` forward by `k + 1`.
4. Otherwise advance `i` by 1.
5. Repeat until `i` runs past the point where a length-`k` window still
   fits.

## Python Solution

```python
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        n = len(s)
        count = 0
        i = 0

        while i <= n - k:
            if is_pal(i, i + k - 1):
                count += 1
                i += k
            elif i + k < n and is_pal(i, i + k):
                count += 1
                i += k + 1
            else:
                i += 1

        return count
```

## Complexity

- **Time:** O(n × k) — each palindrome check costs up to O(k), performed
  across a single linear pass over the string.
- **Space:** O(1) — just a pointer and a counter, no auxiliary
  structures.

## Video

Full walkthrough with the intuition trace, greedy loop build-up, and
two in-video quizzes: (video link coming soon)

## Article

Full write-up with dry run, complexity proof, and comparison to the
DP/interval-scheduling alternative: (video link coming soon)
