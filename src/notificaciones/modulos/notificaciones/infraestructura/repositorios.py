""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from uuid import UUID

from notificaciones.config.db import db
from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.dominio.fabricas import FabricaNotificaciones
from notificaciones.modulos.notificaciones.dominio.objetos_valor import \
    TipoMedio
from notificaciones.modulos.notificaciones.dominio.repositorios import \
    RepositorioNotificaciones

from .dto import Notificacion as NotificacionDTO
from .mapeadores import MapeadorNotificacion


class RepositorioNotificacionesSQLite(RepositorioNotificaciones):
    """ Repositorio de notificaciones en SQLite """

    def __init__(self):
        self._fabrica_notificaciones: FabricaNotificaciones = FabricaNotificaciones()

    @property
    def fabrica_notificaciones(self):
        """ Fabrica de notificaciones """
        return self._fabrica_notificaciones

    def obtener_por_id(self, id: UUID) -> Notificacion:
        """ Obtener una notificacion por su id """
        cliente_dto = db.session.query(
            NotificacionDTO).filter_by(id=str(id)).one()
        return self._fabrica_notificaciones.crear_objeto(cliente_dto, MapeadorNotificacion())

    def obtener_todos(self) -> list[Notificacion]:
        """ Obtener todos los notificaciones """
        notificaciones = db.session.query(NotificacionDTO).all()
        return self._fabrica_notificaciones.crear_objeto(notificaciones, MapeadorNotificacion())

    def agregar(self, notificacion: NotificacionDTO):
        """ Agregar un notificacion """
        print(f'INFRAESTRUCTURA - Notificacion recibida en repositorio: {notificacion}')
        notificacion_dto = self.fabrica_notificaciones.crear_objeto(
            notificacion, MapeadorNotificacion())
        print(f'INFRAESTRUCTURA - Notificacion creada en repositorio: {notificacion_dto}')
        db.session.add(notificacion_dto)
        db.session.commit()
        print("INFRAESTRUCTURA - ok")

    def actualizar(self, cliente: Notificacion):
        """ Actualizar un notificacion """
        db.session.query(NotificacionDTO).filter(
            NotificacionDTO.id == cliente.idDesdeBD).update({'estado_plan': cliente.estadoPlan})
        db.session.commit()

    def eliminar(self, cliente_id: UUID):
        """ Eliminar un notificacion """
        raise NotImplementedError
