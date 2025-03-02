
import strawberry
from .esquemas import *

@strawberry.type
class Query:
    clientes: typing.List[Cliente] = strawberry.field(resolver=obtener_clientes)