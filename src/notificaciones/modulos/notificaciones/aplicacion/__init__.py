from pydispatch import dispatcher

from .handlers import HandlerClienteDominio

dispatcher.connect(HandlerClienteDominio.handle_pago_realizado, signal='PagoRealizadoDominio')
