# Longest Substring of One Repeating Character (LeetCode 2213)

## Problem

Given a string `s` and a series of updates — each replacing one character
at a given index — return, after each update, the length of the longest
substring containing only one repeated character.

## Intuition

A single-character edit only disturbs the runs directly adjacent to it;
everything else in the string is unaffected. Rescanning the whole string
after every update wastes that fact. Instead, build a tree that summarizes
ranges of the string, so an update only needs to recompute a handful of
ancestor summaries.

## Approach

Use a **segment tree** where each node stores:

- `max_run`: longest repeated-character run fully inside this range
- `left_run`: run length starting at the range's left edge
- `right_run`: run length ending at the range's right edge

**Merge(left, right):**
- `max_run = max(left.max_run, right.max_run)`
- If the seam characters match, also consider `left.right_run + right.left_run`
- Extend `left_run`/`right_run` into the sibling range when a child is
  entirely one repeated character

**Update:** rewrite the target leaf, then re-merge every ancestor on the
path to the root — `O(log n)` nodes touched per update.

## Python Solution

```python
class SegmentTree:
    def __init__(self, s):
        self.s = list(s)
        self.n = len(self.s)
        self.tree = [None] * (4 * self.n)
        self._build(1, 0, self.n - 1)

    def _build(self, node, lo, hi):
        if lo == hi:
            self.tree[node] = (1, 1, 1)
            return
        mid = (lo + hi) // 2
        self._build(2 * node, lo, mid)
        self._build(2 * node + 1, mid + 1, hi)
        self.tree[node] = self._merge(node, lo, mid, hi)

    def _merge(self, node, lo, mid, hi):
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        left_len = mid - lo + 1
        right_len = hi - mid

        max_run = max(left[0], right[0])
        left_run, right_run = left[1], right[1]

        if self.s[mid] == self.s[mid + 1]:
            max_run = max(max_run, left[2] + right[1])
            if left[1] == left_len:
                left_run = left_len + right[1]
            if right[2] == right_len:
                right_run = right_len + left[2]

        return (max_run, left_run, right_run)

    def update(self, node, lo, hi, idx, char):
        if lo == hi:
            self.s[idx] = char
            self.tree[node] = (1, 1, 1)
            return
        mid = (lo + hi) // 2
        if idx <= mid:
            self.update(2 * node, lo, mid, idx, char)
        else:
            self.update(2 * node + 1, mid + 1, hi, idx, char)
        self.tree[node] = self._merge(node, lo, mid, hi)

    def longest_repeating(self):
        return self.tree[1][0]


def longestRepeating(s, queryCharacters, queryIndices):
    tree = SegmentTree(s)
    n = len(s)
    answers = []
    for char, idx in zip(queryCharacters, queryIndices):
        tree.update(1, 0, n - 1, idx, char)
        answers.append(tree.longest_repeating())
    return answers
```

## Complexity

- **Build:** O(n)
- **Per update:** O(log n)
- **Total for k queries:** O(n + k log n)
- **Space:** O(n)

## Video

Full walkthrough, dry run, and diagrams: (video link coming soon)

## Article

Full write-up with intuition, brute force comparison, and interview
follow-ups: (video link coming soon)
