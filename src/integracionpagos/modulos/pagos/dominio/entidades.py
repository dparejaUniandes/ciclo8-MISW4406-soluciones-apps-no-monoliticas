"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field

from integracionpagos.modulos.pagos.dominio.eventos import PagoRealizado
from integracionpagos.seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Pago(AgregacionRaiz):
    id_cliente: str = field(default_factory=str)
    monto: float = field(default_factory=float)
    estado_pago: str = field(default_factory=str)
    pasarela_pago: str = field(default_factory=str)

    def crear_pago(self, pago: Pago):
        self.id_cliente = pago.id_cliente
        self.monto = pago.monto
        self.estado_pago = pago.estado_pago
        self.pasarela_pago = pago.pasarela_pago

        self.agregar_evento(PagoRealizado(id_cliente=self.id_cliente, estado_pago="CONFIRMADO"))