""" Caso de uso para crear una Notificación """
from dataclasses import dataclass

from notificaciones.modulos.notificaciones.aplicacion.dto import ClienteDTO
from notificaciones.modulos.notificaciones.aplicacion.mapeadores import \
    MapeadorCliente
from notificaciones.modulos.notificaciones.dominio.entidades import Cliente
from notificaciones.modulos.notificaciones.infraestructura.repositorios import \
    RepositorioClientes
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
    nombre: str
    apellidos: str
    correo: str
    contrasena: str
    estado_plan: str

class CrearNotificacionHandler(NotificacionBaseHandler):
    
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
            fecha_actualizacion=comando.fecha_actualizacion,
            fecha_creacion=comando.fecha_creacion,
            id=comando.id,
            nombre=comando.nombre,
            apellidos=comando.apellidos,
            correo=comando.correo,
            contrasena=comando.contrasena,
            estadoPlan=comando.estadoPlan
        )

        cliente: Cliente = self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearCliente)
def ejecutar_comando_crear_cliente(comando: CrearCliente):
    handler = CrearClienteHandler()
    handler.handle(comando)
    