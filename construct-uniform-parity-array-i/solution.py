class Solution:
    def canConstruct(self, nums1):
        # Every array can become all-odd or all-even:
        # already uniform -> keep it; mixed -> subtract
        # an odd number from an even one, always odd
        return True
