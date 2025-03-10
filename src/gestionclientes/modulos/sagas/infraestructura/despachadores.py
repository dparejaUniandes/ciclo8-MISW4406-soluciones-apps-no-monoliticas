import datetime

import pulsar
from pulsar.schema import *

from gestionclientes.modulos.sagas.infraestructura.schema.v1.comandos import (
    ComandoRevertir, ComandoRevertirPayload)
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

    def publicar_comando(self, comando, topico):
        payload = ComandoRevertirPayload(
            id_correlacion=str(comando.id_correlacion),
            id_cliente=str(comando.id_cliente)
        )
        print("Comando ", comando.command_type, " publicado desde saga")
        comando_integracion = ComandoRevertir(data=payload, command_type=comando.command_type)
        self._publicar_mensaje(comando_integracion, topico, AvroSchema(ComandoRevertir))
