from dataclasses import dataclass
from gestionclientes.modulos.sagas.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.comandos import ComandoHandler
from gestionclientes.seedwork.aplicacion.comandos import Comando

@dataclass
class SagaInfo(Comando):
    id_correlacion: str
    id_cliente: str

class SagaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    