from dataclasses import dataclass, field

from gestionclientes.modulos.clientes.aplicacion.dto import ClienteDTO
from gestionclientes.modulos.clientes.aplicacion.mapeadores import \
    MapeadorCliente
from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.infraestructura.repositorios import \
    RepositorioClientes
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import CrearClienteBaseHandler


@dataclass
class CrearCliente(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str
    nombre: str


class CrearClienteHandler(CrearClienteBaseHandler):
    
    def handle(self, comando: CrearCliente):
        cliente_dto = ClienteDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            ,   nombre=comando.nombre)

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
    