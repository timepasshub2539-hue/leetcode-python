    top3 = nums[-1] * nums[-2] * nums[-3]
    low2 = nums[0] * nums[1] * nums[-1]
    return max(top3, low2)
