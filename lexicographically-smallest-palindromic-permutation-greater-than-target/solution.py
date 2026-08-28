class Solution:
    def smallestGreaterPalindrome(self, s: str, target: str) -> str:
        from collections import Counter
        n = len(s)
        cnt = Counter(s)
        odds = [c for c in cnt if cnt[c] % 2]
        if len(odds) > 1:
            return ""
        mid = odds[0] if odds else ""
        half = n // 2
        half_cnt = {c: cnt[c] // 2 for c in cnt}
        t_left = target[:half]

        def fits(counts, word):
            need = Counter(word)
            return all(need[c] <= counts.get(c, 0) for c in need)

        def smallest(counts):
            return "".join(c * counts[c] for c in sorted(counts) if counts[c])

        if fits(half_cnt, t_left):
            left = t_left
            cand = left + mid + left[::-1]
            if cand > target:
                return cand

        stack = [dict(half_cnt)]
        prefix = []
        pos = 0
        while pos < half and stack[pos].get(t_left[pos], 0) > 0:
            c = t_left[pos]
            prefix.append(c)
            nxt = dict(stack[pos])
            nxt[c] -= 1
            stack.append(nxt)
            pos += 1

        start = pos - 1 if pos == half else pos
        for p in range(start, -1, -1):
            avail = stack[p]
            bigger = sorted(c for c in avail if avail[c] > 0 and c > t_left[p])
            if bigger:
                c = bigger[0]
                rem = dict(avail)
                rem[c] -= 1
                left = "".join(prefix[:p]) + c + smallest(rem)
                return left + mid + left[::-1]
        return ""
