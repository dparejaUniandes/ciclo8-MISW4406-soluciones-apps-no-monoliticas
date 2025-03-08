import logging
import time
import traceback
import uuid

import _pulsar
import pulsar
from pulsar.schema import *

from integracionpagos.modulos.pagos.aplicacion.comandos.realizar_pago import \
    RealizarPago
from integracionpagos.modulos.pagos.infraestructura.schema.v1.comandos import \
    ComandoRealizarPago
from integracionpagos.modulos.pagos.infraestructura.schema.v1.eventos import \
    EventoPagoRealizado
from integracionpagos.seedwork.aplicacion.comandos import ejecutar_commando
from integracionpagos.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-pago', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='integracionpagos-sub-eventos', schema=AvroSchema(EventoPagoRealizado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento emitido desde integración: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-pago', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='integracionpagos-sub-comandos', schema=AvroSchema(ComandoRealizarPago))

        while True:
            mensaje = consumidor.receive()
            print('=========================================')
            print("Comando Recibido desde integración pago: '%s'" % mensaje.value().data)
            print('=========================================')

            data = mensaje.value().data
            comando = RealizarPago(
                id_cliente=data.id_cliente,
                monto=data.monto
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