# LeetCode 835 — Image Overlap

## Problem

Given two n x n binary matrices `img1` and `img2`, you may translate
(slide) one image any number of units left, right, up, or down (no
rotation). After sliding, the overlap is the number of positions
where both images have a 1. Return the largest possible overlap.

## Intuition

Overlap can only occur where a 1 in `img1` aligns with a 1 in `img2`.
Instead of testing every possible slide position across the whole
grid, extract the coordinates of every 1-cell in each image, then for
every pair of points (one from each image) compute the shift vector
that would align them. The shift vector with the most votes gives the
maximum overlap.

## Approach

1. Collect coordinates of all 1-cells in `img1` -> `pts1`.
2. Collect coordinates of all 1-cells in `img2` -> `pts2`.
3. If either list is empty, return 0.
4. For every pair `(p1, p2)` in `pts1 x pts2`, compute the shift
   vector `(p1.row - p2.row, p1.col - p2.col)` and increment its
   count in a hash map.
5. Return the maximum count in the hash map.

## Python Solution

\`\`\`python
from collections import defaultdict
from typing import List


def largest_overlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)

    pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
    pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

    if not pts1 or not pts2:
        return 0

    counts = defaultdict(int)
    for r1, c1 in pts1:
        for r2, c2 in pts2:
            shift = (r1 - r2, c1 - c2)
            counts[shift] += 1

    return max(counts.values())
\`\`\`

## Complexity

- Time: O(|pts1| * |pts2|), bounded by O(n^4) worst case but typically
  far smaller for sparse grids.
- Space: O(distinct shift vectors).

## Video

Full walkthrough with diagrams and quizzes: (video link coming soon)

## Article

Full write-up: (video link coming soon)
