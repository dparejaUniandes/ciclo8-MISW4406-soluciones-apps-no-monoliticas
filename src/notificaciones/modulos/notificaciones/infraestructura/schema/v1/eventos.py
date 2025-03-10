from pulsar.schema import *

from integracionpagos.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class PagoConfirmadoPayload(Record):
    """ Payload para el evento de pago confirmado """
    id_correlacion = String()
    tipo = String()
    valor = String()
    medio = String()

class EventoPagoConfirmado(EventoIntegracion):
    """ Evento de pago confirmado """
    data = PagoConfirmadoPayload()
