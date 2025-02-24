from dataclasses import dataclass

from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacion
from gestionclientes.modulos.facturacion.infraestructura.repositorios import \
    RepositorioFacturacion
from gestionclientes.seedwork.aplicacion.queries import (Query, QueryHandler,
                                                         QueryResultado)
from gestionclientes.seedwork.aplicacion.queries import ejecutar_query as query

from .base import FacturacionQueryBaseHandler


@dataclass
class ObtenerFacturacion(Query):
    id: str

class ObtenerFacturacionHandler(FacturacionQueryBaseHandler):

    def handle(self, query: ObtenerFacturacion) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacion.__class__)
        facturacion =  self.fabrica_vuelos.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorFacturacion())
        return QueryResultado(resultado=facturacion)

@query.register(ObtenerFacturacion)
def ejecutar_query_obtener_facturacion(query: ObtenerFacturacion):
    handler = ObtenerFacturacionHandler()
    return handler.handle(query)