# Hash Map Collision Attacks — Mechanism, Exploit, and Defenses

## Problem

Hash maps promise O(1) lookups, but that promise is average-case only.
Because more possible keys exist than buckets, collisions are mathematically
guaranteed (pigeonhole principle). Left unaddressed, an attacker who can
predict a hash function can craft keys that all collide into one bucket,
degrading every operation on that bucket from O(1) to O(n) — an algorithmic
complexity attack.

## Intuition

"O(1)" was never a claim about any single lookup — it's a claim that every
bucket stays short. Break that assumption on purpose, and the data structure
degrades into a linked list wearing a hash map's interface.

## Approach

1. Demonstrate a naive hash map (`VulnerableBucketMap`) using a fixed, public
   hash function.
2. Show how crafted keys collide into a single bucket, inflating chain length.
3. Fix it with `SeededBucketMap`, mixing a random per-instance seed into the
   hash — the same technique CPython uses by default for `str`/`bytes` hashing.
4. Note the two remaining production defenses not implemented here:
   treeifying overloaded buckets, and load-factor-triggered resizing.

## Python Solution

```python
import os
import hashlib


class VulnerableBucketMap:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        digest = hashlib.md5(key.encode()).hexdigest()
        return int(digest, 16) % self.size

    def insert(self, key: str, value):
        bucket = self.buckets[self._hash(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: str):
        bucket = self.buckets[self._hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def max_chain_length(self) -> int:
        return max(len(b) for b in self.buckets)


class SeededBucketMap(VulnerableBucketMap):
    def __init__(self, size=16):
        self.seed = os.urandom(16)
        super().__init__(size)

    def _hash(self, key: str) -> int:
        digest = hashlib.md5(self.seed + key.encode()).hexdigest()
        return int(digest, 16) % self.size
```

## Complexity

| | Average case | Worst case (crafted keys) |
|---|---|---|
| Time (unseeded) | O(1) | O(n) |
| Time (seeded) | O(1) | O(1) — infeasible to reproduce collisions without the seed |
| Space | O(n) | O(n) |

## Video

Full walkthrough with a live simulation of chain growth under attack: (video link coming soon)

## Article

Written companion covering intuition, dry run, and edge cases in full: (video link coming soon)
