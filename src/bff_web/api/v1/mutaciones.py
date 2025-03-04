import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:   
    @strawberry.mutation
    async def realizar_pago(self, info: Info, pago: RealizarPagoInput) -> ClienteRespuesta:
        payload = dict(
            idCliente = pago.idCliente,
            monto = pago.monto,
            medioPago = pago.medioPago
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "record",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "SaludTech BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comandos-pago-bff", "public/default/comandos-pago-bff")
        
        return ClienteRespuesta(mensaje="Procesando Mensaje", codigo=203)