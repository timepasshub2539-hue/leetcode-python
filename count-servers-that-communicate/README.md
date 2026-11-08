# LeetCode 1267 — Count Servers that Communicate

## Problem

Given an `m x n` grid of 0s and 1s representing a data center, where 1 denotes
a server, count how many servers can communicate with at least one other
server. Two servers communicate if they share the same row or the same
column, regardless of distance between them.

## Intuition

Checking every server against every other server is a pairwise comparison —
expensive on large grids. Instead, notice that a server only needs to know
two numbers to determine if it has company: how many servers total are in
its row, and how many are in its column. If either count exceeds 1, it
communicates. Identity of the other servers doesn't matter.

## Approach

1. First pass over the grid: tally server counts per row and per column into
   two arrays.
2. Second pass over the grid: for each server, check if its row's tally or
   column's tally is greater than 1. If so, count it.

Row and column counts must be checked independently — summing them causes
servers at busy intersections to be miscounted.

## Python Solution

\`\`\`python
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        row_count = [0] * rows
        col_count = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1):
                    total += 1

        return total
\`\`\`

## Complexity

- **Time:** O(m × n) — two linear passes over the grid.
- **Space:** O(m + n) — two tally arrays sized to rows and columns.

## Video

Full walkthrough with the brute-force comparison, the tally-based fix, and a
real debugging detour: (video link coming soon)

## Article

Full write-up with examples, dry run, and complexity breakdown: see the
accompanying blog post in this repo / linked in the video description.
