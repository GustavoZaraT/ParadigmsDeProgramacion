from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

class BaseDeDatos(RepositorioDeUsuarios):
    __host: str
    __user: str
    __password: str

    def __inti__(mi, host:str, user:str, password:str):
        mi.__host = host
        mi.__user = huser
        mi.__password = password

    def abrir(mi) -> None:
        print(f"Abriendo la conexion a la base de datos: {mi.__host}:{mi.__user}@{mi.__pasword}")

    def guardar(mi, usuario:Usuario) -> None:
        userElements = {"nombre":usuario.getNombre(),"apellido":usuario.getApellido(),"edad":usuario.getEdad()}
        print(f"Gusardando el usuario en la base de datos {usuario.getNombre()}\n")
        print(f"INSERTAR DATOS DEL USUARIO ('{userElements['nombre']}','{userElements['apellido']}','{userElements['edad']}')")

    def cerrar(mi) -> None:
        print("Cerrando la conexion")
