# Minimum Number of Pushes to Type Word II

## Problem

Design a keypad using keys 2–9 (8 keys total) to type a given word with the
fewest total button presses. You choose which letters go on which key and in
what order. The nth letter placed on a key costs n presses to type.

## Intuition

Think spice rack: the letter you use most often should sit in the cheapest
slot (1 press), while rarely-used letters can sit in more expensive slots.
Sorting letters by frequency and filling 8 keys round robin gives the optimal
layout — provable via a simple swap/exchange argument (swapping an
out-of-order pair of letters never increases total cost).

## Approach

1. Count frequency of each letter (`collections.Counter`).
2. Sort frequencies descending.
3. Assign cost `rank // 8 + 1` to each rank (0-indexed).
4. Sum `frequency * cost` across all letters.

## Python Solution

\`\`\`python
from collections import Counter

def minimum_pushes(word: str) -> int:
    freq = Counter(word)
    counts = sorted(freq.values(), reverse=True)

    total = 0
    for i, count in enumerate(counts):
        cost = i // 8 + 1
        total += count * cost

    return total
\`\`\`

## Complexity

- **Time:** O(n) — one pass to count the word; sorting is over at most 26
  values (English alphabet), effectively constant.
- **Space:** O(1) relative to alphabet size — at most 26 entries stored.

## Video

Full walkthrough with hand-traced examples and proof of correctness: (video link coming soon)

## Article

Full write-up with dry run, complexity analysis, and common mistakes:
see the linked article on the Fun with Learning Technology series.
