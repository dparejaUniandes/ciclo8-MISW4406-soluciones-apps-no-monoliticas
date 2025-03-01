"""Entidades del dominio de notificaciones

En este archivo usted encontrará las entidades del dominio de notificaciones

"""

from __future__ import annotations
from dataclasses import dataclass, field

import notificaciones.modulos.clientes.dominio.objetos_valor as ov
from notificaciones.seedwork.dominio.entidades import AgregacionRaizNotificacion


@dataclass
class Notificacion(AgregacionRaizNotificacion):
    """ Entidad de notificaciones """
    tipo: ov.NombreCliente = field(default_factory=ov.NombreCliente)
    valor: ov.CorreoCliente = field(default_factory=ov.CorreoCliente)
    medio: ov.TipoMedio = field(default_factory=ov.TipoMedio)


    def crear_notificacion(self, notificacion: Notificacion):
        """ Crea una notificacion """
        self.tipo = notificacion.tipo
        self.valor = notificacion.valor
        self.medio = notificacion.medio
