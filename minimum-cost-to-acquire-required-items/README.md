# LeetCode 3789 — Minimum Cost to Acquire Required Items

A Python solution to LeetCode 3789, with full reasoning for why the obvious
greedy approach fails and why checking just three candidate values is
provably sufficient.

## Problem

You must satisfy two separate requirements, `need1` and `need2`. You can buy:

- a **type 1** item at `cost1`, counting only toward `need1`
- a **type 2** item at `cost2`, counting only toward `need2`
- a **combined** item at `cost_both`, counting toward both at once

Find the minimum total cost to satisfy both requirements. `cost1`, `cost2`,
`cost_both` ≤ 1,000,000; `need1`, `need2` ≤ 1,000,000,000 — too large to
simulate purchases one at a time.

## Intuition

The natural instinct is to buy the combined item only for the overlap
(`min(need1, need2)`), then fill the rest separately. This is **wrong**: a
combined item keeps paying off past that point as long as its price per unit
still beats the alternative, even if part of it goes unused on one side.

The total cost, as a function of how many combined items you buy, is
piecewise linear with slope changes at exactly two points: where `need1`
gets covered, and where `need2` gets covered. A piecewise linear function's
minimum is always at a slope-change point or the left boundary — so only
three candidate quantities ever need to be checked: `0`, `min(need1, need2)`,
and `max(need1, need2)`.

## Approach

1. Write a helper `price(x)` that costs out buying `x` combined items plus
   whatever single-type items are still needed.
2. Evaluate `price()` at the three candidates.
3. Return the minimum.

## Python Solution

```python
def min_cost_to_acquire(cost1: int, cost2: int, cost_both: int,
                         need1: int, need2: int) -> int:
    def price(num_combined: int) -> int:
        remaining1 = max(0, need1 - num_combined)
        remaining2 = max(0, need2 - num_combined)
        return num_combined * cost_both + remaining1 * cost1 + remaining2 * cost2

    smaller_need = min(need1, need2)
    larger_need = max(need1, need2)
    return min(price(x) for x in (0, smaller_need, larger_need))
```

## Complexity

- **Time:** O(1) — three fixed evaluations, independent of `need1`/`need2`.
- **Space:** O(1) — a constant number of integer variables.

## Video

Full walkthrough with the worked example and the greedy trap live: (video link coming soon)

## Article

Full write-up with intuition, dry run, complexity proof, and common
mistakes: see the companion article in this repo / linked in the video
description.
