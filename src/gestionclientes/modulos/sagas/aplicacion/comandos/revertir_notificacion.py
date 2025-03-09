from dataclasses import dataclass
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler, SagaInfo
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando

@dataclass
class RevertirNotificacion(SagaInfo):
    ...

class RevertirNotificacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirNotificacion):
        print("********************** EJECUCIÓN COMANDO RevertirNotificacion, emite evento compensación")


@comando.register(RevertirNotificacion)
def ejecutar_comando_revertir_notificacion(comando: RevertirNotificacion):
    handler = RevertirNotificacionHandler()
    handler.handle(comando)
    