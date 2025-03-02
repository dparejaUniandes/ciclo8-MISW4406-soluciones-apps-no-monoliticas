from dataclasses import dataclass, field

from integracionpagos.modulos.pagos.aplicacion.dto import PagoDTO
from integracionpagos.modulos.pagos.aplicacion.mapeadores import MapeadorPago
from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.modulos.pagos.infraestructura.repositorios import \
    RepositorioPagos
from integracionpagos.seedwork.aplicacion.comandos import Comando
from integracionpagos.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from integracionpagos.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import PagoBaseHandler


@dataclass
class RealizarPago(Comando):
    id_cliente: str
    monto: float

class RealizarPagoHandler(PagoBaseHandler):
    
    def handle(self, comando: RealizarPago):
        pago_dto = PagoDTO(
            id_cliente=comando.id_cliente,
            monto=comando.monto
        )

        pago: Pago = self.fabrica_pagos.crear_objeto(pago_dto, MapeadorPago())
        pago.crear_pago(pago)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPagos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, pago)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(RealizarPago)
def ejecutar_comando_crear_cliente(comando: RealizarPago):
    handler = RealizarPagoHandler()
    handler.handle(comando)
    