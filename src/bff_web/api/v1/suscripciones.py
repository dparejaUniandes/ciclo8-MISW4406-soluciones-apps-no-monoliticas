import asyncio
import strawberry

from .esquemas import *

@strawberry.type
class Suscripcion:
    @strawberry.subscription
    async def eventos_clientes(self, info: strawberry.Info, id_correlacion: str,) -> Cliente:
        # TODO Oye los eventos de reserva
        connection_params: dict = info.context.get("connection_params")
        token: str = connection_params.get(
            "authToken"
        )
        if not token == "Bearer I_AM_A_VALID_AUTH_TOKEN":
            raise Exception("Forbidden!")
        