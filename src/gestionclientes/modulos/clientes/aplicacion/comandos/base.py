from gestionclientes.modulos.clientes.dominio.fabricas import FabricaClientes
from gestionclientes.modulos.clientes.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.comandos import ComandoHandler


class CrearClienteBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: FabricaClientes = FabricaClientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes    
    