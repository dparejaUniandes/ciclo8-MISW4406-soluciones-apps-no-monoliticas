from dataclasses import dataclass, field

from pulsar.schema import *

from integracionpagos.seedwork.infraestructura.schema.v1.comandos import \
    ComandoIntegracion


class ComandoRealizarPagoPayload(ComandoIntegracion):
    id_cliente = String()
    monto = Float()

class ComandoRealizarPago(ComandoIntegracion):
    data = ComandoRealizarPagoPayload()