"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from gestionclientes.seedwork.dominio.objetos_valor import ObjetoValor


@dataclass(frozen=True)
class MedioPago(ObjetoValor):
    medioPago: str

@dataclass(frozen=True)
class IdCliente(ObjetoValor):
    idCliente: str
