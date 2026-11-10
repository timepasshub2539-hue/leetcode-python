from typing import List

class Solution:
    def minCost(self, n: int, costs: List[int]) -> int:
        dp = [0] + [float('inf')] * n
        for j in range(1, n + 1):
            for k in (1, 2, 3):
                i = j - k
                if i >= 0:
                    cost = costs[j - 1] + k * k
                    dp[j] = min(dp[j], dp[i] + cost)
        return dp[n]
