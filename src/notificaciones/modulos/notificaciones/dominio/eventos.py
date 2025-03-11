from __future__ import annotations

import uuid
from dataclasses import dataclass

from notificaciones.seedwork.dominio.eventos import EventoDominio


@dataclass
class NotificacionCreada(EventoDominio):
    id_cliente: str = None
    id_correlacion: str = None
    event_type: str = None
