from multiprocessing import Process
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

procesos = []
cpus = os.cpu_count()
print("Nucleos en tu CPU: ", cpus)
for i in range(cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

for p in procesos:
    p.start()

for p in procesos:
    p.join()

end = time.time()
print("Se tardo: ", end-start)
