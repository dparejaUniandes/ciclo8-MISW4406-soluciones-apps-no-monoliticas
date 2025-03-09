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
        print("********************** EJECUCIÓN COMANDO RevertirNotificacion, emite evento compensación")
        eventoDominio = NotificacionRevertida(
            id_correlacion = comando.id_correlacion, id_cliente = comando.id_cliente, command_type="revertir_notificacion")
        despachador = Despachador()
        despachador.publicar_comando(eventoDominio, 'comandos-compensacion-saga')


@comando.register(RevertirNotificacion)
def ejecutar_comando_revertir_notificacion(comando: RevertirNotificacion):
    handler = RevertirNotificacionHandler()
    handler.handle(comando)
    