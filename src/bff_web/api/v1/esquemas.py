import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


SALUDTECH_HOST = os.getenv("SALUDTECH_ADDRESS", default="localhost")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_clientes(root) -> typing.List["Cliente"]:
    clientes_json = requests.get(f'http://{SALUDTECH_HOST}:5000/clientes').json()
    clientes = []

    for cliente in clientes_json:
        clientes.append(
            Cliente(
                fecha_creacion=datetime.strptime(cliente.get('fecha_creacion'), FORMATO_FECHA), 
                fecha_actualizacion=datetime.strptime(cliente.get('fecha_actualizacion'), FORMATO_FECHA), 
                id=cliente.get('id'), 
            )
        )

    return clientes

@strawberry.type
class Cliente:
    id: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    nombre: str
    correo: str
    contrasena: str
    estadoPlan: str
    idDesdeBD: str


@strawberry.type
class ClienteRespuesta:
    mensaje: str
    codigo: int



