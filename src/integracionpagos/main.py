import os
import time
import uuid

import _pulsar
import pulsar
from pulsar.schema import *


def time_millis():
    return int(time.time() * 1000)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class PagoRealizadoPayload(Record):
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoPagoRealizado(EventoIntegracion):
    data = PagoRealizadoPayload()

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('comandos-pago', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-comandos-pago', schema=AvroSchema(EventoPagoRealizado))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Comunicación con pasarela de pagos ====')

    consumer.acknowledge(msg)

client.close()