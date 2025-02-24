import json

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, session, url_for)

import gestionclientes.seedwork.presentacion.api as api
from gestionclientes.modulos.clientes.aplicacion.comandos.crear_cliente import \
    CrearCliente
from gestionclientes.modulos.clientes.aplicacion.mapeadores import \
    MapeadorClienteDTOJson
from gestionclientes.modulos.clientes.aplicacion.queries.obtener_cliente import \
    ObtenerCliente
from gestionclientes.modulos.clientes.aplicacion.servicios import \
    ServicioFacturacion
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.aplicacion.queries import ejecutar_query
from gestionclientes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('clientes', '/clientes')

@bp.route('/cliente', methods=('POST',))
def crear_cliente():
    try:
        cliente_dict = request.json
        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        sr = ServicioFacturacion()
        dto_final = sr.crear_cliente(cliente_dto)

        return jsonify(map_cliente.dto_a_externo(dto_final))
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=500, mimetype='application/json')

@bp.route('/cliente-comando', methods=('POST',))
def crear_cliente_asincrono():
    try:
        cliente_dict = request.json
        map_cliente = MapeadorClienteDTOJson()
        cliente_dto = map_cliente.externo_a_dto(cliente_dict)

        comando = CrearCliente(
            cliente_dto.fecha_creacion, 
            cliente_dto.fecha_actualizacion, 
            cliente_dto.id, 
            cliente_dto.nombre,
            cliente_dto.apellidos,
            cliente_dto.correo,
            cliente_dto.contrasena,
            cliente_dto.estadoPlan
        )
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=500, mimetype='application/json')

@bp.route('/cliente', methods=('GET',))
@bp.route('/cliente/<id>', methods=('GET',))
def dar_cliente(id=None):
    if id:
        sr = ServicioFacturacion()
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(sr.obtener_cliente_por_id(id))
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/cliente-query', methods=('GET',))
@bp.route('/cliente-query/<id>', methods=('GET',))
def dar_cliente_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerCliente(id))
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(query_resultado.resultado)
    else:
        sr = ServicioFacturacion()
        map_cliente = MapeadorClienteDTOJson()
        
        return map_cliente.dto_a_externo(sr.obtener_todos_los_clientes())