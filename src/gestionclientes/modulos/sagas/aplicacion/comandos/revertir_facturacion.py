from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.entidades import Saga
from gestionclientes.modulos.sagas.dominio.eventos.facturacion import \
    FacturacionRevertida
from gestionclientes.modulos.sagas.dominio.repositorios import RepositorioSagas
from gestionclientes.modulos.sagas.infraestructura.despachadores import \
    Despachador
from gestionclientes.seedwork.aplicacion.comandos import Comando
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class RevertirFacturacion(SagaInfo):
    ...

class RevertirFacturacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirFacturacion):
        print("********************** EJECUCIÓN COMANDO REVERTIR FACTURACIÓN, EMITE EVENTO DE REVERSIÓN")
        eventoDominio = FacturacionRevertida(
            id_correlacion = comando.id_correlacion, id_cliente = comando.id_cliente, command_type="revertir_facturacion")
        despachador = Despachador()
        despachador.publicar_comando(eventoDominio, 'comandos-compensacion-saga')


@comando.register(RevertirFacturacion)
def ejecutar_comando_revertir_facturacion(comando: RevertirFacturacion):
    handler = RevertirFacturacionHandler()
    handler.handle(comando)
    