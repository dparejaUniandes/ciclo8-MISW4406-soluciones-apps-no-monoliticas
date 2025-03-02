from integracionpagos.modulos.pagos.dominio.entidades import Pago
from integracionpagos.seedwork.dominio.repositorios import Mapeador as RepMap

from .dto import PagoDTO


class MapeadorPago(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Pago.__class__


    def entidad_a_dto(self, entidad: Pago) -> PagoDTO:
        return PagoDTO(
            entidad.id_cliente,
            entidad.monto,
            entidad.estado_pago,
            entidad.pasarela_pago
        )

    def dto_a_entidad(self, dto: PagoDTO) -> Pago:
        pago = Pago(
            id_cliente = dto.id_cliente,
            monto = dto.monto,
            estado_pago = "CONFIRMADO",
            pasarela_pago = "STRIPE"
        )
        
        return pago
