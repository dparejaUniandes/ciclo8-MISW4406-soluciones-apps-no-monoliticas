from dataclasses import dataclass, field

from gestionclientes.modulos.facturacion.aplicacion.dto import FacturacionDTO
from gestionclientes.modulos.facturacion.aplicacion.mapeadores import \
    MapeadorFacturacion
from gestionclientes.modulos.facturacion.dominio.entidades import Facturacion
from gestionclientes.modulos.facturacion.dominio.eventos import PagoConfirmado
from gestionclientes.modulos.facturacion.infraestructura.despachadores import \
    Despachador
from gestionclientes.modulos.facturacion.infraestructura.repositorios import \
    RepositorioFacturacion
from gestionclientes.modulos.facturacion.infraestructura.repositorios_no_sqlalchemy import \
    RepositorioFacturacionNoSQLAlchemy
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando

from .base import FacturacionBaseHandler


@dataclass
class RevertirFacturacion(Comando):
    id_cliente: str
    estadoReportado: str
    id_correlacion: str

class RevertirFacturacionHandler(FacturacionBaseHandler):
    
    def handle(self, comando: RevertirFacturacion):
        facturacion_dto = FacturacionDTO(
            idCliente=comando.id_cliente,
            estadoReportado=comando.estadoReportado
        )

        facturacion: Facturacion = self.fabrica_facturacion.crear_objeto(facturacion_dto, MapeadorFacturacion())

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioFacturacionNoSQLAlchemy)
        repositorio.actualizar(facturacion)

        pago_confirmado = PagoConfirmado(
            tipo="ALERTA-REVERSION",
            valor = "pepe@gmail.com",
            medio="correo",
            event_type="facturacion_actualizada_revertida"
            id_correlacion=comando.id_correlacion
        )
        despachador = Despachador()
        despachador.publicar_evento_notificacion(pago_confirmado, 'eventos-gestionclientes-notificacion')


@comando.register(RevertirFacturacion)
def ejecutar_comando_actualizar_facturacion(comando: RevertirFacturacion):
    handler = RevertirFacturacionHandler()
    handler.handle(comando)
    