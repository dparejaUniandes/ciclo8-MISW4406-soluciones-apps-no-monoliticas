from abc import ABC

from gestionclientes.seedwork.dominio.repositorios import Repositorio


class RepositorioSagas(Repositorio, ABC):
    ...
