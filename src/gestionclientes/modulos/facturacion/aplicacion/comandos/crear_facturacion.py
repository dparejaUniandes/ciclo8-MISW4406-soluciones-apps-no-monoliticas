from dataclasses import dataclass, field

from gestionclientes.modulos.facturacion.aplicacion.dto import FacturacionDTO
from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacion
from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.infraestructura.repositorios import \
    RepositorioFacturacion
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

from .base import CrearFacturacionBaseHandler


@dataclass
class CrearFacturacion(Comando):
    id: str
    medio_pago: str
    id_cliente: str
    monto: int

class CrearFacturacionHandler(CrearFacturacionBaseHandler):
    
    def handle(self, comando: CrearFacturacion):
        facturacion_dto = FacturacionDTO(
            id=comando.id,
            medioPago=comando.medio_pago,
            idCliente=comando.id_cliente,
            monto=comando.monto,
        )

        facturacion: Facturacion = self.fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())
        facturacion.crear_facturacion(facturacion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacion.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, facturacion)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearFacturacion)
def ejecutar_comando_crear_facturacion(comando: CrearFacturacion):
    handler = CrearFacturacionHandler()
    handler.handle(comando)
    