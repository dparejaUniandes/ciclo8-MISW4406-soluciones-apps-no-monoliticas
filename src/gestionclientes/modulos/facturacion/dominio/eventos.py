from __future__ import annotations

import uuid
from dataclasses import dataclass

from gestionclientes.seedwork.dominio.eventos import EventoDominio


@dataclass
class PagoRealizado(EventoDominio):
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None
