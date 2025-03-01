"""Entidades del dominio de notificaciones

En este archivo usted encontrará las entidades del dominio de notificaciones

"""

from __future__ import annotations
from dataclasses import dataclass, field

import notificaciones.modulos.clientes.dominio.objetos_valor as ov
from notificaciones.seedwork.dominio.entidades import AgregacionRaizNotificacion


@dataclass
class Notificacion(AgregacionRaizNotificacion):
    nombre: ov.NombreCliente = field(default_factory=ov.NombreCliente)
    correo: ov.CorreoCliente = field(default_factory=ov.CorreoCliente)
    contrasena: str = field(default_factory=str)
    estadoPlan: ov.EstadoPlan = field(default_factory=ov.EstadoPlan)
    idDesdeBD: str = field(default_factory=str)

    def crear_notificacion(self, cliente: Notificacion):
        """ Crea una notificacion """
        self.nombre = cliente.nombre
        self.correo = cliente.correo
        self.contrasena = cliente.contrasena
        self.estadoPlan = cliente.estadoPlan
