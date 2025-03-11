import datetime

import pulsar
from pulsar.schema import *

from notificaciones.modulos.notificaciones.infraestructura.schema.v1.eventos import (
    EventoNotificacionCreada, NotificacionCreadaPayload)
from notificaciones.seedwork.infraestructura import utils

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Despachador:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()

    def publicar_evento(self, evento, topico):
        print("evento emitido desde notidicaciones ", evento)
        payload = NotificacionCreadaPayload(
            id_cliente=str(evento.id_cliente), 
            id_correlacion=str(evento.id_correlacion)
        )
        evento_integracion = EventoNotificacionCreada(data=payload, event_type=evento.event_type)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoNotificacionCreada))
    
