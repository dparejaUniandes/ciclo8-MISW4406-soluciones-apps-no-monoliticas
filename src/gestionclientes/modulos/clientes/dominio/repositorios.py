""" Interfaces para los repositorios del dominio de notificaciones

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de notificaciones

"""

from abc import ABC

from gestionclientes.seedwork.dominio.repositorios import Repositorio


class RepositorioNotificaciones(Repositorio, ABC):
    """ Interfaz para los repositorios de notificaciones """
