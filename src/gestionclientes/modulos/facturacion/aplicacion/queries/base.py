from gestionclientes.modulos.facturacion.dominio.fabricas import FabricaFacturacion
from gestionclientes.modulos.facturacion.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.seedwork.aplicacion.queries import QueryHandler


class FacturacionQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaFacturacion = FabricaFacturacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_vuelos(self):
        return self._fabrica_vuelos    