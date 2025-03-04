"""Consumidores de mensajes"""
import logging
import time
import traceback
import uuid

import _pulsar
import pulsar
from pulsar.schema import *

from notificaciones.modulos.notificaciones.aplicacion.comandos.crear_notificacion import \
    CrearNotificacion
from notificaciones.modulos.notificaciones.infraestructura.schema.v1.comandos import \
    ComandoRealizarPago
from notificaciones.modulos.notificaciones.infraestructura.schema.v1.eventos import \
    EventoPagoConfirmado
from notificaciones.seedwork.aplicacion.comandos import ejecutar_commando
from notificaciones.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    """Suscribirse a eventos"""
    cliente = None
    try:
        print("Esperando mensajes en Pulsar...")
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-gestionclientes',
                                       consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='notificaciones-sub-eventos',
                                       schema=AvroSchema(EventoPagoConfirmado))

        while True:
            mensaje = consumidor.receive()
            print(
                f'Evento recibido desde integración gestionclientes ========> notificaciones: {mensaje.value().data}')
            data = mensaje.value().data
            comando = CrearNotificacion(
                fecha_creacion=str(time.time()),
                fecha_actualizacion=str(time.time()),
                id=str(uuid.uuid4()),
                tipo=data.tipo,
                medio=data.medio,
                valor=data.valor
            )
            ejecutar_commando(comando)
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def suscribirse_a_comandos():
    """ Suscribirse a comandos """
    cliente = None
    try:
        print("Esperando mensajes en Pulsar...")
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-integracionauditoria',
                                       consumer_type=_pulsar.ConsumerType.Shared,
                                       subscription_name='notificaciones-sub-comandos',
                                       schema=AvroSchema(ComandoRealizarPago))

        while True:
            mensaje = consumidor.receive()
            print(
                f'Comando recibido desde integracionauditoria ========> notificaciones: {mensaje.value().data}')
            print('=========================================')
            print("Comando Recibido desde auditoria : '%s'" %
                  mensaje.value().data)
            print('=========================================')

            data = mensaje.value().data
            comando = CrearNotificacion(
                fecha_creacion=str(time.time()),
                fecha_actualizacion=str(time.time()),
                id=str(uuid.uuid4()),
                tipo=data.tipo,
                medio=data.medio,
                valor=data.valor
            )
            ejecutar_commando(comando)

            print('==== Comunicación con pasarela de pagos ====')

            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
