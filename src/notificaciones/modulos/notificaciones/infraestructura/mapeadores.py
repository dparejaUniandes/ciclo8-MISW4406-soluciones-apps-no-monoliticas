""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.dominio.objetos_valor import (
    TipoNotificacion, TipoMedio, MedioNotificacion)
from notificaciones.seedwork.dominio.repositorios import Mapeador

from .dto import Notificacion as NotificacionDTO


class MapeadorNotificacion(Mapeador):
    """ Mapeador de notificaciones a DTOs """
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Notificacion.__class__

    def entidad_a_dto(self, entidad: Notificacion) -> NotificacionDTO:

        notificacion_dto = NotificacionDTO()
        notificacion_dto.fecha_creacion = entidad.fecha_creacion
        notificacion_dto.fecha_actualizacion = entidad.fecha_actualizacion
        notificacion_dto.id = str(entidad.id)
        notificacion_dto.tipo = entidad.tipo
        notificacion_dto.medio = entidad.medio
        notificacion_dto.valor = entidad.valor

        return notificacion_dto

    def dto_a_entidad(self, dto: NotificacionDTO) -> any:
        try:
            print(type(dto))
            print(NotificacionDTO)
            if type(dto) is Notificacion:
                tipo = TipoNotificacion(
                    tipo=dto.tipo,

                )

                # medio = MedioNotificacion(
                #     medio=dto.medio,
                #     valor=dto.valor
                # )
                print("Medio DTO n\"", dto.medio)

                notificacion = Notificacion(
                    dto.id,
                    dto.fecha_creacion,
                    dto.fecha_actualizacion,
                    tipo=tipo,
                    medio=dto.medio.value,
                    valor=dto.valor,

                )
                return notificacion

            notificaciones = []

            for notificacionDTO in dto:

                notificaciones.append(Notificacion(
                    notificacionDTO.id,
                    notificacionDTO.fecha_creacion,
                    notificacionDTO.fecha_actualizacion,
                    tipo=notificacionDTO.tipo,
                    medio=notificacionDTO.medio,
                    valor=notificacionDTO.valor,

                ))
            return notificaciones
        except Exception as e:
            print(f'Error en mapeador: {e}')
