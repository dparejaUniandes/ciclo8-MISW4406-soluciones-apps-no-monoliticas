from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class RealizarPago(SagaInfo):
    ...

class RealizarPagoHandler(SagaBaseHandler):
    def handle(self, comando: RealizarPago):
        print("********************** EJECUCIÓN COMANDO REALIZAR PAGO, es correcto, la saga ya se guardó")


@comando.register(RealizarPago)
def ejecutar_comando_realizar_pago(comando: RealizarPago):
    handler = RealizarPagoHandler()
    handler.handle(comando)
    