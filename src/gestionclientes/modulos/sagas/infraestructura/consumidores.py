import logging
import time
import traceback
import uuid

import _pulsar
import pulsar
from pulsar.schema import *
from pydispatch import dispatcher

from gestionclientes.modulos.sagas.dominio.eventos.pagos import (PagoFallido,
                                                                 PagoRealizado)
from gestionclientes.modulos.sagas.dominio.eventos.facturacion import (FacturacionCreada,
                                                                 FacturacionFallida)
from gestionclientes.modulos.sagas.infraestructura.schema.v1.eventos import \
    EventoPagoRealizado, EventoPagoConfirmado
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-pago', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sagas-sub-eventos', schema=AvroSchema(EventoPagoRealizado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde integración de pagos hacia sagas: {mensaje.value().data}')

            data = mensaje.value().data
            event_type = mensaje.value().event_type
            if event_type == "pago_realizado":
                print("**************** Consumidor saga: SE RECIBE PAGO REALIZADO **************")
                evento = PagoRealizado(
                    id_correlacion = data.id_correlacion,
                    id_cliente = data.id_cliente,
                    estado = data.estado
                )
                dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
            
            elif event_type == "pago_realizado_revertido":
                print("**************** Consumidor saga: SE RECIBE PAGO REALIZADO REVERTIDO**************")
                evento = PagoFallido(
                    id_correlacion = data.id_correlacion,
                    id_cliente = data.id_cliente,
                    estado = data.estado
                )
                dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)


            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_eventos_facturacion():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-gestionclientes-notificacion', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='sagas-sub-eventos', schema=AvroSchema(EventoPagoConfirmado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido desde facturación hacia sagas: {mensaje.value().data}')

            data = mensaje.value().data
            event_type = mensaje.value().event_type
            if event_type == "facturacion_actualizada":
                print("**************** Consumidor saga: SE RECIBE PAGO CONFIRMADO facturación **************")
                evento = FacturacionCreada(
                    id_correlacion = data.id_correlacion,
                    id_cliente = data.id_cliente,
                    estado = data.estado
                )
                dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)
            
            elif event_type == "facturacion_actualizada_revertida":
                print("**************** Consumidor saga: SE RECIBE PAGO CONFIRMADO facturación REVERTIDO**************")
                evento = FacturacionFallida(
                    id_correlacion = data.id_correlacion,
                    id_cliente = data.id_cliente,
                    estado = data.estado
                )
                dispatcher.send(signal=f'{type(evento).__name__}Dominio', evento=evento)


            consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()
