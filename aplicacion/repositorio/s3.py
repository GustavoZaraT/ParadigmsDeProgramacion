from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario


class S3(RepositorioDeUsuarios):
    __clienteId: str
    __scurityKey: str
    __bucket: str

    def __init__(mi, clienteId: str, secretKey: str, bucket: str):
        mi.__clienteId = clienteId
        mi.__secretKey = secretKey
        mi.__bucket = bucket

    def abrir(mi) -> None:
        print(f"Estableciendo conexion a AWS S3 {mi.__clienteId}:{mi.__secretKey}")

    def guardar(mi, usuario:Usuario) -> None:
        userData = {"nombre": usuario.getNombre(), "apellido": usuario.getApellido(), "edad": usuario.getEdad()}
        print(f"Gusardando usuario de la bandeja:{mi.__bucket}: {userData}")

    def cerrar(mi) -> None:
        print("Cerrando conexion AWS S3")
