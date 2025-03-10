from pulsar.schema import *

from notificaciones.seedwork.infraestructura.schema.v1.eventos import \
    EventoIntegracion


class NotificacionCreadaPayload(Record):
    id_correlacion = String()
    id_cliente = String()

class EventoNotificacionCreada(EventoIntegracion):
    data = NotificacionCreadaPayload()
    event_type = String()