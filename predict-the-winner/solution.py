from functools import lru_cache

def predictWinner(nums):
    n = len(nums)

    @lru_cache(None)
    def dp(i, j):
        if i == j:
            return nums[i]
