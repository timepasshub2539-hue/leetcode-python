import bisect
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        for a in arr1:
            i = bisect.bisect_left(arr2, a)
            ok = True
            if i < len(arr2) and abs(arr2[i]-a) <= d: ok = False
            if i > 0 and abs(arr2[i-1]-a) <= d: ok = False
            if ok: count += 1
        return count
