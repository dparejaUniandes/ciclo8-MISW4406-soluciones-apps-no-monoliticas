from dataclasses import dataclass, field

from gestionclientes.modulos.facturacion.aplicacion.dto import FacturacionDTO
from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacion
from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.infraestructura.repositorios import \
    RepositorioFacturacion
from gestionclientes.modulos.facturacion.infraestructura.repositorios_no_sqlalchemy import \
    RepositorioFacturacionNoSQLAlchemy
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from gestionclientes.modulos.facturacion.infraestructura.despachadores import \
    Despachador
from gestionclientes.modulos.facturacion.dominio.eventos import PagoRealizado

from .base import FacturacionBaseHandler


@dataclass
class CrearFacturacion(Comando):
    id: str
    medio_pago: str
    id_cliente: str
    monto: int

class CrearFacturacionHandler(FacturacionBaseHandler):
    
    def handle(self, comando: CrearFacturacion):
        facturacion_dto = FacturacionDTO(
            id=comando.id,
            medioPago=comando.medio_pago,
            idCliente=comando.id_cliente,
            monto=comando.monto,
        )

        facturacion: Facturacion = self.fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())
        facturacion.crear_facturacion(facturacion)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacionNoSQLAlchemy)
        repositorio.agregar(repositorio)

        evento = PagoRealizado(id_cliente=facturacion.idCliente, estado="PAGADO", monto=facturacion.monto)
        despachador = Despachador()
        despachador.publicar_comando(evento, 'comandos-pago')

        # UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, facturacion)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()


@comando.register(CrearFacturacion)
def ejecutar_comando_crear_facturacion(comando: CrearFacturacion):
    handler = CrearFacturacionHandler()
    handler.handle(comando)
    