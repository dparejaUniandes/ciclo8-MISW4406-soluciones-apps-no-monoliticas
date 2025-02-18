"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field

import aeroalpes.modulos.vuelos.dominio.objetos_valor as ov
from aeroalpes.seedwork.dominio.entidades import AgregacionRaizCliente


@dataclass
class Cliente(AgregacionRaizCliente):
    nombre: ov.NombreCliente = field(default_factory=ov.NombreCliente)