from threading import Thread
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

threads =[]
cpus = os.cpu_count()
print("Nucleos en tu cpu: ", cpus)
for i in range(cpus):
    print("registradondo el hilo %d" % i)
    threads.append(Thread())

start = time.time()

for t in threads:
    t.start()

for t in threads:
    t.join()

end = time.time()
print("Se tardo : ", end-start, "s")
