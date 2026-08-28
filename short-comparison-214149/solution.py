from multiprocessing import Process
from threading import Thread

def work(n): print(n * n)

# Processes: separate memory, true parallel CPU
workers = [Process(target=work, args=(i,)) for i in range(4)]

# Threads: shared memory, same core (GIL-bound)
workers = [Thread(target=work, args=(i,)) for i in range(4)]
