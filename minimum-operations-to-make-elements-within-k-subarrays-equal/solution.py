from bisect import insort
from itertools import accumulate

class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        costs = self._window_costs(nums, x)
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                best = dp[i - 1][j]
                if i >= x and dp[i - x][j - 1] < INF:
                    best = min(best, dp[i - x][j - 1] + costs[i - x])
                dp[i][j] = best
        return dp[n][k]

    def _window_costs(self, nums, x):
        window = sorted(nums[:x])
        n = len(nums)
        costs = [0] * (n - x + 1)
        costs[0] = self._median_cost(window)
        for i in range(1, n - x + 1):
            window.remove(nums[i - 1])
            insort(window, nums[i + x - 1])
            costs[i] = self._median_cost(window)
        return costs

    def _median_cost(self, window):
        size = len(window)
        mid = (size - 1) // 2
        m = window[mid]
        prefix = list(accumulate(window, initial=0))
        left_sum = prefix[mid + 1]
        right_sum = prefix[size] - left_sum
        return (m * (mid + 1) - left_sum) + (right_sum - m * (size - mid - 1))
