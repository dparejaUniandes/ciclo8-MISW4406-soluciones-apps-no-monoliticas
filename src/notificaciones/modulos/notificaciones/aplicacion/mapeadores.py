from gestionclientes.modulos.clientes.dominio.entidades import Notificacion
from gestionclientes.modulos.clientes.dominio.objetos_valor import (
    CorreoNotificacion, EstadoPlan, NombreNotificacion)
from gestionclientes.seedwork.aplicacion.dto import Mapeador as AppMap
from gestionclientes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import NotificacionDTO


class MapeadorNotificacionnDTOJson(AppMap):
    """ Mapeador de notificaciones a DTOs """

    def externo_a_dto(self, externo: dict) -> NotificacionDTO:
        cliente_dto = NotificacionDTO(
            tipo=externo.get('tipo', ""),
            medio=externo.get('medio', ""),
            valor=externo.get('valor', ""),
        )

        return cliente_dto

    def dto_a_externo(self, dto: NotificacionDTO) -> any:
        if type(dto) is NotificacionDTO:
            clienteExterno = {
                "fecha_actualizacion": dto.fecha_actualizacion,
                "fecha_creacion": dto.fecha_creacion,
                "id": dto.idDesdeBD,
                "nombre": dto.nombre,
                "apellidos": dto.apellidos,
                "correo": dto.correo,
                "contrasena": dto.contrasena,
                "estadoPlan": dto.estadoPlan
            }
            return clienteExterno

        clientesExterno = []
        for cliente in dto:
            clientesExterno.append({
                "fecha_actualizacion": cliente.fecha_actualizacion,
                "fecha_creacion": cliente.fecha_creacion,
                "id": cliente.idDesdeBD,
                "nombre": cliente.nombre,
                "apellidos": cliente.apellidos,
                "correo": cliente.correo,
                "contrasena": cliente.contrasena,
                "estadoPlan": cliente.estadoPlan
            })
        return clientesExterno


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
                entidad.nombre.tipo,
                entidad.nombre.medio,
                entidad.correo.valor,

            )

        clientesDTO = []
        for cliente in entidad:
            fecha_creacion = cliente.fecha_creacion.strftime(
                self._FORMATO_FECHA)
            fecha_actualizacion = cliente.fecha_actualizacion.strftime(
                self._FORMATO_FECHA)
            _id = str(cliente.id)
            clientesDTO.append(NotificacionDTO(
                fecha_creacion,
                fecha_actualizacion,
                _id,
                cliente.nombre.nombre,
                cliente.nombre.apellidos,
                cliente.correo.correo,
                cliente.contrasena,
                cliente.estadoPlan,
                cliente.idDesdeBD
            ))
        return clientesDTO

    def dto_a_entidad(self, dto: NotificacionDTO) -> Notificacion:
        nombre = NombreNotificacion(dto.nombre, dto.apellidos)
        cliente = Notificacion(
            nombre=nombre,
            correo=CorreoNotificacion(dto.correo),
            contrasena=dto.contrasena,
            estadoPlan=dto.estadoPlan,
            idDesdeBD=dto.idDesdeBD
        )

        return cliente
