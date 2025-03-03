"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re

from notificaciones.seedwork.dominio.objetos_valor import ObjetoValor


class TipoMedio(Enum):
    """ Posibles medios de notificación """
    CORREO = "correo"
    SMS = "sms"
    PUSH = "push"

@dataclass(frozen=True)
class TipoNotificacion(ObjetoValor):
    """ Tipo de notificación (ej. Alerta, Recordatorio) """
    tipo: str

@dataclass(frozen=True)
class MedioNotificacion(ObjetoValor):
    """ Medio de notificación con validación """
    medio: TipoMedio
    valor: str

    def __post_init__(self):
        if self.medio == TipoMedio.CORREO:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.valor):
                raise ValueError(f"Correo inválido: {self.valor}")
