class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left, right = num[:half], num[half:]
        cnt1, cnt2 = left.count('?'), right.count('?')
        sum1 = sum(int(c) for c in left if c != '?')
        sum2 = sum(int(c) for c in right if c != '?')
        if (cnt1 + cnt2) % 2:
            return True
        return sum1 - sum2 != 9 * (cnt2 - cnt1) // 2
