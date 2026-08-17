class Solution:
    def stoneGameV(self, stoneValue):
        from itertools import accumulate
        n = len(stoneValue)
        p = [0] + list(accumulate(stoneValue))
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    l, r = p[k+1]-p[i], p[j+1]-p[k+1]
                    if l <= r: dp[i][j] = max(dp[i][j], l + dp[i][k])
                    if r <= l: dp[i][j] = max(dp[i][j], r + dp[k+1][j])
        return dp[0][n - 1]
