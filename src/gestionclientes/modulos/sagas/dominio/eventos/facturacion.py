import uuid
from dataclasses import dataclass

from gestionclientes.seedwork.dominio.eventos import EventoDominio


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
    command_type: str = None

@dataclass
class FacturacionFallida(EventoFacturacion):
    id_correlacion: str = None
    id_cliente: uuid.UUID = None
    estado: str = None
    monto: float = None