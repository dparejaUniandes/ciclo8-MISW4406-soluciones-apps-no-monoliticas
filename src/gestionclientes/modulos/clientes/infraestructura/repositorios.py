""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from uuid import UUID

from gestionclientes.config.db import db
from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.fabricas import FabricaClientes
from gestionclientes.modulos.clientes.dominio.objetos_valor import \
    NombreCliente
from gestionclientes.modulos.clientes.dominio.repositorios import \
    RepositorioClientes

from .dto import Cliente as ClienteDTO
from .mapeadores import MapeadorCliente


class RepositorioClientesPostgresql(RepositorioClientes):

    def __init__(self):
        self._fabrica_clientes: FabricaClientes = FabricaClientes()

    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes

    def obtener_por_id(self, id: UUID) -> Cliente:
        cliente_dto = db.session.query(ClienteDTO).filter_by(id=str(id)).one()
        return self._fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())

    def obtener_todos(self) -> list[Cliente]:
        clientes = db.session.query(ClienteDTO).all()
        return self._fabrica_clientes.crear_objeto(clientes, MapeadorCliente())

    def agregar(self, cliente: Cliente):
        cliente_dto = self.fabrica_clientes.crear_objeto(cliente, MapeadorCliente())
        db.session.add(cliente_dto)
        db.session.commit()

    def actualizar(self, cliente: Cliente):
        db.session.query(ClienteDTO).filter(ClienteDTO.id == cliente.idDesdeBD).update({'estado_plan': cliente.estadoPlan})
        db.session.commit()

    def eliminar(self, cliente_id: UUID):
        # TODO
        raise NotImplementedError
