from dataclasses import dataclass, field

from pulsar.schema import *

from integracionpagos.seedwork.infraestructura.schema.v1.comandos import \
    ComandoIntegracion


class ComandoRealizarPagoPayload(ComandoIntegracion):
    """ Payload para el comando de realizar pago """
    id_cliente = String()
    monto = Float()


class ComandoRealizarPago(ComandoIntegracion):
    """ Comando para realizar pago """
    data = ComandoRealizarPagoPayload()
