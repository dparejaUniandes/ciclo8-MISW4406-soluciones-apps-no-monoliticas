""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from uuid import UUID
import uuid

from gestionclientes.config.db import db
from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.fabricas import \
    FabricaFacturacion
from gestionclientes.modulos.facturacion.dominio.objetos_valor import MedioPago
from gestionclientes.modulos.facturacion.dominio.repositorios import \
    RepositorioFacturacion

from .dto import Facturacion as FacturacionDTO
from .mapeadores import MapeadorFacturacion


class RepositorioFacturacionPosgresql(RepositorioFacturacion):

    def __init__(self):
        self._fabrica_facturacion: FabricaFacturacion = FabricaFacturacion()

    @property
    def fabrica_facturacion(self):
        return self._fabrica_facturacion

    def obtener_por_id(self, id: UUID) -> Facturacion:
        facturacion_dto = db.session.query(FacturacionDTO).filter_by(id=str(id)).one()
        return self._fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())

    def obtener_todos(self) -> list[Facturacion]:
        facturacion = db.session.query(FacturacionDTO).all()
        return self._fabrica_facturacion.crear_objeto(facturacion, MapeadorFacturacion())

    def agregar(self, facturacion: Facturacion):
        facturacion_dto = self.fabrica_facturacion.crear_objeto(facturacion, MapeadorFacturacion())
        facturacion_dto.id = str(uuid.uuid4())
        db.session.add(facturacion_dto)
        db.session.commit()

    def actualizar(self, reserva: Facturacion):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError
