class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        idx = 1
        first = prev_idx = last = None
        min_dist = float('inf')
        while curr.next:
            is_peak = curr.val > prev.val and curr.val > curr.next.val
            is_valley = curr.val < prev.val and curr.val < curr.next.val
            if is_peak or is_valley:
                if first is None:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
                last = idx
            prev, curr = curr, curr.next
            idx += 1
        if first is None or first == last:
            return [-1, -1]
        return [min_dist, last - first]
