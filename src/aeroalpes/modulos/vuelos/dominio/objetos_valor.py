"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NombreCliente():
    nombre: str
