""" DTO de notificaciones """
from dataclasses import dataclass, field
from datetime import datetime
from notificaciones.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NotificacionDTO(DTO):
    """ DTO de notificaciones """
    fecha_creacion: datetime =  field(default=datetime.now())
    fecha_actualizacion: datetime =  field(default=datetime.now())
    id: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
    medio: str = field(default_factory=str)
    valor: str = field(default_factory=str)
