def f(a, *args, **kwargs):
    print(a)        # first value
    print(args)     # the rest
    print(kwargs)   # named ones

f(1, 2, 3, x=9)
