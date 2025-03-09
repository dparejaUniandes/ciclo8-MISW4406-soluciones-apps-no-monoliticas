from dataclasses import dataclass
from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler, SagaInfo
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas

@dataclass
class RevertirFacturacion(SagaInfo):
    ...

class RevertirFacturacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirFacturacion):
        print("********************** EJECUCIÓN COMANDO REVERTIR FACTURACIÓN, EMITE EVENTO DE REVERSIÓN")
        saga = Saga(
            id_correlacion = comando.id_correlacion,
            id_cliente = comando.id_cliente,
            nombre_paso = comando.nombre_paso,
            estado = comando.estado,
            index = comando.index
        )

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas)
        repositorio.agregar(saga)


@comando.register(RevertirFacturacion)
def ejecutar_comando_revertir_facturacion(comando: RevertirFacturacion):
    handler = RevertirFacturacionHandler()
    handler.handle(comando)
    