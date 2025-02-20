"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field

import gestionclientes.modulos.clientes.dominio.objetos_valor as ov
from gestionclientes.seedwork.dominio.entidades import AgregacionRaizCliente


@dataclass
class Cliente(AgregacionRaizCliente):
    nombre: ov.NombreCliente = field(default_factory=ov.NombreCliente)