from gestionclientes.modulos.clientes.aplicacion.comandos.base import \
    SagaBaseHandler
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


class RealizarPago():
    ...

class RevertirPago():
    id_correlacion: str
    id_cliente: str
    estado: str

class RevertirPagoHandler(SagaBaseHandler):
    def handle(self, comando: RevertirPago):
        print("********************** EJECUCIÓN COMANDO REVERTIR PAGO, EMITE EVENTO DE REVERSIÓN")
        # entidad = CrearEntidad para revertir pago(
        #     comando.id_correlacion,
        #     comando.id_cliente,
        #     comando.estado
        # )

        # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)


@comando.register(RevertirPago)
def ejecutar_comando_revertir_pago(comando: RevertirPago):
    handler = RevertirPagoHandler()
    handler.handle(comando)
    