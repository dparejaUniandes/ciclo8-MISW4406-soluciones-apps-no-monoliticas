""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import uuid
from uuid import UUID

from gestionclientes.config.db import db
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas

from .mapeadores import MapeadorSagaLog
from .dto import SagaLog

class RepositorioSagasPostgresql(RepositorioSagas):

    def obtener_por_id(self, id: UUID) -> Saga:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> list[Saga]:
        # TODO
        raise NotImplementedError

    def agregar(self, saga: Saga):
        # TODO
        print("Saga agregada***, ", saga)
        saga_dto= SagaLog(
            id=saga.id,
            id_cliente = saga.id_cliente,
            id_correlacion = saga.id_correlacion,
            nombre_paso = saga.nombre_paso,
            estado=saga.estado,
            index = saga.index,
            fecha_creacion = saga.fecha_creacion
        )
        
        db.session.add(saga_dto)
        db.session.commit()

    def actualizar(self, saga: Saga):
        # TODO
        raise NotImplementedError

    def eliminar(self, saga_id: UUID):
        # TODO
        raise NotImplementedError
