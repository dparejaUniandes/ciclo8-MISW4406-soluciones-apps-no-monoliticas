from __future__ import annotations

from dataclasses import dataclass, field

from gestionclientes.seedwork.dominio.eventos import EventoDominio


class EventoNotificacion(EventoDominio):
    ...


@dataclass
class NotificacionCreada(EventoNotificacion):
    id_correlacion: str = None
    tipo: str = None
    medio: str = None
    valor: str = None

@dataclass
class NotificacionRevertida(EventoNotificacion):
    id_correlacion: str = None
    id_cliente: str = None
    command_type: str = None

@dataclass
class NotificacionFallida(EventoNotificacion):
    id_correlacion: str = None
    tipo: str = None
    medio: str = None
    valor: str = None
