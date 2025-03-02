from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.objetos_valor import (
    IdCliente, MedioPago)
from gestionclientes.seedwork.aplicacion.dto import Mapeador as AppMap
from gestionclientes.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import FacturacionDTO


class MapeadorFacturacionDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> FacturacionDTO:
        facturacion_dto = FacturacionDTO(
            medioPago = externo.get('medioPago', ""),
            idCliente = externo.get('idCliente', ""),
            monto = externo.get('monto', 0)
        )

        return facturacion_dto

    def dto_a_externo(self, dto: FacturacionDTO) -> any:
        if type(dto) is FacturacionDTO:
            facturacionExterno = {
                "id": dto.id,
                "medioPago": dto.medioPago,
                "idCliente": dto.idCliente,
                "monto": dto.monto
            }
            return facturacionExterno
        return dto

class MapeadorFacturacion(RepMap):
    def obtener_tipo(self) -> type:
        return Facturacion.__class__


    def entidad_a_dto(self, entidad: Facturacion) -> any:
        if type(entidad) is Facturacion:
            _id = str(entidad.id)
            return FacturacionDTO(
                _id, 
                entidad.medioPago, 
                entidad.idCliente,
                entidad.monto
            )
        
        facturacionDTO = []
        for facturacion in entidad:
            _id = str(facturacion.id)
            facturacionDTO.append(FacturacionDTO(
                _id, 
                facturacion.medioPago, 
                facturacion.idCliente,
                facturacion.monto
            ))
        return facturacionDTO

    def dto_a_entidad(self, dto: FacturacionDTO) -> Facturacion:
        facturacion = Facturacion(
            medioPago = dto.medioPago,
            idCliente = dto.idCliente,
            monto = dto.monto,
            estado_reportado=dto.estadoReportado
        )
        
        return facturacion
