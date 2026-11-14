from bisect import bisect_left, insort

class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        window, best = [], -1
        for end in range(l, n + 1):
            insort(window, prefix[end - l])
            if end - r - 1 >= 0:
                window.remove(prefix[end - r - 1])
            pos = bisect_left(window, prefix[end])
            if pos > 0:
                gap = prefix[end] - window[pos - 1]
                if best == -1 or gap < best:
                    best = gap
        return best
