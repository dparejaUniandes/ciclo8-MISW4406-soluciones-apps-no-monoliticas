from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.fabricas import FabricaFacturacion
from gestionclientes.modulos.facturacion.infraestructura.fabricas import \
    FabricaRepositorio
from gestionclientes.modulos.facturacion.infraestructura.repositorios import \
    RepositorioFacturacion
from gestionclientes.seedwork.aplicacion.servicios import Servicio

from .dto import FacturacionDTO
from .mapeadores import MapeadorFacturacion


class ServicioFacturacion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_facturacion: FabricaFacturacion = FabricaFacturacion()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_facturacion(self):
        return self._fabrica_facturacion

    def crear_facturacion(self, facturacion_dto: FacturacionDTO) -> FacturacionDTO:
        facturacion: Facturacion = self.fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacion.__class__)
        repositorio.agregar(facturacion)
        facturacion.idDesdeBD = facturacion.id
        return self.fabrica_facturacion.crear_objeto(facturacion, MapeadorFacturacion())

    def obtener_facturacion_por_id(self, id) -> FacturacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacion.__class__)
        return self.fabrica_facturacion.crear_objeto(repositorio.obtener_por_id(id), MapeadorFacturacion())
    
    def obtener_todas_las_facturaciones(self) -> FacturacionDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacion.__class__)
        return self.fabrica_facturacion.crear_objeto(repositorio.obtener_todos(), MapeadorFacturacion())

