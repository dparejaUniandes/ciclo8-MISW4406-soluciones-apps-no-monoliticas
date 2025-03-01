""" DTO de notificaciones """
from dataclasses import dataclass, field

from gestionclientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NotificacionDTO(DTO):
    """ DTO de notificaciones """
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    medio: str = field(default_factory=str)
    valor: str = field(default_factory=str)
