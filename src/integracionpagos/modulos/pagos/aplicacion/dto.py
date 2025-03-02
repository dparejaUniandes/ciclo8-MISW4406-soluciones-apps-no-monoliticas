from dataclasses import dataclass, field

from integracionpagos.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class PagoDTO(DTO):
    id_cliente: str = field(default_factory=str)
    monto: float = field(default_factory=float)
    estado_pago: str = field(default_factory=str)
    pasarela_pago: str = field(default_factory=str)