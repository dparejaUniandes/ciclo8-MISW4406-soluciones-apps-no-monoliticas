from dataclasses import dataclass

from gestionclientes.modulos.sagas.aplicacion.comandos.base import (
    SagaBaseHandler, SagaInfo)
from gestionclientes.modulos.sagas.dominio.eventos.notificacion import \
    NotificacionRevertida
from gestionclientes.modulos.sagas.infraestructura.despachadores import \
    Despachador
from gestionclientes.seedwork.aplicacion.comandos import \
    ejecutar_commando as comando


@dataclass
class RevertirNotificacion(SagaInfo):
    ...

class RevertirNotificacionHandler(SagaBaseHandler):
    def handle(self, comando: RevertirNotificacion):
        # La reversión de la notificación se realiza desde facturación en actualizar, dada la naturaleza del flujo.
        print("********************** EJECUCIÓN COMANDO RevertirNotificacion, emite evento compensación")


@comando.register(RevertirNotificacion)
def ejecutar_comando_revertir_notificacion(comando: RevertirNotificacion):
    handler = RevertirNotificacionHandler()
    handler.handle(comando)
    