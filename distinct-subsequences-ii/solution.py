class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0
        last = [None] * 26
        for c in s:
            idx = ord(c) - ord('a')
            prev = dp
            if last[idx] is None:
                dp = (2 * dp + 1) % MOD
            else:
                dp = (2 * dp - last[idx]) % MOD
            last[idx] = prev
        return dp % MOD
