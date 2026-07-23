# Number of Unique XOR Triplets I

Python solution to the LeetCode daily challenge **Number of Unique XOR Triplets I**.

## Problem

Given an array `nums` that is a permutation of `1..n`, count the number of distinct
values obtainable from `nums[i] ^ nums[j] ^ nums[k]` for all index triplets with
`i <= j <= k` (repeats allowed).

## Intuition

- `a ^ a == 0` is the core XOR fact behind this problem.
- Because `nums` is a permutation, choosing indices `i <= j <= k` is equivalent to
  choosing a multiset of three values from `{1, ..., n}` — the array's actual order
  is irrelevant.
- Combining three values from `{1, ..., n}` via XOR can produce every integer from
  `0` up to the next power of two above `n`. This follows from `{1,...,n}` spanning
  every bit position below `bit_length(n)` as a vector space over GF(2).
- `n = 1` and `n = 2` are too small for that full range to be reachable, so they're
  handled as special cases.

## Approach

1. If `n == 1`, return `1` (only one possible triplet).
2. If `n == 2`, return `2` (verified directly by enumeration).
3. Otherwise, return `1 << n.bit_length()` — the smallest power of two strictly
   greater than `n`.

No loop over `nums` is required; only `len(nums)` matters.

## Python Solution

```python
def unique_xor_triplets(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 1 << n.bit_length()


assert unique_xor_triplets(1) == 1
assert unique_xor_triplets(2) == 2
assert unique_xor_triplets(4) == 8
assert unique_xor_triplets(5) == 8
```

## Complexity

- **Time:** O(1)
- **Space:** O(1)

## Video

Full visual walkthrough: (video link coming soon)

## Article

Full write-up with intuition, dry run, and complexity analysis: see the accompanying article in this repo/newsletter.
