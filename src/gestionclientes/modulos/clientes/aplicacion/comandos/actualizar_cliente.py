from dataclasses import dataclass, field

from gestionclientes.modulos.clientes.aplicacion.dto import ClienteDTO
from gestionclientes.modulos.clientes.aplicacion.mapeadores import \
    MapeadorCliente
from gestionclientes.modulos.clientes.dominio.entidades import Cliente
from gestionclientes.modulos.clientes.dominio.objetos_valor import EstadoPlan
from gestionclientes.modulos.clientes.infraestructura.repositorios import \
    RepositorioClientes
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import ClienteBaseHandler


@dataclass
class ActualizarCliente(Comando):
    id: str
    estadoPlan: str

class ActualizarClienteHandler(ClienteBaseHandler):
    
    def handle(self, comando: ActualizarCliente):
        cliente_dto = ClienteDTO(
            idDesdeBD=comando.id,
            estadoPlan=comando.estadoPlan
        )

        cliente: Cliente = self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())
        cliente.crear_cliente(cliente)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, cliente)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(ActualizarCliente)
def ejecutar_comando_crear_cliente(comando: ActualizarCliente):
    handler = ActualizarClienteHandler()
    handler.handle(comando)
    