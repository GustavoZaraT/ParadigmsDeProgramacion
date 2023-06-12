from mpi4py import MPI

class Mensaje:
    def __init__(self, rank):
        self.x = range(rank*10)
        self.p = "vengo del proceso " + str(rank)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)
    fuente = rank-1 if rank!=0 else size-1
    destino = rank+1 if rank!=size-1 else 0

    if rank%2==0:
        comm.send(s, dest=destino)
        m = comm.recv(source=fuente)
    else:
        m = comm.recv(source=fuente)
        comm.send(s,dest=destino)

    print("SOy el proceso ", rank, ", el resultado es ", len(m.x), " ", m.p)
