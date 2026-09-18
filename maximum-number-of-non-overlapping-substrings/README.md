# LeetCode 1520 — Maximum Number of Non-Overlapping Substrings

## Problem

Given a string of lowercase letters, select the maximum number of
non-overlapping substrings such that if a substring contains an occurrence
of a character, it contains *all* occurrences of that character in the
string. If multiple selections tie on count, prefer the one with the
smallest total length.

## Intuition

A naive left-to-right cut fails because a letter can reappear later and
get split across a cut. Instead:

1. Every letter has a **forced range**: first occurrence → last occurrence.
2. Forced ranges that overlap must be **merged** into one sealed block —
   a range isn't safe to use until nothing overlaps it.
3. Once merged, sealed blocks are scheduled greedily: sort by end
   position, take a block whenever it starts after the last taken block
   ends.

This is merge-intervals followed by interval-scheduling.

## Approach

- Build `first` and `last` dictionaries for each letter in one pass.
- For each letter, expand a range from its first occurrence, growing the
  end whenever a passed-over letter's own last occurrence reaches
  further out. This performs the merge.
- Deduplicate ranges, sort by end position.
- Greedily pick non-overlapping ranges in that order.

## Python Solution

```python
def max_num_of_substrings(s: str) -> list[str]:
    first = {}
    last = {}
    for i, ch in enumerate(s):
        if ch not in first:
            first[ch] = i
        last[ch] = i

    ranges = set()
    for ch, start in first.items():
        end = last[ch]
        i = start
        while i <= end:
            ch_i = s[i]
            if last[ch_i] > end:
                end = last[ch_i]
            i += 1
        ranges.add((start, end))

    result = []
    last_end = -1
    for start, end in sorted(ranges, key=lambda r: r[1]):
        if start > last_end:
            result.append(s[start:end + 1])
            last_end = end

    return result
```

## Complexity

- **Time:** O(n) — first/last pass is O(n), range expansion is O(26n)
  bounded by the fixed alphabet size, sorting and scheduling are O(1)
  relative to n.
- **Space:** O(1) auxiliary (26-letter dictionaries), O(n) for output.

## Video

Full walkthrough with proof sketch and quiz checkpoints: (video link coming soon)

## Article

Full write-up with dry run, edge cases, and interview follow-ups:
see the accompanying article in this repo / linked in the video
description.
