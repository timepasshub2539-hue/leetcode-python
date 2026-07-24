# Number of Unique XOR Triplets II

## Problem
Given an array of integers, consider every triplet of indices `(i, j, k)`
with `i <= j <= k` (indices may repeat). Count how many distinct values
`nums[i] ^ nums[j] ^ nums[k]` can be produced.

## Intuition
Brute forcing every triplet is O(n^3) — too slow once `n` approaches 1500
(over half a billion combinations). But XOR of values under a bound `V` can
never produce a result needing more bits than `V`. So if every value is
under 1500 (11 bits), every possible XOR result is under 2048 — a fixed
ceiling regardless of array size.

## Approach
Build the reachable XOR-value space in stages instead of enumerating
triplets directly:

1. Dedupe the array (`x ^ x = 0`, so duplicates add nothing new).
2. XOR every pair of unique values to get everything reachable in 2 picks.
3. XOR that set against the unique values once more for everything
   reachable in 3 picks.
4. The size of that final set is the answer.

## Python Solution
\`\`\`python
def unique_xor_triplets(nums: list[int]) -> int:
    uniq = set(nums)
    xor2 = {a ^ b for a in uniq for b in uniq}
    xor3 = {x ^ a for x in xor2 for a in uniq}
    return len(xor3)
\`\`\`

## Complexity
- Time: `O(n)` dedup + `O(u^2)` for each stage, where `u = min(n, 2048)`
- Space: `O(u)`, bounded by the value domain, not the array length

## Video
Full walkthrough (beginner / intermediate / advanced): https://youtu.be/-BBX3keqfJg

## Article
Complete write-up with brute force, dry run, and edge cases: https://youtu.be/-BBX3keqfJg
