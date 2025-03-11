from dataclasses import dataclass, field

from gestionclientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class SagaLogDTO(DTO):
    id: str = field(default_factory=str)
    id_cliente: str = field(default_factory=str)
    id_correlacion: str = field(default_factory=str)
    nombre_paso: str = field(default_factory=int)
    estado: str = field(default_factory=str)
    index : int = field(default_factory=int)
    fecha_creacion : str = field(default_factory=str)