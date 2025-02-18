from dataclasses import dataclass, field

from gestionclientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class ClienteDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)