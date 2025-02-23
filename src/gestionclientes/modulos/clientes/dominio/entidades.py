"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de vuelos

"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field

import gestionclientes.modulos.clientes.dominio.objetos_valor as ov
from gestionclientes.seedwork.dominio.entidades import AgregacionRaizCliente


@dataclass
class Cliente(AgregacionRaizCliente):
    nombre: ov.NombreCliente = field(default_factory=ov.NombreCliente)
    correo: ov.CorreoCliente = field(default_factory=ov.CorreoCliente)
    contrasena: str = field(default_factory=str)
    estadoPlan: ov.EstadoPlan = field(default_factory=ov.EstadoPlan)

    def crear_cliente(self, cliente: Cliente):
        self.nombre = cliente.nombre
        self.correo = cliente.correo
        self.contrasena = cliente.contrasena
        self.estadoPlan = cliente.estadoPlan