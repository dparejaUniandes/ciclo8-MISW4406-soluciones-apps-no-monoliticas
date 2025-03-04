""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import os
# Sin Flask
import sqlite3
import uuid
from uuid import UUID

from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.fabricas import \
    FabricaFacturacion
from gestionclientes.modulos.facturacion.dominio.repositorios import (
    RepositorioFacturacion, RepositorioFacturacionNoSQLAlchemy)

from .dto import Facturacion as FacturacionDTO
from .mapeadores import MapeadorFacturacion

sqliteConnection = None

def init_db():
    global sqliteConnection
    if sqliteConnection is None:
        sqliteConnection = sqlite3.connect(
            os.path.join('/workspace/ciclo8-MISW4406-soluciones-apps-no-monoliticas/src/gestionclientes/config', 'database.db'))
        cursor = sqliteConnection.cursor()
        return sqliteConnection
    else:
        return sqliteConnection


class RepositorioFacturacionPostgresqlNoSQLAlchemy(RepositorioFacturacionNoSQLAlchemy):

    def __init__(self):
        self._fabrica_facturacion: FabricaFacturacion = FabricaFacturacion()

    @property
    def fabrica_pagos(self):
        return self._fabrica_facturacion

    def obtener_por_id(self, id: UUID) -> Facturacion:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Facturacion]:
        # TODO
        raise NotImplementedError

    def agregar(self, facturacion: Facturacion):
        return None

    def actualizar(self, facturacion: Facturacion):
        cursor = init_db().cursor()
        cursor.execute("UPDATE facturacion SET estado_reportado = ? WHERE id_cliente = ?", 
                       (facturacion.estado_reportado,
                       facturacion.idCliente)
                    )
        cursor.close()

    def eliminar(self, facturacion_id: UUID):
        # TODO
        raise NotImplementedError
