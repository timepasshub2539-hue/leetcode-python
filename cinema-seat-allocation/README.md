# Cinema Seat Allocation — LeetCode 1386 (Python)

## Problem

Given a cinema with `n` rows of 10 seats each and a list of already-reserved
seats, return the maximum number of four-person groups that can be seated
together. Each group must occupy one of three fixed blocks per row:

- Block A: seats 2-5
- Block B: seats 4-7
- Block C: seats 6-9

Seats 1 and 10 are never part of any block.

## Intuition

The search space is smaller than it looks: there are only three possible
seat blocks per row, not "any four consecutive seats." Blocks A and C never
overlap, so an empty row seats two groups, not one — B is the only block
that conflicts with both.

## Approach

1. Build a dictionary mapping each row with at least one reservation to an
   8-bit mask (seats 2-9, one bit per seat).
2. Represent blocks A, B, C as constant bitmasks.
3. For rows with no reservations, add 2 groups per row directly.
4. For rows with reservations, check `mask & BLOCK == 0` to test if a block
   is free, and sum the best non-overlapping combination.

## Python Solution

```python
from collections import defaultdict
from typing import List


def max_number_of_families(n: int, reserved_seats: List[List[int]]) -> int:
    BLOCK_A = 0b00001111  # seats 2-5
    BLOCK_B = 0b00111100  # seats 4-7
    BLOCK_C = 0b11110000  # seats 6-9

    row_masks = defaultdict(int)

    for row, seat in reserved_seats:
        if 2 <= seat <= 9:
            row_masks[row] |= 1 << (seat - 2)

    total_groups = (n - len(row_masks)) * 2

    for mask in row_masks.values():
        if mask & BLOCK_A == 0 and mask & BLOCK_C == 0:
            total_groups += 2
        elif (mask & BLOCK_A == 0) or (mask & BLOCK_B == 0) or (mask & BLOCK_C == 0):
            total_groups += 1

    return total_groups
```

## Complexity

- **Time:** O(k), where k is the number of reservations.
- **Space:** O(k), for the row-to-mask dictionary.

## Video

Full walkthrough: (video link coming soon)

## Article

Full written breakdown with dry run and complexity analysis: (video link coming soon)
