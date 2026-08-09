def avg(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i+1]
    return total / len(nums)

avg([4, 8, 15, 16])
# IndexError: list index out of range
