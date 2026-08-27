from collections import Counter

class Solution:
    def getSmallestString(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        neg = 0
        for c in target[:-1]:
            bad = count[c] < 0
            count[c] -= 1
            if not bad and count[c] < 0:
                neg += 1
        for i in range(n - 1, -1, -1):
            if neg == 0:
                for code in range(ord(target[i]) + 1, 123):
                    ch = chr(code)
                    if count[ch] > 0:
                        count[ch] -= 1
                        rest = "".join(chr(x) * count[chr(x)] for x in range(97, 123))
                        return target[:i] + ch + rest
            if i > 0:
                p = target[i - 1]
                bad = count[p] < 0
                count[p] += 1
                if bad and count[p] >= 0:
                    neg -= 1
        return ""
