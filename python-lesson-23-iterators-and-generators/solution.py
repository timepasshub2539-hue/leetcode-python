def count_up():
    yield 1
    yield 2
    yield 3

gen = count_up()
print(next(gen))  # 1, pauses here
print(next(gen))  # 2, pauses here
print(next(gen))  # 3, done after this
