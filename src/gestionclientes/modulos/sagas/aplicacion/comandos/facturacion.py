from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.aplicacion.comandos import Comando


class RevertirFacturacion(Comando):
    ...

class CrearFacturacion(Comando):
    ...

class RevertirFacturacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirFacturacion):
        print("********************** EJECUCIÓN COMANDO REVERTIR FACTURACIÓN, EMITE EVENTO DE REVERSIÓN")
        # entidad = CrearEntidad para revertir pago(
        #     comando.id_correlacion,
        #     comando.id_cliente,
        #     comando.estado
        # )

        # repositorio = self.fabrica_repositorio.crear_objeto(RepositorioClientes.__class__)


@comando.register(RevertirFacturacion)
def ejecutar_comando_revertir_facturacion(comando: RevertirFacturacion):
    handler = RevertirFacturacionHandler()
    handler.handle(comando)
    