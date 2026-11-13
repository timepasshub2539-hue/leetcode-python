from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        m = nums[::-1]
        n = len(m)
        stack = deque()
        cost = 0
        l = 0
        ans = 0
        for r in range(n):
            cnt = 1
            while stack and stack[-1][0] <= m[r]:
                v, c = stack.pop()
                cost += (m[r] - v) * c
                cnt += c
            stack.append([m[r], cnt])
            while cost > k:
                v = stack[0][0]
                cost -= v - m[l]
                stack[0][1] -= 1
                if stack[0][1] == 0:
                    stack.popleft()
                l += 1
            ans += r - l + 1
        return ans
