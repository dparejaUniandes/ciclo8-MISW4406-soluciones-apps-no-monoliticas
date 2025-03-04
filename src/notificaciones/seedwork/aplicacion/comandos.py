""" Comandos """
from abc import ABC, abstractmethod
from functools import singledispatch


class Comando:
    """ Comando """

class ComandoHandler(ABC):
    """ Manejador de comandos """
    @abstractmethod
    def handle(self, comando: Comando):
        """ Ejecutar comando """
        raise NotImplementedError()

@singledispatch
def ejecutar_commando(comando):
    """ Ejecutar comando """
    raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')