from pulsar.schema import *

from gestionclientes.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class PagoRealizadoPayload(Record):
    id_correlacion = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoPagoRealizado(EventoIntegracion):
    data = PagoRealizadoPayload()
    event_type = String()

class PagoConfirmadoPayload(Record):
    id_correlacion = String()
    tipo = String()
    valor = String()
    medio = String()

class EventoPagoConfirmado(EventoIntegracion):
    data = PagoConfirmadoPayload()
    event_type = String()