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

from .base import FacturacionBaseHandler


@dataclass
class ActualizarFacturacion(Comando):
    id_cliente: str
    estadoReportado: str

class ActualizarFacturacionHandler(FacturacionBaseHandler):
    
    def handle(self, comando: ActualizarFacturacion):
        facturacion_dto = FacturacionDTO(
            idCliente=comando.id_cliente,
            estadoReportado=comando.estadoReportado
        )

        facturacion: Facturacion = self.fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacionNoSQLAlchemy.__class__)
        repositorio.actualizar(facturacion)

        # UnidadTrabajoPuerto.registrar_batch(repositorio.actualizar, facturacion)
        # UnidadTrabajoPuerto.savepoint()
        # UnidadTrabajoPuerto.commit()


@comando.register(ActualizarFacturacion)
def ejecutar_comando_actualizar_facturacion(comando: ActualizarFacturacion):
    handler = ActualizarFacturacionHandler()
    handler.handle(comando)
    