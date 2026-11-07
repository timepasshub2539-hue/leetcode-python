import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)
        avail = [(servers[i], i) for i in range(n)]
        heapq.heapify(avail)
        busy = []
        ans = [0] * len(tasks)
        for j, dur in enumerate(tasks):
            t = j
            if not avail:
                t = max(t, busy[0][0])
            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(avail, (w, i))
            w, i = heapq.heappop(avail)
            ans[j] = i
            heapq.heappush(busy, (t + dur, w, i))
        return ans
