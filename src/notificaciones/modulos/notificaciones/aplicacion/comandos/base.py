""" Módulo de comandos base """
from notificaciones.modulos.notificaciones.dominio.fabricas import FabricaNotificaciones
from notificaciones.modulos.notificaciones.infraestructura.fabricas import \
    FabricaRepositorio
from notificaciones.seedwork.aplicacion.comandos import ComandoHandler


class NotificacionBaseHandler(ComandoHandler):
    """ Clase base para los handlers de los comandos de notificaciones """

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_notificaciones: FabricaNotificaciones = FabricaNotificaciones()

    @property
    def fabrica_repositorio(self):
        """ Fabrica de repositorios """
        return self._fabrica_repositorio

    @property
    def fabrica_notificaciones(self):
        """ Fabrica de Notificaciones """
        return self._fabrica_notificaciones
