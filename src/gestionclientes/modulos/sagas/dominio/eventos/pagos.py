from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from gestionclientes.seedwork.dominio.eventos import EventoDominio


class EventoPago(EventoDominio):
    ...

@dataclass
class PagoRealizado(EventoPago):
    id_correlacion: str = None
    id_cliente: str = None, 
    estado: str = None

@dataclass
class PagoFallido(EventoPago):
    id_correlacion: str = None
    id_cliente: str = None, 
    estado: str = None

@dataclass
class PagoRevertido(EventoPago):
    id_correlacion: str = None
    id_cliente: str = None
    command_type: str = None