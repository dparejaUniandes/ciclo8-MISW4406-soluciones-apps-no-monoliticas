""" DTO de notificaciones """
from dataclasses import dataclass, field

from gestionclientes.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class NotificacionDTO(DTO):
    """ DTO de notificaciones """
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    nombre: str = field(default_factory=str)
    apellidos: str = field(default_factory=str)
    correo: str = field(default_factory=str)
    contrasena: str = field(default_factory=str)
    estadoPlan: str = field(default_factory=str)
    idDesdeBD: str = field(default_factory=str)
