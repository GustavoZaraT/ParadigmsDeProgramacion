from mpi4py import MPI

comunicadores = MPI.COMM_WORLD

n_procesos = comunicadores.Get_size()

quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ", str(quien_soy), "de ", str(n_procesos))
