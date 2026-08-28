from multiprocessing import Process
p = Process(target=worker)
p.start()
