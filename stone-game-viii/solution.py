from itertools import accumulate
from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = list(accumulate(stones))
        best = prefix[-1]
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i] - best)
        return best
