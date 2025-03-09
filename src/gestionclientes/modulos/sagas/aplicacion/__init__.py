from pydispatch import dispatcher

from gestionclientes.modulos.sagas.dominio.eventos.pagos import (PagoRealizado,
                                                                 PagoFallido)
from gestionclientes.modulos.sagas.dominio.eventos.facturacion import (FacturacionCreada,
                                                                 FacturacionFallida)

from .handlers import HandlerSagaDominio

dispatcher.connect(HandlerSagaDominio.handle_pago_realizado_correcto, signal=f'{PagoRealizado.__name__}Dominio')
dispatcher.connect(HandlerSagaDominio.handle_pago_realizado_revertido, signal=f'{PagoFallido.__name__}Dominio')
dispatcher.connect(HandlerSagaDominio.handle_factura_creada_correcto, signal=f'{FacturacionCreada.__name__}Dominio')
dispatcher.connect(HandlerSagaDominio.handle_factura_creada_revertido, signal=f'{FacturacionFallida.__name__}Dominio')
