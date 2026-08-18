class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        if k >= n:
            return max(nums)
        def cov(i):
            return min(i, k-1, n-k, n-1-i) + 1
        cand = {nums[i] for i in
            list(range(k-1)) + list(range(n-k+1, n))}
        ans = -1
        for v in cand:
            total = sum(cov(i) for i in range(n) if nums[i] == v)
            if total == 1:
                ans = max(ans, v)
        return ans
