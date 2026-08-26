class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        best_len = None
        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == '1':
                    ones += 1
                if ones == k:
                    length = j - i + 1
                    if (best_len is None or length < best_len
                            or (length == best_len and s[i:j+1] < best)):
                        best_len = length
                        best = s[i:j+1]
                    break
        return best
