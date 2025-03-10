""" Caso de uso para crear una Notificación """
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Column, DateTime

from notificaciones.modulos.notificaciones.aplicacion.dto import \
    NotificacionDTO
from notificaciones.modulos.notificaciones.aplicacion.mapeadores import \
    MapeadorNotificacion
from notificaciones.modulos.notificaciones.dominio.entidades import \
    Notificacion
from notificaciones.modulos.notificaciones.dominio.eventos import \
    NotificacionCreada
from notificaciones.modulos.notificaciones.infraestructura.despachadores import \
    Despachador
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
    id_correlacion: str


class CrearNotificacionHandler(NotificacionBaseHandler):
    """ Manejador del comando para crear una notificación """

    def handle(self, comando: CrearNotificacion):
        """ Ejecutar comando para crear una notificación """
        print("Iniciando comando...")
        notificacion_dto = NotificacionDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            tipo=comando.tipo,
            medio=comando.medio,
            valor=comando.valor,
        )

        notificacion: Notificacion = self.fabrica_notificaciones.crear_objeto(
            notificacion_dto, MapeadorNotificacion())
        notificacion.crear_notificacion(notificacion)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioNotificaciones.__class__)
        repositorio.agregar(notificacion)

        event_type="notificacion_creada"
        if "REVERSION" in comando.tipo:
            event_type = "notificacion_revertida"
        notificacion_creada = NotificacionCreada(
            id_correlacion = comando.id_correlacion,
            id_cliente = comando.valor,
            event_type = event_type
        )
        despachador = Despachador()
        despachador.publicar_evento(notificacion_creada, 'eventos-notificaciones')



@comando.register(CrearNotificacion)
def ejecutar_comando_crear_notificacion(comando: CrearNotificacion):
    """ Ejecutar comando para crear una notificacion """
    handler = CrearNotificacionHandler()
    handler.handle(comando)
