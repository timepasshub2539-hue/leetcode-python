class Solution:
    def maxNumOfSubstrings(self, s):
        first, last = {}, {}
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        ranges = []
        for c, start in first.items():
            end = last[c]
            i = start
            while i <= end:
                end = max(end, last[s[i]])
                i += 1
            ranges.append((start, end))

        ranges.sort(key=lambda r: r[1])
        result = []
        prev_end = -1
        for start, end in ranges:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
        return result
