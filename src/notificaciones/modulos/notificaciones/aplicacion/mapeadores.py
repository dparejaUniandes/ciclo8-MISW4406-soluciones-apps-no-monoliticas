from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.dominio.objetos_valor import (
    TipoNotificacion, MedioNotificacion, TipoMedio)
from notificaciones.seedwork.aplicacion.dto import Mapeador as AppMap
from notificaciones.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import NotificacionDTO


class MapeadorNotificacionDTOJson(AppMap):
    """ Mapeador de notificaciones a DTOs """

    def externo_a_dto(self, externo: dict) -> NotificacionDTO:
        notificacion_dto = NotificacionDTO(
            tipo=externo.get('tipo', ""),
            medio=externo.get('medio', ""),
            valor=externo.get('valor', ""),
        )

        return notificacion_dto

    def dto_a_externo(self, dto: NotificacionDTO) -> any:
        if type(dto) is NotificacionDTO:
            notificacionExterno = {
                "fecha_actualizacion": dto.fecha_actualizacion,
                "fecha_creacion": dto.fecha_creacion,
                "id": dto.idDesdeBD,
                "tipo": dto.tipo,
                "medio": dto.medio,
                "valor": dto.valor

            }
            return notificacionExterno

        notificacionesExterno = []
        for notificacion in dto:
            notificacionesExterno.append({
                "fecha_actualizacion": notificacion.fecha_actualizacion,
                "fecha_creacion": notificacion.fecha_creacion,
                "id": notificacion.idDesdeBD,
                "tipo": notificacion.tipo,
                "medio": notificacion.medio,
                "valor": notificacion.valor
            })
        return notificacionesExterno


class MapeadorNotificacion(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Notificacion.__class__

    def entidad_a_dto(self, entidad: Notificacion) -> any:
        if type(entidad) is Notificacion:
            fecha_creacion = entidad.fecha_creacion.strftime(
                self._FORMATO_FECHA)
            fecha_actualizacion = entidad.fecha_actualizacion.strftime(
                self._FORMATO_FECHA)
            _id = str(entidad.id)
            return NotificacionDTO(
                fecha_creacion,
                fecha_actualizacion,
                _id,
                entidad.tipo,
                entidad.medio,
                entidad.valor,

            )

        notificacionesDTO = []
        for notificacion in entidad:
            fecha_creacion = notificacion.fecha_creacion.strftime(
                self._FORMATO_FECHA)
            fecha_actualizacion = notificacion.fecha_actualizacion.strftime(
                self._FORMATO_FECHA)
            _id = str(notificacion.id)
            notificacionesDTO.append(NotificacionDTO(
                fecha_creacion,
                fecha_actualizacion,
                _id,
                notificacion.nombre.tipo,
                notificacion.nombre.medio,
                notificacion.correo.valor,
            ))
        return notificacionesDTO

    def dto_a_entidad(self, dto: NotificacionDTO) -> Notificacion:
        notificacion = Notificacion(
            id=dto.id,
            fecha_creacion=dto.fecha_creacion,
            fecha_actualizacion=dto.fecha_actualizacion,
            tipo=dto.tipo,
            medio=TipoMedio(dto.medio),
            valor=dto.valor
        )

        return notificacion
