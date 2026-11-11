class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        lo = min(need1, need2)
        hi = max(need1, need2)
        best = float('inf')
        for x in (0, lo, hi):
            total = (x * costBoth
                + max(0, need1 - x) * cost1
                + max(0, need2 - x) * cost2)
            best = min(best, total)
        return best
