# Maximize Active Section with Trade II — Python Solution

> Daily Python LeetCode · Hard · Range Queries · Sparse Table

## Problem

You're given a binary string `s` of length `n`, where `1` marks an **active**
section and `0` an **inactive** one, plus a list of queries `[l, r]`.

For each query you may perform **at most one trade** on the slice `s[l..r]`:

1. Take a run of `1`s that has `0`s on both sides and turn it into `0`s.
2. Then flood the merged run of `0`s (now bounded by `1`s) into `1`s.

Return the maximum number of active sections in the **whole string** after the
trade, for each query.

## Intuition

A trade **never changes the total number of `1`s** — it removes a run of ones
and refunds exactly those ones when it floods. So its only real effect is
merging two zero-gaps around a lonely one-run.

Therefore:

```

answer = total\_ones + best\_gain\_in\_window

````

Every candidate move is a **0-1-0 sandwich**: a run of `1`s (the filling) with a
run of `0`s on each side (the bread). Its gain is `left_zeros + right_zeros`.
The best move in a window is the sandwich with the most bread.

Sandwiches don't move, so a sandwich fully inside a window has a gain we can
**precompute once**. Only the two sandwiches at the window's edges can have
their bread clipped by the boundary.

## Approach

1. **Run decomposition** — single pass, store `(char, start, end)` with absolute
   indices. Count total ones once (it's invariant).
2. **Candidate precompute** — for every `1`-run flanked by `0`-runs, store its
   edges and gain `(a - c) + (d - b)`. Candidates come out sorted by index.
3. **Sparse table** over the gains for `O(1)` range maximum (static data +
   idempotent `max`, so no segment tree / lazy propagation needed).
4. **Per query** — binary-search the strictly-interior candidates (`l+1`,
   `r-1`), clip the two edge candidates against the boundary, and range-max the
   middle.

## Python Solution

```python
from bisect import bisect_left, bisect_right


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries):
        n = len(s)
        total_ones = s.count("1")

        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], i, j - 1))
            i = j

        A, B, C, D, gain = [], [], [], [], []
        for k in range(1, len(runs) - 1):
            ch, a, b = runs[k]
            if ch != "1":
                continue
            c = runs[k - 1][1]
            d = runs[k + 1][2]
            A.append(a); B.append(b); C.append(c); D.append(d)
            gain.append((a - c) + (d - b))

        sparse = self._build_sparse(gain)

        out = []
        for l, r in queries:
            i0 = bisect_left(A, l + 1)
            i1 = bisect_right(B, r - 1) - 1
            g = 0
            if i0 <= i1:
                left = (A[i0] - max(C[i0], l)) + (min(D[i0], r) - B[i0])
                right = (A[i1] - max(C[i1], l)) + (min(D[i1], r) - B[i1])
                g = max(left, right)
                if i0 + 1 <= i1 - 1:
                    g = max(g, self._range_max(sparse, i0 + 1, i1 - 1))
            out.append(total_ones + g)
        return out

    @staticmethod
    def _build_sparse(arr):
        m = len(arr)
        if m == 0:
            return []
        table = [arr[:]]
        length = 1
        while length * 2 <= m:
            prev = table[-1]
            table.append([max(prev[i], prev[i + length])
                          for i in range(m - 2 * length + 1)])
            length *= 2
        return table

    @staticmethod
    def _range_max(table, lo, hi):
        k = (hi - lo + 1).bit_length() - 1
        return max(table[k][lo], table[k][hi - (1 << k) + 1])
````

## Complexity

| Metric      | Value                    |
| ----------- | ------------------------ |
| Build time  | `O(n log n)`             |
| Query time  | `O(log n)`               |
| Total time  | `O(n log n + q log n)`   |
| Space       | `O(n log n)`             |

Brute force is `O(n·q)` — `10^10` at `n = q = 10^5`, an instant TLE. Keep it
around as an oracle for differential testing the fast path.

## Video

▶️ Full three-level walkthrough: (video link coming soon)

## Article

📖 Deep-dive write-up with dry run, edge cases, and interview follow-ups: (video link coming soon)

---

Part of the **Daily Python LeetCode** series — one problem a day, intuition
first. #Python #LeetCode #CodingInterview #Algorithms #DataStructures
