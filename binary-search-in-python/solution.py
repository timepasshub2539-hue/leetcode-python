arr = [3, 8, 12, 17, 21, 25, 29, 33, 37, 41]
binary_search(arr, 33)

# low=0 high=9 mid=4 -> arr[4]=21, too small
# low=5 high=9 mid=7 -> arr[7]=33, match
# returns 7
