from pulsar.schema import *

import integracionpagos.seedwork.presentacion.api as api
from integracionpagos.modulos.pagos.infraestructura.despachadores import \
    Despachador
from integracionpagos.modulos.pagos.infraestructura.schema.v1.eventos import (
    EventoPagoRealizado, PagoRealizadoPayload)

bp = api.crear_blueprint('pagos', '/pagos')

@bp.route('/simular-evento-de-compensacion', methods=('POST',))
def crear_cliente():
    despachador = Despachador()
    payload = PagoRealizadoPayload(
        id_cliente="abcd-1234", 
        estado="CANCELADO"
    )
    evento_integracion = EventoPagoRealizado(data=payload, event_type="pago_realizado_revertido")
    despachador._publicar_mensaje(evento_integracion, 'eventos-pago', AvroSchema(EventoPagoRealizado))
    return {"mensaje": "Evento de compensación emitido"}