from pydispatch import dispatcher

from integracionpagos.modulos.pagos.dominio.eventos import PagoRealizado

from .handlers import HandlerPagoIntegracion

dispatcher.connect(HandlerPagoIntegracion.handle_pago_realizado, signal=f'{PagoRealizado.__name__}Integracion')
