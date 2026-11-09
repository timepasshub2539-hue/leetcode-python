import heapq, bisect

class Solution:
    def busiestServers(self, k, arrival, load):
        available = list(range(k))
        busy = []
        count = [0] * k
        for i, t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, s = heapq.heappop(busy)
                bisect.insort(available, s)
            if not available:
                continue
            pos = bisect.bisect_left(available, i % k)
            pos = pos if pos < len(available) else 0
            s = available.pop(pos)
            count[s] += 1
            heapq.heappush(busy, (t + load[i], s))
        best = max(count)
        return [i for i, c in enumerate(count) if c == best]
