class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        def cost(i, j):
            m = j - i + 1
            if m == 1:
                return 0
            best = m
            for d in range(1, m):
                if m % d:
                    continue
                total = 0
                for r in range(d):
                    g = s[i + r:j + 1:d]
                    total += sum(
                        g[x] != g[-1 - x]
                        for x in range(len(g) // 2)
                    )
                best = min(best, total)
            return best
        table = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                table[i][j] = cost(i, j)
        INF = float('inf')
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for kk in range(1, k + 1):
                for j in range(kk - 1, i):
                    if dp[j][kk - 1] < INF:
                        dp[i][kk] = min(
                            dp[i][kk],
                            dp[j][kk - 1] + table[j][i - 1]
                        )
        return dp[n][k]
