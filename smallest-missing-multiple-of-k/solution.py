class Solution:
    def smallestMissingMultiple(self, nums, k):
        present = set(nums)
        m = k
        while m in present:
            m += k
        return m


if __name__ == "__main__":
    s = Solution()
    assert s.smallestMissingMultiple([8, 2, 3, 4, 6], 2) == 10
    assert s.smallestMissingMultiple([1, 4, 7, 10, 15], 5) == 5
    print("ok")

