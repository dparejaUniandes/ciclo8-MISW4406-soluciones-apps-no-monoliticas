""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import uuid
from uuid import UUID

from gestionclientes.config.db import db
from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.fabricas import FabricaClientes
from gestionclientes.modulos.clientes.dominio.objetos_valor import \
    NombreCliente
from gestionclientes.modulos.clientes.dominio.repositorios import \
    RepositorioClientes

from .dto import SagaLog as ClienteDTO


class RepositorioClientesPostgresql(RepositorioClientes):

    def __init__(self):
        self._fabrica_clientes: FabricaClientes = FabricaClientes()

    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes

    def obtener_por_id(self, id: UUID) -> Cliente:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Cliente]:
        # TODO
        raise NotImplementedError

    def agregar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def actualizar(self, cliente: Cliente):
        # TODO
        raise NotImplementedError

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError
