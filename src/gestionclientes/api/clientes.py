import json
import logging
import traceback

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, session, url_for)

import gestionclientes.seedwork.presentacion.api as api
from gestionclientes.modulos.clientes.aplicacion.mapeadores import \
    MapeadorClienteDTOJson
from gestionclientes.modulos.clientes.aplicacion.servicios import \
    ServicioCliente
from gestionclientes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/cliente', methods=('POST',))
def crear_cliente():
    try:
        cliente_dict = request.json
        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)
        sr = ServicioCliente()
        dto_final = sr.crear_cliente(cliente_dto)
        return jsonify(map_cliente.dto_a_externo(dto_final))
    except ExcepcionDominio as e:
        print("*** Error")
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    except Exception as e:
        print("***Some Error ", e)
        return Response(json.dumps(dict(error=str(e))), status=500, mimetype='application/json')

@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id>', methods=('GET',))
def dar_cliente(id=None):
    if id:
        sr = ServicioCliente()
        
        return sr.obtener_cliente_por_id(id)
    else:
        return [{'message': 'GET!'}]