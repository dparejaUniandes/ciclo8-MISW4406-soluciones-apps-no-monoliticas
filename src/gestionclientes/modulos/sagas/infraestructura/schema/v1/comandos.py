from dataclasses import dataclass, field

from pulsar.schema import *

from gestionclientes.seedwork.infraestructura.schema.v1.comandos import \
    ComandoIntegracion


class ComandoRevertirPayload(ComandoIntegracion):
    id_correlacion = String()
    id_cliente = String()

class ComandoRevertir(ComandoIntegracion):
    data = ComandoRevertirPayload()
    command_type = String()
