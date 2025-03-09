"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from gestionclientes.seedwork.dominio.entidades import AgregacionRaizCliente


@dataclass
class Saga(AgregacionRaizCliente):
    id_correlacion: str = field(default_factory=str)
    id_cliente: str = field(default_factory=str)
    nombre_paso: str = field(default_factory=str)
    estado: str = field(default_factory=str)
    index: int = field(default_factory=int)
    fecha_creacion_saga: datetime =  field(default=datetime.now())