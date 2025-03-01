"""Entidades del dominio de notificaciones

En este archivo usted encontrará las entidades del dominio de notificaciones

"""

from __future__ import annotations
from dataclasses import dataclass, field

import notificaciones.modulos.notificaciones.dominio.objetos_valor as ov
from notificaciones.seedwork.dominio.entidades import AgregacionRaizNotificacion


@dataclass
class Notificacion(AgregacionRaizNotificacion):
    """ Entidad de notificaciones """
    tipo: ov.TipoNotificacion = field(default_factory=ov.TipoNotificacion)
    valor: ov.MedioNotificacion = field(default_factory=ov.MedioNotificacion)
    medio: ov.MedioNotificacion = field(default_factory=ov.MedioNotificacion)


    def crear_notificacion(self, notificacion: Notificacion):
        """ Crea una notificacion """
        self.tipo = notificacion.tipo
        self.valor = notificacion.valor
        self.medio = notificacion.medio
