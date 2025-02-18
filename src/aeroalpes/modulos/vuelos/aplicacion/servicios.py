from aeroalpes.modulos.vuelos.dominio.entidades import Cliente
from aeroalpes.modulos.vuelos.dominio.fabricas import FabricaClientes
from aeroalpes.modulos.vuelos.infraestructura.fabricas import \
    FabricaRepositorio
from aeroalpes.modulos.vuelos.infraestructura.repositorios import \
    RepositorioClientes
from aeroalpes.seedwork.aplicacion.servicios import Servicio

from .dto import ClienteDTO
from .mapeadores import MapeadorCliente


class ServicioReserva(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_clientes: FabricaClientes = FabricaClientes()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_clientes(self):
        return self._fabrica_clientes

    def crear_cliente(self, cliente_dto: ClienteDTO) -> ClienteDTO:
        cliente: Cliente = self.fabrica_clientes.crear_objeto(cliente_dto, MapeadorCliente())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        repositorio.agregar(cliente)

        return self.fabrica_clientes.crear_objeto(cliente, MapeadorCliente())

    def obtener_cliente_por_id(self, id) -> ClienteDTO:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)
        return repositorio.obtener_por_id(id).__dict__

