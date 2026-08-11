def solve(nums):
    total = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            total += nums[i]
        else:
            break
    if nums[0] != 1:
        return 1
    candidate = total + 1
    while candidate in nums:
        candidate += 1
    return candidate
