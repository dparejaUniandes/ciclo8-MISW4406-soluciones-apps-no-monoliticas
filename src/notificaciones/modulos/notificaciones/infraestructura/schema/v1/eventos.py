from pulsar.schema import *

from integracionpagos.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class PagoConfirmadoPayload(Record):
    """ Payload para el evento de pago confirmado """
    tipo = String() # ALERTA, RECORDATORIO, INFORMATIVO
    valor = String() # pepe@gmail.com
    medio = String() # correo

class EventoPagoConfirmado(EventoIntegracion):
    """ Evento de pago confirmado """
    data = PagoConfirmadoPayload()
