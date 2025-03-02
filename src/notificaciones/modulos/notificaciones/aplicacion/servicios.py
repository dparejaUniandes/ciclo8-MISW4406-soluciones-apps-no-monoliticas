from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.dominio.fabricas import FabricaNotificaciones
from notificaciones.modulos.notificaciones.infraestructura.fabricas import \
    FabricaRepositorio
from notificaciones.modulos.notificaciones.infraestructura.repositorios import \
    RepositorioNotificaciones
from notificaciones.seedwork.aplicacion.servicios import Servicio

from .dto import NotificacionDTO
from .mapeadores import MapeadorNotificacion


class ServicioNotificacion(Servicio):
    """ Servicio de notificaciones """

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_notificaciones: FabricaNotificaciones = FabricaNotificaciones()

    @property
    def fabrica_repositorio(self):
        """ Fabrica de repositorios """
        return self._fabrica_repositorio

    @property
    def fabrica_notificaciones(self):
        """ Fabrica de notificaciones """
        return self._fabrica_notificaciones

    def crear_notificacion(self, notification_dto: NotificacionDTO) -> NotificacionDTO:
        """ Crear una notificacion """
        print(f'APLICACION - Notificacion recibida: {notification_dto}')
        print(type(notification_dto))
        notificacion: Notificacion = self.fabrica_notificaciones.crear_objeto(
            notification_dto, MapeadorNotificacion())
        print(f'APLICACION - Notificacion creada: {notificacion}')
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioNotificaciones.__class__)
        print(f'APLICACION - Repositorio: {repositorio}')
        repositorio.agregar(notificacion)
        print(f'APLICACION - Notificacion agregada: {notificacion}')
        notificacion.idDesdeBD = notificacion.id
        return self.fabrica_notificaciones.crear_objeto(notificacion, MapeadorNotificacion())

    def obtener_notificacion_por_id(self, id) -> NotificacionDTO:
        """ Obtener una notificacion por id """
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioNotificaciones.__class__)
        return self.fabrica_notificaciones.crear_objeto(repositorio.obtener_por_id(id), MapeadorNotificacion())

    def obtener_todos_las_notificaciones(self) -> NotificacionDTO:
        """ Obtener todos los notificaciones """
        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioNotificaciones.__class__)
        return self.fabrica_notificaciones.crear_objeto(repositorio.obtener_todos(), MapeadorNotificacion())
