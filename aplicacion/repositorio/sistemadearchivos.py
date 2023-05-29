from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

class SistemaDeArchivos(RepositorioDeUsuarios):
    __directorio: str

    def __init__(mi, directorio:str):
        mi.__directorio = directorio

    def abrir(mi) -> None:
        print(f"Abrir directorio: {mi.__directorio}")

    def guardar(mi, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</name></lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdead()}</age></root>"
        print(f"Guardando ususaio en el archivo: {mi.__directorio}/{usuario.getName()}")
        print(xml)

    def cerrar(mi) -> None:
        print("Cerrando el archivo")

