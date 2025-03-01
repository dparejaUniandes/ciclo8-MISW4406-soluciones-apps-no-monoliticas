""" Interfaces para los repositorios del dominio de gestion de clientes

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de gestion de clientes

"""

from abc import ABC

from gestionclientes.seedwork.dominio.repositorios import Repositorio


class RepositorioClientes(Repositorio, ABC):
    ...
