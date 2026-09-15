class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        count = 0
        i = 0
        while i <= n - k:
            if is_pal(i, i + k - 1):
                count += 1
                i += k
            elif i + k < n and is_pal(i, i + k):
                count += 1
                i += k + 1
            else:
                i += 1
        return count
