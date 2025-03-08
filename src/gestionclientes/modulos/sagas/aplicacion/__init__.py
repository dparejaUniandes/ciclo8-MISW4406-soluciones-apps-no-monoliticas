from pydispatch import dispatcher

from gestionclientes.modulos.sagas.dominio.eventos.pagos import (PagoRealizado,
                                                                 PagoRevertido)

from .handlers import HandlerSagaDominio

dispatcher.connect(HandlerSagaDominio.handle_pago_realizado_correcto, signal=f'{PagoRealizado.__name__}Dominio')
dispatcher.connect(HandlerSagaDominio.handle_pago_realizado_revertido, signal=f'{PagoRevertido.__name__}Dominio')
