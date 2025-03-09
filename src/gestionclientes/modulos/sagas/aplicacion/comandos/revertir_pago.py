from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.eventos.pagos import PagoRevertido
from gestionclientes.modulos.sagas.infraestructura.despachadores import \
    Despachador
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class RevertirPago(SagaInfo):
    ...

class RevertirPagoHandler(SagaBaseHandler):
    def handle(self, comando: RevertirPago):
        print("********************** EJECUCIÓN COMANDO REVERTIR PAGO, EMITE EVENTO DE REVERSIÓN")
        # eventoDominio = PagoRevertido(
        #     id_correlacion = comando.id_correlacion, id_cliente = comando.id_cliente, command_type="revertir_pago")
        # despachador = Despachador()
        # despachador.publicar_comando(eventoDominio, 'comandos-compensacion-saga')


@comando.register(RevertirPago)
def ejecutar_comando_revertir_pago(comando: RevertirPago):
    handler = RevertirPagoHandler()
    handler.handle(comando)
    