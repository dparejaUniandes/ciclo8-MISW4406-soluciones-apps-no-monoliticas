import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def crear_cliente(self, id_cliente: str, cliente: Cliente, 
                            id_correlacion: str, info: Info) -> ClienteRespuesta:
        print(f"ID Cliente: {id_cliente}, ID Correlación: {id_correlacion}")
        payload = dict(
            cliente = cliente,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "SaludTech BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-cliente", "public/default/comando-crear-cliente")
        
        return ClienteRespuesta(mensaje="Procesando Mensaje", codigo=203)
    
    @strawberry.mutation
    async def realizar_pago(self, id_cliente: str, id_correlacion: str, info: Info,
                            medio_pago: str, monto: str) -> ClienteRespuesta:
        print(f"ID Cliente: {id_cliente}, ID Correlación: {id_correlacion}")
        payload = dict(
            id_cliente = id_cliente,
            medio_pago = medio_pago,
            monto = monto,
            id_correlacion = id_correlacion,
            fecha_creacion = utils.time_millis()
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "SaludTech BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "comando-crear-cliente", "public/default/comando-crear-cliente")
        
        return ClienteRespuesta(mensaje="Procesando Mensaje", codigo=203)