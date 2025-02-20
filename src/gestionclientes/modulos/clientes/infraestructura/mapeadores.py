""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.objetos_valor import \
    NombreCliente
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
        cliente_dto.nombre = entidad.nombre

        return cliente_dto

    def dto_a_entidad(self, dto: ClienteDTO) -> Cliente:
        cliente = Cliente(dto.id, dto.fecha_creacion, dto.fecha_actualizacion, dto.nombre)
        cliente.nombre = dto.nombre
        return cliente