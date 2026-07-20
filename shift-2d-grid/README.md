# Shift 2D Grid — LeetCode 1260 (Python)

A clean, O(m×n) Python solution using the flatten-and-rotate pattern.

## Problem

Given a 2D `grid` of size `m x n` and an integer `k`, shift the grid `k` times.

In one shift operation:
- Each element moves one position to the right.
- The last element of a row wraps to the start of the next row.
- The bottom-right element wraps around to the top-left.

Return the grid after `k` shifts.

**Example**


Input:  grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]


## Intuition

The grid *looks* two-dimensional, but a single shift just moves each value to
the next cell in reading order. Read the grid as one long line (row by row,
like a snake) and a shift becomes a **1D right rotation**.

Two key insights:
1. **Flatten the grid** → a shift is a right rotation of the flat list.
2. **Rotation loops** → rotating by `m*n` returns to the start, so only
   `k % (m*n)` matters.

## Approach

1. Reduce `k` with `k %= m * n` — skip full loops.
2. Flatten the grid into a 1D list (reading order).
3. Right-rotate the list: `flat[-k:] + flat[:-k]`.
4. Reshape into `m` rows of length `n`.

## Python Solution

```python
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # Only the shift within one full loop matters.
        k %= m * n

        # Flatten the grid into one list (reading order).
        flat = [val for row in grid for val in row]

        # Right rotation of the flat list by k.
        flat = flat[-k:] + flat[:-k]

        # Reshape back into m rows of length n.
        return [flat[i * n:(i + 1) * n] for i in range(m)]
```

## Complexity

| Approach            | Time         | Space    |
|---------------------|--------------|----------|
| Flatten & rotate    | O(m × n)     | O(m × n) |
| Simulate each shift | O(k × m × n) | O(m × n) |

Since `k` can be up to 100, simulation does up to 100× more work for the same
result.

## Edge Cases

- `k = 0` → grid returned unchanged.
- `k` larger than the grid → modulo shrinks it to a safe shift.
- `k` a multiple of `m*n` → full loop, grid unchanged.
- 1×1 grid → maps to itself for any `k`.

## Video

📺 Watch the full walkthrough: https://youtu.be/aaYx4Q1R1j0

## Article

📖 Full written deep-dive (intuition, dry run, common mistakes, follow-ups):
part of the **Daily Python LeetCode** series.
