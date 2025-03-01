from dataclasses import dataclass, field

from notificaciones.modulos.notificaciones.aplicacion.dto import ClienteDTO
from notificaciones.modulos.notificaciones.aplicacion.mapeadores import \
    MapeadorCliente
from notificaciones.modulos.notificaciones.dominio.entidades import Cliente
from notificaciones.modulos.notificaciones.dominio.objetos_valor import EstadoPlan
from notificaciones.modulos.notificaciones.infraestructura.repositorios import \
    RepositorioClientes
from notificaciones.seedwork.aplicacion.comandos import Comando
from notificaciones.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from notificaciones.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import NotificacionBaseHandler


@dataclass
class ActualizarNotificacion(Comando):
    """ Comando para actualizar un notificacion """
    id: str
    estadoPlan: str


class ActualizarNotificacionHandler(NotificacionBaseHandler):
    """ Manejador del comando para actualizar un notificacion """

    def handle(self, comando: ActualizarNotificacion):
        """ Manejar comando para actualizar una notificacion """
        cliente_dto = ClienteDTO(
            idDesdeBD=comando.id,
            estadoPlan=comando.estadoPlan
        )

        cliente: Cliente = self.fabrica_clientes.crear_objeto(
            cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(
            RepositorioClientes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ActualizarNotificacion)
def ejecutar_comando_crear_notificacion(comando: ActualizarNotificacion):
    """ Ejecutar comando para actualizar una notificacion """
    handler = ActualizarNotificacionHandler()
    handler.handle(comando)
