import copy
a = [[1,2], [3,4]]
b = copy.deepcopy(a)
b[0][0] = 99
print(a)  # [[1,2],[3,4]] -- unchanged
