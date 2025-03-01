from notificaciones.modulos.notificaciones.dominio.fabricas import FabricaNotificaciones
from notificaciones.modulos.notificaciones.infraestructura.fabricas import \
    FabricaRepositorio
from notificaciones.seedwork.aplicacion.queries import QueryHandler


class NotificacionQueryBaseHandler(QueryHandler):
    """ Clase base para los handlers de los queries de notificaciones """

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_vuelos: FabricaNotificaciones = FabricaNotificaciones()

    @property
    def fabrica_repositorio(self):
        """ Fabrica de repositorios """
        return self._fabrica_repositorio

    @property
    def fabrica_notificaciones(self):
        """ Fabrica de vuelos """
        return self._fabrica_vuelos
