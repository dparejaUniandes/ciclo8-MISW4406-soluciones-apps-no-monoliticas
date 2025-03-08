from gestionclientes.modulos.sagas.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.comandos import ComandoHandler


class SagaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    