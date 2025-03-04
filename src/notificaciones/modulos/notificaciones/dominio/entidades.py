"""Entidades del dominio de notificaciones

En este archivo usted encontrará las entidades del dominio de notificaciones

"""

from __future__ import annotations
from enum import Enum
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


class NotificationType(Enum):
    """ Tipos de notificaciones """
    ORDER_CONFIRMATION = "order_confirmation"
    PAYMENT_REMINDER = "payment_reminder"
    PROMOTION = "promotion"


class NotificationMedium(Enum):
    """ Medios de notificación """
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"


class Notification:
    """ Entidad de notificaciones """

    def __init__(self, notification_type: NotificationType, medium: NotificationMedium, value: str):
        self.notification_type = notification_type
        self.medium = medium
        self.value = value  # Puede ser un mensaje o contenido JSON

    def __repr__(self):
        return f"Notification(type={self.notification_type.value}, medium={self.medium.value}, value={self.value})"
