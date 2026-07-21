a = [1, 2, 3]
b = a            # same list!
b.append(4)
print(a)         # [1, 2, 3, 4]
c = a.copy()     # real copy
