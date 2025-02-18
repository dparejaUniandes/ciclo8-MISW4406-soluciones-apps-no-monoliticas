import json

from flask import (Response, redirect, render_template, request, session,
                   url_for)

import aeroalpes.seedwork.presentacion.api as api
from aeroalpes.modulos.vuelos.aplicacion.mapeadores import \
    MapeadorClienteDTOJson
from aeroalpes.modulos.vuelos.aplicacion.servicios import ServicioCliente
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/cliente', methods=('POST',))
def reservar():
    try:
        cliente_dict = request.json

        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        sr = ServicioCliente()
        dto_final = sr.crear_cliente(cliente_dto)

        return map_cliente.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioCliente()
        
        return sr.obtener_cliente_por_id(id)
    else:
        return [{'message': 'GET!'}]