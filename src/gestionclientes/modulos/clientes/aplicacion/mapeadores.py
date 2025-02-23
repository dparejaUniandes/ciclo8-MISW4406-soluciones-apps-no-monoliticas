from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.objetos_valor import (
    CorreoCliente, EstadoPlan, NombreCliente)
from gestionclientes.seedwork.aplicacion.dto import Mapeador as AppMap
from gestionclientes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import ClienteDTO


class MapeadorClienteDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> ClienteDTO:
        cliente_dto = ClienteDTO(
            nombre = externo.get('nombre', ""),
            apellidos = externo.get('apellidos', ""),
            correo = externo.get('correo', ""),
            contrasena = externo.get('contrasena', ""),
            estadoPlan = EstadoPlan.PENDIENTE.value
        )

        return cliente_dto

    def dto_a_externo(self, dto: ClienteDTO) -> dict:
        clienteExterno = {
            "fecha_actualizacion": dto.fecha_actualizacion,
            "fecha_creacion": dto.fecha_creacion,
            "id": dto.id,
            "nombre": dto.nombre,
            "apellidos": dto.apellidos,
            "correo": dto.correo,
            "contrasena": dto.contrasena,
            "estadoPlan": dto.estadoPlan
        }
        return clienteExterno

class MapeadorCliente(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Cliente.__class__


    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        return ClienteDTO(
            fecha_creacion, 
            fecha_actualizacion, 
            _id, 
            entidad.nombre.nombre, 
            entidad.nombre.apellidos,
            entidad.correo.correo,
            entidad.contrasena,
            entidad.estadoPlan
        )

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        nombre = NombreCliente(dto.nombre, dto.apellidos)
        cliente = Cliente(
            nombre = nombre,
            correo = CorreoCliente(dto.correo),
            contrasena = dto.contrasena,
            estadoPlan = dto.estadoPlan
        )
        
        return cliente
