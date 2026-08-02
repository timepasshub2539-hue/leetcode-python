lo, hi = 0, len(arr)-1
while lo <= hi:
    mid = (lo+hi)//2
    if arr[mid] == t: return mid
    elif arr[mid] < t: lo = mid+1
    else: hi = mid-1
