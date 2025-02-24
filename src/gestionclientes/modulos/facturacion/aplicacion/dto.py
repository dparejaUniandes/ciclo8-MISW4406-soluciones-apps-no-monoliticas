from dataclasses import dataclass, field

from gestionclientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class FacturacionDTO(DTO):
    id: str = field(default_factory=str)
    medioPago: str = field(default_factory=str)
    idCliente: str = field(default_factory=str)
    monto: str = field(default_factory=int)