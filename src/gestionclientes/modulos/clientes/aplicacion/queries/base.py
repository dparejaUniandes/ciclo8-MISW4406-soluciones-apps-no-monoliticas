from gestionclientes.modulos.clientes.dominio.fabricas import FabricaClientes
from gestionclientes.modulos.clientes.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.queries import QueryHandler


class ClienteQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaClientes = FabricaClientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    