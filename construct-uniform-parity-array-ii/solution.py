class Solution:
    def canConstruct(self, nums1: list[int]) -> bool:
        odds = [x for x in nums1 if x % 2 == 1]
        if not odds:
            return True
        min_odd = min(odds)
        for x in nums1:
            if x % 2 == 0 and x < min_odd:
                return False
        return True
