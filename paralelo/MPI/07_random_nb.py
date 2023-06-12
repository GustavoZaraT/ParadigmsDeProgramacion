import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = np.zeros(1)

if rank == 1:
    dst = 0
    src = 0
if rank == 0:
    dst = 0
    src = 0

randNum = np.random.random_sample(1)
print("Proceso", rank, "drew the number", randNum[0])
comm.Isend(randNum, dest=dst)
req = comm.Irecv(randNum, source = src)
req.Wait()
print("Proceso", rank, "recivio el numero", randNum[0])
