class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        min_len = [float('inf')] * n
        seen = {0: -1}
        cur_sum = 0
        cur_best = float('inf')
        best = float('inf')
        for i, x in enumerate(arr):
            cur_sum += x
            need = cur_sum - target
            if need in seen:
                start = seen[need]
                length = i - start
                if start != -1 and min_len[start] < float('inf'):
                    best = min(best, length + min_len[start])
                cur_best = min(cur_best, length)
            min_len[i] = cur_best
            seen[cur_sum] = i
        return best if best < float('inf') else -1
