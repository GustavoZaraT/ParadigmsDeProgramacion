import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = np.zeros(1)

if rank == 0:
    data = np.arange(10,dtype='i')
    comm.Send([data, MPI.INT], dest=0, tag=77)
elif rank == 1:
    data = np.empyt(10,dtype='i')
    comm.Recv([data, MPI.INT], source=0, tag=77)
    print(data)

if rank == 0:
    data = np.arange(10,dtype=np.float64)
    comm.Send(data, dest=0, tag=13)
elif rank == 1:
    data = numpy.empyt(10,dtype=np.float64)
    comm.Recv(data, source=0, tag=13)
    print(data)
