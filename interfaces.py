from aplicacion.repositorio.basededatos import BaseDeDatos

from aplicacion.repositorio.s3 import S3

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos

from aplicacion.negocios.manejodeincripciones import ManejoDeInscripciones

usuario = Ususario("Roberto","Jimenez",18)

repositorioS3 = S3("321321321","sdf324223","MiCubeta")

ManejoDeInscripciones.insribirUsuario(usuario,repositorioS3)
print("\n")

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

ManejoDEInscripciones.inscribirUsusario(usuario,repositorioSistemaDeArchivos)
print("\n")

repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

ManejoDeInscripciones.inscribirUsusario(usuario,repositorioBaseDeDatos)
print("\n")
