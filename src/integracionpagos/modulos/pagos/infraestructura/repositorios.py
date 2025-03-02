""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

import uuid
from uuid import UUID

from integracionpagos.config.db import db
from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.modulos.pagos.dominio.fabricas import FabricaPagos
from integracionpagos.modulos.pagos.dominio.repositorios import \
    RepositorioPagos

from .dto import Pago as PagoDTO
from .mapeadores import MapeadorPago


class RepositorioPagosPostgresql(RepositorioPagos):

    def __init__(self):
        self._fabrica_pagos: FabricaPagos = FabricaPagos()

    @property
    def fabrica_pagos(self):
        return self._fabrica_pagos

    def obtener_por_id(self, id: UUID) -> Pago:
        pago_dto = db.session.query(PagoDTO).filter_by(id=str(id)).one()
        return self._fabrica_pagos.crear_objeto(pago_dto, MapeadorPago())

    def obtener_todos(self) -> list[Pago]:
        pagos = db.session.query(PagoDTO).all()
        return self._fabrica_pagos.crear_objeto(pagos, MapeadorPago())

    def agregar(self, pagos: Pago):
        pago_dto = self.fabrica_pagos.crear_objeto(pagos, MapeadorPago())
        pago_dto.id = str(uuid.uuid4())
        db.session.add(pago_dto)
        db.session.commit()

    def actualizar(self, pago: Pago):
        db.session.query(PagoDTO).filter(PagoDTO.id == pago.idDesdeBD).update({'estado_plan': pago.estadoPlan})
        db.session.commit()

    def eliminar(self, pago_id: UUID):
        # TODO
        raise NotImplementedError
