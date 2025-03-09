from dataclasses import dataclass
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler, SagaInfo
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas

@dataclass
class RevertirNotificacion(SagaInfo):
    ...

class RevertirNotificacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirNotificacion):
        print("********************** EJECUCIÓN COMANDO RevertirNotificacion, emite evento compensación")
        saga = Saga(
            id_correlacion = comando.id_correlacion,
            id_cliente = comando.id_cliente,
            nombre_paso = comando.nombre_paso,
            estado = comando.estado,
            index = comando.index
        )

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas)
        repositorio.agregar(saga)


@comando.register(RevertirNotificacion)
def ejecutar_comando_revertir_notificacion(comando: RevertirNotificacion):
    handler = RevertirNotificacionHandler()
    handler.handle(comando)
    