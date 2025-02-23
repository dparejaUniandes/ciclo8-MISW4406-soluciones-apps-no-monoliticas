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

    def dto_a_externo(self, dto: ClienteDTO) -> any:
        if type(dto) is ClienteDTO:
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
        return dto

class MapeadorCliente(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Cliente.__class__


    def entidad_a_dto(self, entidad: Cliente) -> any:
        if type(entidad) is Cliente:
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
                entidad.estadoPlan,
                entidad.idDesdeBD
            )
        
        clientesDTO = []
        for cliente in entidad:
            fecha_creacion = cliente.fecha_creacion.strftime(self._FORMATO_FECHA)
            fecha_actualizacion = cliente.fecha_actualizacion.strftime(self._FORMATO_FECHA)
            _id = str(cliente.id)
            clientesDTO.append(ClienteDTO(
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

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        nombre = NombreCliente(dto.nombre, dto.apellidos)
        cliente = Cliente(
            nombre = nombre,
            correo = CorreoCliente(dto.correo),
            contrasena = dto.contrasena,
            estadoPlan = dto.estadoPlan
        )
        
        return cliente
