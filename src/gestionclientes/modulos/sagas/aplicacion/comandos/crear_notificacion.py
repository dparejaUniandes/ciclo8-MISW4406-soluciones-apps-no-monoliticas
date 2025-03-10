from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class CrearNotificacion(SagaInfo):
    ...

class CrearNotificacionHandler(SagaBaseHandler):
    def handle(self, comando: CrearNotificacion):
        print("********************** EJECUCIÓN COMANDO CrearNotificacion, es correcto, la saga ya se guardó")


@comando.register(CrearNotificacion)
def ejecutar_comando_crear_notificacion(comando: CrearNotificacion):
    handler = CrearNotificacionHandler()
    handler.handle(comando)
    