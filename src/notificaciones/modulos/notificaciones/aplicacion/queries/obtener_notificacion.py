from dataclasses import dataclass

from gestionclientes.modulos.clientes.aplicacion.mapeadores import \
    MapeadorCliente
from gestionclientes.modulos.clientes.infraestructura.repositorios import \
    RepositorioClientes
from gestionclientes.seedwork.aplicacion.queries import (Query, QueryHandler,
                                                         QueryResultado)
from gestionclientes.seedwork.aplicacion.queries import ejecutar_query as query

from .base import NotificacionQueryBaseHandler


@dataclass
class ObtenerNotificacion(Query):
    """ Query para obtener una notificación """
    id: str


class ObtenerNotificacionHandler(NotificacionQueryBaseHandler):
    """ Manejador del query para obtener una notificación """

    def handle(self, query: ObtenerNotificacion) -> QueryResultado:
        """ Manejar query para obtener una notificación """
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioClientes.__class__)
        cliente = self.fabrica_vuelos.crear_objeto(
            repositorio.obtener_por_id(query.id), MapeadorCliente())
        return QueryResultado(resultado=cliente)


@query.register(ObtenerNotificacion)
def ejecutar_query_obtener_notificacion(query: ObtenerNotificacion):
    """ Ejecutar query para obtener una notificación """
    handler = ObtenerNotificacionHandler()
    return handler.handle(query)
