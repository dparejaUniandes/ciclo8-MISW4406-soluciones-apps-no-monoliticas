from dataclasses import dataclass
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.modulos.sagas.aplicacion.comandos.base import \
    SagaBaseHandler, SagaInfo
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando

@dataclass
class CrearNotificacion(SagaInfo):
    ...

class CrearNotificacionHandler(SagaBaseHandler):
    def handle(self, comando: CrearNotificacion):
        print("********************** EJECUCIÓN COMANDO CrearNotificacion, es correcto y guarda saga")


@comando.register(CrearNotificacion)
def ejecutar_comando_crear_notificacion(comando: CrearNotificacion):
    handler = CrearNotificacionHandler()
    handler.handle(comando)
    