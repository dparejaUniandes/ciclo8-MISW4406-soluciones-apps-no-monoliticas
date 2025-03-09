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
        print("********************** EJECUCIÓN COMANDO REALIZAR PAGO, es correcto y guarda saga")
        saga = Saga(
            id_correlacion = comando.id_correlacion,
            id_cliente = comando.id_cliente,
            nombre_paso = comando.nombre_paso,
            estado = comando.estado,
            index = comando.index
        )

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioSagas)
        repositorio.agregar(saga)

        # pago_confirmado = PagoConfirmado(
        #     tipo="ALERTA",
        #     valor = "pepe@gmail.com",
        #     medio="correo"
        # )
        # despachador = Despachador()
        # despachador.publicar_evento_notificacion(pago_confirmado, 'eventos-gestionclientes-notificacion')


@comando.register(RealizarPago)
def ejecutar_comando_realizar_pago(comando: RealizarPago):
    handler = RealizarPagoHandler()
    handler.handle(comando)
    