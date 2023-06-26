from multiprocessing import Process, Pipe

def f(x):
    x.send([0,1,2,3,4])
    x.close()

def g(x):
    a = x.recv()
    for i in a:
        a[i] += 100
    print(a)

if __name__ == "__main__":
    x1, x2, = Pipe()
    p1 = Process(target=f, args=(x1,))
    p2 = Process(target=f, args=(x2,))
    p2.start()
    p1.start()
    p1.join()
    p2.join()
