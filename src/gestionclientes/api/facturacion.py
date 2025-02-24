import json

from flask import (Flask, Response, jsonify, redirect, render_template,
                   request, session, url_for)

import gestionclientes.seedwork.presentacion.api as api
from gestionclientes.modulos.facturacion.aplicacion.comandos.crear_facturacion import \
    CrearFacturacion
from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacionDTOJson
from gestionclientes.modulos.facturacion.aplicacion.queries.obtener_facturacion import \
    ObtenerFacturacion
from gestionclientes.modulos.facturacion.aplicacion.servicios import \
    ServicioFacturacion
from gestionclientes.seedwork.aplicacion.comandos import ejecutar_commando
from gestionclientes.seedwork.aplicacion.queries import ejecutar_query
from gestionclientes.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('facturacion', '/facturacion')

@bp.route('/realizar-pago', methods=('POST',))
def realizar_pago():
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

@bp.route('/realizar-pago-comando', methods=('POST',))
def realizar_pago_asincrono():
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
