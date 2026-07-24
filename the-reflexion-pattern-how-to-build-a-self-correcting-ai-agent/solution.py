def sum_list(nums):
    total = nums[0]
    for n in nums[1:]:
        total += n
    return total
# fails on empty list, crashes
