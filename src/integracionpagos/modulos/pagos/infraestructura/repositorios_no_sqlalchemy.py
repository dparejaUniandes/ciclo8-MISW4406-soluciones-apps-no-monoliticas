""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import uuid
from uuid import UUID

from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.modulos.pagos.dominio.fabricas import FabricaPago
from integracionpagos.modulos.pagos.dominio.repositorios import (
    RepositorioPagos, RepositorioPagosNoSQLAlchemy)

from .dto import Pago as PagoDTO
from .mapeadores import MapeadorPago

# Sin Flask
import sqlite3

sqliteConnection = None

def init_db():
    global sqliteConnection
    if sqliteConnection is None:
        sqliteConnection = sqlite3.connect('sql_integracionpagos.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pagos(id, fecha_creacion, fecha_actualizacion,id_cliente,monto,estado_pago,pasarela_pago)")
        cursor.close()
        return sqliteConnection
    else:
        return sqliteConnection


class RepositorioPagosPostgresqlNoSQLAlchemy(RepositorioPagosNoSQLAlchemy):

    def __init__(self):
        self._fabrica_pagos: FabricaPago = FabricaPago()

    @property
    def fabrica_pagos(self):
        return self._fabrica_pagos

    def obtener_por_id(self, id: UUID) -> Pago:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Pago]:
        # TODO
        raise NotImplementedError

    def agregar(self, pagos: Pago):
        pago_dto = self.fabrica_pagos.crear_objeto(pagos, MapeadorPago())
        cursor = init_db().cursor()
        data = cursor.execute("SELECT * FROM pagos")
        cursor.execute("INSERT INTO pagos VALUES(?,?,?,?,?,?,?)", 
                       (pago_dto.id,
                       pago_dto.fecha_creacion,
                       pago_dto.fecha_actualizacion,
                       pago_dto.id_cliente,
                       pago_dto.monto,
                       pago_dto.estado_pago,
                       pago_dto.pasarela_pago)
                    )
        cursor.close()
        # pago_dto.id = str(uuid.uuid4())
        # db.session.add(pago_dto)
        # db.session.commit()

    def actualizar(self, pago: Pago):
        # TODO
        raise NotImplementedError

    def eliminar(self, pago_id: UUID):
        # TODO
        raise NotImplementedError
