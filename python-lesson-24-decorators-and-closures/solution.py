import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        print(func.__name__, "took", time.time() - start)
        return result
    return wrapper

@timer
def slow():
    time.sleep(1)

slow()
