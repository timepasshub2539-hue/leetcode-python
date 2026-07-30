# Minimum Number of Pushes to Type Word I

A greedy, frequency-bucket solution to LeetCode's keypad remapping problem, in Python.

## Problem

You're given a word made of unique lowercase letters. Design a mapping of letters onto an 8-key keypad (multiple letters per key allowed) to minimize total keypresses. On any key, the 1st assigned letter costs 1 push, the 2nd costs 2, the 3rd costs 3, and so on. Return the minimum total pushes needed to type the word.

## Intuition

Since every letter in the word is unique, identity doesn't matter — only *position* after sorting does. There are only 8 cheap (1-push) slots. Fill those first, then the next 8 at 2 pushes each, then the next 8 at 3, and so on.

## Approach

1. Count letter frequencies with `Counter`.
2. Sort frequencies descending.
3. For each letter at sorted index `i`, compute `group = i // 8 + 1`.
4. Add `group * frequency` to the running total.

## Python Solution

```python
from collections import Counter


def minimum_pushes(word: str) -> int:
    freq = Counter(word)
    counts = sorted(freq.values(), reverse=True)

    total_pushes = 0
    for index, count in enumerate(counts):
        group_number = index // 8 + 1
        total_pushes += group_number * count

    return total_pushes


if __name__ == "__main__":
    assert minimum_pushes("abcdefghi") == 10
    assert minimum_pushes("xycdefghij") == 12
    assert minimum_pushes("abc") == 3
    assert minimum_pushes("a") == 1
    print("all checks passed")
```

## Complexity

- **Time:** O(n log n) — dominated by sorting.
- **Space:** O(n) — for the counter and sorted list.

## Video

Full walkthrough, built up from scratch with a worked example and brute-force comparison: (video link coming soon)

## Article

Complete write-up with dry run, edge cases, and interview follow-ups: (video link coming soon)
