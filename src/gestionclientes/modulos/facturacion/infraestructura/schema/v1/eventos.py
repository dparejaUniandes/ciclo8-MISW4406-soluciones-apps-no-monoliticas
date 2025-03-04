from pulsar.schema import *

from gestionclientes.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class PagoRealizadoPayload(Record):
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoPagoRealizado(EventoIntegracion):
    data = PagoRealizadoPayload()

class PagoConfirmadoPayload(Record):
    tipo = String()
    valor = String()
    medio = String()

class EventoPagoConfirmado(EventoIntegracion):
    data = PagoConfirmadoPayload()