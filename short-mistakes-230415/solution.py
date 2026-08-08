funcs = []
for i in range(3):
    funcs.append(lambda: i)
print(funcs[0]())  # 2, not 0
