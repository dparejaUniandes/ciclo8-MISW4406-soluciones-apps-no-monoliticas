from pulsar.schema import *

from integracionpagos.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class PagoRealizadoPayload(Record):
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()
    event_type = String()

class EventoPagoRealizado(EventoIntegracion):
    data = PagoRealizadoPayload()
    event_type = String()