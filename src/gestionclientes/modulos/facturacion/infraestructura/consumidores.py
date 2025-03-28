import logging
import time
import traceback
import uuid

import _pulsar
import pulsar
from pulsar.schema import *

from gestionclientes.modulos.facturacion.aplicacion.comandos.actualizar_facturacion import \
    ActualizarFacturacion
from gestionclientes.modulos.facturacion.aplicacion.comandos.crear_facturacion import \
    CrearFacturacion
from gestionclientes.modulos.facturacion.aplicacion.comandos.revertir_facturacion import \
    RevertirFacturacion
from gestionclientes.modulos.facturacion.infraestructura.schema.v1.comandos import (
    ComandoRealizarPago, ComandoRealizarPagoBFF, ComandoRevertir)
from gestionclientes.modulos.facturacion.infraestructura.schema.v1.eventos import \
    EventoPagoRealizado
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.infraestructura import utils


def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-pago', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='gestionclientes-sub-eventos', schema=AvroSchema(EventoPagoRealizado))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento emitido desde integración de pagos hacia facturacion: {mensaje.value().data}')

            data = mensaje.value().data
            comando = ActualizarFacturacion(
                id_cliente=data.id_cliente,
                estadoReportado=data.estado,
                id_correlacion=data.id_correlacion
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
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-pago', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='gestionclientes-sub-comandos', schema=AvroSchema(ComandoRealizarPago))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido desde facturación: {mensaje.value().data}')

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_bff():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-pago-bff', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='gestionclientes-sub-comandos-bff', schema=AvroSchema(ComandoRealizarPagoBFF))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido desde facturación: {mensaje.value().data}')

            data = mensaje.value().data
            comando = CrearFacturacion(
                id=data.idCliente,
                medio_pago=data.medioPago,
                id_cliente=data.idCliente,
                monto=data.monto,
                id_correlacion=str(uuid.uuid4())
            )
            ejecutar_commando(comando)

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos_saga():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-compensacion-saga', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='gestionclientes-sub-comandos-saga', schema=AvroSchema(ComandoRevertir))

        while True:
            mensaje = consumidor.receive()

            data = mensaje.value().data
            command_type = mensaje.value().command_type
            if command_type == "revertir_facturacion":
                print(f'Comando recibido desde saga: {mensaje.value().data}')
                comando = RevertirFacturacion(
                    id_correlacion=data.id_correlacion,
                    id_cliente=data.id_cliente,
                    estadoReportado="CANCELADO"
                )
                ejecutar_commando(comando)

            consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()