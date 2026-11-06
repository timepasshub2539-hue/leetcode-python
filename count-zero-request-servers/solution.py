class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        count = [0] * (n + 1)
        active = 0
        left = right = 0
        result = [0] * len(queries)
        for i in order:
            q = queries[i]
            while right < len(logs) and logs[right][1] <= q:
                sid = logs[right][0]
                if count[sid] == 0:
                    active += 1
                count[sid] += 1
                right += 1
            while left < len(logs) and logs[left][1] < q - x:
                sid = logs[left][0]
                count[sid] -= 1
                if count[sid] == 0:
                    active -= 1
                left += 1
            result[i] = n - active
        return result
