""" Módulo de notificaciones """
import json
from flask import (Response,
                   jsonify,
                   request)
import notificaciones.seedwork.presentacion.api as api
from notificaciones.modulos.notificaciones.aplicacion.comandos.crear_notificacion import \
    CrearNotificacion
from notificaciones.modulos.notificaciones.aplicacion.mapeadores import \
    MapeadorNotificacionDTOJson
from notificaciones.modulos.notificaciones.aplicacion.queries.obtener_notificacion import \
    ObtenerNotificacion
from notificaciones.modulos.notificaciones.aplicacion.servicios import \
    ServicioNotificacion
from notificaciones.seedwork.aplicacion.comandos import ejecutar_commando
from notificaciones.seedwork.aplicacion.queries import ejecutar_query
from notificaciones.seedwork.dominio.excepciones import ExcepcionDominio

bp = api.crear_blueprint('notificaciones', '/notificaciones')

@bp.route('/notificacion', methods=('POST',))
def notificar_informacion():
    """ Crea una notificación de información """
    try:
        notificacion_dict = request.json
        print(f'API -Notificacion recibida: {notificacion_dict}')
        map_notificacion = MapeadorNotificacionDTOJson()
        print(f'API -Mapeador: {map_notificacion}')
        notificacion_dto = map_notificacion.externo_a_dto(notificacion_dict)
        print(f'API -Notificacion DTO: {notificacion_dto}')

        print(notificacion_dto)
        sr = ServicioNotificacion()
        print(f'API - Servicio: {sr}')
        dto_final = sr.crear_notificacion(notificacion_dto)
        print(f'API - DTO final: {dto_final}')

        return jsonify(map_notificacion.dto_a_externo(dto_final))
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))),
                        status=400,
                        mimetype='application/json')
    except Exception as e:
        print(str(e))
        return Response(json.dumps(dict(error=str(e))),
                        status=500,
                        mimetype='application/json')


@bp.route('/notificacion-comando', methods=('POST',))
def notificar_informacion_asincrono():
    """ Crea una notificación de información """
    try:
        notificacion_dict = request.json
        map_notificacion = MapeadorNotificacionDTOJson()
        notificacion_dto = map_notificacion.externo_a_dto(notificacion_dict)

        comando = CrearNotificacion(
            notificacion_dto.fecha_creacion,
            notificacion_dto.fecha_actualizacion,
            notificacion_dto.id,
            notificacion_dto.tipo,
            notificacion_dto.medio,
            notificacion_dto.valor,
        )
        ejecutar_commando(comando)

        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))),
                        status=400,
                        mimetype='application/json')
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))),
                        status=500,
                        mimetype='application/json')


@bp.route('/notificacion', methods=('GET',))
@bp.route('/notificacion/<id>', methods=('GET',))
def dar_notificacion(id=None):
    """ Obtiene una notificación de información """
    if id:
        sr = ServicioNotificacion()
        map_notificacion = MapeadorNotificacionDTOJson()

        return map_notificacion.dto_a_externo(sr.obtener_notificacion_por_id(id))
    else:
        return [{'message': 'GET!'}]


@bp.route('/notificacion-query', methods=('GET',))
@bp.route('/notificacion-query/<id>', methods=('GET',))
def dar_notificacion_query(id=None):
    """ Obtiene una notificación de información """
    if id:
        query_resultado = ejecutar_query(ObtenerNotificacion(id))
        map_notificacion = MapeadorNotificacionDTOJson()

        return map_notificacion.dto_a_externo(query_resultado.resultado)
    else:
        sr = ServicioNotificacion()
        map_notificacion = MapeadorNotificacionDTOJson()

        return map_notificacion.dto_a_externo(sr.obtener_todos_las_notificaciones())
