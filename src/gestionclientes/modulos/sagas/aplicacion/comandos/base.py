from dataclasses import dataclass
from datetime import datetime

from gestionclientes.modulos.sagas.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.comandos import (Comando,
                                                          ComandoHandler)


@dataclass
class SagaInfo(Comando):
    id_correlacion: str
    id_cliente: str
    nombre_paso: str
    estado: str
    index: int

class SagaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    