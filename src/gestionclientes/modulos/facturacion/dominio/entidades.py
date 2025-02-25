"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field

import gestionclientes.modulos.facturacion.dominio.objetos_valor as ov
from gestionclientes.modulos.facturacion.dominio.eventos import PagoRealizado
from gestionclientes.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class Facturacion(AgregacionRaiz):
    medioPago: ov.MedioPago = field(default_factory=ov.MedioPago)
    idCliente: ov.IdCliente = field(default_factory=ov.IdCliente)
    monto: int = field(default_factory=int)


    def crear_facturacion(self, facturacion: Facturacion):
        self.medioPago = facturacion.medioPago
        self.idCliente = facturacion.idCliente
        self.monto = facturacion.monto

        self.agregar_evento(PagoRealizado(id_cliente=self.idCliente, estado="PAGADO"))
