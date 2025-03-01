""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.objetos_valor import (
    CorreoCliente, NombreCliente)
from gestionclientes.seedwork.dominio.repositorios import Mapeador

from .dto import Cliente as ClienteDTO


class MapeadorCliente(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Cliente.__class__

    def entidad_a_dto(self, entidad: Cliente) -> ClienteDTO:
        
        cliente_dto = ClienteDTO()
        cliente_dto.fecha_creacion = entidad.fecha_creacion
        cliente_dto.fecha_actualizacion = entidad.fecha_actualizacion
        cliente_dto.id = str(entidad.id)
        cliente_dto.nombre = entidad.nombre.nombre
        cliente_dto.apellidos = entidad.nombre.apellidos
        cliente_dto.correo = entidad.correo.correo
        cliente_dto.contrasena = entidad.contrasena
        cliente_dto.estado_plan = entidad.estadoPlan

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> any:
        if type(dto) is ClienteDTO:
            nombre = NombreCliente(
                nombre = dto.nombre,
                apellidos = dto.apellidos
            )
            correo = CorreoCliente(
                correo = dto.correo
            )
            cliente = Cliente(
                dto.id, 
                dto.fecha_creacion, 
                dto.fecha_actualizacion, 
                nombre=nombre,
                correo=correo,
                contrasena=dto.contrasena,
                estadoPlan=dto.estado_plan.value,
                idDesdeBD=dto.id, 
            )
            return cliente
        clientes = []
        for clienteDTO in dto:
            nombre = NombreCliente(
                nombre = clienteDTO.nombre,
                apellidos = clienteDTO.apellidos
            )
            correo = CorreoCliente(
                correo = clienteDTO.correo
            )
            clientes.append(Cliente(
                clienteDTO.id, 
                clienteDTO.fecha_creacion, 
                clienteDTO.fecha_actualizacion, 
                nombre=nombre,
                correo=correo,
                contrasena=clienteDTO.contrasena,
                estadoPlan=clienteDTO.estado_plan.value,
                idDesdeBD=clienteDTO.id
            ))
        return clientes
