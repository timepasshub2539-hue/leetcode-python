import bisect

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][0])
        l = [intervals[i][0] for i in order]
        r = [intervals[i][1] for i in order]
        w = [intervals[i][2] for i in order]
        nxt = [bisect.bisect_right(l, r[i]) for i in range(n)]
        dp = [[0] * 5 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for k in range(1, 5):
                skip = dp[i + 1][k]
                take = w[i] + dp[nxt[i]][k - 1]
                dp[i][k] = max(skip, take)
        res, i, k = [], 0, 4
        while i < n and k > 0:
            skip = dp[i + 1][k]
            take = w[i] + dp[nxt[i]][k - 1]
            if take > skip:
                res.append(order[i])
                i, k = nxt[i], k - 1
            else:
                i += 1
        return sorted(res)
