# Maximize Active Section with Trade I — Python Solution

## Problem
Given a binary string `s`, you may perform exactly one operation: erase a
maximal group of `1`s that is bordered by `0`s on both sides, then fill the
entire span (the erased `1`s and both bordering `0`s) with `1`s. Return the
maximum number of active (`1`) positions achievable.

## Intuition
The block of `1`s you erase gets rebuilt as `1`s regardless — it contributes
zero net change. The only real gain comes from the `0`-runs bordering it,
which flip to active. So the problem reduces to finding the `1`-block whose
two adjacent zero-runs sum to the largest value.

## Approach
1. Pad `s` with a `'1'` sentinel on each end to remove edge-case branching.
2. Run-length encode the padded string with `itertools.groupby`.
3. Skip the two sentinel runs; for every interior `1`-run, compute
   `left_zero_run + right_zero_run`.
4. Track the maximum gain, add it to the original `1`-count.

## Python Solution
\`\`\`python
from itertools import groupby


def max_active_section(s: str) -> int:
    baseline_ones = s.count("1")

    padded = "1" + s + "1"
    runs = [(char, len(list(group))) for char, group in groupby(padded)]

    best_gain = 0
    for i in range(1, len(runs) - 1):
        char, length = runs[i]
        if char == "1":
            left_zeros = runs[i - 1][1]
            right_zeros = runs[i + 1][1]
            best_gain = max(best_gain, left_zeros + right_zeros)

    return baseline_ones + best_gain
\`\`\`

## Complexity
- **Time:** O(n) — one pass to count, one pass to run-length encode, one
  pass over the runs.
- **Space:** O(n) worst case for the runs list (bounded by number of runs).

## Video
Full walkthrough with dry run and edge cases: (video link coming soon)

## Article
Complete written breakdown: see the linked Substack article for intuition,
brute force comparison, dry run, and interview follow-ups.
