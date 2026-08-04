def find_missing_elements(nums):
    lo, hi = min(nums), max(nums)
    tracker = list(range(lo, hi + 1))
    for num in nums:
        idx = num - lo
        tracker[idx] = -abs(tracker[idx])
    return [val for val in tracker if val > 0]
