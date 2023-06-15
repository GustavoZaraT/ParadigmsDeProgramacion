from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

class ManejoDeInscripciones:
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios: RepositorioDeUsuarios)-> None:
        print("----->Gusradndo usario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
