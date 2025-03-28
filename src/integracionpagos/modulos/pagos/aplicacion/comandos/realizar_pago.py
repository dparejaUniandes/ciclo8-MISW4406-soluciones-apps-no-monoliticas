from dataclasses import dataclass, field

from integracionpagos.modulos.pagos.aplicacion.dto import PagoDTO
from integracionpagos.modulos.pagos.aplicacion.mapeadores import MapeadorPago
from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.modulos.pagos.dominio.eventos import PagoRealizado
from integracionpagos.modulos.pagos.dominio.repositorios import \
    RepositorioPagosNoSQLAlchemy
from integracionpagos.modulos.pagos.infraestructura.despachadores import \
    Despachador
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
    id_correlacion: str

class RealizarPagoHandler(PagoBaseHandler):
    
    def handle(self, comando: RealizarPago):
        pago_dto = PagoDTO(
            id_cliente=comando.id_cliente,
            monto=comando.monto
        )

        print("Pago xyz. ", pago_dto)

        pago: Pago = self.fabrica_pagos.crear_objeto(pago_dto, MapeadorPago())
        pago.crear_pago(pago)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioPagosNoSQLAlchemy.__class__)
        repositorio.agregar(pago)

        pago_realizado = PagoRealizado(
            id_cliente=pago_dto.id_cliente,
            estado_pago = "CONFIRMADO",
            id_correlacion=comando.id_correlacion
        )
        despachador = Despachador()
        despachador.publicar_evento(pago_realizado, 'eventos-pago')

        # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, pago)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()


@comando.register(RealizarPago)
def ejecutar_comando_realizar_pago(comando: RealizarPago):
    handler = RealizarPagoHandler()
    handler.handle(comando)
    