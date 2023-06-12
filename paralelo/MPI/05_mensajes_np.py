from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self, rank):
        self.x = np.array([float(x+rank) for x in range(rank*10)])
        self.p = "vengo del proceso " + str(rank)
        
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0
    m = s.x
    comm.Isend(m, dest=dst)
    a = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(a, source=src)
    req.Wait()

    print("SOy el proceso ", rank, ", el resultado es ", a)                                                                                
