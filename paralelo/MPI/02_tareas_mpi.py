from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.Get_size()

rank = comm.Get_rank()

if rank == 0:
    print("Yo soy el proceso 0")

elif rank == 1:
    print("Yo soy el porceso 1")

else:
    print("Yo no soy ninguno de los dos primeros procesos")

print("Reportándome, soy el proceso ", str(rank), " de ", str(size))
