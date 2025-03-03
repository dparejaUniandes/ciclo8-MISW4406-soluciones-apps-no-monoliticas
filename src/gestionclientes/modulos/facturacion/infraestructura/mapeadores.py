""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.objetos_valor import (
    IdCliente, MedioPago)
from gestionclientes.seedwork.dominio.repositorios import Mapeador

from .dto import Facturacion as FacturacionDTO


class MapeadorFacturacion(Mapeador):

    def obtener_tipo(self) -> type:
        return Facturacion.__class__

    def entidad_a_dto(self, entidad: Facturacion) -> FacturacionDTO:
        
        facturacion_dto = FacturacionDTO()
        facturacion_dto.id = str(entidad.id)
        facturacion_dto.medio_pago = entidad.medioPago
        facturacion_dto.id_cliente = entidad.idCliente
        facturacion_dto.monto = entidad.monto
        facturacion_dto.estado_reportado = "PAGO_ENVIADO"

        return facturacion_dto

    def dto_a_entidad(self, dto: FacturacionDTO) -> any:
        if type(dto) is FacturacionDTO:
            print("infra only dto")
            facturacion = Facturacion(
                dto.id, 
                medioPago=dto.medio_pago,
                idCliente=dto.id_cliente,
                monto=dto.monto,
                estado_reportado=dto.estadoReportado
            )
            return facturacion
        print("infra all dto", dto)
        facturacion = []
        for facturacionDTO in dto:
            facturacion.append(Facturacion(
                medioPago=facturacionDTO.medio_pago,
                idCliente=facturacionDTO.id_cliente,
                monto=facturacionDTO.monto
            ))
        print("infra all dto Fin")
        return facturacion
