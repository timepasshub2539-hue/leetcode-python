class Solution:
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        min_prefix = [float('inf')] * k
        min_prefix[0], best = 0, float('-inf')
        for j in range(1, n + 1):
            r = j % k
            if min_prefix[r] != float('inf'):
                best = max(best, prefix[j] - min_prefix[r])
            min_prefix[r] = min(min_prefix[r], prefix[j])
        return best
