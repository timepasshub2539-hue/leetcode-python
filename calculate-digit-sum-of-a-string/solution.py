class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            next_s = []
            for i in range(0, len(s), k):
                group = s[i:i + k]
                total = sum(
                    int(ch) for ch in group if ch.isdigit()
                )
                next_s.append(str(total))
            s = "".join(next_s)
        return s
