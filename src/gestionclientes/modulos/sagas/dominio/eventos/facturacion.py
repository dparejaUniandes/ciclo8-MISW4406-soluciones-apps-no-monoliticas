import uuid
from dataclasses import dataclass

from integracionpagos.seedwork.dominio.eventos import EventoDominio


class EventoFacturacion(EventoDominio):
    ...

@dataclass
class FacturacionCreada(EventoFacturacion):
    id_correlacion: str = None
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None

@dataclass
class FacturacionRevertida(EventoFacturacion):
    id_correlacion: str = None
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None

@dataclass
class FacturacionFallida(EventoFacturacion):
    id_correlacion: str = None
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None