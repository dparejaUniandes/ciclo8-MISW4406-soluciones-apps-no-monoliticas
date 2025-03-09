from dataclasses import dataclass, field

from pulsar.schema import *

from gestionclientes.seedwork.infraestructura.schema.v1.comandos import \
    ComandoIntegracion


class ComandoRealizarPagoPayload(ComandoIntegracion):
    id_correlacion = String()
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

class ComandoRevertirPayload(ComandoIntegracion):
    id_correlacion = String()
    id_cliente = String()

class ComandoRevertir(ComandoIntegracion):
    data = ComandoRevertirPayload()
    command_type = String()
