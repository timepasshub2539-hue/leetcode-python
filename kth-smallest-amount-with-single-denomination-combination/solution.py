class Solution:
    def findKthSmallest(self, coins, k):
        from itertools import combinations
        from math import lcm

        def count(x):
            total = 0
            for size in range(1, len(coins) + 1):
                for combo in combinations(coins, size):
                    l = lcm(*combo)
                    total += (x // l) if size % 2 else -(x // l)
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
