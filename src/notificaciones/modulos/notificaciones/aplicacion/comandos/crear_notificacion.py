""" Caso de uso para crear una Notificación """
from dataclasses import dataclass

from notificaciones.modulos.notificaciones.aplicacion.dto import NotificacionDTO
from notificaciones.modulos.notificaciones.aplicacion.mapeadores import \
    MapeadorNotificacion
from notificaciones.modulos.notificaciones.dominio.entidades import Notificacion
from notificaciones.modulos.notificaciones.infraestructura.repositorios import \
    RepositorioNotificaciones
from notificaciones.seedwork.aplicacion.comandos import Comando
from notificaciones.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from notificaciones.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import NotificacionBaseHandler


@dataclass
class CrearNotificacion(Comando):
    """ Comando para crear una notificación """
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    tipo: str
    medio: str
    valor: str


class CrearNotificacionHandler(NotificacionBaseHandler):

    def handle(self, comando: CrearNotificacion):
        """ Ejecutar comando para crear una notificación """
        cliente_dto = NotificacionDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            tipo=comando.tipo,
            medio=comando.medio,
            valor=comando.valor,
        )

        cliente: Notificacion = self.fabrica_clientes.crear_objeto(
            cliente_dto, MapeadorNotificacion())
        cliente.crear_notificacion(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioNotificaciones.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearNotificacion)
def ejecutar_comando_crear_notificacion(comando: CrearNotificacion):
    """ Ejecutar comando para crear una notificacion """
    handler = CrearNotificacionHandler()
    handler.handle(comando)
