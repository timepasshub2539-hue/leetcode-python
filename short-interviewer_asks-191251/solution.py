from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def spin(n):
    x = 0
    for i in range(n):
        x += i * i
    return x

# ThreadPoolExecutor(4): ~2.1s
# ProcessPoolExecutor(4): ~0.6s
