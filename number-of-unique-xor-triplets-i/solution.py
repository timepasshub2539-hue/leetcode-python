def numberOfUniqueXorTriplets(nums):
    n = len(nums)
    if n == 1:
        return 1
    if n == 2:
        return 2
    return 1 << n.bit_length()

assert numberOfUniqueXorTriplets([1, 2]) == 2
assert numberOfUniqueXorTriplets([3, 1, 2]) == 4
