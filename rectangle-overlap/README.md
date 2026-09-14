# LeetCode 836 — Rectangle Overlap (Python)

## Problem

Given two axis-aligned rectangles, each defined by bottom-left and top-right
corners `[x1, y1, x2, y2]`, determine whether they overlap with a strictly
positive area. Rectangles that only touch along an edge or at a corner do
not count as overlapping.

## Intuition

Checking whether a corner of one rectangle lies inside the other seems
natural but is wrong: a thin rectangle can slice through a wider one with
real overlapping area while none of its corners land inside the other shape.

Instead, flip the question. Two rectangles fail to overlap only if one is
entirely left of, right of, above, or below the other. Ruling out those four
cases is equivalent to confirming overlap — no corner-checking required.

## Approach

Project both rectangles onto the x-axis and y-axis independently:

- x-ranges overlap when `rec1.x1 < rec2.x2 and rec2.x1 < rec1.x2`
- y-ranges overlap when `rec1.y1 < rec2.y2 and rec2.y1 < rec1.y2`

Both must hold. Strict inequalities exclude edge- and corner-touching, since
a shared boundary produces zero width or height on one side.

## Python Solution

```python
class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        x_overlap = x1 < x4 and x3 < x2
        y_overlap = y1 < y4 and y3 < y2

        return x_overlap and y_overlap
```

## Complexity

- **Time:** O(1) — four fixed comparisons, independent of coordinate size.
- **Space:** O(1) — no auxiliary structures.

## Video

Full walkthrough with intuition, dry run, and quiz rounds: (video link coming soon)

## Article

Full write-up: see the accompanying article for problem breakdown, brute
force discussion, edge cases, and common mistakes.
