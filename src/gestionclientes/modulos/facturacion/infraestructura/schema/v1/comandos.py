from dataclasses import dataclass, field

from pulsar.schema import *

from gestionclientes.seedwork.infraestructura.schema.v1.comandos import \
    ComandoIntegracion


class ComandoRealizarPagoPayload(ComandoIntegracion):
    id_cliente = String()
    monto = Float()

class ComandoRealizarPago(ComandoIntegracion):
    data = ComandoRealizarPagoPayload()

class ComandoRealizarPagoPayloadBFF(ComandoIntegracion):
    medioPago = String()
    idCliente = String()
    monto = Float()

class ComandoRealizarPagoBFF(ComandoIntegracion):
    data = ComandoRealizarPagoPayloadBFF()