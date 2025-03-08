from __future__ import annotations

import uuid
from dataclasses import dataclass

from gestionclientes.seedwork.dominio.eventos import EventoDominio


@dataclass
class FacturacionCreada(EventoDominio):
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None

@dataclass
class PagoConfirmado(EventoDominio):
    tipo: str = None
    valor: str = None
    medio: str = None