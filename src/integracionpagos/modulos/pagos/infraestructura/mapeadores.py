""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.seedwork.dominio.repositorios import Mapeador

from .dto import Pago as PagoDTO


class MapeadorPago(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pago.__class__

    def entidad_a_dto(self, entidad: Pago) -> PagoDTO:
        
        pago_dto = PagoDTO()
        pago_dto.fecha_creacion = entidad.fecha_creacion
        pago_dto.fecha_actualizacion = entidad.fecha_actualizacion
        pago_dto.id = str(entidad.id)
        pago_dto.id_cliente = entidad.id_cliente
        pago_dto.monto = entidad.monto
        pago_dto.estado_pago = entidad.estado_pago
        pago_dto.pasarela_pago = entidad.pasarela_pago

        return pago_dto

    def dto_a_entidad(self, dto: PagoDTO) -> Pago:
        pass