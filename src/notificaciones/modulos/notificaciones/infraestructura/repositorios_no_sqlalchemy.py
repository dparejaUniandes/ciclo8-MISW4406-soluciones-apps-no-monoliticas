""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import uuid
from uuid import UUID

from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.dominio.fabricas import FabricaNotificaciones
from notificaciones.modulos.notificaciones.dominio.repositorios import (
    RepositorioNotificaciones, RepositorioNotificacionesNoSQLAlchemy)

from .dto import Notificacion as NotificacionDTO
from .mapeadores import MapeadorNotificacion

# Sin Flask
import sqlite3

sqliteConnection = None

def init_db():
    global sqliteConnection
    if sqliteConnection is None:
        sqliteConnection = sqlite3.connect('sql_notificaciones.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS notificaciones(id, fecha_creacion, fecha_actualizacion,tipo,valor,medio)")
        cursor.close()
        return sqliteConnection
    else:
        return sqliteConnection


class RepositorioNotificacionesPostgresqlNoSQLAlchemy(RepositorioNotificacionesNoSQLAlchemy):

    def __init__(self):
        self._fabrica_notificaciones: FabricaNotificaciones = FabricaNotificaciones()

    @property
    def fabrica_notificaciones(self):
        return self._fabrica_notificaciones

    def obtener_por_id(self, id: UUID) -> Notificacion:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Notificacion]:
        # TODO
        raise NotImplementedError

    def agregar(self, notificacion: Notificacion):
        notificacion_dto = self.fabrica_notificaciones.crear_objeto(notificacion, MapeadorNotificacion())
        cursor = init_db().cursor()
        cursor.execute("INSERT INTO notificaciones VALUES(?,?,?,?,?,?)", 
                       (notificacion_dto.id,
                       notificacion_dto.fecha_creacion,
                       notificacion_dto.fecha_actualizacion,
                       notificacion_dto.tipo,
                       notificacion_dto.valor,
                       notificacion_dto.medio.value)
                    )
        cursor.close()

    def actualizar(self, pago: Notificacion):
        # TODO
        raise NotImplementedError

    def eliminar(self, notificacion_id: UUID):
        # TODO
        raise NotImplementedError
