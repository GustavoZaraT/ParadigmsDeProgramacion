from multiprocessing import Process, Queue
def pow2(x,q):
    q.put((x,x*x))

if __name__ == "__main__":
    q = Queue()
    pr = [Process(target = pow2, args=(i,q)) for i in range(2, 10)]
    for p in pr:
        p.start()
    for p in pr:
        p.join()
        r = [q.get() for p in pr]
        print(r)
