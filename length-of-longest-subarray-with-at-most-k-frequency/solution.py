def maxSubarrayLength(nums, k):
    counts = {}
    left = 0
    best = 0
    for right, val in enumerate(nums):
        counts[val] = counts.get(val, 0) + 1
        while counts[val] > k:
            left_val = nums[left]
            counts[left_val] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
