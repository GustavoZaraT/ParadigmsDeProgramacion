from aplicacion.repositorio.basededatos import BaseDeDatos
from aplicacion.repositorio.s3 import S3
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones
from aplicacion.modelos.usuario import Usuario

usuario = Usuario("Roberto","Jimenez",18)

repositorioS3 = S3("321321321","sdf324223","MiCubeta")

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")
