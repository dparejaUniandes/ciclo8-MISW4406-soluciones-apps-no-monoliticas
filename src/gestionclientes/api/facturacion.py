import json

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, session, url_for)

import gestionclientes.seedwork.presentacion.api as api
from gestionclientes.modulos.facturacion.aplicacion.comandos.crear_cliente import \
    CrearFacturacion
from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacionDTOJson
from gestionclientes.modulos.facturacion.aplicacion.queries.obtener_cliente import \
    ObtenerFacturacion
from gestionclientes.modulos.facturacion.aplicacion.servicios import \
    ServicioFacturacion
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.aplicacion.queries import ejecutar_query
from gestionclientes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('facturaciones', '/facturaciones')

@bp.route('/facturacion', methods=('POST',))
def crear_facturacion():
    try:
        facturacion_dict = request.json
        map_facturacion = MapeadorFacturacionDTOJson()
        facturacion_dto = map_facturacion.externo_a_dto(facturacion_dict)

        sr = ServicioFacturacion()
        dto_final = sr.crear_facturacion(facturacion_dto)

        return jsonify(map_facturacion.dto_a_externo(dto_final))
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=500, mimetype='application/json')

@bp.route('/facturacion-comando', methods=('POST',))
def crear_cliente_asincrono():
    try:
        facturacion_dict = request.json
        map_facturacion = MapeadorFacturacionDTOJson()
        facturacion_dto = map_facturacion.externo_a_dto(facturacion_dict)

        comando = CrearFacturacion(
            facturacion_dto.id, 
            facturacion_dto.medioPago,
            facturacion_dto.idCliente,
            facturacion_dto.monto
        )
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=500, mimetype='application/json')

@bp.route('/facturacion', methods=('GET',))
@bp.route('/facturacion/<id>', methods=('GET',))
def dar_cliente(id=None):
    if id:
        sr = ServicioFacturacion()
        map_facturacion = MapeadorFacturacionDTOJson()
        
        return map_facturacion.dto_a_externo(sr.obtener_cliente_por_id(id))
    else:
        return [{'message': 'GET!'}]
    
@bp.route('/facturacion-query', methods=('GET',))
@bp.route('/facturacion-query/<id>', methods=('GET',))
def dar_cliente_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerFacturacion(id))
        map_facturacion = MapeadorFacturacionDTOJson()
        
        return map_facturacion.dto_a_externo(query_resultado.resultado)
    else:
        sr = ServicioFacturacion()
        map_facturacion = MapeadorFacturacionDTOJson()
        
        return map_facturacion.dto_a_externo(sr.obtener_todos_los_clientes())