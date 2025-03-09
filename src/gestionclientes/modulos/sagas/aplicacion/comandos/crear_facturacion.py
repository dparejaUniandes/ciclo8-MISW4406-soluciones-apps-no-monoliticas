from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class CrearFacturacion(SagaInfo):
    ...

class CrearFacturacionHandler(SagaBaseHandler):
    def handle(self, comando: CrearFacturacion):
        print("********************** EJECUCIÓN COMANDO CREAR FACTURACIÓN, es correcto, la saga ya se guardó")


@comando.register(CrearFacturacion)
def ejecutar_comando_crear_facturacion(comando: CrearFacturacion):
    handler = CrearFacturacionHandler()
    handler.handle(comando)
    