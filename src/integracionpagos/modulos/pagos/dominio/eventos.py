from __future__ import annotations

import uuid
from dataclasses import dataclass

from integracionpagos.seedwork.dominio.eventos import EventoDominio


@dataclass
class PagoRealizado(EventoDominio):
    id_cliente: uuid.UUID = None
    estado_pago: str = None
    id_correlacion: str = None
