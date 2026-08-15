def longest_subsequence(nums):
    total = 0
    for x in nums:
        total ^= x
    if total != 0:
        return len(nums)
    if any(x != 0 for x in nums):
        return len(nums) - 1
    return 0
