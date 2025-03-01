"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from gestionclientes.seedwork.dominio.objetos_valor import ObjetoValor


@dataclass(frozen=True)
class NombreCliente(ObjetoValor):
    nombre: str
    apellidos: str

@dataclass(frozen=True)
class CorreoCliente(ObjetoValor):
    correo: str

class EstadoPlan(Enum):
    PAGADO = "PAGADO"
    ATRASADO = "ATRASADO"
    PENDIENTE = "PENDIENTE"