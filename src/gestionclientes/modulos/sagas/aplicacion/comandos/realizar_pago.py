from dataclasses import dataclass
from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler, SagaInfo
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.aplicacion.comandos import Comando

@dataclass
class RealizarPago(SagaInfo):
    ...

class RealizarPagoHandler(SagaBaseHandler):
    def handle(self, comando: RealizarPago):
        print("********************** EJECUCIÓN COMANDO REALIZAR PAGO, es correcto y guarda saga")
        # entidad = CrearEntidad para revertir pago(
        #     comando.id_correlacion,
        #     comando.id_cliente,
        #     comando.estado
        # )

        # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)


@comando.register(RealizarPago)
def ejecutar_comando_realizar_pago(comando: RealizarPago):
    handler = RealizarPagoHandler()
    handler.handle(comando)
    