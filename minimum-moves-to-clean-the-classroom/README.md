# LeetCode 3568 — Minimum Moves to Clean the Classroom

## Problem

A student starts on a marked cell in a grid classroom with a fixed amount of
energy. Moving to an adjacent cell costs 1 energy. Reset cells (`R`) restore
energy to full on arrival, regardless of current energy. Obstacle cells (`X`)
cannot be entered. Find the minimum number of moves to collect all litter
(`L`) cells, or `-1` if some litter is unreachable.

## Intuition

Every move costs exactly 1 step — energy is a legality constraint, not an
edge weight. That means plain BFS finds the optimal answer, as long as
"state" captures everything that affects future moves: position, remaining
energy, and which litter has been collected. With at most 10 litter cells,
the collected set is packed into a bitmask for O(1) comparison.

## Approach

1. Scan the grid for the start cell and index each litter cell to a bit.
2. BFS over states `(row, col, energy, mask)`, one move per layer.
3. On each move: reset cells refill energy, litter cells clear a mask bit.
4. Return the move count the instant a state's mask matches `full_mask`.
5. If the queue empties first, return `-1`.

## Python Solution

See [`solution.py`](./solution.py) — `min_moves_to_clean(grid, energy_cap)`.

## Complexity

- **Time:** `O(rows * cols * energy_cap * 2^litter_count)`
- **Space:** same bound, for the visited set and BFS queue

Worst case (~20M states) runs comfortably within typical interview/contest
time limits.

## Video

Full derivation and walkthrough: (video link coming soon)

## Article

Full written breakdown with dry run, edge cases, and interview follow-ups:
part of the *Fun with Learning Technology* series.
