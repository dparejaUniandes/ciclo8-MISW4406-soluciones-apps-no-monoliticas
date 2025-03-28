import datetime

import pulsar
from pulsar.schema import *

from gestionclientes.modulos.facturacion.infraestructura.schema.v1.comandos import (
    ComandoRealizarPago, ComandoRealizarPagoPayload)
from gestionclientes.modulos.facturacion.infraestructura.schema.v1.eventos import (
    EventoPagoConfirmado, EventoPagoRealizado, PagoConfirmadoPayload,
    PagoRealizadoPayload)
from gestionclientes.seedwork.infraestructura import utils

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
        payload = PagoRealizadoPayload(
            id_cliente=str(evento.id_cliente), 
            estado=str(evento.estado), 
            fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
        )
        evento_integracion = EventoPagoRealizado(data=payload)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPagoRealizado))
    
    def publicar_evento_notificacion(self, evento, topico):
        payload = PagoConfirmadoPayload(
            id_correlacion=str(evento.id_correlacion),
            tipo=str(evento.tipo), 
            valor=str(evento.valor), 
            medio=str(evento.medio)
        )
        evento_integracion = EventoPagoConfirmado(data=payload, event_type=evento.event_type)
        self._publicar_mensaje(evento_integracion, topico, AvroSchema(EventoPagoConfirmado))

    def publicar_comando(self, comando, topico):
        payload = ComandoRealizarPagoPayload(
            id_correlacion=comando.id_correlacion,
            id_cliente=str(comando.id_cliente),
            monto = float(comando.monto)
        )
        comando_integracion = ComandoRealizarPago(data=payload)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoRealizarPago))
